import random
random.seed()

class Monster:
    def __init__(self):
        raise NotImplementedError
    
    def retrieveStats(self):
        stats = {
            'name': self.name,
            'health': self.health,
            'attack': self.attack,
            'defense': self.defense,
        }
        return stats

    def attack(self):
        pass
    
    def defend(self):
        pass

######### Monster archtypes ##########
class Archtype(Monster):
    def __init__(self):
        raise NotImplementedError
    
class Abomination(Archtype):
    def __init__(self):
        raise NotImplementedError

class Undead(Archtype):
    def __init__(self):
        raise NotImplementedError

class Beast(Archtype):
    def __init__(self):
        raise NotImplementedError
######################################

class Slime(Abomination):
    def __init__(self):
        self.name = 'Slime'
        self.health = 10
        self.attack = 2
        self.defense = 2

class Rat(Beast):
    def __init__(self):
        self.name = 'Rat'
        self.health = 5
        self.attack = 1
        self.defense = 1

class Wolf(Beast):
    def __init__(self):
        self.name = 'Wolf'
        self.health = 10
        self.attack = 5
        self.defense = 1



### Monster Generator/Catalog ###
class Bestiary:
    def __init__(self): # Monster Archtype lists are dict name -> object mappings
        self.beasts = self.dictBeasts() 
        self.abominations = self.dictAbominations()
    
    def generateLowLevelMonster(self, quantity, level=1):
        outcomes = [self.beasts, self.abominations]
        monsters = []
        for _ in range(0, quantity):
            for _ in range(0, len(outcomes)):
                index = random.randint(0, len(outcomes)-1) # Select a random Archtype
                chosenArchtype = outcomes[index]
                keys = [*chosenArchtype]
                index = random.randint(0, len(chosenArchtype)-1) # Select a random Monster in its Archtype
            monsters.append(chosenArchtype[keys[index]])
        return monsters

    def test(self):
        print(len(self.beasts))
        for Beast in self.beasts:
            print(self.beasts[Beast].retrieveStats())
        print(self.generateLowLevelMonster(3))

    def dictBeasts(self):
        beast_list = {
            'Wolf': Wolf(),
            'Rat': Rat(),
        }
        return beast_list
    
    def dictAbominations(self):
        abomination_list = {
            'Slime': Slime(),
        }
        return abomination_list

if __name__ == "__main__":
    pass