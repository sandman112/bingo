#!/usr/bin/python
import sys
from time import sleep
import fontv16 as fontv
import ldp
import random
from threading import Thread
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(True)
GPIO.setup(35, GPIO.IN)
GPIO.setup(37, GPIO.IN)
GPIO.setup(33, GPIO.IN)

matrix=[[0 for i in xrange(64)] for i in xrange(16)]

def shiftmatrix():
	for row in range(16):
		for col in range(63,0,-1):
			matrix[row][col]=matrix[row][col-1]

def showmatrix(n):
	getnumber(n)
	while GPIO.input(35)==0 and GPIO.input(37)==0 and GPIO.input(37)==0:
		for row in range(16):
			for col in range(64):
				ldp.colourshift(matrix[row][col])
			ldp.showrow(row)
		sleep(0.001)
	getnumber("CLEANUP")
ldp.init()

displaywidth=64
totalwidth=0

def getnumber(n):
	if n=="CLEANUP":
		colour=0
	else:
		colour=2
	if type(n)==int:
		textinput=str(n)
	else:
		textinput=n

	inputarray=[]
	for char in textinput:
		inputarray.append(ord(char))
	dotarray=[[] for i in xrange(64)]

	for row in range(16):
		for ascii in inputarray:
			width=fontv.array[ascii][0]
			binary='{0:{fill}{align}{width}{base}}'.format(fontv.array[ascii][row+1],base='b',fill='0',align='>',width=width)
			for digit in range(width):
				if binary[digit] == '0':
					dotarray[row].append(0)
				else:
					dotarray[row].append(colour)

	totalwidth=len(dotarray[0])

	offset=int((displaywidth - totalwidth) / 2)

	for col in range(offset):
		for row in range(16):
			matrix[row][col]=0
	for col in range(totalwidth):
		for row in range(16):
			matrix[row][offset+col]=(dotarray[row][col])

status=1

num=range(1,91)
called=[]
disp="Start"

while True:
	sleep(0.01)
	try:
		showmatrix(disp)
		if GPIO.input(35)==1: #next number button
			if len(num)>0:
				n=random.choice(num)
				if n<10:
					print "On its own number %d\n\n" %n
				else:
					digit=list(str(n))
					if (digit[0]==digit[1]):
						print "all the %s's ... %d\n\n" %(digit[0], n)
					else:
						print "%s and %s ... %d\n\n" %(digit[0], digit[1], n)
				p = num.index(n)
				num.pop(p)
				called.append(n)
				disp = n
				sleep(0.3)
				#print called
				#print len(called)
		if GPIO.input(37)==1: #reset the game back to the begining
			called=[]
			num=range(1,91)
			print "Reseting game"
			status=0
			disp="Start"
			print num
			sleep(1)
		#if GPIO.input(37)==1: #this is the last 5 numbers called ... dunno if this feature will remain
		#	sleep(0.3)
		#	count=len(called)
		#	if count<5:
		#		for i in range(count):
		#			disp=called[i]
		#			sleep(0.3)
		#			showmatrix(disp)
		#	else:
		#		for i in range(count-5,count):
		#			disp=called[i]
		#			sleep(0.3)
		#			showmatrix(disp)

	except KeyboardInterrupt:
		ldp.clear()
		sys.exit()
#while True:
#	try:
#		showmatrix()
#
#	except KeyboardInterrupt:
#		ldp.clear()
#		print "Finished"
#		sys.exit()
