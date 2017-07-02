class Item:

    def __init__(self, name, item_type, attack=2):
        self.name = name
        self.item_type = item_type
        self.attack = attack

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Spell(Item):
    def __init__(self, name):
        param = {'fire spell': [50, 'on fire']}
        self.status_change = param[name][1]
        super().__init__(name, 'spell', param[name][0])

class Furniture(Item):
    def __init__(self, name):
        self.box_in = None
        if name == 'box':
            self.box_in = Spell('fire spell')
        param = {'box': [10, self.box_in], 'barrel': [10, None]}
        super().__init__(name, 'furniture', param[name][0])
        self.has = param[name][1]

class Maker_maker(Item):
    def __init__(self, name):
        param = {'maker maker': ['maker', 'Maker_maker'], 'barrel maker': ['barrel', 'Furniture'], 'love maker': ['love spell', 'Spell']}
        self.makes = param[name][0]
        self.makes_type = param[name][1]
        super().__init__(name, 'maker', 0)
        

# This will create a 'casted', which is a magical spell travelling, or is
# a moving flame. This has direction, which is where it's going (it's a
# tuple that's made of 1s and -1s and 0s). It also has casted_momentum
# which is how far it can travel before it disappears, and it leaves
# a place_status on the coordinate it touches, which has place_momentum
# Some casteds will release another spell, which means that it 'has' the
# spell until it runs out of hold momentum
# {{
class Casted(Item):
    def __init__(self, name, direction, casted_momentum=5, place_status='None', place_momentum=2, hold_momentum=2, has=None):
        param = {'flame': 25, 'love': -10000}
        damage = param[name]
        super().__init__(name, 'casted', damage)
        self.direction = direction
        self.casted_momentum = momentum
        self.place_status = place_status
        self.place_momentum = place_momentum
        self.hold_momentum = hold_momentum
        self.has = has
# }}
        
