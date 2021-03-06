#!/usr/bin/python
import sys
import time
import fontv16 as fontv
import ldp
import RPi.GPIO as GPIO
GPIO.setup(33,GPIO.IN)

# the matrix is a representation of the led's that are lit on the 80x8 display
#
matrix=[[0 for i in xrange(64)] for i in xrange(16)]
#
# function to shift left all the vaules of the matrix array
# this allows us to put new data in the first column
#
def shiftmatrix():
	for row in range(16):
		for col in range(63,0,-1):
			matrix[row][col]=matrix[row][col-1]
# end def

# function to read the matrix array and output the values to the display device
#
def showmatrix():
	for row in range(16):
		for col in range(64):
			#if ((matrix[row][col])==2):
			#	print (matrix[row][col]),
			#else:
			#	print " ",
			ldp.colourshift(matrix[row][col])
		#print ""
		ldp.showrow(row)
# end def

#
# Main
#
# initialise the display
#
ldp.init()

displaywidth=64
totalwidth=0
#
# assign the command line args for the text and colour
#
textinput=str(sys.argv[1])
colour=2


# save the ascii values of the input characters into the inputarray 
# the font module uses the ascii value to index the font array
inputarray=[]
for char in textinput:
	inputarray.append(ord(char))

# dotarray is  8 X n
# n is determined by the number of characters multiplyed by 8 
# n will be len(dotarray[0]) after filling dotarray from characters
# in the inputarray
#
dotarray=[[] for i in xrange(64)]
#
# fill the dot array with the colour digits
# this is the dot pattern that we want to show
#
for row in range(16):
	for ascii in inputarray:
		# get the width of the character from the first element of the font variable
		width=fontv.array[ascii][0]
		binary='{0:{fill}{align}{width}{base}}'.format(fontv.array[ascii][row+1],base='b',fill='0',align='>',width=width)
		#binary='{0:0>{width}h}'.format(fontv.array[ascii][row+1],base='b',fill='0',align='>',width=width)
		#print binary
		for digit in range(width):
			if binary[digit] == '0':
				dotarray[row].append(0)
			else:
				dotarray[row].append(colour)


totalwidth=len(dotarray[0])
if totalwidth > displaywidth:
	print 'Message is Larger than the Display'
	sys.exit()

offset=int((displaywidth - totalwidth) / 2)

# Fill the matrix initially with offset spaces to centre align the message
#
for col in range(offset):
	for row in range(16):
		matrix[row][col]=0
# now fill the rest of the matrix with the dotarray
for col in range(totalwidth):
	for row in range(16):
		# copy the current dotarray column values to the first column in the matrix
		matrix[row][offset+col]=(dotarray[row][col])

#
# Continually output to the display until Ctrl-C
#
while True:
	try:
		# now that we have updated the matrix lets show it
		showmatrix()
		if GPIO.input(33)==1:
			print "222"
			ldp.clear()
		#time.sleep(0.0001)

	except KeyboardInterrupt:
		ldp.clear()
		print "Finished"
		sys.exit()
