def main():
	def add(num1, num2):
		print(num1+num2)

	def sub(num1, num2):
		print(num1-num2)

	def multiply(num1, num2):
		print(num1*num2)

	def divide(num1, num2):
		print(num1/num2)


	num1 = int(input("Enter Number 1: "))
	opr = input("Enter Operator (+, -, *, /):" )
	num2 = int(input("Enter Number 2: "))

	if opr == '+':
		add(num1, num2)
	elif opr == '-':
		sub(num1, num2)
	elif opr == '*':
		multiply(num1, num2)
	elif opr == '/':
		divide(num1, num2)
	else:
		print("Operator not found!!")

main()


