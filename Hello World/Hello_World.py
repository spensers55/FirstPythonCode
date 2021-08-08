# print("Hello World")

# n1 = 5
# n2 = 2
# sum = n1 * n2
# print(n1*n2)

# number1 = int(input("enter first number: "))
# number2 = int(input("enter second number: "))
# sum = number1+number2
# print("{0}+{1}={2}".format(number1, number2, sum))

# target = int(input("Enter the target number"))
# exponent = int(input("Enter the exponent"))
# result = 1
# i = 0
# while i < exponent:
# 	result *= target
# 	i+=1
# print("{0}^{1}={2}".format(target, exponent, result))

# ^^^ getting used to python ^^^

#-----------SOLVE ARITHMETIC START HERE-------------

#start input validation loop
while True:
	#get equation from user
	equation = input("Enter a simple arithmetic equation: ") 
	
	#prepare variables
	operatorLoc = -1
	operator = ' '
	validated = True

	#find the operator
	operatorLoc = equation.find("+")
	if operatorLoc == -1:
		operatorLoc = equation.find("-")
	if operatorLoc == -1:
		operatorLoc = equation.find("*")
	if operatorLoc == -1:
		operatorLoc = equation.find("/")
	if operatorLoc == -1: #validated input condition
		validated = False


	#capturing operator
	operator = equation[operatorLoc]

	#substring out the parts before and after the operator
	firstPart = ""
	secondPart = ""
	firstPart = equation[0: operatorLoc]
	try:
		firstPart = int(firstPart)
	except ValueError:
		print("Please enter an Integer")
		validated = False
	secondPart = equation[operatorLoc+1:len(equation)]
	try:
		secondPart = int(secondPart)
	except ValueError:
		print("Please enter an Integer")
		validated = False

	if validated == True:
		break
#end input validation loop

#prepare result variable
result = 0

#perform arithmetic
if operator == "+":
	result = firstPart + secondPart
elif operator == "-":
	result = firstPart - secondPart
elif operator == "*":
	result = firstPart * secondPart
elif operator == "/":
	result = firstPart / secondPart

#print result
print("{0}={1}".format(equation, result))