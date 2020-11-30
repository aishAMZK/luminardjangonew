employees=[[1001,"ajay","qa",1981,2003],
           [1002,"vijay","developer",1992,2008],
           [1003,"arun","ba",1989,2010],
           [1004,"amal","developer",2009,2014],
           [1004,"vimal","developer",1987,1989]]
#print all employee designation
for employee in employees:
    print(employee[1])

#print all employee whose desig=developer
for employee in employees:
    if employee[2]=="developer":
        print(employee)

#print all employee those who are working in 1980's
for employee in employees:
    if employee[4]>1980:
        print(employee)

#print all employee details whose experience > 9 years