import room, item, curses
from time import sleep
from random import randint



# This will look up the visual character representation based on the
# inputed item's name
# {{
def get_visual_character(item):
    visual_char_dict = {'barrel': '🛢', 'box': '☐', 'player': '👵'}
    return visual_char_dict[item.name]
# }}


# This function prints the room to the screen. It checks the z0 value
# of every room coordinate (which is whatever is on the floor), and
# if there's nothing there then it will print a period. Otherwise it
# uses the get_visual_character() function to figure out what to place
# in the coordinates, based on the z0 item's name.
# All coordinates are shifted so that the x-axis is doubled in length,
# because otherwise it looks compressed.
# {{
def print_room(in_room, the_player):
    for (i, j) in in_room.coord_dict:
        if in_room.coord_dict[(i, j)].z0 == None:
            try:
                myscreen.addstr(i, j * 2, '.')
            except:
                pass
        else:
            visual_char = in_room.coord_dict[(i, j)].z0
            myscreen.addstr(i, j * 2, get_visual_character(visual_char))
    myscreen.addstr(the_player.location[0], the_player.location[1] * 2, get_visual_character('player'))
    myscreen.refresh()
# }}


# This allows you to place an item with map coordinates. It takes in
# the room and coordinates, and it access the Coord object based
# on that information. The Coord object has a "place" method that
# this function uses.
# {{
def place_with_map_coords(in_room, in_item, in_coords):
    in_room.coord_dict[(in_coords[0], in_coords[1])].place(in_item)
# }}

def check_win(player):
    pass

def check_death(player):
    pass

def update_player(player):
    check_win(player)
    check_death(player)
    

def update_characters(characters):
    for i in characters:
        if i.health < 0:
            pass #kill them here
    pass

def update_room(in_room):
    for i in in_room.room_coord:
        i.update

def update(player, in_room, characters):
    update_player(player)
    update_characters(characters)
    update_room(in_room)


# This will build a room. First it creates an empty list,
# coordinate_builder, and it receives the central coordinates for
# it's map. It builds off the map coordinates, making a room with
# two points above and two points below
# {{
def build_room(in_coord):
    coordinate_builder = []
    iterate_y = in_coord[0]
    iterate_x = in_coord[1]
    for i in range(iterate_y - 12, iterate_y + 12):
        for j in range(iterate_x - 12, iterate_x + 12):
            coordinate_builder.append((i, j))
    room1 = room.Room([], coordinate_builder)
    return room1
# }}


# This will build a bunch of rooms and swap coordinates
# with the rooms around them
# {{
def build_room_list():
    # This makes a dictionary of rooms with a tuple as
    # the key for each room. 
    room_dict = {}
    for i in range(12, 112, 25):
        for j in range(12, 112, 25):
            room_dict[(i, j)] = build_room((i, j)) 
    #for (i, j) in room_dict:
    #    try:
            
        
    return room_list_of_list
# }}
                


players = []
rooms = []

# The game is not over, and the player has not yet done anything to
# use up their turn
# {{
game_over = False
turn_finished = False
# }}

# Establish a screen {{
myscreen = curses.initscr()
# }}


# Establish a test room, and place items into that test room
# {{
test_room = build_room((12, 12))
item1 = item.Furniture('barrel')
item2 = item.Furniture('box')
place_with_map_coords(test_room, item1, (0, 1))
place_with_map_coords(test_room, item2, (2, 3))
# }}

print_room(test_room)
sleep(3)
curses.endwin()


# This while-loop will run throughout the game
# {{
#while not game_over:
#    pass
# }}



