import random
random.seed()

class monster:
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
class archtype(monster):
    def __init__(self):
        raise NotImplementedError
    
class abomination(archtype):
    def __init__(self):
        raise NotImplementedError

class undead(archtype):
    def __init__(self):
        raise NotImplementedError

class beast(archtype):
    def __init__(self):
        raise NotImplementedError
######################################

class slime(abomination):
    def __init__(self):
        self.name = 'Slime'
        self.health = 10
        self.attack = 2
        self.defense = 2

class rat(beast):
    def __init__(self):
        self.name = 'Rat'
        self.health = 5
        self.attack = 1
        self.defense = 1

class wolf(beast):
    def __init__(self):
        self.name = 'Wolf'
        self.health = 10
        self.attack = 5
        self.defense = 1



### Monster Generator/Catalog ###
class bestiary:
    def __init__(self): # Monster archtype lists are dict name -> object mappings
        self.beasts = self.dictBeasts() 
        self.abominations = self.dictAbominations()
    
    def generateLowLevelMonster(self, quantity, level=1):
        outcomes = [self.beasts, self.abominations]
        monsters = []
        for _ in range(0, quantity):
            for _ in range(0, len(outcomes)):
                index = random.randint(0, len(outcomes)-1) # Select a random archtype
                chosenArchtype = outcomes[index]
                keys = [*chosenArchtype]
                index = random.randint(0, len(chosenArchtype)-1) # Select a random monster in its archtype
            monsters.append(chosenArchtype[keys[index]])
        return monsters

    def test(self):
        print(len(self.beasts))
        for beast in self.beasts:
            print(self.beasts[beast].retrieveStats())
        print(self.generateLowLevelMonster(3))

    def dictBeasts(self):
        beast_list = {
            'wolf': wolf(),
            'rat': rat(),
        }
        return beast_list
    
    def dictAbominations(self):
        abomination_list = {
            'slime': slime(),
        }
        return abomination_list

if __name__ == "__main__":
    pass