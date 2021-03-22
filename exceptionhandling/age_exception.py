# age<18
# age=int(input("enter age"))
#
# if age<18:
#     raise Exception("sorry invalid age")

#raise-customised exception

num=int(input("enter value"))
if type(num) !="int":
     raise Exception("only integers allowed")
