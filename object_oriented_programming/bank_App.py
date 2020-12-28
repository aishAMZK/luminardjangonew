class Bank:
    bank_name="sbk"
    def create_account(self,acno,person_name,balance):
        self.acno=acno
        self.person_name=person_name
        self.balance=balance


    def deposit(self,amount):
        self.balance+=amount
        print("your account",self.acno,"has been credited with amount",amount,"your aval bal=",self.balance)

    def withdraw(self,amount):
        if(amount>self.balance):
            print("insufficient balance in your account",self.acno,"transaction cancelled")
        else:
            self.balance-=amount
            print("your account".self.acno,"has been debited with amount",amount,"your aval bal=",self.balance)

    def balance_enq(self):
        print("your aval balance",self.balance)

obj=Bank()
obj.create_account(1001,"ammu",500)
#obj.deposit(5000)
#obj.withdraw(10000)
obj.balance_enq()

#how to access instance variables outside class
print()


#different types of variables

#.instance variables
#instance variables are always pretended with self keyword
#we can access instance variable outside class by using reference name

#.static variables
#static is a key word used for efficient memory utilization
#we can access the static variable by using class name


#different types of method

#.instance method

#.static method-> utility functionality, @staticmethod

#.class level method-> manipulating class level variables, @classmethod
