#Copying
a=[10,20,30,40,50]
b=[0]*len(a)
for i in range(len(a)):
    b[i]=a[i]
print("after copying:",b)

#Join two list
a=[1,2,3]
b=[4,5,6]
c=a+b
print("Joining two list:",c)

#Join two tuple
a=(1,2,3)
b=(9,10,11)
c=a+b
print("Joining two tuples:",c)

#if else
print("\nIf else")
a=int(input("Enter a number:"))
if a%2==0:
    print("Even number")
else:
    print("Odd number")

#while
print("While loop")
i=10
while(i<=20):
    print(i,end=" ")
    i+=1

#for
print("\n For loop")
sum_=0
for i in range(10):
    sum_+=i
print(sum_)