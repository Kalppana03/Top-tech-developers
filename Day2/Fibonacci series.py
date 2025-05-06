#Fibonacci using for loop
print("Using for loop")
a=0
b=1
n=int(input("enter the number:"))
for i in range(n):
    print(a)
    a,b=b,a+b
    
#Fibonacci using while loop
print("\nUsing while loop")
s=0
m=1
count=0
while(count<n):
    print(s)
    s,m=m,s+m
    count+=1
