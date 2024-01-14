message = input('Напишите телеграмму: ')

msg = message.split()
msg = ''.join(msg)
x = len(msg)
y = x * 30
price = f'{y // 100} руб. {y % 100} коп.'

print(price)

#Напишите телеграмму: грузите апельсины бочках братья карамазовы
#11 руб. 40 коп