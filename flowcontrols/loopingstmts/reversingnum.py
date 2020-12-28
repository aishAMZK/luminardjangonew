number=int(input("enter number"))
result=0
while(number!=0):#123
    digit=number%10
    result=result*10+digit
    number=number//10
print(result)

#123%10=3
#123/10=12.3
#123//10=12
#12%10=2
#12//10=1
#1%10=1