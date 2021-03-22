#KL08BS1375 => valid
#GJ08BN2211 => invalid

from re import *
rule='KL\d{2}[A-Z]{2,2}\d{1,4}'

vehiclenum=input("enter vehicle registration number")
matcher=fullmatch(rule,vehiclenum)
if matcher!=None:
    print("valid vehicle number")
else:
    print("invalid registration number")