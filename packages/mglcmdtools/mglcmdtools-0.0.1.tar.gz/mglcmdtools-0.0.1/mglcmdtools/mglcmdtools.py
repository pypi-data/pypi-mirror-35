#!/usr/bin/env python3
import subprocess
import sys
import os
import time

def rm_and_mkdir(directory, force=False):
    '''
    create the `directory`. 

    If it already exists, when `force=True`, will forcely delete the `directory` and recreate it, otherwise, do nothing and return `None`.

    '''

    if os.path.exists(directory):
        if force:
            cmd = 'rm -rf {0}'.format(directory)
            subprocess.check_output(cmd, shell=True)
        else:
            print(directory, 'already exists!', file=sys.stderr)
            return None

    os.mkdir(directory)

    return directory


def runcmd(command, verbose=False):
    '''
    Run `command`. if `verbose`, print time, and command content to stdout.

    Will 
    '''
    try:
        if verbose:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S",
                                            time.localtime(time.time()))
            print(current_time, "\n", command, "\n", sep="", flush=True)
        subprocess.check_output(command, shell=True)

    except Exception as e:
        print(e, file=sys.stderr)
        raise RuntimeError("Error occured when running command:\n{0}".format(command))

    return command
