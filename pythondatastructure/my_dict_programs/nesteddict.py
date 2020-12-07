students={
    100:{"rol":100,"name":"ajay","total":140,"course":"bca"},
    101:{"rol":101,"name":"vijay","total":145,"course":"bca"},
    102:{"rol":102,"name":"anu","total":130,"course":"bca"},
    103:{"rol":103,"name":"jino","total":135,"course":"mca"},}
print(students[100])


#print name only
print(students[100]["name"])
print(students[100]["total"])


def printStudents(**kwargs):
    id=kwargs.get("id")#100
    if(id in students):
        if "property" in kwargs:
            prop=kwargs.get("property")
            if prop in students[id]:
                print(students[id][prop])

        print(students[id]["name"])

    else:
        print("students with this rol not exist")
printStudents(id=100,property="total")



