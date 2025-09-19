from abc import ABC, abstractmethod
from copy import deepcopy
from datetime import datetime, date, time, timezone
import uuid
from typing import List, TypedDict, NotRequired
from typing_extensions import Self

class GlobalException(Exception):
    def __init__(self, message) -> None:
        self.message = message
        super().__init__(f'{message}')

class EmployeeData(TypedDict):
    id: NotRequired[str]
    first_name: str
    last_name: str
    departament: str
    experience: int
    base_salary: int | float
    assigned_projects: str

class Employee(ABC):
    def __init__(self, id: str, name: str = 'Emma', last_name: str = 'Juárez', experience: int = 0, departament: str = 'developer', salary: int | float = 500, assigned_projects: str = '') -> None:
        self.__id = id
        self._first_name = name
        self._last_name = last_name
        self._departament = departament
        self._experience = experience
        self._base_salary = salary
        self._assigned_projects = assigned_projects

    @property
    def id(self):
        return self.__id

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def calculate_salary(self):
        pass


    @abstractmethod
    def calculate_productivity(self):
        pass

    @abstractmethod
    def calculate_promotion(self):
        pass

    def update(self, new_data):
        for k, v in new_data.items():
            # hasattr(obj, name)
            # Verifica si la instacia tiene un atributo en especifico, retorna un boleano.
            if hasattr(self, k):
                # setattr(obj, name, value)
                # Setea la propiedad en la instacia con su clave-valor.
                setattr(self, k, v)

    def request_vacation(self):
        pass

class Developer(Employee):
    def __init__(self, id, first_name: str, last_name: str, experience: int, departament: str, base_salary: int | float, assigned_projects: str) -> None:
        super().__init__(id, first_name, last_name, experience, departament, base_salary, assigned_projects)

    def work(self):
        pass

    def calculate_salary(self):
        pass

    def calculate_productivity(self):
        pass

    def calculate_promotion(self):
        pass

    def request_vacation(self):
        pass

class ProductManager(Employee):
    def __init__(self, id, first_name: str, last_name: str, experience: int, departament: str, base_salary: int | float, assigned_projects: str) -> None:
        super().__init__(id, first_name, last_name, experience, departament, base_salary, assigned_projects)

    def work(self):
        pass

    def calculate_salary(self):
        pass

    def calculate_productivity(self):
        pass

    def calculate_promotion(self):
        pass

    def request_vacation(self):
        pass

class Designer(Employee):
    def __init__(self, id, first_name: str, last_name: str, experience: int, departament: str, base_salary: int | float, assigned_projects: str) -> None:
        super().__init__(id, first_name, last_name, experience, departament, base_salary, assigned_projects)

    def work(self):
        pass

    def calculate_salary(self):
        pass

    def calculate_productivity(self):
        pass

    def calculate_promotion(self):
        pass

    def request_vacation(self):
        pass

class CompanyDB:
    __instace = None
    def __new__(cls):
        if cls.__instace is None:
            cls.__instace = super().__new__(cls)
        
        return cls.__instace

    def __init__(self) -> None:
        self.__roles = { role: self.slice_role(role) for role in { 'software_engineer', 'backend_engineer', 'frontend_engineer', 'ui_designer', 'product_manager' } }
        self.__employees: List[Employee] = []

    # @staticmethod
    # Decorador que permite crear un metodo que no recibe algun parametro implicito como self o cls; son utilizados comúnmente como utilidades de la misma clase.
    @staticmethod
    def slice_role(role) -> str:
        if not role:
            raise ValueError('El valor no es valido.')

        code_role = role[0]
        
        i = 0
        while '_' in role and i < len(role):
            # En Javascript no se necesita hacer esto, se puede acceder al elemento si retorna undefined quiere decir que se salio del rango.
            if role[i] == '_':
                code_role = code_role + role[i + 1]
            i = i + 1

        if len(code_role) == 1:
            code_role = code_role + 'xx'
            return code_role

        return code_role

    @property
    def employees(self):
        return self.__employees
    
    @property
    def roles(self):
        return self.__roles
    
    def add_employee_to_db(self, employee: Employee) -> None:
        self.__employees.append(employee)

    def remove_employee_from_db(self, index: int) -> Employee:
        return self.__employees.pop(index)
    
    def update_employee_from_db(self, index, data) -> Employee:
        self.__employees[index].update(data)
        return self.__employees[index]
    
    def update_all_employee_data_in_the_db(self, index, data) -> Employee:
        self.__employees[index] = data
        return self.__employees[index]

    def is_exist_employees(self):
        return len(self.__employees) < 1


