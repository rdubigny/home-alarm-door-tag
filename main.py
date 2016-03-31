#!/usr/bin/env python3.5

import time
import RPi.GPIO as io

from modules import logger
from modules.message import Message
from modules.counter import Counter

message = Message()
counter = Counter()

io.setmode(io.BCM)

door_pin = 23
vibration_pin = 25

io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)
io.setup(vibration_pin, io.IN, pull_up_down=io.PUD_UP)


def opened_callback(channel):
    message.send('door opened')


def hit_callback(channel):
    if counter.incr():
        message.send('door hit')

io.add_event_detect(door_pin, io.RISING, callback=opened_callback, bouncetime=2000)
io.add_event_detect(vibration_pin, io.RISING, callback=hit_callback, bouncetime=500)

logger.logger.info('TAG LISTENING!')

while True:
    time.sleep(1)
