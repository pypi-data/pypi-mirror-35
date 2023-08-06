#!/usr/bin/python3
# -*- encoding: utf-8 -*-
# File: sunfluidhbox/processcom.py
# License: CeCILL-2.1
"""Common code to start process and communicate values up to stop request from one side.

Main process is responsible for:

- creation of communication pipes.
- start of secondary process with an environment containig ad-hoc SUNFLUIDH_PYCOMREF variable.

When starting sunfluidh as main process, the environment variable SUNFLUIDH_CTRL_COMMAND is
defined before launching sunfluidh, to provide the command starting control code without
modifying / recompiling code (ie. its just a data in an eventual startup script).


Use of ProcessCommunication objects
-----------------------------------

pc = ProcessCommunication(…)

pairvalue = pc.prepare_communication(myinitvalue)

while True:
    pairvalue = pc.exchange(myvalue)
    if pc.test_finish():
        break
    if detect_my_termination():
        pc.send_finish()
        break
    # Computing loop:
    # Use pairvalue for computing parameters.
    # Create new my value.

pc.terminate_communication()

Environment variables
---------------------

- SUNFLUIDH_PYCOMREF — set by main process when starting second one
- SUNFLUIDH_CTRL_COMMAND - must be set when sunfluidh is main

See more complete communication protocol and logical sequences in ProcessCommunication
documentation.

:author: Laurent Pointal <laurent.pointal@limsi.fr>
"""

from uuid import uuid4
import logging
import os
import os.path as osp
import random
import shlex
import signal
import subprocess
import sys
import threading
import time
import typing
import numpy as np
from . import pipecom

# Note: box and embed module define their own logging policy (level, log filename…).
# Here we just define a logger for our module.
logger = logging.getLogger("sunfluidhbox.processcom")

# Environment variable searched for communication reference (uuid for pipes names).
COMREF_ENVVAR = "SUNFLUIDH_PYCOMREF"

# Identification of this pair for communication.
# It is set upon embeded flag of first
PROCESSPAIR = None


