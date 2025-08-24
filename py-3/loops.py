# LOOPS
print('> LOOPS')

# for <k, v> in obj
print('for <k, v> in obj')
nicknames = ['iamallanjuarez', 'aej', 'so']
for nickname in nicknames:
    print('username:', nickname)

# range(<number> | <number, x...)
# range() no crea una nueva lista ahorra espacio en memoria y lo unico que genera es una progresion aritmetica que se puede iterar.
print('range(<number>):')
numbers = [2, 30, 837, 999, 1]
for i in range(len(numbers)): # len genera el tamaño del rango
    print('#', numbers[i])

# Los rangos se pueden invertir con reversed(range(x)) o tambien ordenar con sorted()
# Tambien existe el metodo set() para evitar duplicados como JavaScript

# enumerate(<object>)
# Permite obtener el indice y el valor al mismo tiempo.
print('enumerate(<object>):')
steps = ['tic', 'tac', 'toe']
for k, v in enumerate(steps):
    print(k, v)

# Bloques else en bucles
print('Bloques else en bucles:')
users = { 'Allan': 'online', 'Aranza': 'online', 'Bruno': 'ofline', 'Gemma': 'ofline' }

for k, v in users.items():
    if(v == 'online'):
        print(f'El usuario {k} se encuentra:', v)
    else:
        print(f'El usuario {k} no se encuentra activo de momento.')
# Los bucles for o while pueden tener su propios bloques "else", estos solo se ejecutaran cuando termine las iteraciones o cuando no exista una exeption.
else:
    print('EL bucle termino')


# --------
print('# --------')