# FUNCTIONS
print("> FUNCTIONS")

brands = { "Apple": "Cupertino, California", "Google": "Montain View, California", "Huawei": "Shenzhen, China", }

new_brands = list(map(lambda name: name[::-1], brands))
print("New Brands", new_brands) # ["elppA", "elgooG", "gnusmaS"]

var_global = 0

# Cuando se declara la funcion genera una tabla de simbolos local.
# Ademas el nombre de la funcion es asociado con el objeto de la funcion en la tabla de simbolos.
def fn():
    """Tablas"""
    var_local = 1
    var_local_2 = 9999
    # Al utilizar una variable esta primero se buscara en la tabla de simbolos local.
    print(var_local)
    # Si no encuentra esta variable localmente la buscara en la tabla global.
    print(var_global)

    # Esta variable no esta definida porque no busca de afuera hacia adentro sino de adentro hacia fuera.
    # print(hell) # Error

    # NOTA: cuando se llama a si misma o a otra funccion crea una nueva tabla de simbolos.
    def inner_fn():
        # Lo mismo pasara cuando busque la variable y no la encuentre.
        print("Dentro de otra funcion:", var_local_2)

        hell = "diavolo"
        return

    inner_fn()

    # Al final de una funcion si se envia un retunr vacio o no retorna -> None === void in javascript
    return

print(fn) # <function fn at 0x7e6fee5da2a0>
print(fn.__doc__)
fn()

usa_cities = ["New York", "California", "Florida"]

# Se pueden definir valores por defecto como en javascript
print("Valores por defecto:")
def is_city_exist(city="New York"):
    return dict(query=city, is_exist=city in usa_cities)

find_city = is_city_exist()
print(f"La ciudad {find_city["query"]} esta en la lista" if find_city["is_exist"] else f"La ciudad {find_city["query"]} no esta en la lista")

# Forma corta con Lambda.
is_city_lambda = lambda city="New York": dict(query=city, is_exist=city in usa_cities)
print("Default values with Lambdas", is_city_lambda("Texas"))

# Los valores predeterminados son definidos solo en la definicion de la funcion
x = 1
def new_fn(other_value=x):
    print(other_value) # Siempre sera 1 aunque se cambie el valor posteriormente.

x = 4
new_fn()

# MAPPING
print("> MAPPING")

# Los parametros de tipo **name reciben un diccionario y los tipo *name una tupla
def maps(origin, code, **args):
    whitelist = []
    print(args)
    for k, v in args.items():
        if(v['status'] == code and v['origin'] == origin):
            whitelist.append(k)
    return whitelist
            
webs_online = maps('San Francisco', 200, google={ "status": 200, "origin": "San Francisco" }, claude={ "status": 200, "origin": "San Francisco" }, instagram={ "status": 500, "origin": "Menlo Park" }, figma={ "status": 500, "origin": "San Francisco" }, adobe={ "status": 500, "origin": "San Jose" })

# new_dict = dict(google=200, claude=200, instagram=500, figma=200, adobe=500)
# webs_online = maps(200, new_dict) # Esto genera un error 

print("Webs online:", webs_online)

# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I"m sorry, we"re all out of", kind)
#     for arg in arguments:
#         print("WTF", arg)
#     print("-" * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])

# cheeseshop("Limburger", "It"s very runny, sir.",
# "It"s really very, VERY runny, sir.",
# shopkeeper="Michael Palin",
# client="John Cleese",
# sketch="Cheese Shop Sketch")