lista = [100, 99, 201, 19, 22, 76, 137]

lista.sort()

print('Lista posortowana metodą sort()')
print(lista)

sec = lista[1]
listlen = len(lista)-2
last = lista[listlen]
print(' ')
print('Druga najnisza liczba listowanie obiektu [1]')
print(sec)
print(' ')
print('Druga najwyższa liczba listowanie obiektu len(lista)-2')
print(last)
print(' ')
print('Wynik odejmowania drugiej najmniejszej od drugiej największej: ')
print(last - sec)
print(' ')