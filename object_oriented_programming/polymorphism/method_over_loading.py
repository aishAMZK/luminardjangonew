class Maths:
    def add(self):
        print("inside no arg add method")

    def add(self,num1):
        print("inside single arg add method")

    def add(self,num1,num2):
        print("inside two arg add method")

#same method name different number of arguments

m=Maths()

#m.add(10,20)
m.add(10)

#if we want to do functional overloading remove class,self,m=