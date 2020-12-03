text="hello hai hai hello hai"
#o/p hello:2 hai:3
words=text.split(" ")
dict={}
#dict[words]=1#(hello:1) if that word is not in dictionary
#dict[words]+=1#if that word is in dictionary
for word in words:#hello"
    if(word not in dict):
        dict[word]=1
    else:
        dict[word]+=1
print(dict)