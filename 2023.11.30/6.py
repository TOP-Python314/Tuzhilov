ticket = input()

n1 = sum(int(i) for i in ticket[0:3])
n2 = sum(int(i) for i in ticket[3:6])

if n1 == n2:
    print('да')
else:
    print('нет')
    
#183534
#да

#401367
#нет