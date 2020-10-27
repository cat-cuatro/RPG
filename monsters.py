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



### Monster Generator/Catalog
class bestiary:
    def __init__(self):
        self.beasts = self.beasts()
        self.abomination = self.abominations()
    
    def generateLowLevelMonster(self, level=1):
        pass

    def test(self):
        print(len(self.beasts))
        for beast in self.beasts:
            print(self.beasts[beast].retrieveStats())

    def beasts(self):
        beast_list = {
            'wolf': wolf(),
            'rat': rat(),
        }
        return beast_list
    
    def abominations(self):
        abomination_list = {
            'slime': slime(),
        }
        return abomination_list

if __name__ == "__main__":
    pass