number=int(input("enter number"))
result=0
while(number!=0):
    digit=number%10
    result=result*10+digit
    number=number//10
print(result)