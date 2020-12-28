from re import *

#predefined character sets

# pattern='[a-z]'#check for lowercase a to z characters
# pattern='[0-9]'#check for all digits
# pattern='[^0-9]'#except numbers
# pattern='[^a-z]'#except lowercase characters
# pattern='[a-zA-Z]' #check for both lower and upper case characters

#lowercase uppercase digit
# pattern='[a-zA-Z0-9]'

#special characters
# pattern='[^a-zA-Z0-9]'
# pattern="\s"#checking for spaces
# pattern="\S"#except space
# pattern="\d"#checking for digits
# pattern="\D"#except digit
pattern="\w"#except special characters
matcher=finditer(pattern,"abc Z@7k")
for match in matcher:
    print(match.start())#0 1 2
    print(match.group())#a b c k
# out=[(match.start(),match.group()) for match in matcher]
# print(out)

