#!/usr/bin/python
#import fontv16 as fontv
#test updated file update 2
import static2
from subprocess import Popen
import imp
import RPi.GPIO as gpio
import random
from time import sleep
from threading import Thread as thread

def show(n)
	static2

t=thread(target=show, args=(n,))
threads.append(t)

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
	t.start()
	#static2.showmatrix(n)
	#Popen(["./static.py", str(n)])
	sleep (2)
	print "clearing"
	static2.ldp.clear()
	#Popen(["pkill", "static.py"])
	sleep(0.5)

