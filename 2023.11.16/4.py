num = int(input('Введите трёхзначное целое число: '))
unit_of_hundreds = num // 100
unit_of_tens = num % 100 // 10
units = num%10

print(f"""Сумма цифр = {unit_of_hundreds + unit_of_tens + units}
Произведение цифр = {unit_of_hundreds * unit_of_tens * units}""")

#Введите трёхзначное целое число: 333
#Сумма цифр = 9
#Произведение цифр = 27
