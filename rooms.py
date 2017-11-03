import os, sys, time

global player_location
player_location = 10 

def set_available_directions(room):
    available_directions = "" 
    if room.u != False:
        available_directions += "U"
    if room.d != False:
        available_directions += " D"
    if room.l != False:
        available_directions += " L"
    if room.r != False:
        available_directions += " R"
    return available_directions

class Room():
    def __init__(self, room_id, name, description, u, d, l, r):
        self.room_id = room_id
        self.name = name
        self.description = description
        self.u = u 
        self.d = d
        self.l = l 
        self.r = r


# 1 Foyer
# 2 Living Room
# 3 UpHallway
# 4 Kitchen
# 5 Up Bathroom
# 6 Spare BR
# 7 Parent BR
# 8 Kids BR 
# 9 Dining Room 
# 10 Porch
# 11 Parent BR Hall

room_list = [] 
new_room = Room(7, 'Parents Bedroom', 'You enter a massive bedroom.  There is a king size bed and two tables with lamps on your right.  A tan chair and foot rest is in the corner.  A small dresser is to your right, and another is on your left with a TV on top. Between the chair and TV is mirrored hallway', False, 3, 11, False)
room_list.append(new_room)

new_room = Room(10, 'Porch', 'You are standing on a small porch.  There are two doors ahead of you and a small table to your left.  The table has some small halloween decorations and a rotting pumpkin.', 1, False, False, False)
room_list.append(new_room)

new_room = Room(1, 'Foyer', 'You are standing on in the entryway. To your left is a split staircase, going up to a hallway and down to a living area.  Ahead of you is a living room and you can see a sofa.  To your right is an entryway into the Kitchen.', 2, 10, 3, 4)
room_list.append(new_room)

new_room = Room(2, 'Living Room', 'You are in a living room.  There is a large leather sofa, a chair in the corner and a chest against the wall.  There is also a fireplace here.  You can see a dining room ahead.', 9, 1, False, False)
room_list.append(new_room)

new_room = Room(3, 'Upstairs Hallway', 'You are in an upstairs hallway.  There are two doors on the left side, a bathroom straight ahead, and double doors to your right', 5, 1, 6, 7)
room_list.append(new_room)

new_room = Room(4, 'Kitchen', 'You are in a kitchen with a hardwood floor.  There is a round table with 4 chairs.  There are granite countertops with a stove built in.  The refridgerator is on the far side of the room and hums quietly.  A dog bowl is on the floor. On the left at the far end of the room, you see an entrance into the dining room. ', False, 1, 9, False)
room_list.append(new_room)

new_room = Room(5, 'Upstairs Bathroom', 'You are in a small bathroom.  There are two sinks and a mirror on your right.  The toilet is hidden behind the open door.  The shower has a glass door and is partially open.  There are many towels hanging on the hooks. ', False, 3, False, False)
room_list.append(new_room)


rooms = {}
for each_room in room_list:
    rooms[each_room.room_id] = each_room


def get_next_room(room):
    while True:
        choice = raw_input("Which way? ")
        if choice.lower() == 'u' and room.u != False:
            return room.u
        if choice.lower() == 'd' and room.d != False:
            return room.d
        if choice.lower() == 'l' and room.l != False:
            return room.l
        if choice.lower() == 'r' and room.r != False:
            return room.r
        print "Invalid choice"

while True:
    os.system('clear')
    available_directions = set_available_directions(rooms[player_location])
    print
    print 
#    print rooms[player_location].name
#    print
    print rooms[player_location].description
    print
    print "Available Directions: " + available_directions
    print
    next_room = get_next_room(rooms[player_location])
    player_location = next_room



