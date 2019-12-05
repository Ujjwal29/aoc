import math

def solve(m):
	return math.floor(m/3) - 2

if __name__ == "__main__":
	f = open('input1.txt', 'r')
	final_mass=0
	for line in f.readlines():
		final_mass += solve(int(line))
	print(final_mass)