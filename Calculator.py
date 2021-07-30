def add(x,y):
	return x+y
def sub(x,y):
	return x-y
def mul(x,y):
	return x*y
def div(x,y):
	return x/y
def pow(x,y):
	return x**y
def mod(x,y):
	return x|y

print("select your choice:")
print("1.+")
print("1.-")
print("3.*")
print("4./")
print("5.**")
print("6.|")

num = input("enter your choice:(1,2,3,4,5,6):")
x = int(input("enter your 1st number:"))
y = int(input("enter your 2nd number:"))

if num == '1':
	print(add(x,y))
elif num == '2':
	print(sub(x,y))
elif num == '3':
	print(mul(x,y))
elif num == '4':
	print(div(x,y))
elif num == '5':
	print(pow(x,y))
elif num == '6':
	print(mod(x,y))
else:
	print("Invalid input!!!")


