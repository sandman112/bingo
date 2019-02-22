#!/usr/bin/python
import RPi.GPIO as gpio
import random
from time import sleep


print "hello"
num=[]
for x in range (1,91):
	num.append(x)
while len(num)>0:
	n=random.choice(num)
	print n
	if n<10:
		print "on its own number %d" %n
	else:
		digit=list(str(n))
		if (digit[0]==digit[1]):
			print "All the %s's .... %d" %(digit[0],n)
		else:
			print "%s and %s .... %d" %(digit[0], digit[1], n)
	p=num.index(n)
	num.pop(p)
	sleep (0.01)
	print "\n\n"
