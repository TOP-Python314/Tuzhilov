email = input('Введите e-mail: ')

if email.count('@') == 1 and email[0]!='@' and email.count ('.ru'):
    print('Да')
else:
    print('Нет')
    
#Введите e-mail: sgd@ya.ru
#Да

#Введите e-mail:  abcde@fghij
#Нет