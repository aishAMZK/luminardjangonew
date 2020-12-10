class Bank:
    def create_account(self,acno,person_name,balance,bank_name):
        self.acno=acno
        self.person_name=person_name
        self.balance=balance
        self.bank_name=bank_name

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
obj.create_account(1001,"ammu",5000,"sbk")
#obj.deposit(5000)
#obj.withdraw(10000)
obj.balance_enq()