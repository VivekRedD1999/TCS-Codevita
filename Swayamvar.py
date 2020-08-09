## Swayamwar (Codevita)
#========================================================

no_of_pairs=int(input())
mem_of_bribe=input()
mem_of_groom=input()
bride=list(mem_of_bribe)
groom=list(mem_of_groom)
bride1=bride
groom1=groom
initi=0
for bri1 in bride:
    if bri1 == groom[0]:
        initi+=1
if initi>0:
    for bri in bride:
        for gro in groom:
            if bri == gro:
                groom1.remove(gro)
                break
            else:
                continue
        else :
            break
    print(len(groom1))
else:
    print(len(groom1))
