#find highest salary
from functools import*
class Employee:
    def __init__(self,eid,ename,desig,sal,exp):
        self.eid=eid
        self.ename=ename
        self.desig=desig
        self.sal=sal
        self.exp=exp
    def __str__(self):
        return self.ename

#read from file
f=open("employee","r")
employee=[]
for lines in f:
    eid,ename,desig,sal,exp=lines.rstrip("\n").split(",")
    employee.append(Employee(eid,ename,desig,sal,exp))

#highest salary
highestsalary=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,list(map(lambda emp:emp.sal,employee)))
print(highestsalary)

#print highest salary employee details
employee=list(filter(lambda emp:emp.sal==highestsalary,employee))
for emp in employee:
    print(emp.ename)

#find highest salary whose designation-developer
devopsal=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,list(map(lambda emp:emp.sal,list(filter(lambda emp:emp.desig=="developer",employee)))))
print(devopsal)
