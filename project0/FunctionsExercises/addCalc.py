'''
Addition Calculator¶
Write a function that takes in two numbers, and adds them
together. Make your function print out a sentence showing
the two numbers, and the result.
Call your function with three different sets of numbers.
'''

def addCalc(num1, num2):
    sum = num1 + num2
    print("The inputs were " + str(num1) + " and " + str(num2) + ". The sum of these two is " + str(sum))

addCalc(3, 5)
addCalc(4, 1)
addCalc(35, 72)