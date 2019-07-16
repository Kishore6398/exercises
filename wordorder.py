#example
wrd=['abc','xyz','abc','pqr','xyz','xyz']
s=set(wrd)
lst=[]
print(len(s))
for i in wrd:
    if i not in lst:
        lst.append(i)
        print(wrd.count(i),i)
