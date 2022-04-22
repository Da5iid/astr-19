import numpy as np

#program that displays 1000 entries of sin(x) vs x.
#also adds the same but for cos(x) as an extra and prep for propt 6.
def main():

	x = np.linspace(0.0,2.0*np.pi,1000)
	print(f"sin(x)          cos(x)")

	for i in range(1000):
		print(f"{np.sin(x[i]):10.5e}     {np.cos(x[i]):10.5e}")

if __name__ == '__main__':
	main()