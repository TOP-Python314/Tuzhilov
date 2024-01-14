number = int(input())
end_number = int('1' + '0' * number)
start_number = end_number // 10
count = 0
for num in range(start_number, end_number):
    for div in range(2, num):
        if num % div == 0:
            break
        elif num % div != 0 and div == num - 1:
            count += 1
            
print(count)    

#3
#143