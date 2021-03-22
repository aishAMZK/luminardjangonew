#quantifiers

from re import *
# pattern="a+" #chk for a and morethan one a
# pattern="a*" #a+ plus zero occurance of a
# pattern="a?" #a plus zero number of a
# pattern="^a" #chk for starting with a
# pattern="a$" #ending with a
pattern='a[2,3]' #chk for mininum 2 a and maximum 3
matcher=finditer(pattern,"aaababaaaaa")
for match in matcher:
    print(match.start())
    print(match.group())

