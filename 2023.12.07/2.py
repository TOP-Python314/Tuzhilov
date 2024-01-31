fruits_list = []

while True:
    fruit = input('Фрукты: ')
    if fruit == '':
        break
    fruits_list.append(fruit)

if len(fruits_list) > 1:
    result = ', '.join(fruits_list[:-1]) + f" и {fruits_list[-1]}"
else:
    result = fruits_list[0]

print(result)

#яблоко

#яблоко

#яблоко
#груша

#яблоко и груша

#яблоко
#груша
#апельсин

#яблоко, груша и апельсин