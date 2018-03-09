#!/usr/bin/env python3
import sys
import subprocess
from math import cos, sin, pi
from time import time, sleep


def current_millis():
    return int(round(time() * 1000))


def easing_out_sin(curr, start, dx, dur):
    return dx * sin((curr/dur) * (pi/2)) + start


def easing_in_sin(curr, start, dx, dur):
    return -dx * cos((curr/dur) * (pi/2)) + dx + start


def easing_executor(total, dur, start, end, fn):
    curve = [start]
    for i in range(dur, total+dur, dur):
        curve.append(fn(i, start, end-start, total))
    return curve


def save_brightness_cmd():
    subprocess.run("brightnessctl -s", shell=True,
                    stdout=subprocess.DEVNULL)


def set_brightness_cmd(value):
    subprocess.run("brightnessctl s {}".format(value), shell=True, 
                    stdout=subprocess.DEVNULL)


def get_max_brightness_cmd():
    return int(subprocess.check_output("brightnessctl m", shell=True))


def get_current_brightness_cmd():
    return int(subprocess.check_output("brightnessctl g", shell=True))


def dim(percentage=20, millis=1000, interval=10, save=True):
    cur_brightness = get_current_brightness_cmd()
    if save:
        save_brightness_cmd()
    target = int((cur_brightness * (percentage / 100)))
    values = easing_executor(millis, interval, cur_brightness, target, easing_out_sin)
    for value in values:
        set_brightness_cmd(value)
        sleep(interval / 1000) # Uses seconds


def main():
    dim()


if __name__ == "__main__":
    main()