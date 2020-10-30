# John Lorenz IV // Simple RPG program
import dungeon as d
import player as p
DEFAULT_DIFFICULTY = 1

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

def play():
    dungeon = d.dungeon(DEFAULT_DIFFICULTY)
    admin = p.player(TEST_PROFILE)
    admin.printStats()
    

def main():
    play()

if __name__ == "__main__":
    main()