# Observer Pattern
# Define un mecanismo de suscripción que permite que un sujeto(notificador) avise a uno o más oyentes (subscriptores) cada vez que exista un cambio.
# Caracteristicas:
# - Los suscriptores tienen la posibilidad suscribirse y de eliminar su sucripción del notificador.
# - Principio de abierto/cerrado; se pueden agregar más suscriptores al mismo notificador sin necesidad de modificar su codigo interno.
# - 
class EventManager(ABC):
    @abstractmethod
    def subscribe(self, listener):
        pass

    @abstractmethod
    def un_subscribe(self, listener):
        pass

    @abstractmethod
    def notify(self, payload):
        pass

class EventListener(ABC):
    @abstractmethod
    def update_employee_projects(self, payload):
        pass

class ProjectNotifier(EventManager):
    _subscribers: List[EventListener] = []
    _state = None
    
    def subscribe(self, listener) -> None:
        if not listener:
            raise GlobalException('The listener not exists.')
        
        print('A listener subscribed')
        self._subscribers.append(listener)

    def un_subscribe(self, listener) -> None:
        if not listener:
            raise GlobalException('The listener not exists.')
        
        print('A listener was removed')
        self._subscribers.remove(listener)

    def notify(self, payload):
        for subscriber in self._subscribers:
            subscriber.update_employee_projects(payload)

class Project:
    def __init__(self, id, title, budget, status, is_active, deadline) -> None:
        self.__id = id
        self._title = title
        self._budget = budget
        self._status = status
        self._is_active = is_active
        self._deadline = deadline
        self._assigned_employees = []
        self._created_at = datetime.now(timezone.utc)
        self._updated_at = datetime.now(timezone.utc)

    @property
    def status(self): return self._status
    
    @property
    def deadline(self): return self._deadline

    @property
    def assigned_employees(self): return self._assigned_employees
    
    @property
    def created_at(self): return self.created_at
    
    @property
    def updated_at(self): return self.updated_at

    @status.setter
    def status(self, new_status):
        self._status = new_status
    
    @deadline.setter
    def deadline(self, new_status):
        self._status = new_status
    
    @assigned_employees.setter
    def assigned_employees(self, employee):
        self._assigned_employees.append(employee)
        return self._assigned_employees
    
    def data(self):
        print(self.__id, self._title, self._budget, self._status, self._is_active, self.deadline, 'created:', self._created_at, 'updated:', self._updated_at)
        pass

class ProjectSystem:
    def __init__(self) -> None:
        self.event = ProjectNotifier()

    def assign_employee_to_project(self):
        pass

    def delete_employee_to_project(self):
        pass

    def update_progress_project(self):
        pass

    def get_all_projects_by_status(self):
        pass


class BuildEmployee:
    def __init__(self, db) -> None:
        self.db = db

    def __generate_employee_id(self) -> int:
        # return (self.db.roles[departament] + '-' + str(uuid.uuid4())[0:4]).lower()
        # self.db.roles[departament] + '-' +
        return len(self.db.employees) + 1

    # FACTORY PATTERN
    # Es la capacidad de una clase de crear una instacia sin especificar explicitamente su clase.
    def build(self, data, index = None):
        try:
            if not data['departament'] in self.db.roles:
                raise GlobalException('El departamento no existe, no es posible generar el usuario.')
            
            data['id'] = self.__generate_employee_id() if not index else index

            match data['departament']:
                case 'software_engineer' | 'backend_engineer' | 'frontend_engineer':
                    return Developer(**data)
                case 'product_manager':
                    return ProductManager(**data)
                case 'ui_designer':
                    return Designer(**data)
        except GlobalException as e:
            print('Error (create_employee):', e)
            return None

class AddEmployee:
    def __init__(self, db) -> None:
        self.db = db
        self.create_employee = BuildEmployee(self.db).build

    def by_lotes(self, new_employees: List[EmployeeData]):
        for data in new_employees:
            new_employee = self.create_employee(data)

            if not new_employee:
                continue

            self.db.add_employee_to_db(new_employee)

        print('El o los empleados se crearon con exito.')

class RemoveEmployee:
    def __init__(self, db) -> None:
        self.db = db

    def by_id(self, id):
        if self.db.is_exist_employees():
            print('No hay empleados en la empresa.')
            return
        
        if not id:
            raise GlobalException('No se puede eliminar el empleado si no se envia su id.')

        for index, employee in enumerate(self.db.employees):
            if id == employee.id:
                employee_deleted = self.db.remove_employee_from_db(index)
                print(f'El empleado con ID: {employee_deleted.id} fue eliminado con exito.')
                break
        else:
            print(f'El empleado con ID: {id}, no existe en la base de datos.')

