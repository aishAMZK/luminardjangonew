f=open("complete.csv")

dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[1]
    confirmed_cases=data[4]
    if state not in dict:
        dict[state]=confirmed_cases
    else:
        dict[state]=confirmed_cases
for k,v in dict.items():
    print(k,v)

#find which state have highest confirmed_cases
highest=max(dict,key=dict.get)
print(highest,dict[highest])

#find which state have lowest confirmed_cases
lowest=min(dict,key=dict.get)
print(lowest,dict[lowest])

#find the states depends on confirmed_cases
srt=sorted(dict,key=dict.get,reverse=True)
print("sorted",srt)