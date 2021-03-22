number=int(input("enter number"))
flag=0
for i in range(2,number):
    if(number%i==0):
        flag=1
        break
    else:
        flag=0
if(flag==0):
    print("prime number")
else:
    print("not prime number")

# for i in range(1,13):
#     print(i)

#  read low limit read upper limit (10,50) print all prime number from (10,50)

# low=int(input("enter lower limit"))#10
# upper=int(input("enter upper number"))#51
# for i in range(low,upper):
#     flag=0
#     for j in range(2,j):
#         if(i%j==0):
#             flag=1
#             break
#         if(flag==0):
#             print(i,end=" ")
