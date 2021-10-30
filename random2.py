import random
n=int(input('введите длинну масива'))
array=[random.randint(0,10)for number in range(n)]
print(array)
m=int(input('введите число которое ищете'))
print(array.index(m))

