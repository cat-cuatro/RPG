# John Lorenz IV 
import dungeon as d
import player
DEFAULT_DIFFICULTY = 1

def play():
    dungeon = d.dungeon(DEFAULT_DIFFICULTY)
    dungeon.test()

def main():
    play()

if __name__ == "__main__":
    main()
