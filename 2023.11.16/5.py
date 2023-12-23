int_number = int(input('Введите целую часть числа миль: '))
float_number = int(input('Введите дробную часть числа миль: '))
miles = int_number + float_number / 10 
kilometers = miles * 1.61 

print(f'{miles:.1f} миль = {kilometers:.1f} км') 

#Введите целую часть числа миль: 15
#Введите дробную часть числа миль: 7
#15.7 миль = 25.3 к