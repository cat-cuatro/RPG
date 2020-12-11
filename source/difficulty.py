import random
from math import ceil
class Adjuster:
    def decideFloorCount(difficulty):
        floorCount = 1 + (difficulty * random.randint(1, 2)) + difficulty
        return floorCount

    def decideMonsterDifficulty(difficulty, floorCount):
        floorWeight = floorCount/(difficulty * 5)
        monsterWeight = 1/floorWeight
        level = monsterWeight*difficulty + 2
        minLevel = ceil(level - ceil(difficulty/5))
        maxLevel = ceil(level)
        levelRange = {
            'min': minLevel,
            'max': maxLevel,
        }
        return levelRange


    