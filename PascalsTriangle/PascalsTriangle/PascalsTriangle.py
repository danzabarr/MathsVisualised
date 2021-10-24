import math

def nCr(n, r) -> int :
	return (int)(math.factorial(n) / math.factorial(r) / math.factorial(n - r))

def print_triangle(n):

	for x in range(n):

		string = " " * (n - x) * 3
		
		for y in range(x + 1):

			string += str(nCr(x, y)).rjust(6, " ")
		
		print(string)


print_triangle(18)
