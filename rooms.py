import os, sys, time
import title
import client

class Player():
    def __init__(self, name, location, facing):
        self.name = name
        self.location = location
        self.facing = facing
        self.hp = 100
        nickname = client.create_player(name, location)

    def turn_east(self):
        self.facing = "East"
    def turn_west(self):
        self.facing = "West"
    def turn_north(self):
        self.facing = "North"
    def turn_south(self):
        self.facing = "South"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'        

class Room():
    def __init__(self, room_id, name, description, n, s, w, e, u, d):
        self.room_id = room_id
        self.name = name
        self.description = description
        self.n = n
        self.s = s 
        self.e = e
        self.w = w 
        self.u = u
        self.d = d 

def main_menu():
    title.print_title()
    print("\n\n")
    user = raw_input("Your name: ")
    player_loc = client.check_player_exists(user)
    if player_loc:
        player = Player(user, player_loc, 'North')
    else:
        player = Player(user, 10, 'North')
    return player

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
    room_list.append(Room(9, ' Room', '', False, 3, False, False)
    room_list.append(new_room)
    North, South, West, East
    '''
    room_list.append(Room(8, 'Kids Bedroom', 'A large bunk bed takes up most of the room.', 13, False, False, False, False, False))
    room_list.append(Room(14, 'Outside Deck', 'A large wooden deck with furniture and a hammock.', False, 9, False, False, False, False))
    room_list.append(Room(13, 'West Upstairs Hall', 'The west end of the hallway has the laundry closet.', False, 8, 5, 3, False, False))
    room_list.append(Room(12, 'Master Bathroom', 'A shower with a glass door at one end and a bath tub at the other.  A window on the other side of the tub overlooks the neighborhood.', False, False, False, 11, False, False))
    room_list.append(Room(11, 'Master Bedroom Hall', 'A double sink on one side and a mirrored closet on the other.', False, False, 12, 7, False, False))

    room_list.append(Room(9, 'Dining Room', 'There is a large dining table here with chairs.  A few extra chairs are against the wall.', 14, 4, 2, False, False, False))
    
    room_list.append(Room(6, 'Guest Room', 'A mostly empty room with a fold out bed.', 3, False, False, False, False, False))

    room_list.append(Room(8, 'Kids Bedroom', 'You are in a kid\'s bedroom.  A large bunk bed takes up most of the room.  There are two dressers in the other corners.  Clothes and books are scattered around.  Its very messy', 13, False, False, False, False, False))

    room_list.append(Room(7, 'Parents Bedroom', 'You enter a massive bedroom.  There is a king size bed and two tables with lamps on your right.  A tan chair and foot rest is in the corner.  A small dresser is to your right, and another is on your left with a TV on top. Between the chair and TV, to the west, is mirrored hallway', False, 3, 11, False, False, False))

    room_list.append(Room(10, 'Porch', 'You are standing on a small porch.  There are two doors ahead of you to the north and a small table to your left.  The table has some small halloween decorations and a rotting pumpkin.', 1, False, False, False, False, False))

    room_list.append(Room(1, 'Foyer', 'You are standing on in the entryway. To the west is a split staircase, going up to a hallway and down to a living area.  Ahead of you is a living room and you can see a sofa.  To your right is an entryway into the Kitchen.', 2, 10, 3, 4, False, False))

    room_list.append(Room(2, 'Living Room', 'The living room opens up to your right.  There is a large leather sofa, a chair in the corner and a chest against the wall.  There is also a fireplace here.  You can see a dining room ahead to the north.', False, 1, False, 9, False, False))

    room_list.append(Room(3, 'East Upstairs Hallway', 'You are in an upstairs hallway.  There are two doors on the west side, a bathroom straight ahead north , and double doors to the east on your right', 7, 6, 13, 1, False, False))

    room_list.append(Room(4, 'Kitchen', 'You are in a kitchen with a hardwood floor.  There is a round table with 4 chairs.  There are granite countertops with a stove built in.  The refridgerator is on the far side of the room and hums quietly.  A dog bowl is on the floor. At the far end of the room, you see an entrance into the dining room. ', 9, False, 1, False, False, False))

    room_list.append(Room(5, 'Upstairs Bathroom', 'You are in a small bathroom.  There are two sinks and a mirror on your right.  The toilet is hidden behind the open door.  The shower has a glass door and is partially open.  There are many towels hanging on the hooks. ', False, False, False, 13, False, False))

    rooms = {}
    for each_room in room_list:
        rooms[each_room.room_id] = each_room
    return rooms




def get_next_room(room, player):
    while True:
        choice = raw_input("Which way? (q to quit)")
        if choice.lower() == 'q':
            sys.exit()
        if choice.lower() == 'who':
            who()
        if choice.lower() == 'n' and room.n != False:
            player.turn_north()
            client.move_player_to_room(player.name, room.n)
            return room.n
        if choice.lower() == 's' and room.s != False:
            player.turn_south()
            client.move_player_to_room(player.name, room.s)
            return room.s
        if choice.lower() == 'w' and room.w != False:
            player.turn_west()
            client.move_player_to_room(player.name, room.w)
            return room.w
        if choice.lower() == 'e' and room.e != False:
            player.turn_east()
            client.move_player_to_room(player.name, room.e)
            return room.e
        print "Invalid choice"

def check_server_status():
    server_status = client.server_status()
    if server_status != 200:
        print server_status
        print bcolors.FAIL,
        print "Server not responding.\n",
        print bcolors.ENDC
        sys.exit()


def startup():
    check_server_status()
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
    title.print_title()
    print bcolors.OKBLUE,
    if player.location == 10 or player.location == 14:
        print("\n  You are on the %s, facing %s\n" % (rooms[player.location].name, player.facing))
    else:
        print("\n  You are in the %s, facing %s\n" % (rooms[player.location].name, player.facing))
    print bcolors.ENDC,

    items = client.get_objects_in_room(player.location)
    
    print bcolors.OKGREEN,
    if items[0]:
        print("These items are here:"),
        for item in items[0]:
            print("%s," % item), 
    else:
        print("There are no items here"),
    print bcolors.ENDC,
    
    print bcolors.HEADER,
    if len(items[1]) > 1:
        print("\n  These others are here :"),
        for item in items[1]:
            for person in item.split():
                if person != player.name:
                    print("%s" % person),
    else:
        print("\n  There are no others here")
    print bcolors.ENDC,

def who():
    stuff = client.who()
    print stuff
    return
    


def run_game(rooms):
    player = main_menu()
    #player = Player('Carl', 10, 'North')
    
    while True:
        #os.system('clear')
        tell_player_status(rooms, player)
        available_directions = set_available_directions(rooms[player.location])
        print
        print 
        print rooms[player.location].description
        print
        print "Available Directions: " + available_directions
        print
        next_room = get_next_room(rooms[player.location], player)
        player.location = next_room


if __name__ == '__main__':
    startup()
