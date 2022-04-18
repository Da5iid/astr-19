def cubed(x):
	y = (x**3) + 8
	return y

def main():
	x = 9
	x = cubed(x)

	print(x)

	if x>27:
		print("YAY")
	else:
		print("NAY")

if __name__ == '__main__':
	main()