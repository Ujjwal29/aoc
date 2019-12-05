import math

def solve(m):
	value = math.floor(m/3) - 2
	return value if value > 0 else 0

if __name__ == "__main__":
	f = open('input1.txt', 'r')
	final_mass=0
	for line in f.readlines():
		module_fuel = solve(int(line))
		final_module_fuel = module_fuel
		while module_fuel > 0:
			module_fuel = solve(int(module_fuel))
			final_module_fuel += module_fuel
		final_mass += final_module_fuel
	print(final_mass)