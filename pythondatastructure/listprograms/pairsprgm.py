lst=[2,1,3,4,6,7]
lst.sort()
#[1,2,3,4,6,7]
# l         u
#6
#lst[l]+lst[u]==6  (1+7=8)
low=0
upp=len(lst)-1
element=int(input("enter element"))
while(low<=upp):
    total=lst[low]+lst[upp]
    #case 1
    if(element>total):
        low=upp-1
    #case 2
    elif(element<total):
        low=low+1
    #case 3
    elif(element==total):
        print("pairs are",lst[low],",",lst[upp])
