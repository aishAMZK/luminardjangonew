
size=int(input("enter the size of stack"))
stk=[]

n=1
def push():
    print("push")
def pop():
    print("pop")
def display():
    print("display")
while(n!=0):
    option=int(input("enter operation u want to perform 1)push 2)pop 3)display"))
    if(option==1):
        push()
    elif(option==2):
        pop()
    elif(option==3):
        display()
    else:
        print("invalid option")
    n=int(input("enter do u want to continue press 0 for exit"))

#queue:-
#fifo
#insert
#delete

#data structures:
#manipulation,storage,organizing
