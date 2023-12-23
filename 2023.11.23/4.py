x = input()
y = input()

move1 = ord(x[0]) + int(x[1])
move2 = ord(y[0]) + int(y[1])

if move1 % 2 == 0 and move2 % 2 == 0:
    print('Да')
elif move1 % 2 != 0 and move2 % 2 != 0:
    print('Да')
else:
    print('Нет')
    
#a1
#b2
#Да

#a1
#b1
#Нет