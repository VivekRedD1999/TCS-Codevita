## Minimum Gifts ( CodeVita Season 9)
=============================================================
x=int(input())
y,z=[],[]
for i in range(x):
   y.append(int(input()))
   z.append([int(j) for j in input().split()])
final=[]
for rule in z:
    result = 0
    imp = []
    minimum = min(rule)
    for p in rule:
        if p > minimum:
            if p in imp:
                result+=1
            else:
                result+=2
                imp.append(p)
        elif p==minimum:
            result+=1
    final.append(result)
    del imp[:]
    result=0
for val in final:
    print(val)
