import numpy as np

#program that displays 1000 entries of sin(x) and cos(x) using individual functions for each,
#then prints both within main()

def sin(num):
	sinData = []
	x = np.linspace(0.0,2.0*np.pi,num)

	for i in range(num):
		sinData.append(f"{np.sin(x[i]):10.5e}")

	return sinData


def cos(num):
	cosData = []
	x = np.linspace(0.0,2.0*np.pi,num)
	
	for i in range(num):
		cosData.append(f"{np.cos(x[i]):10.5e}")

	return cosData
    

def main():
	num = 1000
	s = sin(num)
	c = cos(num)

	print(f"sin(x)          cos(x)")

	for i in range(10):
		print(f"{s[i]}     {c[i]}")


if __name__ == '__main__':
	main()