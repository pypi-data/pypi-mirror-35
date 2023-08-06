#!/usr/bin/python3
# -*- encoding: utf-8 -*-
# File: sunfluidhbox/box.py
# License: CeCILL-2.1
"""Wrapper class for start/stop and communications with sunfluidh.

:author: Laurent Pointal <laurent.pointal@limsi.fr>

Environment variables:
    SUNFLUID_PYCOMREF — set by sunfluidh when sunfluidh is main
"""

# http://www.roman10.net/2011/04/21/named-pipe-in-linux-with-a-python-example/



import atexit
import logging
import logging.config
import os
import os.path as osp
import signal
import threading

import numpy as np

from . import processcom

# Setup logging system using boxlog.conf file within current working directory, 
# else use a default debugging with log file
if osp.isfile("boxlog.conf"):
    logging.config("boxlog.conf")
else:
    FORMAT = '%(asctime)-15s %(name)s - %(message)s'
    logging.basicConfig( format=FORMAT, level=logging.DEBUG, filename='logssunfluidhbox.log',)
logger = logging.getLogger("sunfluidhbox.box")

g_boxes_mutex = threading.Lock()
g_boxes = []


class SunFluidh(processcom.ProcessCommunication):
    """Simple class which wraps sunfluidh start/stop and communications into a methods API.
    
    Configuration file directory is used as current working directory when starting
    sunfluidh.
    
    :ivar str comref: uuid used to identify pipes.
    :ivar bool ismain: boolean indicating that control is main program.
    :ivar bool stop: boolean indicating that a stop request has been received
    :ivar ndarray lastvect: last value sent by sunfluidh
    :ivar comlock: lock around communications in case of multiprocessing.
    :ivar workdir: path of configuration file.
    :ivar sfpath: path of sunfluid binary.
    :ivar proc: process manipulation object (Pipe).
    """
    def __init__(self, *,
                 ctrlinit: np.ndarray=np.zeros(10),
                 workdir: str, 
                 binary: str="sunfluidh"
                 ):
        """
        One loop compute n steps, then wait for the controling process to do its stuff
        before transmitting a new control parameter and request several new steps.
       
        :param ctrlinit: initial value of control.
        :param workdir: path to directory containing configuration file for sunfluidh.
        :param binary: path to start sunfluidh binary.
        :param mpi: flag to enable use of MPI when starting sunfluidh.
        """
        super().__init__(embeded=False,
                 workdir=workdir,
                 binary=binary)
        with g_boxes_mutex:
            g_boxes.append(self)
                   
    def before_computing(self):
        """Called before control value computation.
        
        Retrieve last value from sunfluidh probes. 
        """
        self.receive_value()
        # Caller must use 
        #   test_finish() method to know if it must exit computing loop
        #   lastvector() method to retrieve the vector used for computing control

    def after_computing(self, newcontrol):
        """Called at end of computing to send new control value.
        """
        self.send_value(newcontrol)
            
    def lastvector(self) -> np.ndarray:
        """Return last vector
        """
        return self.lastreceived

    def terminate_communication(self, *args):
        """Remove box from active ones and terminate normally communications.
        """
        with g_boxes_mutex:
            g_boxes.remove(self)
        super().terminate_communication(*args)

# ===== Install Cltr-C signal handling =====================================
g_prev_handler = None
def ctrl_c_handler(*args):
    with g_boxes_mutex:
        for box in g_boxes:
            try:
                box.kill_communication()
            except:
                logger.exception("Error in ctrl-c handler")    
        g_boxes.clear()
    if callable(g_prev_handler):
        g_prev_handler(*args)
        
g_prev_handler = signal.getsignal(signal.SIGINT)
signal.signal(signal.SIGINT, ctrl_c_handler)      

# ===== Install normal exit handling ======================================
# In case caller miss to correcly cleanup (and properly stop communications)
def atexit_handler():
    with g_boxes_mutex:
        for box in g_boxes:
            try:
                box.kill_communication()
            except:
                logger.exception("Error in atexit handler")
        g_boxes.clear()
atexit.register(atexit_handler)

