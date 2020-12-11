# John Lorenz IV // Simple RPG program
import dungeon as d
import player as p
DEFAULT_DIFFICULTY = 2

TEST_PROFILE = {
    'name' : 'Cuatro',
    'health': 150,
    'attack': 25,
    'defense': 10,
    'intellect': 10,
    'role': 'admin',
    'charisma': 100,
    'luck': 100,
    'perception': 100,
}

def iAmTrue():
    return True

def tests():
    dungeon = d.Dungeon(DEFAULT_DIFFICULTY)
    dungeon.test()

def play():
    dungeon = d.Dungeon(DEFAULT_DIFFICULTY)
    admin = p.Player()
    

def main():
    play()

if __name__ == "__main__":
    tests()
    main()
