lst=[10,10,20,30,40,50,50,51,51,52]
st=set(lst)
lst=list(st)
print(lst)


name=["a","b","c","d","e","f"]
passed=["a","b","c"]

name_set=set(name)
passed_set=set(passed)
failed_set=name_set-passed_set
print(failed_set)