import item
from random import randint
class Coord():
    def __init__(self, in_coord, item=None):
        # Every set of coordinates has 3 points on the z-axis to place
        # items. It also has a status.
        # {{
        self.coord = in_coord
        self.z0 = item
        self.z1 = None
        self.z2 = None
        self.status = None
        # }}

    def __str__(self):
        return str(self.coord)

    def fall(self):
        # Stuff falls down when there's nothing below it
        # {{
        if not (self.z0 == None and self.z1 == None and self.z2 == None):
            if self.z0 == None and self.z1 == None:
                self.z0 = self.z2
                self.z2 = None
            if self.z0 == None:
                if self.z1 != None:
                    self.z0 = self.z1
                    self.z1 = self.z2
                    self.z2 = None
            if self.z1 == None:
                if self.z2 != None:
                    self.z1 = self.z2
                    self.z2 = None
        # }}

    def place(self, item_in):
        # Place something on top of the lowest level of coordinates
        # available.
        # {{
        if self.z0 != None:
            if self.z1 != None:
                if self.z2 != None:
                    print("This space is occupied")
                else:
                    self.z2 = item_in
            else:
                self.z1 = item_in
        else:
            self.z0 = item_in
        # }}

    def announce(self):
        # This will print the stack on a space. First it checks if the space is empty. If it isn't, it builds a list of objects
        # that exist on the space. It adjusts the output based on how many objects are on the space.
        # {{
        if self.z0 == None and self.z1 == None and self.z2 == None:
            return "The space is empty."
        else:
            not_empty = []
            for i in [self.z0, self.z1, self.z2]:
                if i != None:
                    not_empty.append(i)
            if len(not_empty) == 3:
                return "The {} is on the {}, which is on the {}.".format(not_empty[2], not_empty[1], not_empty[0])
            elif len(not_empty) == 2:
                return "The {} is on the {}.".format(not_empty[1], not_empty[0])
            else:
                return "The {} is on the ground.".format(not_empty[0])
        # }}
            
    def take(self, myitem):
        # Take the item from it's z-coordinate, and 
        # let everythinge else fall one space
        # {{
        if str(z0) == myitem:
            returnie = z0
            z0 = z1
            z1 = z2
            z2 = None
            return returnie
        elif str(z1) == myitem:
            returnie = z1
            z1 = z2
            z2 = None
            return returnie
        elif str(z2) == myitem:
            returnie = z2
            z2 = None
            return returnie
        # }}

    def take_z0(self):
        returnie = self.z0
        self.z0 = self.z1
        self.z1 = self.z2
        return returnie 

    def update():
        pass

# This creates a room with 25 by 25 coordinate objects, and then it randomly places
# barrels and boxes in the room. It also assigns the room one map coordinate
# {{
class Room():

    def __init__(self, characters, map_coord):
        self.characters = characters
        self.map_coord = map_coord
        self.coord_dict = {}

        for i in range(0, 25):
            for j in range(0, 25):
                self.coord_dict[(i, j)] = Coord((i, j))

        random_count = 0
        while random_count < 21:
            if random_count <= 10:
                in_item = item.Furniture('barrel')
            else:
                in_item = item.Furniture('box')
            self.coord_dict[(randint(0, 24), randint(0, 24))].place(in_item)
            random_count = randint(0, 21)

    def __str__(self):
        return str(self.map_coord)

    def __repr__(self):
        return str(self.map_coord)

    def update_characters(self, characters):
        self.characters = list(characters)
# }}
