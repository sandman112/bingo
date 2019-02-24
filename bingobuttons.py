#!/usr/bin/python

# adapted from https://github.com/recantha/EduKit3-RC-Keyboard/blob/master/rc_keyboard.py

import sys, termios, tty, os, time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

button_delay = 0.11
print "s to start bingo"
print "n for next number"
print "R to reset"
print "l for last 5 numbers"
print "c to check all numbers called"


while True:
    char = getch()
    if (char == "p"):
        print("Stop!")
        exit(0)

    if (char == "s"):
        print("start BINGO")
	GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        time.sleep(button_delay)
	GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    elif (char == "n"):
        print("next number")
	GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        time.sleep(button_delay)
        GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        #time.sleep(button_delay)

    elif (char == "r"):
        print("Reset")
	GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        time.sleep(button_delay)
        GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        #time.sleep(button_delay)

    elif (char == "l"):
        print("Last 5")
	GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        time.sleep(button_delay)
        GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        #time.sleep(button_delay)

    elif (char == "c"):
	print("check numbers")
	GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	time.sleep(button_delay)
	GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    elif (char == "C"):
        print("Number 1 pressed")
        time.sleep(button_delay)
