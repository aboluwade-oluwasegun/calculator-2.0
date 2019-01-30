'''
This calculator would be able to perform simple 
arithmetic operations as well as statistical calclulations
'''

from tkinter import *
import math
import numpy
from scipy import stats
import statistics


#initialize GUI
gui = Tk()

#set GUI title
gui.title('Python Calc')

#set GUI background color
gui.configure(background = '#89d5bc')

#initialize the expression variable
expression = ''

#list to hold numbers for statistical calculations
nums = []

#list to hold numbers for display purposes
numsCopy = []

#set text in the expression display to accept strings
equationE = StringVar()

#set text in the result display to accept strings
equationR = StringVar()

#create and position the expression display
displayE = Entry(width=32, font="Arial 15 bold", bg = '#e6f353', justify=RIGHT, textvariable=equationE)
displayE.grid(column=0, row=0, columnspan=6)

#create and position the result display
displayR = Entry(width=32, font="Arial 15 bold", bg = '#e6f353', justify=RIGHT, textvariable=equationR)
displayR.grid(column=0, row=1, columnspan=6)

#set the default display to 0
displayR.insert(0, '0')

#create radio buttons and position them
v = IntVar() #holds integer value for the radio buttons

simpleCalc = Radiobutton(gui, text="Simple", variable=v, value=1, height=1, width=20, bg='#f0c0c0', fg='#926c34', command=lambda: enableDisable())
simpleCalc.grid(column=0, row=2, padx=5, pady=5, columnspan=3)
v.set(1)

statCalc = Radiobutton(gui, text="Stats", variable=v, value=2, height=1, width=20, bg='#f0c0c0', fg='#926c34', command=lambda: enableDisable())
statCalc.grid(column=3, row=2, padx=5, pady=5, columnspan=3)

#create the other buttons and position them using grid
b1 = Button(gui, text='1', height=1, width=5, bg='#96b371', command=lambda: printChar(1))
b1.grid(column=0, row=6, sticky=W+E, padx=2, pady=2)

b2 = Button(gui, text='2', height=1, width=5, bg='#96b371', command=lambda: printChar(2))
b2.grid(column=1, row=6, sticky=W+E, padx=2, pady=2)

b3 = Button(gui, text='3', height=1, width=5, bg='#96b371', command=lambda: printChar(3))
b3.grid(column=2, row=6, sticky=W+E, padx=2, pady=2)

b4 = Button(gui, text='4', height=1, width=5, bg='#96b371', command=lambda: printChar(4))
b4.grid(column=0, row=5, sticky=W+E, padx=2, pady=2)

b5 = Button(gui, text='5', height=1, width=5, bg='#96b371', command=lambda: printChar(5))
b5.grid(column=1, row=5, sticky=W+E, padx=2, pady=2)

b6 = Button(gui, text='6', height=1, width=5, bg='#96b371', command=lambda: printChar(6))
b6.grid(column=2, row=5, sticky=W+E, padx=2, pady=2)

b7 = Button(gui, text='7', height=1, width=5, bg='#96b371', command=lambda: printChar(7))
b7.grid(column=0, row=4, sticky=W+E, padx=2, pady=2)

b8 = Button(gui, text='8', height=1, width=5, bg='#96b371', command=lambda: printChar(8))
b8.grid(column=1, row=4, sticky=W+E, padx=2, pady=2)

b9 = Button(gui, text='9', height=1, width=5, bg='#96b371', command=lambda: printChar(9))
b9.grid(column=2, row=4, sticky=W+E, padx=2, pady=2)

b0 = Button(gui, text='0', height=1, width=5, bg='#96b371', command=lambda: printChar(0))
b0.grid(column=0, row=7, sticky=W+E, padx=2, pady=2)

mean = Button(gui, text='Mean', height=1, width=5, bg='#ffb444', fg='#33230a', state=DISABLED, command=lambda: meanF())
mean.grid(column=0, row=3, sticky=W+E, padx=2, pady=2)

