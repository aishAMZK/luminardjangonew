low=int(input("enter lower limit"))
upper=int(input("enter upper limit"))
sum=0
if(low>upper):
    print("error")
while(low<=upper):
    if(low%2!=0):
        sum+=low
    low+=1
print(sum)

evensum=0
oddsum=0
for i in range(low,u)
