#regular expression
#used for pattern matching
#step 1
#package not in builtins.py it is in re
import re
matcher=re.finditer("ab","abaabababbbabab")
cnt=0
for match in matcher:
    #print (match.group())
    print(match.start())
    cnt+=1
print(cnt)