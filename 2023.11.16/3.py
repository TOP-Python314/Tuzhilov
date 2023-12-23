numbers = int(input('Введите кол-во минут: '))
hours = numbers // 60
mins = numbers % 60

print(f'{numbers} минут - это {hours} час {mins} минут')

#Введите кол-во минут: 150
#150 минут - это 2 час 30 минут