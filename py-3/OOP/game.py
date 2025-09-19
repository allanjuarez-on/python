import random
from abc import ABC, abstractmethod

# E1
print('E1')

# Wizzard: Arcane
# Warrior: Physical
# Archer: Precision

# Arcane > Physical
# Wizard > Warrior

# Physical > Precision
# Warrior > Archer

# Precision > Arcane
# Archer > Wizard

def verify_method(fn):
    def engine(self, opponent):
        try:
            if not isinstance(opponent, Fighter):
                raise ValueError('El valor es incorrecto.')
            
            fn(self, opponent)
        except ValueError as e:
            print('Error:', e)

    return engine 

class Fighter(ABC):
    '''Character base'''
    # Por definicion **kwargs es de tipo dict[str, any]
    # Para poder darle un tipo y evitar doble anidamiento de dict solo agregar el tipo -> **kwargs: int | str -> (parameter) kwargs: dict[str, str | int]
    def __init__(self, **kwargs: str | int):
        self.__id = self.__generate_id()
        self._is_attack = False
        self._is_defending = False

        defaults: dict[str, str | int] = {
            '_name': 'Zero',
            '_type': 'normal',
            '_level': 1,
            '_base_force': 10,
            '_hp': 100,
            '_mp': 10,
            '_xp': 0,
        }

        # obj.update()
        # Actualiza un dict, si tiene la propiedad la sobreescribe; si no, la crea.
        defaults.update(kwargs)

        for key, value in defaults.items():
            setattr(self, key, value) # es igual a -> self._<key> = value

    # Getter
    @property
    def id(self):
        return self.__id
    
    @property
    def hp(self):
        return self._hp
    
    @property
    def mp(self):
        return self._hp
    
    @property
    def xp(self):
        return self._hp
    
    @property
    def base_force(self):
        return self._base_force
    
    @property
    def is_defending(self):
        return self._is_defending
    
    @property
    def is_attack(self):
        return self._is_attack
    
    # Setter
    @hp.setter
    def hp(self, value):
        try:
            is_value_valid = isinstance(value, (int, float))

            if not is_value_valid:
                raise ValueError('El valor no es valido.')

            self._hp = value
        except ValueError as e:
            print('Error type:', e)
    
    @mp.setter
    def mp(self, value):
        try:
            is_value_valid = is_value_valid = isinstance(value, (int, float)) and value > 0

            if not is_value_valid:
                raise ValueError('El valor no es valido.')

            self._mp = value
        except ValueError as e:
            print('Error type:', e)
    
    @xp.setter
    def xp(self, value):
        try:
            is_value_valid = is_value_valid = isinstance(value, (int, float)) and value > 0

            if not is_value_valid:
                raise ValueError('El valor no es valido.')
            
            self._xp = value
        except ValueError as e:
            print('Error type:', e)

    @is_defending.setter
    def is_defending(self, value):
        self._is_defending = value

    @is_attack.setter
    def is_attack(self, value):
        self._is_attack = value
    
    @abstractmethod
    def attack(self, opponent) -> dict[str, str | int]:
        pass

    @abstractmethod
    def defence(self, opponent) -> dict[str, str | int | bool]:
        pass

    # abstractmethod(verify_method(calculate_attack_damage(self, opponent))
    @abstractmethod
    @verify_method
    def calculate_attack_damage(self, opponent) -> int | float:
        pass

    def __generate_id(self):
        letters_id = ('A', 'B', 'C', 'X', 'Y', 'Z')
        new_id = f'{letters_id[random.randint(0, len(letters_id) - 1)]}{random.randrange(2, 9999, 3)}'
        return new_id

