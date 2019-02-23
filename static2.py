#this is for git
#!/usr/bin/python
import sys
import time
import fontv16 as fontv
import ldp

matrix=[[0 for i in xrange(64)] for i in xrange(16)]

def shiftmatrix():
	for row in range(16):
		for col in range(63,0,-1):
			matrix[row][col]=matrix[row][col-1]

def showmatrix(n):
	getnumber(n)

	for row in range(16):
		for col in range(64):
			ldp.colourshift(matrix[row][col])
		ldp.showrow(row)
	time.sleep(0.001)

ldp.init()

displaywidth=64
totalwidth=0

def getnumber(n):
	colour=2
	textinput=str(n)

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

#while True:
#	try:
#		showmatrix()
#
#	except KeyboardInterrupt:
#		ldp.clear()
#		print "Finished"
#		sys.exit()
