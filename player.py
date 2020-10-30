class player:
    def __init__(self, profile=None):
        if profile != None:
            self.load(profile)
        else:
            self.name = None
            self.health = 100
            self.attack = 10
            self.defense = 10
            self.intellect = 10
            self.role = combatClassType()

    def load(self, profile):
        # if a player profile exists, unpack it and pass as a dictionary
        self.name = profile['name']
        self.attack = profile['attack']
        self.health = profile['health']
        self.defense = profile['defense']
        self.intellect = profile['intellect']
        self.role = combatClassType(profile=profile)

    def printStats(self):
        print('Player Stats:')
        print('health:', self.health)
        print('attack:', self.attack)
        print('defense:', self.defense)
        print('intellect:', self.intellect)
        self.role.printStats()

class combatClassType:
    #TODO: This method isn't very self-descriptive. Explore using @classmethods in the future as a replacement
    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            self.load(kwargs['profile'])
        else:
            self.role = self.selectCombatRole()
            self.charisma = 0
            self.luck = 0
            self.perception = 0

    def load(self, profile):
        self.role = profile['role']
        self.charisma = profile['charisma']
        self.luck = profile['luck']
        self.perception = profile['perception']

    def selectCombatRole(self):
        pass

    def menu(self):
        print('Please select a class for your adventurer.')
        print('1. Barbarian')
        print('2. Thief')
        print('3. Knight')
        print('4. Bard')
        print('5. Mercenary')

    def printStats(self):
        print('Combat Role stats:')
        print('role:', self.role)
        print('charisma:', self.charisma)
        print('luck:', self.luck)
        print('perception:', self.perception)

if __name__ == "__main__":
    pass