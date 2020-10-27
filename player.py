class player:
    def __init__(self, profile=None):
        if profile != None:
            self.load(profile)
        else:
            self.name = None
            self.health = 100
            self.attack = 10
            self.defense = 10

    def load(self):
        self.name = profile['name']
        self.health = profile['health']
        self.defense = profile['defense']

if __name__ == "__main__":
    pass