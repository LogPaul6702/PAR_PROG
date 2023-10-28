import math

lista = [100, 99, 201, 19, 22, 76, 137]

print(lista)
print(' ')

for a in lista:
    print('Z biblioteki math sqrt oraz pow')
    print('Pierwiastek z ' + str(a) + ': ' + str(math.sqrt(a)))
    print('Druga potęga z ' + str(a) + ': ' + str(math.pow(a,2)))
    print('Trzecia potęga z ' + str(a) + ': ' + str(math.pow(a,3)))
    print(' ')
