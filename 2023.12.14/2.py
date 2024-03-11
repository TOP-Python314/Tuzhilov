def taxi_cost(lenght: int, wtime = 0) -> int | None:
     
    price = 80
    lenght_cost = lenght / 150 * 6
    waiting_cost = wtime * 3
     
    if lenght < 0:
       print( )
    elif lenght == 0:
        return round(price + 80 + waiting_cost)
    else:
        return round(price + lenght_cost + waiting_cost)


# >>> taxi_cost(1500)
# 140
# >>> taxi_cost(2560)
# 182
# >>> taxi_cost(0, 5)
# 175
# >>> taxi_cost(42130, 8)
# 1789
# >>> print(taxi_cost(-300))

# None
# >>>
    
     