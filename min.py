'''l1=[1,2,3,4,4,5]
print(min(l1))'''
l1=[-57,57,-57,57]
s=set(l1)

#print(sorted(s))
l1=list(s)
l1.sort()
if(l1[1]>l1[0]):
    print(l1[0])
else:
    print(l1[1])

    
