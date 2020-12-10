#create a class student consist of attributes rol,name,course,total
#must have aibutes for setting and printing those attributes
class Student:
    def set_student(self,rol,name,course,total):
        #instence variables,self.rol,self.name,self.course,self.total
        self.rol=rol
        self.name=name
        self.course=course
        self.total=total
    def print_student(self):
        print("rol=",self.rol)
        print("name=",self.name)
        print("course=",self.course)
        print("total=",self.total)

obj=Student()
obj.set_student(100,"anu","mca",150)
obj.print_student()

#we can access the instance variable outside class by using refernec
#print[obj.name]