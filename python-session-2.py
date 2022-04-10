def main():

	#Short program that does some small math with 
	#integers and floating point data-types.
	
	#int numbers
	i_num1 = 5
	i_num2 = 8

	#float point numbers
	f_num1 = 4.5
	f_num2 = 8.25

	#quicc maths
	print("Float: " + str(f_num1) + " + " + str(f_num2) + " = " + str(f_num1+f_num2))

	print("String: " + str(i_num1) + " / " + str(i_num2) + " = " + str(i_num1/i_num2))

	print("Float + String: " + str(i_num1) + " * " + str(f_num2) + " = " + str(i_num1/f_num1))

if __name__=="__main__":
	main()