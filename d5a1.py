lst=[1,5,6,4,1,2,3,5]
sublst2=[1,1,5]
for i in lst:
    if i==sublst2[0]:
        while i>=0:
            lst.pop(i)
            i=i-1
lst.pop(0)

for i in lst:
    if i==sublst2[2]:
        a="true"
        break
    else:
        a="false"
if a=="true":
    print("Its a match")
else:
    print("Its gone")
