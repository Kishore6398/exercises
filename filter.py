#Validating Email Addresses With a Filter

import re
list1=[]
n=int(input())
for i in range(n):
    str1=input()
    match=re.search(r'[a-zA-Z0-9_-]*@[a-zA-Z0-9]*.[a-z]{1,3}',str1)
    list1.append(match.group(0))

list1.sort()
print(list1)
