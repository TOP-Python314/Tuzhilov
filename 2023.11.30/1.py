numbers = []
while True:
    n = int(input('Введите число > '))
    if n%7 == 0:
        numbers.append(n)
    else:
        print(' '.join(map(str, reversed(numbers))))
        break
        
#Введите число > 7
#Введите число > 7
#Введите число > 14
#Введите число > 21
#Введите число > 13
#21 14 7 7
 


