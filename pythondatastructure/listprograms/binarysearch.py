lst=[2,1,5,8,7,6,8,10,3,11]
#step1 we have to sort the array
for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if(lst[i]>lst[j]):
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
print(lst)

#[1,2,3,5,6,7,8,8,10,11]
# 0 1 2 3 4 5 6 7 8  9
#low      mid           upp
low=0
upp=len(lst)-1

mid=(low+upp)//2
print(mid)
