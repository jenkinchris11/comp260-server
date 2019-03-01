from Room import Room

class Dungeon:
    def __init__(self, items={}, npcs={}):
        self.currentRoom = 0
        self.roomMap ={}
        self.items = items
        self.npcs = npcs




    def Init(self):

        """ Room Setup """
        self.roomMap["room 0"] = Room("room 0", "You arrive at Main Street\nThe story starts here", "room 1", "", "", "")
        self.roomMap["room 1"] = Room("room 1", "You are now standing in front of a large house.\nIt looks as though nobody has lived here in a very long time","", "room 0", "room 3", "room 2")
        self.roomMap["room 2"] = Room("room 2", "You are now stood in front a strange looking statue\nIt feels as though its staring at you", "room 4", "", "", "","")
        self.roomMap["room 3"] = Room("room 3", "You are now near a Old Barn","", "", "", "room 1")
        self.roomMap["room 4"] = Room("room 4", "As you head north you can hear silent wispers as you approach a cemetery\nThis place is pretty creepy", "", "room 2", "room 5", "")
        self.roomMap["room 5"] = Room("room 5", "As you approach a small shack you can hear a voice coming from inside\nSuddenly a Grave Digger comes out of the Shack", "", "room 1", "", "room 4", "npcs={GraveDigger}")

        """ Room player starts in """
        self.currentRoom = "room 0"

    def DisplayCurrentRoom(self):
        """ Display description of room to player """
        print(self.roomMap[self.currentRoom].desc)

        print("Paths")
        """Display exits available to the player """
        exits = ["NORTH", "SOUTH","EAST","WEST"]
        exitStr = ""

        for i in exits:
            if self.roomMap[self.currentRoom].hasExit(i.lower()):
                exitStr += i + " "
        print(exitStr)

    """" if direction is valid move player in that direction """
    def isValidMove(self, direction):
        return self.roomMap[self.currentRoom].hasExit(direction)

    def MovePlayer(self,direction):
        if self.isValidMove(direction):
            if direction == "north":
                self.currentRoom = self.roomMap[self.currentRoom].north
                return

            if direction == "south":
                self.currentRoom = self.roomMap[self.currentRoom].south
                return

            if direction == "east":
                self.currentRoom = self.roomMap[self.currentRoom].east
                return

            if direction == "west":
                self.currentRoom = self.roomMap[self.currentRoom].west
                return