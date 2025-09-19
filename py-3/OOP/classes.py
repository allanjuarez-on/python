import random
from abc import ABC, abstractmethod

# List/dict comprehensions
# Decoradores
# Context managers (with)
# Type hints (PEP 484)
# --

# # Conceptos clave que difieren de JavaScript
# - List/Dict comprehensions
# - Decoradores (@app.get)
# - Context managers (with statements)
# - Generadores e iteradores
# - Type hints (crucial para FastAPI)

# # Enfócate en conceptos únicos de Python
# - Métodos mágicos (__init__, __str__)
# - Herencia múltiple
# - Dataclasses (importantes para FastAPI)
# - Properties y descriptores


# CLASSES
print('> CLASSES')

# Las clases tienen mecanismos combinados entre C++ y modula-3
# Nota | Las clases pueden ser definidas desde diferentes ambitos por en ejempo en un funcion o en un if.
class Client:
    """Clases en python"""
    # __init__
    # Funcion especial constructora que permite personalizar una nueva instacia para la clase.
    # Recibe por defecto self y en si mismo este es la referencia al objeto que se crea.
    def __init__(self, name):
        # Atributo de clase (individual).
        self.client_name = name

        # Atributo protegido por convencion.
        self._balance = 0

        # Atributo privado(SOLO es visible por la propia clase, las subclases no pueden acceder a menos que se utilice un getter o setter).
        self.__key = 'kd213dm'

    # Atributo de clase (global)
    # Todas las intacias de la clase lo tendran.
    financial_institution = 'BBVA'

    # NAME SPACES
    # Son la asignacion de nombres a objetos (identidicador -> objeto); cada modulo tiene su propio conjunto de atributos que pueden definirse como un espacio de nombres.

    # Busqueda por ambito:
    # local -> Enclosing -> Global -> Built-in(builtins module)
    # Nota | los espacios de nombres predefinidos se encuentran en el modulo "builtins"

    def data_client(self):
        print(f"Client name: {self.client_name}\nBalance: {self._balance}")
        print(self.__key) # Desde dentro se puede acceder a datos privados
        pass


# Las clases son un objeto.
print(isinstance(Client, object)) # True

print('Docs:', Client.__doc__)

new_client = Client('Allan')

# new_client._balance = 10000 # Lo modifica, solo es una convencion ya que python no tienen keywods como private o public.

# print(new_client.__key) # Error: Python no deja acceder a datos privados desde fuera.

print('Atributo global:', new_client.financial_institution)

new_client.data_client()


# --------
print("# --------")


# OOP
print('> OOP')

class Phone:
    def __init__(self, id, sku, brand, weight, width, height, color='Space'):
        # Encapsulamiento
        # Controla el acceso a los datos de una clase
        # _ -> Protegido (convencion) se puede acceder a el desde fuera pero no deberia ser asi, su valor debe ser cambiado internamente
        # __ -> Privado solo accesible desde la clase
        self._id = self.create_id(random.randint(0, 10), random.randint(0, 99))
        self._sku = sku
        self.brand = brand
        self.weight = weight
        self.width = width
        self.height = height
        self.color = color

    @property
    def get_id(self):
        print('ID:', self._id)
        return self._id
    
    def create_id(self, n1, n2):
        return n1 + n2
    
    def info(self):
        print("Desde la clase padre:\nBrand: {0}\nWeight: {1}\nHeight: {2}\nColor: {3}".format(self.brand, self.weight, self.height, self.color))

    def call(self):
        print('Calling...')
        

class Smartphone(Phone):
    def __init__(self, id, sku, brand, storage, wifi_version, bluetooth_version, weight, width, height):
        # Herencia
        # La funcion super() llama al a la funcion especial (contructor) de la clase padre (Phone) y estas son las propiedades que se heredaran.
        super().__init__(id, sku, brand, weight, width, height)

        # Encapsulación
        self._storage = storage
        self.wifi_version = wifi_version
        self.bluetooth_version = bluetooth_version

    # Polimorfismo
    # Si este metodo no existe busca el metodo en el padre; ademas estos se pueden reescribir.
    def info(self):
        print(f"Desde la clase hija:\nBrand: {self.brand}\nStorage: {self._storage}\nWeight: {self.weight}\nSKU: {self._sku}")

    # def get_id(self):
    #     # Se puede llamar incluso a los metodos normales del padre con la funcion super()
    #     new_sku = super().create_id(self._id, self._sku)
    #     return new_sku


iphone = Smartphone(id='888', sku='SK0218YEGI86JH', brand='Apple', storage='256gb', wifi_version='7.0', bluetooth_version='5.5', weight='400g', width=2, height=2)

iphone.info() # Desde la clase hija: Brand: Apple Storage: 256gb Weight: 400g SKU: SK0218YEGI86JH
iphone.call() # Calling...
iphone.get_id # ID: 74

# vars(obj) & obj.__dict__
# Permite ver todas las propiedades de una instacia
print(vars(Smartphone))
print(Smartphone.__dict__)