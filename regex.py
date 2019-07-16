import re
stri='if a && b &&& c'
strr='if a || b && c || d'
match=re.search(r'(&&)\s',stri)
n1=re.sub(match.group(1),'and',stri)
print(n1)
#m=re.search(,strr)
n2=re.sub('\|\|','or',strr)
print(n2)

#if match.group(0)=='&&':
 #   str.replace('&&','and')
#if m.group(0)=='|':
 #   str.replace('|','or')
    
