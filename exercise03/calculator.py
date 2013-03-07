# import arithmetic
from arithmetic import add, subtract, multiply, divide, square, cube, power, mod

while True:
	entry = raw_input()
	tEntry = entry.split(" ")
	if tEntry[0] == "q" or tEntry[0] == "Q":
		break
	elif tEntry[0] == "+":
		print add(tEntry[1], tEntry[2])

	elif tEntry[0] == "-":
		print subtract(tEntry[1], tEntry[2])
	elif tEntry[0] == "*":
		print multiply(tEntry[1], tEntry[2])
	elif tEntry[0] == "/":
		print divide(tEntry[1], tEntry[2])
	elif tEntry[0] == "square":
		print square(tEntry[1])
	elif tEntry[0] == "cube":
		print cube(tEntry[1])
	elif tEntry[0] == "pow":
		print power(tEntry[1], tEntry[2])
	elif tEntry[0] == "mod":
		print mod(tEntry[1], tEntry[2])

