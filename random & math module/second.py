l1=['faa','fsaf','jfd','jds','jyxs']
l2=[]
for c in l1:
    if len(c)>=2 and c[0]==c[-1]:
        l2.append(c)
print('total count is: ',len(l2))
