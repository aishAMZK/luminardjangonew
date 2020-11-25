#define by using [] or by using list()
#insertion order is preserved
#updation is possible
#duplicates are allowed
lst=["java","python","c#","javascript"]
print(lst[0])
print(lst[3])
print(lst[-1])
print(lst[-1:-4:-1])
print(lst[-1:-5:-1])
print(lst[0:2])
print(lst[:3])
#[low:upper]
print(lst[0:4:2])#2 is the step

#iteration
for item in lst:
    print(item)

lst.append("dart")
print(lst)

lst[0]="Ruby"
print(lst)

lst.insert(3,"perl")#inserting an object in to a specific position
print(lst)

marks=list()
#insertsome values
#perform slicing
#update a object