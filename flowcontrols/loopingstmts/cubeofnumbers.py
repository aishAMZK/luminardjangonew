#armstrong number

number=int(input("enter the number"))#123
result=0
while(number!=0):#123!=0
    digit=number%10#123%10=3
    result=result+(digit**3)#0+(3*3*3)
    number=number//10#123//10=12
print(result)