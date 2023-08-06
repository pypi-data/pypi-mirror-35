#!/usr/bin/python3
# -*- encoding: utf-8 -*-
# File: sunfluidhbox/embed.py
# License: CeCILL-2.1
"""Embedded in sunfluidh code for communication with starter black box.

This module is embedded into Sunfluidh computing code using our forcallpy library.
In case of MPI execution, functions defined here must be called only from "master"
process, not from other parallel computation process.

Environment variables:
    SUNFLUID_PYCOMREF — set by control when control is main
    SUNFLUID_CTRL_COMMAND - must be set when sunfluidh is main, gives the command to
        call for starting control scripts (ex. "python3 ../mypath/controlmain.py")
    SUNFLUID_CTRL_COMMAND_USESHELL - set to 0/1 True/False… to enable/disable use of
        shell when starting the command (enabled by default).
    
:author: Laurent Pointal <laurent.pointal@limsi.fr>
"""
# Note: OpenMPI + Python: https://www.open-mpi.org/faq/?category=running#loading-libmpi-dynamically

# TODO: Package has been modified to allow both sides (sunfluidh or control) to be the
# main program (which starts the other). More code may be factorized.

import logging
import logging.config
import os
import os.path as osp

import numpy as np

from . import processcom

# Setup logging system using embedlog.conf file within current working directory, 
# else use a default debugging with log file.
if osp.isfile("embedlog.conf"):
    logging.config("embedlog.conf")
else:
    FORMAT = '%(asctime)-15s %(name)s - %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.DEBUG, filename='logssunfluidhemb.log',)
logger = logging.getLogger("sunfluidhbox.embed")


# Unique object to manage embedded side communications (package offer a simple
# functional API).
g_emb = None


ENVVAR_COMMAND = "SUNFLUIDH_CTRL_COMMAND"

class Embedded(processcom.ProcessCommunication):
    """Communication path from embedded code in sunfluidh to boxed code in control.
    
    
    
    :ivar int stop: Flag for Fortran code (this is why we use an integer in place of a bool).
    :ivar bool ismain: Flag to indicate that sunfluidh is main process (starts control code).
    """
    def __init__(self, controlcmde=None):
        global g_emb
        super().__init__(embeded=True,
                 workdir=None,
                 binary=controlcmde)
        
    def prepare_computing_iteration(self, probesvalues):
        """Prepare one computing iteration, called at begin of computing loop.
        
        Once this function has been called, you must call test_finish() method
        and exit computation loop if its true.
        """
        self.send_value(probesvalues)   # Send probes
        self.receive_value()            # Receive actuator (or stop flag)
        
    def lastcontrol(self) -> np.ndarray:
        """Retrieve last value of control.
        """
        return self.lastreceived
        
    
# ===== Define a simple function-like API for Fortran =====================

def prepare_communication(controlcmde=None):
    """Start code to call at begin of sunfluidh.
    """
    global g_emb
    if controlcmde is None:
        try:
            controlcmde = os.environ.get(ENVVAR_COMMAND)
        except KeyError:
            # let controlcmde be None (maybe sunfluidh is the secondary process)
            pass
    g_emb = Embedded(controlcmde)
    g_emb.prepare_communication()
    
    
def terminate_communication():
    """Finish code to call at end of sunfluidh.
    
    forcallpy:
    
    Simple function to call, no parameter, no return value.
    """
    global g_emb
    g_emb.terminate_communication()
    del g_emb  # No longer usable!
    

def prepare_computing_iteration(vect: np.ndarray):
    """Called to compute and retrieve next control value.
    
    forcallpy:
    
    - vect as xv float array (readonly, transmit probes values)
    - outvect as xw float array (writable, return actuator values)
    """
    g_emb.prepare_computing_iteration(vect)


def lastcontrol(outvect: np.ndarray):
    """Return last available value of control into its parameter.
    """
    ctrlval = g_emb.lastcontrol()
    for i,v in enumerate(ctrlval):
        outvect[i] = v


def test_finish() -> int:
    """Test if must finish sunfluidh process.
    
    This shoud be tested just after retrieving a control value, as it is
    the only time where control process can send the termination indication.
    When its true, sunfluidh must exit its computing loop and simply
    call the terminate_communication() function.
    
    forcallpy:
    
    - returns 1 if yes, else 0 (not bool typed values)
    """
    return g_emb.test_finish()
