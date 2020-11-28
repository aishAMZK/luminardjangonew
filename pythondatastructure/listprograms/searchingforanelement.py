lst=[1,2,3,4,5,6,7,8]
element=int(input("enter element for searching"))
if(element in lst):
    print("element found")
else:
    print("element not found")
flg=0
for num in lst:
    if(num==element):
        flg+=1
        break
    else:
        flg=0
if(flg>0):
    print("element found")
else:
    print("element not found")