class ProcessCommunication:
    """Wrap communications establishment and potential start of the secondary process.
    
    If the ProcessCommunication is not the main, then parameters binary is simply ignored.
    Both process can request to stop processing (with their own criteria).

    Use of MPI
    ----------
    
    If you want the launched process to use MPI, you have to provide it into the binary
    parameter, as the ad-hoc mpirun command. 
    Examples: 
      ['mpirun', '-np', '4', 'myapp']
      "mpirun -np4 myapp"
    
    Use shell PATH
    --------------
    
    If you want process start to use the shell to find the binary (via PATH
    environment variable), you must specify it directly in the command.
    Note that the first binary file with ad-hoc name found within the PATH will 
    be used (care of security).
    Examples:
      "/bin/sh -c myapp"
      ["/bin/bash", "-c", "myapp"]

    
    Start secondary process
    -----------------------
    
    Definition of SUNFLUIDH_PYCOMREF environment variable is used to know if current
    process is secondary (it is primary process if SUNFLUIDH_PYCOMREF is not defined).
    The primary process is responsible to start of the secondary one.
    For Fortran programs, see embed.py doc to know how to specify command to
    start control. For Python3 control programs, you can specify the command
    in the binary construction parameter (you may hardcode it or retrieve it
    via an environment variable (as in embed.py code).
    
       main                                                        
    _________
        |
        |initialize_main(…)
        |create ProcessCommunication
        |
        |prepare_communication(…                               secondary
        +----------------------- start process --------------> ___________
        |                                                           |
        |                                    initialize_secondary(…)|
        |                                create ProcessCommunication|
        |                                                           |
        |                                    prepare_communication(…|
        |<=========== transmit secondary process ready =============+
        |…)                                                       …)|
                
                  both process are ready to play their role
    
    So, once secondary process has signaled it is ready, we go into
    embeded/box (sunfluidh/control) processing loops independantly of 
    what process start the other. 
    
    Communication sequence protocol
    -------------------------------
    
    Main and secondary process are both in a "send my value, receive my 
    computing parameter" then exit loop or compute. But both sides need pair 
    to read to fullfill their writing (due to limitations on pipes buffers
    in memory, write of big data via pipes may need several writes and
    corresponding reads on he other side). 
    In short, we cannot use pipes buffers as an intermediate storage for 
    our respective write and later read, this must be in the communications 
    order protocol, else we will finish with some interblocking.

    Both process have a read/write loop, but they are shifted to that one 
    start by a read and the other by a write (computing code must be called 
    after the read in respective loops).

    Some ascii-art schema of computing loop and communications:

     control                                                        sunfluidh
    _________                                                      ___________
        |                                                               |
        |         start secondary process / init communication          |
        |                                                               |
      +>|before_computing(…                prepare_computing_iteration(…|<+
      | |<========================= send probes ========================+ |
      | |…)                                                             | |
      | |                                                               | |
      | + ?finish -->X                                                  | |
      | |                                                               | |
      | + COMPUTE                                                       | |
      | |                                                               | |
      | + ?detect end of computing -->X                                 | |
      | |                                                               | |
      | |after_computing(…                                              | |
      | +========================== send control ======================>| |
      | |…)                                                           …)| |
      +-+                                                               | |
                                                           Y<-- ?finish + |
        X                                                               | |
        |                                                       COMPUTE + |
        |                                                               | |
        |                                 Y<-- ?detect end of computing + |
        |                                                               | |
        |                                                               +-+
        |                   
        |                                                               Y
        |                    terminate communication                    |
        
    At the time one process has to send a value (probe/control), so just 
    before doing another computing iteration, it can exit its own loop, 
    then call the communication termination function which will send a 
    finish flag asking pair process to exit its computing loop too and 
    terminate.
        
    Attributes
    ----------
    
    :ivar bool embeded: boolean flag indicating that we are a process communicaton within
        a Fortran program (ie. a priori in sunfluidh).
    :ivar Lock comlock: mutex around communications - in case of multithread use.
    :ivar str comref: unique reference used to identify communication pipes for one communication.
    :ivar bool ismain: boolean flag indicating that this process is the main one (which start the
        secondary process).
    :ivar str workdir: working directory (for sunfluidh, its the path to search fortran 
        configuration file). Default None to use current working directory.
    :ivar bool usable: flag indicating that the object is usable for communications.
    :ivar str|list binary: command to start second process, if its s atring, it is splitted
        into parts using shell lexer. To provide an unsplitted string, place it as a single
        item in a list. 
    :ivar subprocess.Popen proc: secondary process launched.
    :ivar bool stop: boolean flag indicating that this process must stop its computing loop and
        properly exit. For fortran use an int 0/1 must be used.
    :ivar Any lastreceived: last value received from other process.
    :ivar bool sentfinished: flag indicating that pair process has been notified of finishing
        (prevent trying to send more than once the send stop/notify end data).
    """
    def __init__(self, *,
                 embeded,
                 workdir: str=None,
                 binary: typing.Union[str, list]=None
                 ):
        """
        
        See also more complete documentation in class docs.
        
        Parameters
        ----------
        
        :param bool embeded: boolean indicating that this process is embeded Python in Fortran.
        :ivar str workdir: working directory. Default None to use current working directory.
        :ivar str|list binary: command to start second process. Default None.
        """
        global PROCESSPAIR
        if not PROCESSPAIR:
            if embeded:
                PROCESSPAIR = "Embeded"
            else:
                PROCESSPAIR = "Boxed"
        logger.info(PROCESSPAIR + " object created")
        self.embeded = embeded
        # Communication management data.
        self.comlock = threading.Lock()
        self.comref = os.environ.get(COMREF_ENVVAR)
        if self.comref is None:
            self.ismain = True
            self.comref = str(uuid4())
        else:
            self.ismain = False
        if workdir is None:
            self.workdir = osp.abspath(os.getcwd())
        else:
            self.workdir = osp.abspath(workdir)
        self.usable = False
        self.readpipe = None
        self.writepipe = None
        # Secondary process data.
        self.binary = binary
        self.proc = None
        # Exchanged data.
        self.stop = 0
        self.lastreceived = None
        self.sentfinished = False
        
    def _check_usable(self):
        """Raises an exception if the object is not usable for communications.
        """
        if not self.usable:
            raise RuntimeError("ProcessCommunication not usable for communications.")
    
    def prepare_communication(self):
        """Setup process and pipes to enable communications.
        
        In main process, create pipe files and start secondary process. Both proces open
        pipes. Secondary process write a ready message to pipe which is read by main
        process.
        One this method exit, both process can start their own read/write/process loops
        (see class documentation).
        """
        if self.ismain:
            # ===== Create communication pipes files.  
            logger.debug("Prepare communication pipes.")
            pipecom.createpipes(self.workdir, self.comref)      
            
            if not self.binary:
                # For Fortran, the command to start control process can be providen via 
                # environment variable SUNFLUID_CTRL_COMMAND or in the Fortran code by 
                # specifying it as sf.initialize() parameter.
                # For Python control code, the command to start sundluidh can be providen
                # as a SunFluidh parameter (which value can be hardcoded or searched
                # elsewhere).
                raise RuntimeError("Command to start binary must be providen")   
            
            # ===== Start secondary process.
            # Build ad-hoc environ (current environment + modifications) to start other
            # process.
            env = {}
            env.update(os.environ)
            # Ensure installation package directory of sunfluidhbox will be accessible by 
            # other Python interpreder.
            parentdir = osp.dirname(osp.dirname(osp.abspath(__file__)))
            pathlist = (env.get("PYTHONPATH", "")).split(os.pathsep)
            if parentdir not in pathlist:
                pathlist.insert(0, parentdir)
            env["PYTHONPATH"] = os.pathsep.join(pathlist)
            
            # Setup unique communication reference in environment, retrieved by the secondary
            # process to establish communications.
            env[COMREF_ENVVAR] = self.comref

            # Prepare start arguments for command.
            args = self._buildargs()

            logger.debug("Starting control process with %s", args)
            try:
                self.proc = subprocess.Popen(args, env=env, cwd=self.workdir)    
                time.sleep(3)
                if self.proc.returncode is not None:
                    if self.proc.returncode > 0:
                        logger.error("Secondary process returns code %d", self.proc.returncode)
                    else:
                        logger.error("Error %d when starting secondary process", 
                                     -self.proc.returncode)
                    self.proc = None
                    self._cleanup()     # Release pipes / delete pipes files.
                    raise RuntimeError("Error when starting secondary process")
            except:
                logger.exception("Exception when starting secondary process with ", args)
                raise
            logger.info(PROCESSPAIR + " secondary process created with: %s", args)
        
        else:
            # Secondary process may have binary defined, it is ignored.
            pass
        
        # ===== Connect to pipes. 
        # Its is important to do that AFTER starting the other process, as
        # the pipe opening is blocking… until other side of the pipe open it (see comments in
        # pipecom), so opening pipes before the process is a bug causing an interprocess lock.
        self.readpipe, self.writepipe = self._openpipes()

        # If no exception, then we will be able to use pipes for communications.
        self.usable = True
        
        # ===== Wait for pair process to be ready.
        if self.ismain:
            with self.comlock:
                # Receive… (in main process, we wait)
                res = pipecom.readmessage(self.readpipe)
                #print(PROCESSPAIR+":{}".format(res))
            if (type(res) != type(pipecom.SECONDARY_PROCESS_READY)) or \
                (res != pipecom.SECONDARY_PROCESS_READY):
                    logger.error("Problem in secondary->main process notification "
                                 "at secondary startup, received %r", res)
                    raise RuntimeError("Secondary->main process notification failed")
        else:
            with self.comlock:            
                # Send… (in secondary process we inform we are ready)
                pipecom.writemessage(self.writepipe, pipecom.SECONDARY_PROCESS_READY)

        # ===== Both process are ready to start values exchanges.
        logger.debug("Both process ready to communicate")
                
    def _openpipes(self):
        """Adapt pipes opening to box/embeded role.
        """
        # Note: this may be an overriden method in sunclasses, but writing a
        # simple if condition here allow to have pipecom usage only in this 
        # module.
        with self.comlock:            
            if self.embeded:
                return pipecom.openembpipes(self.workdir, self.comref)
            else:
                return pipecom.openboxpipes(self.workdir, self.comref)

    def _buildargs(self):
        """Adapt arguments building to simple string or list of strings.
        """
        # Use binary as a string or a list of strings
        if isinstance(self.binary, str):
            # Split using shell command-line lexical rules.
            return shlex.split(self.binary)
        else: # Consider we have a sequence of values (list, tuple…)
            # Ensure all values are represented as strings.
            return [str(x) for x in list(self.binary)]

    def send_value(self, value):
        """Send a value to pair process.
        
        Systematically send providen value.
        """
        self._check_usable()
        
        if self.stop:
            logger.error(PROCESSPAIR + " write_value() called while stop set")
            # No longer allow echange communications.
            raise RuntimeError("Cannot write value with this method while stop is set")
        
        if type(value) == type(pipecom.TERMINATE_FLAG) and value == pipecom.TERMINATE_FLAG:
            logger.error(PROCESSPAIR + " write_value() called with termination flag")
            # No longer allow echange communications.
            raise RuntimeError("Cannot write value for termination flag with this method")
            
        with self.comlock:            
            try:
                # Send…
                # note: we dont store sent value, it may be associated (via an ndarray) to
                # a Fortran dynamic array, and we dont know this array lifetime.
                logger.info(PROCESSPAIR + " sent value %s", value)
                pipecom.writemessage(self.writepipe, value)
            except:
                logger.exception("Failure in write_value() code")
                raise

    def receive_value(self):
        """Receive a value from pair process.
        
        Check for possible transmission of the stop flag.
        
        If we receive a stop flag, store it and return last received value.
        """
        self._check_usable()
        
        if self.stop:
            logger.error(PROCESSPAIR + " read_value() called while stop set")
            # No longer allow echange communications.
            raise RuntimeError("Cannot read value with this method while stop is set")
        
        with self.comlock:            
            try:
                # Receive…
                res = pipecom.readmessage(self.readpipe)
                #print("EMBEDED:{}".format(res))
                
                self._received_value(res)
                return self.lastreceived
            except:
                logger.exception("Failure in exchange() code, set stop flag to True")
                self.stop = True
                raise

    def _received_value(self, res):
        """Common code to process received values.
        """
        logger.info(PROCESSPAIR + " retrieved value %s", res)
        # Case of stop message exchange.
        if type(res) == type(pipecom.TERMINATE_FLAG) and res == pipecom.TERMINATE_FLAG:
            self.stop = True
        elif type(res) == type(pipecom.USE_LAST_VALUE) and res == pipecom.USE_LAST_VALUE:
            # Used to indicate to use last transmited value (in case of big data transfert, 
            # avoid streaming unchanged data (it is caller responsibility to know if data
            # has changed or not and specify this special value).
            pass
        else:
            self.lastreceived = res
            
    def test_finish(self):
        """Return stop flag with ad-hoc type."""
        if self.embeded:
            # For Fortran code, embeded boolean value is mapped to 0/1 integer.
            return int(self.stop)
        else:
            return self.stop

    def terminate_communication(self):
        """Terminate communications between processes.
        
        The process which initiates the termination send a TERMINATE_FLAG to the
        other process (whatever it be, sunfluidh or control).
        
        For main process, we must wait for secondary process to terminate.
        For secondary process, we just finish properly with pipes and exit.
        """
        # If termination come from us, then send termination instruction to
        # pair process.
        if self.usable and not self.stop:
            self._send_finish()
            
        # Wait for end of secondary process.
        if self.ismain and self.proc:
            # This will _cleanup communication pipes on secondary process side.
            self.proc.wait()

        self._cleanup()        
        
    def _send_finish(self):
        """Send stop flag to pair process.
        """
        self._check_usable()
        if self.sentfinished:
            raise RuntimeError("Trynig to send finished message twice.")

        with self.comlock:
            try:  
                # Send… STOP
                pipecom.writemessage(self.writepipe, pipecom.TERMINATE_FLAG)
                self.sentfinished = True
            except:
                logger.exception("Failure in send_finish() code, set stop flag to True")
                self.stop = True
                raise
      
    def kill_communication(self):
        """Abruptly terminate communications (and pair process if i'm main).
        """
        if self.proc is not None:
            os.kill(self.proc.pid, signal.SIGKILL)
            self.proc = None
        self._cleanup()

    def _cleanup(self):
        """Reset communication tools between processes.

        After pipes close, main process is responsible for pipe files removal.
        """
        self.usable = False
        pipecom.closepipes(self.readpipe, self.writepipe)
        self.readpipe = self.writepipe = None
        
        if self.ismain:
            # Cleanup communication pipes (on my side)
            pipecom.deletepipes(self.workdir, self.comref)
            
        # Release values.
        self.lastreceived = None

