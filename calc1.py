def add(x,y):
	return x+y
def sub(x,y):
	return x-y
def mul(x,y):
	return x*y
def div(x,y):
	return x/y
def pow(x,y):
	return pow(x,y)

print("Select Operation:")
print("1.Add")
print("2.Sub")
print("3.Mul")
print("4.Div")
print("5.Pow")

choice = input("Enter Your Choice(1,2,3,4,5):")
num1 = int(input("Enter First Value:"))
num2 = int(input("Enter Second Value:"))

if choice == '1':
	print(add(num1,num2))
	
elif choice == '2':
	print(num1 ,"-" ,num2 , "=" ,sub(num1,num2))
	
elif choice == '3':
	print(num1 ,"*" ,num2 , "=" ,mul(num1,num2))
	
elif choice == '4':
	print(num1 ,"/" ,num2 , "=" ,div(num1,num2))
	
elif choice == '5':
	print(num1 ,"^" ,num2 , "=" ,pow(num1,num2))
	
else:
	print("Invalid Input")