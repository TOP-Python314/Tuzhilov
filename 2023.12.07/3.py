numbers1 = input()
numbers2 = input()

n1 = sum(int(i) for i in numbers1[0:2])
n2 = sum(int(i) for i in numbers2)

if n1 == n2:
    print('да')
else:
    print('нет')
    

# 1234
# 12
# да
    
# 1234
# 24
# нет