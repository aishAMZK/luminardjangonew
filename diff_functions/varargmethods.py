def add(num1,num2):
    res=num1+num2
    print(res)
add(10,20)

#variable length argument methods(it accepts any number of methods)

def add(*nums):
    print(nums)
#*args accepting in tuple format
add(10,20)
add(10,20,30,40)
add(10,11,12,13,14)

#to find the sum

def add(*nums):
    total=0
    for num in nums:
        total+=num
    print(total)

add(10,20)
add(10,20,30,40)
add(10,11,12,13,14)


def printEmp(**args):
    print(args)
printEmp(home="kakkanad",name="ajay",working="aluway")
#**args accepting in dictionary format