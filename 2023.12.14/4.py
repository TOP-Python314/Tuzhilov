def countable_nouns(num: int, years: tuple[str, str, str]) -> str:
    if num in range (11, 21) or num%10 in [0, 5, 6, 7, 8, 9]:
        return years[2]
    elif num %10 == 1:
        return years[0]
    else:
        return years[1]
    
# >>> countable_nouns(1, ("год", "года", "лет"))
# 'год'
# countable_nouns(2, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(10, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(12, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(22, ("год", "года", "лет"))
# 'года'
    