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
            self.role = combatClassType(bonus=self.addToStats)

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

    def addToStats(self, bonusList):
        self.health += bonusList[1]
        self.attack += bonusList[2]
        self.defense += bonusList[3]
        self.intellect += bonusList[4]

class combatClassType:
    #TODO: This method isn't very self-descriptive. Explore using @classmethods in the future as a replacement
    def __init__(self, *args, **kwargs):
        applyBonuses = kwargs['bonus']
        if len(kwargs) > 1:
            self.load(kwargs['profile'])
        else:
            self.role = None
            bonuses = self.selectCombatRole()
            self.charisma = 0
            self.luck = 0
            self.perception = 0
            applyBonuses(bonuses)

    def load(self, profile):
        self.role = profile['role']
        self.charisma = profile['charisma']
        self.luck = profile['luck']
        self.perception = profile['perception']

    def selectCombatRole(self):
        while True:
            try:
                self.menu()
                choice = int(input(''))
                break
            except ValueError:
                print('I did not recognize that option.')
        bonuses = self.roleBonusLookup(choice)
        return bonuses

    def menu(self):
        print('Please select a class for your adventurer.')
        print('1. Barbarian')
        print('2. Thief')
        print('3. Knight')
        print('4. Bard')
        print('5. Mercenary')

    def roleBonusLookup(self, selection):
        availableRoles = {
            # Format: [ROLE, HP_Bonus, ATK_Bonus, DEF_Bonus, INT_bonus]
            1: ['Barbarian', 50, 20, 5, 0],
            2: ['Thief', 25, 10, 5, 15],
            3: ['Knight', 35, 10, 20, 10],
            4: ['Bard', 15, 5, 25, 20],
            5: ['Mercenary', 25, 15, 5, 10],
        }
        self.role = availableRoles[selection][0]
        return availableRoles[selection]

    def printStats(self):
        print('Combat Role stats:')
        print('role:', self.role)
        print('charisma:', self.charisma)
        print('luck:', self.luck)
        print('perception:', self.perception)

if __name__ == "__main__":
    pass