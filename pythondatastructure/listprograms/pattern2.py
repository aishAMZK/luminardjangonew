lst=[2,5,6,3]#[14,11,10,13]total=sum(lst
total=sum(lst)#16
out=[]
for num in lst:
    out.append((total-num))#16-2=14,16-5=11,16-6=10,16-3=13
print(out)


lst=[4,3,2,5]#[10,11,12,9]
total=sum(lst)#14
out=[]
for num in lst:
    out.append((total-num))
print(out)