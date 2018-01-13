from functools import reduce

creCardNo=input("Enter a credit card number:")
cList,oList,eList,resList=[],[],[],[]
for i in map(int,creCardNo):
    cList.append(int(i))
    
for a in range(len(cList)):
    if a%2!=0: 
        oList.append(cList[a])
    else:
        eList.append(cList[a])

print(reduce((lambda x,y:x+y),oList))

for b in range(len(eList)):
    if eList[b]>=5:
        eList[b]=eList[b]*2-10+1
    else:
        eList[b]=eList[b]*2

print(reduce((lambda x,y:x+y),eList))
res=0
resList.extend((oList))
resList.extend((eList))

for i in resList:
    res+=i

if res%10==0:
     print("VALID")
else:
     print("NOT VALID")