median = Button(gui, text='Median', height=1, width=5, bg='#ffb444', fg='#33230a', state=DISABLED, command=lambda: medianF())
median.grid(column=1, row=3, sticky=W+E, padx=2, pady=2)

mode = Button(gui, text='Mode', height=1, width=5, bg='#ffb444', fg='#33230a', state=DISABLED, command=lambda: modeF())
mode.grid(column=2, row=3, sticky=W+E, padx=2, pady=2)

standardDev = Button(gui, text='Std Dev', height=1, width=5, bg='#ffb444', fg='#33230a', state=DISABLED, command=lambda: standardDevF())
standardDev.grid(column=3, row=3, sticky=W+E, padx=2, pady=2)

variance = Button(gui, text='Var', height=1, width=5, bg='#ffb444', fg='#33230a', state=DISABLED, command=lambda: varianceF())
variance.grid(column=4, row=3, sticky=W+E, padx=2, pady=2)

clear = Button(gui, text='Clear', height=1, width=5, bg='#aaaad3', command=lambda: clear())
clear.grid(column=5, row=4, sticky=N+S+W+E, padx=2, pady=2, rowspan=2)

delete = Button(gui, text='Del', height=1, width=5, bg='#aaaad3', command=lambda: delete())
delete.grid(column=5, row=6, sticky=N+S+W+E, padx=2, pady=2, rowspan=2)

plus = Button(gui, text='+', height=1, width=5, command=lambda: printChar('+'))
plus.grid(column=3, row=4, sticky=W+E, padx=2, pady=2)

factorial = Button(gui, text='!', height=1, width=5, bg='#aaaad3', command=lambda: ops(factorial))
factorial.grid(column=3, row=8, sticky=W+E, padx=2, pady=2)

minus = Button(gui, text='-', height=1, width=5, command=lambda: printChar('-'))
minus.grid(column=3, row=5, sticky=W+E, padx=2, pady=2)

push = Button(gui, text='\u21E8', height=1, width=5, bg='#ffb444', state=DISABLED, command=lambda: pushF())
push.grid(column=5, row=3, sticky=W+E, padx=2, pady=2)

log = Button(gui, text='log', height=1, width=5, bg='#f2635f', command=lambda: ops(log))
log.grid(column=4, row=5, sticky=W+E, padx=2, pady=2)

sin = Button(gui, text='sin', height=1, width=5, bg='#f2635f', command=lambda: ops(sin))
sin.grid(column=4, row=6, sticky=W+E, padx=2, pady=2)

cos = Button(gui, text='cos', height=1, width=5, bg='#f2635f', command=lambda: ops(cos))
cos.grid(column=4, row=7, sticky=W+E, padx=2, pady=2)

tan = Button(gui, text='tan', height=1, width=5, bg='#f2635f', command=lambda: ops(tan))
tan.grid(column=4, row=4, sticky=W+E, padx=2, pady=2)

multiply = Button(gui, text='x', height=1, width=5, command=lambda: printChar('*'))
multiply.grid(column=3, row=6, sticky=W+E, padx=2, pady=2)

squareRoot = Button(gui, text='\u221A', height=1, width=5, bg='#aaaad3', command=lambda: ops(squareRoot))
squareRoot.grid(column=4, row=8, sticky=W+E, padx=2, pady=2)

power = Button(gui, text='^', height=1, width=5, bg='#aaaad3', command=lambda: printChar('**'))
power.grid(column=5, row=8, sticky=W+E, padx=2, pady=2)

decimal = Button(gui, text='.', height=1, width=5, command=lambda: printChar('.'))
decimal.grid(column=1, row=7, sticky=W+E, padx=2, pady=2)

plusMinus = Button(gui, text='-/+', height=1, width=5, command=lambda: plusMinus())
plusMinus.grid(column=2, row=7, sticky=W+E, padx=2, pady=2)

divide = Button(gui, text='/', height=1, width=5, command=lambda: printChar('/'))
divide.grid(column=3, row=7, sticky=W+E, padx=2, pady=2)

