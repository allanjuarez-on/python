# LIST
print("> LIST")

names = ["Allan", "Emma", "Gemma", "Jade"]
print(names)

# Valores de una lista
print("Valores de una lista:")
print(names[1])
print(names[-1]) # Obtiene el ultimo elemento. names[-1] === [names.length - 1]


# Segmentos
# SIEMPRE retorna una nueva lista es no mutable.
print("Segmentos:")
# De derecha a izquierda primero va el numero en negativo y despues el operador -> :
print(names[-2:]) # ["Gemma", "Jade"]

# De izquierda a derecha primero va el operador -> : y despues el numero
print(names[:3]) # ["Allan", "Emma", "Gemma"]

# MUTABILIDAD
# Las listas son MUTABLES.
print("> MUTABILIDAD")
random_numbers = [2, 4, 6, 8, 10]
print(random_numbers + [2]) # Acepta operadores (+) pero SOLO lista con lista.
# print(random_numbers - [10, 20]) # Error

# Segmentaciones + Mutabilidad
# Toda segementación regresa una copia superficial de una lista.
print("Segmentaciones + Mutabilidad:")
copy_random_numbers = random_numbers[:] # : Genera un copia superficial.
copy_random_numbers[2:4] = [1500, 256] # Incluye el el 2 pero no el 4 (llega solo al 3).

print("Copy", copy_random_numbers) # Cambio los valores de esta ref.
print("Original", random_numbers) # Este sigue intacto.

# Deep copy vs Superficial copy
# Deep copy: construye un obj. compuesto e inserta de manera recursiva copias de cada uno de los hijos del elemento original
# Superficial copy: construye un obj. compuesto y solo inseta ref. de cada hijo original
print("Deep copy vs Superficial copy:")

# append()
# Es un metodo mutable que agregar al final de la lista elementos. append() === push()
print("append()")
random_numbers.append(404)
print(random_numbers)

# len(object)
# Metodo que permite obtener el numero de elementos que contiene una lista, string o diccionario.
print("len()")
colors = ["space-gray", "esmerald", "ultramarine"]
print("Número de elementos:", len(colors)) # 3

# --------
print("# --------")

# TUPLES
print("> TUPLES")
# Es una secuencia de datos homogeneos INMUTABLES. Esta se puede escribir con o sin parentesis.
my_tuple = 1, 2, 3 # Or (1, 2, 3)
print(my_tuple) # (1, 2, 3)
print(my_tuple[0]) # 1
# my_tuple[1] = 5 # Error: todo lo que este dentro de la tupla es inmutable.

other_tuple = (1, "Edgar", ["+", "-", "*", "/"])
other_tuple[2].append("%")
print(other_tuple) # (1, "Edgar", ["+", "-", "*", "/", "%"])

# --------
print("# --------")

# Dictionaries
print("> DICTIONARIES")

brands = { "Apple": "Cupertino, California", "Google": "Montain View, California", "Huawei": "Shenzhen, China", }
print(brands["Apple"]) # Cupertino, California

# del dict[<key>]
# Permite eliminar una clave del dict.
print("del dict[<key>]")
del brands["Huawei"]
print(brands) # "Apple": "Cupertino, California", "Google": "Montain View, California"

# Los diccionarios permiten agregar nuevas claves y valores
brands["Samsung"] = "Suwon-si, South Korea"
print(brands) # { "Apple": "Cupertino, California", "Google": "Montain View, California", "Samsung": "Suwon-si, South Korea" }

# list(<dict>)
# Se obtienen TODAS las claves de un dict.
print("list(<dict>)")
print(list(brands)) # ["Apple", "Google", "Samsung"]

# dict()
# Este constructor permite crear diccionarios apartir de secuencias clave-valor
print("dict()")
words = dict(hello="hola", youAreWelcome="De nada") # or dict([(), ()])
print(words) # {"hello": "hola", "youAreWelcome": "De nada"}

# Iterar diccionarios
print("Iterar diccionarios:")
ages = dict(allan=28, edgar=70, santa=65)
for k in ages:
    print(k) # Solo obtiene la clave -> allan edgar santa
    print(ages[k]) # Aqui su valor

# Dictionary view objects (keys(), values(), items())
# Representa una vista dinamica de las entradas de un diccionario; esto es si los valores cambian este los reflejara.
print("Dictionary view objects (keys(), values(), items())")

# items()
# Obtiene los pares clave-valor de un diccionario.
print("items()")
altitude_cities = {"CDMX": 2240, "Monterrey": 540, "Guadalajara": 1566 }
for city, altitude in altitude_cities.items():
    print(f"Ciudad: {city}\nAltitud: {altitude} m")



# --------
print("# --------")