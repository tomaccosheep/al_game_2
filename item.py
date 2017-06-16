class Item:

    def __init__(self, name, item_type, attack=2):
        self.name = name
        self.item_type = item_type

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Spell(Item):
    def __init__(self, name):
        self.param = {'fire spell': ['spell', 50, 'on fire']}
        self.status_change = self.param[name][2]
        super().__init__(name, self.param[name][0], self.param[name][1])

class Furniture(Item):
    def __init__(self, name):
        self.box_in = None
        self.name = name
        if self.name == 'box':
            self.box_in = Spell('fire spell')
        self.param = {'box': [10, self.box_in], 'barrel': [10, None]}
        self.has = self.param[name][1]

