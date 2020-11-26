lst=[1,2,3,4,6,7]#value=6 (4,2
total=6
for i in lst:
    for j in lst:
        ctotal=i+j
        if(total==ctotal):
            print((i,j))
            break