class Wizard(Fighter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def attack(self, opponent):
        if self._is_defending:
            self._is_defending = False

        self._is_attack = True

        return {
            'type': 'attack',
            'attack_damage': self.calculate_attack_damage(opponent),
            'is_attack': self._is_attack
        }

    def defence(self, opponent):
        self._is_attack = False
        
        if not self._is_defending:
            self._is_defending = not self._is_defending

            return {
                'type': 'defence',
                'is_defending': self._is_defending,
            }
        
        return {
            'type': 'defence',
            'is_defending': self._is_defending,
        }

    def calculate_attack_damage(self, opponent):
        BASE_DAMAGE = self._base_force * self._level
        match opponent._type:
            case 'physical':
                return BASE_DAMAGE + 15
            case 'precision':
                return BASE_DAMAGE + 5
            case _:
                return BASE_DAMAGE

    def expanding_force(self):
        pass

class Warrior(Fighter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def attack(self, opponent):
        if self._is_defending:
            self._is_defending = False

        self._is_attack = True

        return {
            'type': 'attack',
            'attack_damage': self.calculate_attack_damage(opponent),
            'is_attack': self._is_attack
        }

    def defence(self, opponent):
        self._is_attack = False
        
        if not self._is_defending:
            self._is_defending = not self._is_defending

            return {
                'type': 'defence',
                'is_defending': self._is_defending,
            }
        
        return {
            'type': 'defence',
            'is_defending': self._is_defending,
        }

    def calculate_attack_damage(self, opponent):
        BASE_DAMAGE = self._base_force * self._level
        match opponent._type:
            case 'arcane':
                return BASE_DAMAGE + 5
            case 'precision':
                return BASE_DAMAGE + 15
            case _:
                return BASE_DAMAGE
        return 0

    def axe_cut(self):
        pass

class Archer(Fighter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def attack(self, opponent):
        if self._is_defending:
            self._is_defending = False

        self._is_attack = True

        return {
            'type': 'attack',
            'attack_damage': self.calculate_attack_damage(opponent),
            'is_attack': self._is_attack
        }

    def defence(self, opponent):
        self._is_attack = False
        
        return {
            'type': 'defence',
            'is_defending': self._is_defending,
        }
        

    def calculate_attack_damage(self, opponent):
        BASE_DAMAGE = self._base_force * self._level
        match opponent._type:
            case 'physical':
                return BASE_DAMAGE + 5
            case 'arcane':
                return BASE_DAMAGE + 15
            case _:
                return BASE_DAMAGE

    def laser_focus(self):
        pass

class Experience:
    def calculate_new_experience_gained(self, **opponents):
        if opponents['opponent_1'].hp > opponents['opponent_2'].hp:
            opponents['opponent_1'].xp = opponents['opponent_1'].xp + 10
        else:
            opponents['opponent_2'].xp = opponents['opponent_2'].xp + 10

class Combat:
    def versus(self, **opponents):
        pass

# Por cada iteracion muestra el estado del personaje
# Determina el ganador
# Otorga experiencia al ganador
class Coliseum(Experience):
    def __init__(self, name):
        self.name = name
    
    def init_fight(self, opponents):
        print(f'COLISEUM {self.name}')
        input('ENTER PARA INICIAR COMBATE.')

        opponent_1 = opponents[0]['character']
        opponent_2 = opponents[1]['character']

        i = 0
        while i < len(opponents[0]['strategy']):
            if opponent_1.hp < 1 or opponent_2.hp < 1:
                print('La pelea termino, un jugador no puede continuar.')
                break

            opponent_1_strategy = None
            opponent_2_strategy = None

            while not (opponent_1._is_attack and opponent_2._is_attack):
                input('Esperando al jugador 1...')
                opponent_1_strategy = opponents[0]['strategy'][i] if opponents[0]['strategy'][i] is None else opponents[0]['strategy'][i](opponent_2)
                input('Esperando al jugador 2...')
                opponent_2_strategy = opponents[1]['strategy'][i] if opponents[1]['strategy'][i] is None else opponents[1]['strategy'][i](opponent_1)

                # print(opponent_1_strategy, '1')
                # print(opponent_2_strategy, '2')

                # print('Status Attack:', 'Jugador 1', opponent_1._is_attack, 'Jugador 2',opponent_2._is_attack)

                if opponent_1_strategy is None or opponent_2_strategy is None:
                    print('NO CONTRATAQUE!')
                    break

                if opponent_1.is_defending or opponent_1.is_defending:
                    print('DUELO DE DEFENSAS!')
                    break
            else:
                opponent_1.is_attack = False
                opponent_2.is_attack = False
                opponent_1.is_defending = False
                opponent_2.is_defending = False


            if not (opponent_1_strategy is None) and opponent_1.hp >= 1 and opponent_1_strategy['type'] == 'attack':
                new_hp = opponent_2.hp - opponent_1_strategy['attack_damage']
                opponent_2.hp = new_hp

                print(f'{opponent_2._name} recibio un golpe / hp: {opponent_2.hp}')


            if not (opponent_2_strategy is None) and opponent_2.hp >= 1 and opponent_2_strategy['type'] == 'attack':
                new_hp = opponent_1.hp - opponent_2_strategy['attack_damage']
                opponent_1.hp = new_hp

                print(f'{opponent_1._name} recibio un golpe / hp: {opponent_1.hp}')


            if (not (opponent_1_strategy is None) and opponent_1_strategy['type'] == 'defence') or (not (opponent_2_strategy is None) and opponent_2_strategy['type'] == 'defence'):
                i = i + 1
                print('Una o varias defensas pararon los ataques.')
                continue


            i = i + 1

        print('LA PELEA TERMINO.')

        self.calculate_new_experience_gained(**dict(opponent_1= opponent_1, opponent_2 = opponent_2))
        self.show_winner(**dict(opponent_1= opponent_1, opponent_2 = opponent_2))
        

    def show_winner(self, **opponents):
        print(f'GANADOR: {opponents['opponent_1']._name} / hp: {opponents['opponent_1'].hp}' if opponents['opponent_1'].hp > opponents['opponent_2'].hp else f'GANADOR: {opponents['opponent_2']._name} / hp: {opponents['opponent_2'].hp}')



wizard_props = { '_name': 'Old Three', '_type': 'arcane', '_level': 2, '_hp': 100, '_mp': 100, '_xp': 40, '_base_force': 12 }
wizard = Wizard(**wizard_props)

warrior_props = { '_name': 'Diavolo', '_type': 'physical', '_level': 1, '_hp': 100, '_mp': 100, '_xp': 35, '_base_force': 16 }
warrior = Warrior(**warrior_props)

archer_props = { '_name': 'Xis', '_type': 'precision', '_level': 1, '_hp': 100, '_mp': 100, '_xp': 15, '_base_force': 8 }
archer = Archer(**archer_props)

opponents = [{ 'character': wizard, 'strategy': [wizard.attack, None, wizard.defence, wizard.attack, None] }, { 'character': archer, 'strategy': [archer.attack, archer.attack, None, archer.attack, archer.attack] } ]
arena_404 = Coliseum('404')
arena_404.init_fight(opponents)


# if __name__ == '__main__':
# print(__name__)

# REGLA DE ORO:
# - Si puedes decir "X ES-UN Y" naturalmente → HERENCIA
# - Si dices "X TIENE-UN Y" o "X USA-UN Y" → COMPOSICIÓN