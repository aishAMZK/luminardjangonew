low=int(input("enter lower number"))#10
upper=int(input("enter upper number"))#51
for i in range(low,upper):#(10,51)
      if i>1:#10>1
        for j in range(2,i):#(2,10)
            if(i%j==0):
                break
        else:
            print(i)


