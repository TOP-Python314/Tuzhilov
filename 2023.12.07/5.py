scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}

words = input('Введите слово: ')
scor = 0

for letter in words:
    for j in scores_letters:
        if letter.upper() in scores_letters[j]:
            scor += j
            break

print(scor)

# Введите слово: синхрофазатрон
# 29

# Введите слово: паравозик
# 15