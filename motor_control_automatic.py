#!/usr/bin/python

"""

Copyright (c) 2023 Kieran Aponte
This software is licensed under the MIT License.

"""

import pigpio
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


pi = pigpio.pi()
pi.set_mode(25, pigpio.OUTPUT)

pi.set_mode(24, pigpio.OUTPUT)

CLK  = 11
MISO = 9
MOSI = 10
CS   = 8
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
bias = -200

print ("mode: ", pi.get_mode(25))


    
pw = 1500
while True:
    try:
        value = mcp.read_adc(0)
        print(value)
        if value < 600: #extend
            pw -= 1
        elif value < 1023: #neutral
            pass
        elif value >= 1023: #flex
            pw += 1
        
        if pw < 1500:
            pw = 1500
        elif pw > 2200:
            pw = 2200
            
        pi.set_servo_pulsewidth(25, pw + bias)
        pi.set_servo_pulsewidth(24, pw + bias)
    except KeyboardInterrupt:
        print('breaking')
        pi.set_servo_pulsewidth(25, 0)
        pi.set_servo_pulsewidth(24, 0)
        pi.stop()
        break