equal = Button(gui, text='=', height=1, width=5, command=lambda: equals())
equal.grid(column=0, row=8, sticky=W+E, padx=2, pady=2, columnspan=3)

#function to handle buttons
def printChar(num):
	global expression #show python that we meant the expression in the global scope

	expression = expression + str(num)
	#update the display
	equationE.set(expression)

def equals():
	# Try and except statement is used for handling the errors like zero
	# division error etc.

	try:

		global expression

		if (expression != ''):

			total = str(eval(expression))

			equationR.set(total)

		# initialze the expression variable
		# by empty string
		expression = ''

	# if any error is generated then handle with the except block
	except:

		equationR.set('error')
		expression = ''

#handle -/+
def plusMinus():
	global expression
	expression = -(float(expression))
	equationE.set(expression)

#handle clear
def clear():
	global expression
	global nums
	global numsCopy
	expression = ''
	equationE.set('')
	equationR.set(0)
	nums = []
	numsCopy = []

def ops(button):
	global expression
	#get the value of the text on the ops button
	text = button.cget('text')

	#this function updates the expression display with the calculation made
	def updateE(text):
		init = equationE.get()
		equationE.set(text + ' ' + init)

	#calculate log
	if (text == 'log'):
		expression = math.log(int(expression))
		equationR.set(expression)
		updateE(text)
	#calculate sine
	if (text == 'sin'):
		expression = math.sin(int(expression))
		equationR.set(expression)
		updateE(text)
	#calculate cos
	if (text == 'cos'):
		expression = math.cos(int(expression))
		equationR.set(expression)
		updateE(text)
	#calculate tan
	if (text == 'tan'):
		expression = math.tan(int(expression))
		equationR.set(expression)
		updateE(text)
	#calculate factorial
	if (text == '!'):
		init = equationE.get()
		expression = math.factorial(int(expression))
		equationR.set(expression)
		equationE.set(init + '!')
	#calculate squareroot
	if (text == '\u221A'):
		init = equationE.get()
		expression = math.sqrt(int(expression))
		equationR.set(expression)
		equationE.set('root of '+ init)

#handle the delete key
def delete():
	global expression
	expression = expression[:-1]
	equationE.set(expression)
	if(expression == ''):
		equationE.set(0)

def pushF():
	global nums
	global expression
	global numsCopy


	num = equationE.get()
	numsCopy.append(num)
	nums.append(int(num))
	numsString =','.join(numsCopy)
	equationR.set(numsString)
	equationE.set('')
	expression = ''


def meanF():
	global nums
	m = ''
	result = numpy.mean(nums)
	for i in nums:
		m = m + str(i) + ' '
	equationE.set('mean( '+ m + ')') #the user can see the operation they just performed
	equationR.set(result)


def medianF():
	global nums
	m = ''
	result = numpy.median(nums)
	for i in nums:
		m = m + str(i) + ' '
	equationE.set('median( '+ m + ')') #the user can see the operation they just performed
	equationR.set(result)

def modeF():
	global nums
	m = ''
	result = stats.mode(nums)
	for i in nums:
		m = m + str(i) + ' '
	equationE.set('mode( '+ m + ')') #the user can see the operation they just performed
	for i in result[0]:
		equationR.set(i)

def standardDevF():
	global nums
	m = ''
	result = statistics.stdev(nums)
	for i in nums:
		m = m + str(i) + ' '
	equationE.set('Standard Dev( '+ m + ')')
	equationR.set(result)


def varianceF():
	global nums
	m = ''
	result = numpy.var(nums)
	for i in nums:
		m = m + str(i) + ' '
	equationE.set('Variance( '+ m + ')')
	equationR.set(result)

#configure the button states(active or inactive)
def setState(button):
	if v.get() == 1:
		button.config(state=DISABLED)
	if v.get() == 2:
		button.config(state=NORMAL)

#call setState(button) on all necessary buttons
def enableDisable():
	setState(mean)
	setState(median)
	setState(mode)
	setState(standardDev)
	setState(variance)
	setState(push)


#start GUI

gui.mainloop()
