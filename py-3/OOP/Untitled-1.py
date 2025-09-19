# ========================
# CLASES PARA SEPARAR RESPONSABILIDADES
# ========================

class CombatResult:
    """Representa el resultado de una acción de combate"""
    def __init__(self, attacker, defender, action_type, damage=0, blocked=False):
        self.attacker = attacker
        self.defender = defender
        self.action_type = action_type  # 'attack', 'defense', 'special'
        self.damage = damage
        self.blocked = blocked
        self.message = self._generate_message()
    
    def _generate_message(self):
        if self.action_type == 'attack':
            if self.blocked:
                return f"{self.defender._name} bloqueó el ataque de {self.attacker._name}!"
            else:
                return f"{self.attacker._name} atacó a {self.defender._name} causando {self.damage} de daño!"
        elif self.action_type == 'defense':
            return f"{self.attacker._name} se pone en posición defensiva."
        return f"{self.attacker._name} realizó una acción especial."


class TurnManager:
    """Gestiona los turnos y estrategias de los combatientes"""
    def __init__(self, fighters_with_strategies):
        self.fighters_data = fighters_with_strategies  # [{'character': fighter, 'strategy': [actions]}]
        self.current_turn = 0
        self.max_turns = min(len(data['strategy']) for data in fighters_with_strategies)
    
    def get_current_actions(self):
        """Obtiene las acciones del turno actual"""
        if self.current_turn >= self.max_turns:
            return None
            
        actions = []
        for fighter_data in self.fighters_data:
            strategy = fighter_data['strategy']
            if self.current_turn < len(strategy):
                action = strategy[self.current_turn]
                actions.append({
                    'fighter': fighter_data['character'], 
                    'action': action
                })
        return actions
    
    def next_turn(self):
        """Avanza al siguiente turno"""
        self.current_turn += 1
    
    def has_more_turns(self):
        """Verifica si quedan turnos por ejecutar"""
        return self.current_turn < self.max_turns


class CombatProcessor:
    """Procesa las acciones de combate y calcula resultados"""
    
    def process_turn(self, actions):
        """Procesa un turno completo y devuelve los resultados"""
        results = []
        
        # Separar acciones por tipo
        attacks = []
        defenses = []
        
        for action_data in actions:
            fighter = action_data['fighter']
            action = action_data['action']
            
            if action is None:
                continue
                
            # Determinar el objetivo (el otro fighter)
            other_fighters = [a['fighter'] for a in actions if a['fighter'] != fighter]
            target = other_fighters[0] if other_fighters else None
            
            if target and fighter.hp > 0:
                action_result = action(target)
                
                if action_result['type'] == 'attack':
                    attacks.append({
                        'attacker': fighter,
                        'target': target,
                        'damage': action_result['attack_damage']
                    })
                elif action_result['type'] == 'defense':
                    defenses.append(fighter)
        
        # Procesar ataques considerando defensas
        for attack in attacks:
            attacker = attack['attacker']
            target = attack['target']
            damage = attack['damage']
            
            # Verificar si el objetivo se está defendiendo
            is_defending = target in defenses
            
            if is_defending:
                # Reducir daño por defensa (50% de reducción)
                damage = damage // 2
                blocked = True
            else:
                blocked = False
            
            # Aplicar daño
            if damage > 0:
                new_hp = target.hp - damage
                target.hp = new_hp
            
            # Crear resultado
            result = CombatResult(attacker, target, 'attack', damage, blocked)
            results.append(result)
        
        # Agregar resultados de defensas
        for defender in defenses:
            result = CombatResult(defender, None, 'defense')
            results.append(result)
        
        # Resetear estados
        for action_data in actions:
            fighter = action_data['fighter']
            fighter.is_attack = False
            fighter.is_defending = False
        
        return results


class BattleJudge:
    """Determina el estado de la batalla y ganadores"""
    
    def check_battle_status(self, fighters):
        """Verifica el estado actual de la batalla"""
        alive_fighters = [f for f in fighters if f.hp > 0]
        
        if len(alive_fighters) <= 1:
            return {
                'battle_over': True,
                'winner': alive_fighters[0] if alive_fighters else None,
                'reason': 'knockout' if alive_fighters else 'draw'
            }
        
        return {'battle_over': False}
    
    def award_experience(self, winner, loser):
        """Otorga experiencia al ganador"""
        if winner and loser:
            exp_gained = 10 + (loser._level * 5)
            winner.xp += exp_gained
            return exp_gained
        return 0


