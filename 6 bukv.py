kout=0
for B1 in 'tykva':
    for B2 in 'tykva':
        for B3 in 'tykva':
            for B4 in 'tykva':
                for B5 in 'tykva':
                    for B6 in 'tykva':
                        itog = B1+B2+B3+B4+B5+B6
                        if itog[0] in 'tkv' and itog[-1] in 'tkv':
                            if itog.count('a') + itog.count('y')==2:
                                kout+=1

print(kout)
