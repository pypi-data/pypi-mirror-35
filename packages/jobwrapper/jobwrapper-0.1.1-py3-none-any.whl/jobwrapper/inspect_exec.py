#!/usr/bin/env python3
"""This module helps to inspect an executable.
In particulare:
1. If it has been compiled with debug option `_g`
2.
"""

import subprocess as sbp
import os.path


def is_debeg(root=b"./", execname=b"lppic", verbose = True):
    """ return True if the executable has been compiled with debug """
    fname = root+execname
    if verbose:
        print("Inspecting the debug option of the executable")
        print("File name:", fname)
        print("=======================")
    if not os.path.isfile(fname) :
        if verbose:
            print("the executable do not existe ! Check your location or arguments")

        return None


    p = sbp.run(["gdb", root+execname], input=b"q",  stdout=sbp.PIPE)
    iout= p.stdout.strip()
    lines = iout.decode('ascii').splitlines()
    #print(iout.decode())
    line = lines[-3]

    info = line[-35:-9]

    if info == "no debugging symbols found":
        if verbose:
            print("The executable is runing without the debug option")
        return False
    else:
        if verbose:
            print("This executable is running with the debug option `-g`")
        return True


if __name__ == "__main__":
    if is_debeg(verbose=True):
        print("True")
    else:
        print("False")
