import monsters
from difficulty import Adjuster
import random
random.seed()

class DungeonFloor:
    def __init__(self):
        cleared = False
        self.monsters = []
    
    def create(self, difficulty=1):
        spawner = monsters.Bestiary()
        quantity, level = self.spawnNumber(difficulty)
        self.monsters = spawner.generateLowLevelMonster(quantity, level)
    
    def spawnNumber(self, difficulty):
        if difficulty <= 3:
            quantity = random.randint(1, 3)
            level = random.randint(1, 5)
        else:
            quantity = 1
            level = 1
        return quantity, level

    def floorIsCleared(self):
        if self.Monsters:
            return False
        else:
            return True

    def monstersOnThisFloor(self):
        print(self.monsters)
        for monster in self.monsters:
            print(monster.retrieveStats())

class Dungeon:
    def __init__(self, difficulty):
        # TODO: Create as a dynamic floor generating tool, as it is currently static
        self.dungeon = {}
        self.difficulty = difficulty
        self.maxFloors = Adjuster.decideFloorCount(difficulty)
        self.levelRange = Adjuster.decideMonsterDifficulty(difficulty, self.maxFloors)
        self.iterativelyBuildFloors(difficulty)

    def iterativelyBuildFloors(self, difficulty):
        # TODO: Pass difficulty into monster creation
        for i in range(1, self.maxFloors):
            floor = DungeonFloor()
            floor.create()
            floorName = 'Floor '+str(i)
            self.dungeon.update({floorName:floor})

    def recursivelyBuildFloors(self, difficulty, i=0): # Iterative solution is better
        if i < self.maxFloors:
            i+=1
        else:
            return
        floor = DungeonFloor()
        floor.create()
        floorName = 'Floor '+str(i)
        floorDict = {
            floorName: floor
        }
        self.dungeon.update(floorDict)
        self.recursivelyBuildFloors(difficulty, i) 
        # Dictionaries are iterable in the order key-values are added as of Python 3.6, so insertions
        # recursively must be tail-ended

    def test(self):
        print('Difficulty:', self.difficulty,'Floors in this dungeon:',self.maxFloors, 'Monster level range:', self.levelRange)
        print(self.dungeon)
        #for floor in self.dungeon:
        #    self.dungeon[floor].monstersOnThisFloor()

    def traverse(self, adventurer):
        CLEARED = False
        while CLEARED == False:
            if self.dungeon[adventurer.retrieveLocation()].floorIsCleared == False:
                # If our adventurer's current floor isn't cleared, then fight monsters.
                # combat()
                pass
            else:
                # Otherwise, explore.
                # explore()
                pass