num=10
def changer():
    num=20
    print(num)
changer()#20
print(num)#10


num=10
def changer():
    global num
    num=20
    print(num)
changer()#20
print(num)#20