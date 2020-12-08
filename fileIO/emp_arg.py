f=open("employee","r")

emp_dict={}
for lines in f:
    print(lines)
    #100,don,devop,2,25000/n
    id,name,desig,exp,salary=lines.rstrip("/n").split(",")

    if id not in emp_dict:
        emp_dict[id]={"id":id,"name":name,"desig":desig,"exp":exp,"salary":salary}
    print(emp_dict)
        #{100:{id:100,name:don,desig:devop,exp:2,salary:25000}