class UpdateEmployee(EventListener):
    def __init__(self, db) -> None:
        self.db = db
        self.create_employee = BuildEmployee(db).build
    
    @staticmethod
    def remove_prefix(data, prefix = '_'):
        # { mapping.get(k, k): v for k, v in employee_copy.items() }
        return { k[len(prefix):] if k.startswith(prefix) else k: v for k, v in data.items() }

    def by_id(self, id: int, **data):
        try:
            employee_found = [{ 'employee_data': employee, 'employee_index': index } for index, employee in enumerate(self.db.employees) if employee.id == id][0]

            if '_departament' in data:
                employee_copy = vars(deepcopy(employee_found['employee_data']))
                employee_copy.update(data)

                find_attr_id = [attr for attr, _ in employee_copy.items() if attr.endswith('__id')]
                i = 0
                attr_id = find_attr_id[i] if 0 <= i < len(find_attr_id) else '_Employee__id'

                current_id = employee_copy[attr_id]
                del employee_copy[attr_id]
                clean_employee_data = self.remove_prefix(employee_copy)

                new_data_employee = self.create_employee(clean_employee_data, index = current_id)
                employee_updated = self.db.update_all_employee_data_in_the_db(employee_found['employee_index'], new_data_employee)

                print(f'El empleado con ID: {employee_updated.id} se actualizo exito.')
                return

            employee_updated = self.db.update_employee_from_db(employee_found['employee_index'], data)
            print(f'El empleado con ID: {employee_updated.id} se actualizo exito.')
        except ValueError as e:
            print('update_employee_from_db', e)
            return e
        
    def update_employee_projects(self, payload):
        print('The object was updated!')

class EmployeeSystem:
    # SINGLETON PATTERN
    # Garantiza que la instacia de una clase siempre sea unica.
    
    # __new__
    # Crea la instacia, y la devuelve.
    # cls: parametro que hace refencia a la clase actual (EmployeeSystem), funciona muy bien con subclases.
    __instance = None
    def __new__(cls, db):
        print('Class:', cls.__name__)

        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance
    
    # __init__
    # Inicializa la instacia con valores.
    def __init__(self, db) -> None:
        self.db = db
        self.add = AddEmployee(self.db)
        self.remove = RemoveEmployee(self.db)
        self.update = UpdateEmployee(self.db)

    def see_all_employees(self):
        if self.db.is_exist_employees():
            print('No hay empleados en la empresa.')
            return

        for i, employee in enumerate(self.db.employees):
            print('-' * 10)
            print(f'{i + 1}:\nID: {employee.id}\nFirst: {employee._first_name}\nLast: {employee._last_name}\nDepartament: {employee._departament}\nBase salary: ${employee._base_salary}')
            print('-' * 10)


class Company:
    __instance = None

    def __new__(cls, legal_name, db) -> Self:
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance
    
    def __init__(self, legal_name, db) -> None:
        self._legal_name = legal_name
        self.db = db
        self.employee_system = EmployeeSystem(self.db)
        self.project_system = ProjectSystem()

class Application:
    @staticmethod
    def config():
        db = CompanyDB()
        company = Company("Astronave 404", db)

        company.employee_system.add.by_lotes([
            { 
                'first_name': 'Allan', 'last_name': 'Juárez', 'experience': 3, 'departament': 'software_engineer', 'base_salary': 1500, 'assigned_projects': '2' 
            },
            { 
                'first_name': 'John', 'last_name': 'Montana', 'experience': 6, 'departament': 'backend_engineer', 'base_salary': 1800, 'assigned_projects': '4'
            },
            {
                'first_name': 'Gemma', 'last_name': 'Bianchi', 'experience': 4, 'departament': 'ui_designer', 'base_salary': 1000, 'assigned_projects': '4'    
            },
            {
                'first_name': 'Charles', 'last_name': 'Juárez', 'experience': 8, 'departament': 'product_manager', 'base_salary': 2500, 'assigned_projects': '4' 
            },
            { 
                'first_name': 'Michael', 'last_name': 'Jackson', 'experience': 2, 'departament': 'ui_designer', 'base_salary': 750, 'assigned_projects': '1' 
            }
        ])

        company.employee_system.update.by_id(2, **{ '_base_salary': 3500, '_experience': 8, '_assigned_projects': '2' })

        company.employee_system.update.by_id(4, **{ '_last_name': 'Leclerc', '_departament': 'software_engineer', '_base_salary': 2000, '_assigned_projects': '3' })

        company.employee_system.see_all_employees()

        new_project = Project(id=1, title='404 project', budget=1000000, status='in-progress', is_active=True, deadline=datetime(2025, 12, 12, 12, 30, 00, tzinfo=timezone.utc))
        new_project.data()

        print('-' * 10)

        company.project_system.event.subscribe(company.employee_system.update)
        company.project_system.event.notify({ 'status': 'OK' })


if __name__ == '__main__':
    Application().config()
