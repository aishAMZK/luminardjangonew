#values are stored in dictionary in the form of key value pairs

students={"rol":100,"name":"ajay","course":"bca"}
#checking for a specific key
print("rol" in students)

#checking for total key


#print student name "ajay"
#ajay is a value, to fetch value we havto use corresponding key
print(students["name"])
#course
print(students["course"])

for keys in students:
    print(keys)

for keys in students:
    print(keys,students[keys])

for k,v in students.items():
    print(k,v)

