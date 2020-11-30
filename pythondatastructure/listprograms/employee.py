employees=[[1001,"ajay","qa",15000],
          [1002,"vijay","developer",25000],
          [1003,"arun","ba",15000],
          [1004,"amal","developer",30000]]
#print all employer id
for employer in employees:
    print(employer[0])
#find total of salary
total=0
for employer in employees:
    print(employer)


for employer in employees:
    if employer[0]=="developer":
        print(employees)

qasum=0
dsum=0
for employee in employees:
    if(employee[2]=="qa"):
        qasum+=employee[3]
    elif (employee[2]=="developer"):
        dsum+=employee[3]
print(qa)
print(developer)