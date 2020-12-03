#file operations Read r,write w,append a


#step 1:create reference
#reference_name=open(filepath,mode_of_operation)
f=open("names","r")
for lines in f:
    print(lines)

f=open("names","r")
lst=[]
for lines in f:
    lst.append(lines.rstrip("\n"))
print(lst)


