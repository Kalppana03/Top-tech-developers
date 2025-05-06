#Functions with argument and without return value
def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        print(a)
        a,b=b,a+b
n=int(input("Enter a number:"))
fibonacci(n)

#Function with argument and return value
def factorial1(n):
    if n<0:
        print("Enter a valid number!")
    elif n==0:
        print("Factorial of 0 is 1")
    else:
        s=1
        for i in range(1,n+1):
            s=s*i
    return s
a=int(input("Enter a number:"))
b=factorial1(a)
print("Factorial is ",b)

#Function without argument and with return value
def factorial2():
    n=int(input("Enter a number:"))
    if n<0:
        print("Enter a valid number!")
    elif n==0:
        print("Factorial of 0 is 1")
    else:
        s=1
        for i in range(1,n+1):
            s=s*i
    return s
b=factorial2()
print("Factorial is ",b)

#Function without argument and without return value
def factorial3():
    n=int(input("Enter a number:"))
    if n<0:
        print("Enter a valid number!")
    elif n==0:
        print("Factorial of 0 is 1")
    else:
        s=1
        for i in range(1,n+1):
            s=s*i
        print("Factorial is ",s)
factorial3()

