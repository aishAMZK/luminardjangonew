f=open("word_data")
dict={}
for lines in f:
    words=lines.rstrip(".\n").split(" ")
    for word in words:
        word=word.rstrip(",")
        if word not in dict:
            dict[word]=1
        else:
            dict[word]+=1
for k,v in dict.items():
    print(k,v)

#to get highest freq word
highest =max(dict,key=dict.get)
print(highest)
print(highest,dict[highest])