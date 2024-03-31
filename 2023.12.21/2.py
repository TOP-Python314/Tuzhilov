def deck( ):
    numbers = list(range(2, 15))
    suit_of_cards = ['черви', 'бубны', 'пики', 'трефы']
    
    for j in suit_of_cards:
        for n in numbers:
    
            yield(n, j)
            
# >>> list(deck())[::13]
# [(2, 'черви'), (2, 'бубны'), (2, 'пики'), (2, 'трефы')]
# >>> list(deck())[::12]
# [(2, 'черви'), (14, 'черви'), (13, 'бубны'), (12, 'пики'), (11, 'трефы')]
    