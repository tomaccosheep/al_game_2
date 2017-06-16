class Character:
    def __init__(self, name, location, health = 100):
        self.location = location
        self.name = name
        self.health = health

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Player(Character):
    def __init__(self):
        super().__init__('Melgas', (24, 12), 500)
        self.inventory = []

    def inv_out(self):
        return str(self.inventory)
