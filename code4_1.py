def check_double(x):
	x = str(x)
	for i in range(1,len(x)):
		if x[i]==x[i-1]:
			return True
	return False

def check_increasing(x):
	x = str(x)
	for i in range(1,len(x)):
		if x[i]<x[i-1]:
			return False
	return True

if __name__ == "__main__":
	a,b = 284639,748759
	count=0
	for num in range(a,b):
		if check_double(num) and check_increasing(num):
			print(num)
			count+=1
	print(count)
