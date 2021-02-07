'''soundstretch.py'''

import subprocess
import os

def soundstretch(inFile: str, outFile: str, speed=1.):

    speed = (speed / 1) * 100

    # 3.5   ->  250
    # 3     ->  200
    # 2.5   ->  150
    # 2     ->  100
    # 1.5   ->  50
    # 1     ->  0    [YES]
    # 0.5   -> -50
    # 0.25  -> -100
    # 0.125 -> -150


    dirPath = os.path.dirname(os.path.realpath(__file__))


    subprocess.check_output([f'{dirPath}/audiotsm2/mac-soundstretch/bin/soundstretch',
        inFile, outFile, f'-tempo=250'])