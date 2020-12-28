#inheritance
#parent  base     super
#child   derived  subclass

class Parent:
    def phone(self):
        print("have nokia 5310")
    def __lap_top(self):#private method
        print("i have lap")

class Child(Parent):
    def bike(self):
        print("i have duke")


ch=Child()
ch.phone()
ch.bike()