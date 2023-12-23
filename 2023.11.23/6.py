def king_move(coord1, coord2):
  
    x1, y1 = ord(coord1[0]) - ord('a') + 1, int(coord1[1])
    x2, y2 = ord(coord2[0]) - ord('a') + 1, int(coord2[1])

    return (x1 - x2) <= 1 and (y1 - y2) <= 1

coord1 = input().strip()
coord2 = input().strip()

if king_move(coord1, coord2):
    print("Да")
else:
    print("Нет")

#g3
#f2
#Да

#c6
#d4
#Нет