class CombatDisplay:
    """Maneja toda la presentación visual del combate"""
    
    def show_battle_start(self, arena_name, fighters):
        print(f"\n{'='*50}")
        print(f"🏛️  COLISEUM {arena_name.upper()} 🏛️")
        print(f"{'='*50}")
        
        print("\n👥 COMBATIENTES:")
        for fighter in fighters:
            print(f"   🗡️  {fighter._name} ({fighter._type}) - Nivel {fighter._level}")
            print(f"       HP: {fighter.hp} | MP: {fighter.mp} | XP: {fighter.xp}")
        
        print(f"\n{'='*50}")
        input("⚔️  PRESIONA ENTER PARA INICIAR EL COMBATE...")
        print()
    
    def show_turn_start(self, turn_number):
        print(f"\n🔥 ===== TURNO {turn_number} ===== 🔥")
    
    def show_combat_results(self, results):
        """Muestra los resultados de las acciones del turno"""
        for result in results:
            print(f"   {result.message}")
            if result.action_type == 'attack' and result.defender:
                print(f"   💚 {result.defender._name}: {result.defender.hp} HP")
    
    def show_battle_end(self, battle_status, exp_gained=0):
        print(f"\n{'='*50}")
        print("⚡ ¡LA BATALLA HA TERMINADO! ⚡")
        
        if battle_status['winner']:
            print(f"🏆 GANADOR: {battle_status['winner']._name}")
            print(f"   HP restante: {battle_status['winner'].hp}")
            if exp_gained > 0:
                print(f"   XP ganada: +{exp_gained}")
        else:
            print("🤝 ¡EMPATE! Ambos combatientes cayeron.")
        
        print(f"{'='*50}\n")


# ========================
# COLISEUM MEJORADO
# ========================

class Coliseum:
    """Orquesta el combate usando las clases especializadas"""
    
    def __init__(self, name):
        self.name = name
        self.display = CombatDisplay()
        self.processor = CombatProcessor()
        self.judge = BattleJudge()
    
    def init_fight(self, opponents):
        """Inicia y gestiona todo el combate"""
        # Obtener todos los fighters
        fighters = [data['character'] for data in opponents]
        
        # Mostrar inicio de batalla
        self.display.show_battle_start(self.name, fighters)
        
        # Crear gestor de turnos
        turn_manager = TurnManager(opponents)
        
        # Bucle principal de combate
        while turn_manager.has_more_turns():
            # Verificar si la batalla debe continuar
            battle_status = self.judge.check_battle_status(fighters)
            if battle_status['battle_over']:
                break
            
            # Mostrar turno
            self.display.show_turn_start(turn_manager.current_turn + 1)
            
            # Obtener acciones del turno actual
            actions = turn_manager.get_current_actions()
            if not actions:
                break
            
            # Procesar el turno
            results = self.processor.process_turn(actions)
            
            # Mostrar resultados
            self.display.show_combat_results(results)
            
            # Avanzar turno
            turn_manager.next_turn()
            
            # Pequeña pausa para legibilidad
            input("   Presiona ENTER para continuar...")
        
        # Determinar resultado final
        final_status = self.judge.check_battle_status(fighters)
        
        # Otorgar experiencia
        exp_gained = 0
        if final_status['winner']:
            losers = [f for f in fighters if f != final_status['winner']]
            if losers:
                exp_gained = self.judge.award_experience(final_status['winner'], losers[0])
        
        # Mostrar resultado final
        self.display.show_battle_end(final_status, exp_gained)


# ========================
# EJEMPLO DE USO
# ========================

# Tu código existente para crear personajes...
# wizard = Wizard(**wizard_props)
# archer = Archer(**archer_props)

# opponents = [
#     {'character': wizard, 'strategy': [wizard.attack, None, wizard.defence, wizard.attack, None]}, 
#     {'character': archer, 'strategy': [archer.attack, archer.attack, None, archer.attack, archer.attack]}
# ]

# arena_404 = Coliseum('404')
# arena_404.init_fight(opponents)