import os, sys, time


class Player():
    def __init__(self, name, location, facing):
        self.name = name
        self.location = location
        self.facing = facing
        self.hp = 100

    def turn_east(self):
        self.facing = "East"
    def turn_west(self):
        self.facing = "West"
    def turn_north(self):
        self.facing = "North"
    def turn_south(self):
        self.facing = "South"

        

class Room():
    def __init__(self, room_id, name, description, n, s, w, e):
        self.room_id = room_id
        self.name = name
        self.description = description
        self.n = n
        self.s = s 
        self.w = w 
        self.e = e 

def create_rooms():
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
    # 12 Master Bath
    # 13 Upstairs Hall 2
    # 14 Outside Deck

    room_list = [] 
    '''
    new_room = Room(9, ' Room', '', False, 3, False, False)
    room_list.append(new_room)
    '''
    new_room = Room(9, 'Dining Room', 'There is a large dining table here with chairs.  A few extra chairs are against the wall.', False, 4, False, 2)
    room_list.append(new_room)

    new_room = Room(6, 'Kids Bedroom', 'You are in a kid\'s bedroom.  A large bunk bed takes up most of the room.  There are two dressers in the other corners.  Clothes and books are scattered around.  Its very messy', False, 3, False, False)
    room_list.append(new_room)

    new_room = Room(7, 'Parents Bedroom', 'You enter a massive bedroom.  There is a king size bed and two tables with lamps on your right.  A tan chair and foot rest is in the corner.  A small dresser is to your right, and another is on your left with a TV on top. Between the chair and TV, to the west, is mirrored hallway', False, 3, 11, False)
    room_list.append(new_room)

    new_room = Room(10, 'Porch', 'You are standing on a small porch.  There are two doors ahead of you to the north and a small table to your left.  The table has some small halloween decorations and a rotting pumpkin.', 1, False, False, False)
    room_list.append(new_room)

    new_room = Room(1, 'Foyer', 'You are standing on in the entryway. To the west is a split staircase, going up to a hallway and down to a living area.  Ahead of you is a living room and you can see a sofa.  To your right is an entryway into the Kitchen.', 2, 10, 3, 4)
    room_list.append(new_room)

    new_room = Room(2, 'Living Room', 'The living room opens up to your right.  There is a large leather sofa, a chair in the corner and a chest against the wall.  There is also a fireplace here.  You can see a dining room ahead to the north.', 9, 1, False, False)
    room_list.append(new_room)

    new_room = Room(3, 'Upstairs Hallway', 'You are in an upstairs hallway.  There are two doors on the west side, a bathroom straight ahead north , and double doors to the east on your right', 5, 1, 6, 7)
    room_list.append(new_room)

    new_room = Room(4, 'Kitchen', 'You are in a kitchen with a hardwood floor.  There is a round table with 4 chairs.  There are granite countertops with a stove built in.  The refridgerator is on the far side of the room and hums quietly.  A dog bowl is on the floor. At the far end of the room, you see an entrance into the dining room. ', 9, 1, False, False)
    room_list.append(new_room)

    new_room = Room(5, 'Upstairs Bathroom', 'You are in a small bathroom.  There are two sinks and a mirror on your right.  The toilet is hidden behind the open door.  The shower has a glass door and is partially open.  There are many towels hanging on the hooks. ', False, 3, False, False)
    room_list.append(new_room)


    rooms = {}
    for each_room in room_list:
        rooms[each_room.room_id] = each_room
    return rooms




def get_next_room(room, player):
    while True:
        choice = raw_input("Which way? ")
        if choice.lower() == 'n' and room.n != False:
            player.turn_north()
            return room.n
        if choice.lower() == 's' and room.s != False:
            player.turn_south()
            return room.s
        if choice.lower() == 'w' and room.w != False:
            player.turn_west()
            return room.w
        if choice.lower() == 'e' and room.e != False:
            player.turn_east()
            return room.e
        print "Invalid choice"

def startup():
    rooms = create_rooms()
    run_game(rooms)


def set_available_directions(room):
    available_directions = "" 
    if room.n != False:
        available_directions += "N"
    if room.s != False:
        available_directions += " S"
    if room.w != False:
        available_directions += " W"
    if room.e != False:
        available_directions += " E"
    return available_directions

def tell_player_status(rooms, player):
    print("\n")
    print("You are in the %s" % rooms[player.location].name)
    print("\n")
    print("You are facing %s" % player.facing)



def run_game(rooms):
    player = Player('Carl', 10, 'North')
    
    while True:
        #os.system('clear')
        tell_player_status(rooms, player)
        available_directions = set_available_directions(rooms[player.location])
        print
        print 
    #    print rooms[player_location].name
    #    print
        print rooms[player.location].description
        print
        print "Available Directions: " + available_directions
        print
        next_room = get_next_room(rooms[player.location], player)
        player.location = next_room


if __name__ == '__main__':
    startup()
