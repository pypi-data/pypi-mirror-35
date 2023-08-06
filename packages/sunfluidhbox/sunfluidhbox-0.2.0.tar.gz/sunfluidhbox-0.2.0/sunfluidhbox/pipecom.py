#!/usr/bin/python3
# -*- encoding: utf-8 -*-
# File: sunfluidhbox/pipecom.py
# License: CeCILL-2.1
"""Pipes communication between box and embeded.

Messages sent via pipes are packed into binary representation. The message
start by a 4 bytes unsigned int containing binary data length, followed
by pickled version of data.

Note: this fail if message length is over pipe buffer size (generally ~4kb), in
such case nsteps() in box interlock with control() in embed.

:author: Laurent Pointal <laurent.pointal@limsi.fr>
"""
# Blocking at pipe open… need O_NONBLOCK option (os.xxx level), or need to have
# pipe opened at other side to unblock opening process.
# https://stackoverflow.com/questions/5782279/why-does-a-read-only-open-of-a-named-pipe-block


import logging
import os
import os.path as osp
import pickle
import struct

import numpy as np

logger = logging.getLogger("sunfluidhbox.pipecom")

# Remaining option of the time my process locked when opening pipes.
# Can choose to use high level (open()) or low level (os.open()) pipes access.
USE_OS = True

# Messages sent from sunfluidh secondary process to main process.
SECONDARY_PROCESS_READY = b"secondary process ready"

# Message sent from box to sunfluidh embedded.
TERMINATE_FLAG = b"terminate"
USE_LAST_VALUE = b"use last value"

# Complement information for logs (setup when opening pipes).
WHEREIAM = ""


def emb2boxname(pipesdir: str, uuid: str):
    """Build name of pipe for embedded to box communications."""
    return osp.join(pipesdir, "pipe_emb2box-" + uuid)


def box2embname(pipesdir: str, uuid: str):
    """Build name of pipe for box to embedded communications."""
    return osp.join(pipesdir, "pipe_box2emb-" + uuid)


def createpipes(pipesdir: str, uuid: str):
    """Create named pipes files."""
    if not osp.isfile(emb2boxname(pipesdir, uuid)):
        os.mkfifo(emb2boxname(pipesdir, uuid))
    if not osp.isfile(box2embname(pipesdir, uuid)):
        os.mkfifo(box2embname(pipesdir, uuid))


def deletepipes(pipesdir: str, uuid: str):
    """Delete names pipes files."""
    os.remove(emb2boxname(pipesdir, uuid))
    os.remove(box2embname(pipesdir, uuid))


def openembpipes(pipesdir: str, uuid: str) -> tuple:
    """Return read,write pipes for embedded."""
    global WHEREIAM
    WHEREIAM = "Embeded"
    if USE_OS:
        r = os.open(box2embname(pipesdir, uuid), os.O_RDONLY | os.O_SYNC)
        w = os.open(emb2boxname(pipesdir, uuid), os.O_WRONLY | os.O_SYNC)
    else:
        r = open(box2embname(pipesdir, uuid), "rb", buffering=0)
        w = open(emb2boxname(pipesdir, uuid), "wb", buffering=0)
    return r, w


def openboxpipes(pipesdir: str, uuid: str) -> tuple:
    """Return read,write pipes for box."""
    # Important: open box2embname before emb2boxname as in openembpipes(), so that
    # there is not an interlocking between the two (box and emb) process.
    # And ensure starting external fortran process *before* opening pipes
    # (as it is the process which open pipes on the other side).
    # This is necessary to avoir process locking (alternative seeem to open
    # non-blocking and then to change the file option flag via fcntl…).
    global WHEREIAM
    WHEREIAM = "Box"
    if USE_OS:
        w = os.open(box2embname(pipesdir, uuid), os.O_WRONLY | os.O_SYNC)
        r = os.open(emb2boxname(pipesdir, uuid), os.O_RDONLY | os.O_SYNC)
    else:
        w = open(box2embname(pipesdir, uuid), "wb", buffering=0)
        r = open(emb2boxname(pipesdir, uuid), "rb", buffering=0)
    return r, w


def closepipes(r, w):
    """Close both read,write pipes."""
    if r is not None:
        if USE_OS:
            os.close(r)
        else:
            r.close()
    if w is not None:
        if USE_OS:
            os.close(w)
        else:
            w.close()


# Note: Read/write of message bytes from/to the pipe may eventually use
# multiple calls to low level read/write functions.
# This allows to transmit chunk of data larger than pipes system buffers.
def _readpipe(r, n):
    """Read whole binary message of size n from the pipe r."""
    m = b''
    while len(m) < n:
        if USE_OS:
            m += os.read(r, n-len(m))
        else:
            m += r.read(n-len(m))
    return m
    
    
def _writepipe(w, m):
    """Write whole binary message m to the pipe w."""
    remain = len(m)
    while remain > 0:
        if USE_OS:
            remain = remain - os.write(w, m[-remain:])
        else:
            remain = remain - w.write(m[-remain:])
        

# Care: Quote from include/linux/pipe_fs_i.h:
# /* Differs from PIPE_BUF in that PIPE_SIZE is the length of the actual
#    memory allocation, whereas PIPE_BUF makes atomicity guarantees.  */
def readmessage(r):
    """Read one message via the pipe."""
    # 4 bytes containing message size.
    sizeheader = _readpipe(r, 4)
    #logger.debug(WHEREIAM + " Read length bytes: %r", sizeheader)
    datasize = struct.unpack('I', sizeheader)[0]
    #logger.debug(WHEREIAM + " Data length: %d", datasize)
    # Remaining of message (eventually in multiple calls)
    databytes = _readpipe(r, datasize)
    #logger.debug(WHEREIAM + " Read data bytes: %r", databytes)
    data = pickle.loads(databytes)
    logger.debug(WHEREIAM + " Read message: %s", data)
    return data


def writemessage(w, data):
    """Write one message via the pipe."""
    logger.debug(WHEREIAM + " Write message: %s", data)
    databytes = pickle.dumps(data)
    sizeheader = struct.pack('I', len(databytes))
    #logger.debug(WHEREIAM + " Write bytes (length+data): %r", databytes)
    msg = sizeheader + databytes
    _writepipe(w, msg)

