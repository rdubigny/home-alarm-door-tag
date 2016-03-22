#!/usr/bin/env python3.4

import time
import RPi.GPIO as io

from modules.message import Message

message = Message()

io.setmode(io.BCM)

door_pin = 23

io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)  # activate input with PullUp

while True:
    if io.input(door_pin):
        message.send("door opened")
    time.sleep(0.5)
