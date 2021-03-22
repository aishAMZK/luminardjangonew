#variable name rule
#starting with a-k
#second character should be a digit and it must be divisible by 3
#followed by any number of characters
#z2rgg => invalid
#B7vgg => invalid
#a3rgg => valid

from re import *
rule='[a-kA-K][369][a-zA-Z0-9]*'

variablename=input("enter variable name")
matcher=fullmatch(rule,variablename)
if matcher !=None:
    print("valid variable name")
else:
    print("invalid")