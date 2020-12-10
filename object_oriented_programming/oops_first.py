#class?
#plan,design pattern,template,blueprint

#object?
#real world entity (lgseries)

#reference
#to perform operation on object


#class ClassName
class person:
    #attribute of person self_name,age,self_gender
    #initializing attributes of person
    def set_person(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def print_person(self):
        print("name", self.name)
        print("age", self.age)
        print("gender", self.gender)

#reference_name=Class()
obj=person()
obj.set_person("ajay",25,"male")
obj.print_person()


obj1=person()
obj1.set_person("vijay",26,"male")
obj1.print_person()

#self is a key word used to print current class object