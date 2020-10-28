import monsters
import random
random.seed()

class dungeonFloor:
    def __init__(self):
        cleared = False
        self.monsters = []
    
    def create(self, difficulty=1):
        spawner = monsters.bestiary()
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

    def monstersOnThisFloor(self):
        print(self.monsters)
        for monster in self.monsters:
            print(monster.retrieveStats())

        
class dungeon:
    def __init__(self, difficulty):
        # TODO: Create as a dynamic floor generating tool, as it is currently static
        self.dungeon = {
            'Floor 1': [],
            'Floor 2': [],
            'Floor 3': []
        }
        self.recursivelyBuildFloors(difficulty)
        self.maxFloors = 3

    def recursivelyBuildFloors(self, difficulty, i=0):
        if i < 3:
            i+=1
            self.recursivelyBuildFloors(difficulty, i)
        floor = dungeonFloor()
        floor.create()
        floorName = 'Floor '+str(i)
        floorDict = {
            floorName: floor
        }
        self.dungeon.update(floorDict)

    def test(self):
        for floor in self.dungeon:
            self.dungeon[floor].monstersOnThisFloor()