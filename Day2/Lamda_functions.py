Multiply =lambda a,b: a*b
print(Multiply(10,5))

num=[1,2,3,4,5]
s=list(map(lambda x: x**2,num))
print(s)

d=list(filter(lambda x: x<10,s))
print(d)

from functools import reduce
e=reduce(lambda x,y: x+y ,d)
print(e)