from weapon import Weapon
from spell import Spell

class Arsenal:

    def __init__(self, weapon = None, spell = None):
        self.__weapon = weapon
        self.__spell = spell
    
    ''' Switches the arsenals current weapon with a new one. '''
    def equip_weapon(self, weapon = None):
        self.__weapon = weapon
    ''' Switches the aresanls current spell with a new one. '''
    def learn_spell(self, spell= None):
        self.__spell = spell

    ''' Getter methods '''
    def get_weapon(self):
        return str(self.__weapon)
    
    def get_spell(self):
        return str(self.__spell)