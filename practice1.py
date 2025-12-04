# practice exercise
age=input("enter your age:")
birth_year=2025-int(age)
print("your birth year is:",birth_year)

#checking if a number is even or odd
num=int(input("enter the number:"))
if(num%2==0):
    print("the number is even")
else:
    print("the number is odd")


def factorial(num):
    if(num==0):
        return 1
    else:
        return num*factorial(num-1)
    
print("the factorial of the number u entered is :",factorial(num))


list=[1,2,10,50,100,0]
for i in list:
    max=i
    if(i>=max):
        max=i

print("the maximum number in the provided list is ",max)


