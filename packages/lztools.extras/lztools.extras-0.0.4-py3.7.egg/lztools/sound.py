import os
import time
from subprocess import call

def beep(duration=0.4, freq=440):
    call(["play", "--no-show-progress", "--null", "--channels", "2", "synth", str(duration), "sine", str(freq)])
    # os.system('play --no-show-progress --null --channels 2 synth %s sine %f' % (duration, freq))

def beep_on_off(length, duration=0.4, freq=440):
    while length > 0:
        beep(duration, freq)
        time.sleep(duration)
        length -= duration * 2