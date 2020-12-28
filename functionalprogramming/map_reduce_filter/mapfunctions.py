lst=[10,11,12,13,14,15]

#squares
#map(function,iterable)

def squ(no):
    return no**2
squares=list(map(squ,lst))
print(squares)

#using lambda function
squares=list(map(lambda no:no**2,lst))
print(squares)

cube=list(map(lambda no:no**3,lst))
print(cube)


#filter
#fetch only even numbers

even=list(filter(lambda no:no%2==0,lst))
print(even)


names=["ajay","aji","binoy","abhi","anu"]
na=list(map(lambda name:name.upper(),names))
print(na)

aname=list(filter(lambda name:name[0]=='a',names))
print(aname)

#reduce->sum,min,max

from functools import *
lst=[10,11,12,13,14,15]

sum=reduce(lambda no1,no2:no1+no2,lst)
print(sum)

min=reduce(lambda no1,no2:no1 if no1<no2 else no2,lst)
print(min)

max=reduce(lambda no1,no2:no1 if no1>no2 else no2,lst)
print(max)

#calculating sum of even numbers from the list

evensum=reduce(lambda no1,no2:no1+no2,list(filter(lambda no:no%2==0,lst)))
print(evensum)

#minimum of even number
evenmin=reduce(lambda no1,no2:no1 if no1<no2 else no2,list(filter(lambda no:no%2==0,lst)))
print(evenmin)
