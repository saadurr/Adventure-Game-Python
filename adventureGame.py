from os import system, name
from time import sleep

# Rooms have items, players can carry items
class Item:
    def __init__(self, name='Unknown'):
        self.name = name
# A player can enter a room from any of the compass directions
class Room:
    def __init__(self, name='Unknown', north = None, east =
    None, south = None, west = None, item = None):
     # Give each room a sensible name
        self.name = name
        self.roomItems = []
        self.roomItems = item

        # Setup other rooms the player can enter
        self.north = north
        self.east = east
        self.south = south
        self.west = west

        self.totalRooms = 0
        self.calculateRooms()
        self.availableDir = [False,False,False,False]
        #north #south #east #west

    def calculateRooms(self):
        #the complexity of this function is O(1) since every statement would be executed once
        if (self.north):
            self.totalRooms = self.totalRooms + 1
            self.availableDir[0] = True
        if (self.south):
            self.totalRooms = self.totalRooms + 1
            self.availableDir[1] = True
        if (self.east):
            self.totalRooms = self.totalRooms + 1
            self.availableDir[2] = True
        if (self.west):
            self.totalRooms = self.totalRooms + 1
            self.availableDir[3] = True

    def setRooms(self,north,east,west,south,item):
        #the complexity of this would be O(1) since every step would take constant time due to execution a single time
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.roomItems = item
        self.calculateRooms()

# Represents the current player
class Player:
    def __init__(self, name='Unknown'):
        self.name = name
        self.items = []

# Overall game code and logic
class Game:
    def __init__(self, startRoom):
        self.start = startRoom
        self.directArry = []

        #           MAP OF ROOMS ARRAY
        #            0                1
        #            2                3
        #            4                5
        #            6                7
        #            8                9
        #            10               11

        #Map of house
        #Name - North - East - South - West - Item
        self.rooms = [startRoom,
                      Room("Kitchen" ),
                      Room("Living Room"),
                      Room("Library"),
                      Room("Family Room"),
                      Room("Home Office"),
                      Room("Bathroom-1"),
                      Room("Bathroom-2"),
                      Room("Laundry Room"),
                      Room("Master Bedroom"),
                      Room("Kid's Playroom"),
                      Room("Guest Room")]
        startItem = ["Flashlight"]
        self.start.setRooms(self.rooms[1],self.rooms[2],self.rooms[3],self.rooms[4],startItem)
        self.defineMap()
        #self.start.north = self.rooms[1] #kitchen
        #self.start.south = self.rooms[4]  #family room
        #self.start.west  = self.rooms[3]  #library
        #self.start.east  = self.rooms[2]  #living room
        #self.start.calculateRooms()

        #print("Room Name: {}\nRooms: {}".format(self.start.name, self.start.totalRooms))
        self.firstRoom = True
        self.currentRoom = self.start


    def defineMap(self):
        #The complexity of this function is O(1) since every step is executed once only
        #The complexity of setRooms() function is defined with the respective section

        #north east west south

        kitchenItem    = ["Knife", "Lighter", "Pan"]
        libraryItem    = ["Book", "Stapler", "Gold Coin"]
        officeItem     = ["Pen","Sharpener", "Blade", "Coffee Cup"]
        bathroomItem   = ["Soap", "Shampoo","Toothbrush"]
        playroomItem   = ["Rubber Duck","Toy Car"]
        livingRoomItem = ["Mobile Phone", "Electric Switch"]
        bedroomItem    = ["Baby Oil", "Hand Mirror"]
        familyRoomItem = ["TV Remote", "Battery"]

        #Kitchen
        self.rooms[1].setRooms(self.rooms[8], None, None,self.rooms[0], kitchenItem)

        #Living Room
        self.rooms[2].setRooms(self.rooms[9], self.rooms[10], self.rooms[0], self.rooms[7], livingRoomItem)

        #Library
        self.rooms[3].setRooms(self.rooms[6], self.rooms[0], self.rooms[11], self.rooms[5], libraryItem)

        #Family Room
        self.rooms[4].setRooms(self.rooms[0], self.rooms[7], None, None, familyRoomItem)

        #Home Office
        self.rooms[5].setRooms(self.rooms[3], None, None, None, officeItem)

        #Bathroom 1
        self.rooms[6].setRooms(None,None,None, self.rooms[5], bathroomItem)

        #Bathroom 2
        self.rooms[7].setRooms(self.rooms[2], None, self.rooms[4], None, bathroomItem)

        #Laundry Room
        self.rooms[8].setRooms(None, None, None, self.rooms[1], bathroomItem)

        #Master Bedroom
        self.rooms[9].setRooms(None, None, None, self.rooms[2], bedroomItem)

        #Kid's Playroom
        self.rooms[10].setRooms(None, None, self.rooms[2], None, playroomItem)

        #Guest Room
        self.rooms[11].setRooms(None, self.rooms[3], None, None, None)

        self.directArry = {"Kitchen":"North",
                           "Living Room": "South",
                           "Library": "West",
                           "Family Room": "East",
                           "Office": "West, South",
                           "Bathroom 1": "West, North",
                           "Bathroom 2": "East, South",
                           "Laundry Room": "North, North",
                           "Master Bedroom": "East, North",
                           "Kid's Playroom": "East, East",
                           "Guest Room": "West, West"
                           }

        #display stats
    def mainDisplay(self):
        #The complexity of this function would be O(n) in its worst case
        # where n would be the number of items (player.items)
        #At its best, the complexity would be O(1) if the array of items is empty


        clear_screen()
        # display room and player name
        print("Room: {}\t\tPlayer: {}".format(self.currentRoom.name, self.player.name))

        #Display items that player has
        if(not self.player.items):
            print ("\n\n\tInventory Empty: You dont have any items!\n\n")
        else:
            print("\n\n\tPlayer Inventory:")
            for i in self.player.items:
                print("\t\t",i)

    #check if room is available and get room if available
    def getNewRoom(self, move):
        #complexity of this function is O(1) since every statement is executed once.


        if (move == 'n'):
            if(self.currentRoom.north is not None):
                return self.currentRoom.north
        elif (move == 's'):
            if (self.currentRoom.south is not None):
                return self.currentRoom.south
        elif (move == 'e'):
            if (self.currentRoom.east is not None):
                return self.currentRoom.east
        elif (move == 'w'):
            if (self.currentRoom.west is not None):
                return self.currentRoom.west
        else:
            print("\t\tERROR: Wrong Input")
            return None

    def getItemFromRoom(self):
        #complexity of this function would be O(n) in its worst case
        #where n would be the number of items in roomItems array

        clear_screen()
        print("\n\t\tCurrent Room: {}".format(self.currentRoom.name))

        if(self.currentRoom.roomItems is None):
            print("\n\tInfo: The Room has no Items!!\n\n")
            return
        print("\n\n\tThe following items have been found in this room: ")
        #show all items list
        for it in self.currentRoom.roomItems:
            print("\t\t{}".format(it))
        print("\n\n")

        #ask if player wants to add item to their inventory
        for it in self.currentRoom.roomItems:
            choice = input("\t\tDo you want to take ** {} **? (y/n)".format(it))
            if (choice == 'y'):
                self.player.items.append(it)          #add item to player inventory
                self.currentRoom.roomItems.remove(it) #remove item from room
            elif (choice == 'n'):
                print("\t\t Player rejected taking item: {}".format(it))
            else:
                print("\t\tERROR: Wrong Response - Rejecting item")

            input("\n\n\tPress any key to continue..\n\n")

    def inGameMenu(self):
        #the complexity of this function would be O(1)

        clear_screen()
        menuMsg = """\n\t Hello {}! Please make a choice from the following options:
                \n\t\t1. Enter a Room
                \n\t\t2. Search Current Room
                \n\t\t3. Search Set of Rooms
                \n\t\t4. Get Directions for a Room
                \n\t\t5. Self Explore Mode (Hard-Coded)
                \n\t\t0. Exit Game\n"""
        menuMsg = menuMsg.format(self.player.name)

        opt = int(input(menuMsg))

        if (opt <=5 and opt >= 0):
            input("\n\tPress any key to continue...")
            return opt
        else:
            input("\n\tWrong Option - Default option is 1\n\tPress any key to continue...")
            return 1

    def searchCurrentRoom(self):
        #The complexity of this function would be O(n)
        #where n is the number of items in the room (stored in roomItems array)

        clear_screen()
        print("Room: {}\t\tPlayer: {}".format(self.currentRoom.name, self.player.name))

        print("\n\n\tSearching Room: {}".format(self.currentRoom.name))

        if (self.currentRoom.roomItems is None):
            input("\n\tInfo: The Room has no Items!!\n\tPress any key to continue..\n")
            return
        print("\n\n\tThe following items have been found in this room: ")
        # show all items list
        for it in self.currentRoom.roomItems:
            print("\t\t{}".format(it))
        input("\n\n\tPress any key to continue...")

    def enterRoom(self):
        #The complexity of this function would be O(1) since every instruction is executed once.

        self.mainDisplay()
        self.getItemFromRoom()

        self.mainDisplay()
        inpDir = str(input("\n\nEnter a direction to move:"))
        newRoom = self.getNewRoom(inpDir)

        if (newRoom is None):
            print("\t\tSORRY!! There is no room in this direction!")
            input("\n\tPress any key to continue...")
        else:
            self.currentRoom = newRoom
            clear_screen()
            print("\n\t\tEntering Room: {}".format(self.currentRoom.name))
            input("\n\tPress any key to continue...")

    def searchSetOfRooms(self):
        #The complexity of this would be O(n)* O(m) * O(k) in worst case
        #   where
        #       n is the number of rooms to be searched,
        #       m is the total number of available rooms
        #       k is the number of items in each room

        maxRoom = len(self.rooms)

        print("\n\tThe following are available names of rooms:")
        for r in self.rooms:                                            #O(n)
            print ("\t\t",r.name)

        searchStr = str(input("\n\tEnter rooms to search: (each room name should be separated by commas)"))
        searchArr = searchStr.split(",")
        foundItems = []

        #remove extra elements
        while (len(searchArr) > maxRoom):                             #O(n-m)
            searchArr.pop()

        #iterate over rooms
        for toFindRoom in searchArr:                                  #O(n)

            for room in self.rooms:                                   #O(m)

                if(toFindRoom == room.name):

                    for it in room.roomItems:                         #O(k)
                        foundItems.append(it)

        if (foundItems is not None):
            print("\n\n\tThe following items have been found in these rooms: {}".format(searchStr))
            for i in foundItems:                                   #O(n)
                print("\t\t{}".format(i))

        input("\n\n\tPress any key to continue...")

    def getDirectionsForRoom(self):
        #complexity is O(1)

        clear_screen()
        print("Room: {}\t\tPlayer: {}".format(self.currentRoom.name, self.player.name))

        toFind = input("\n\tEnter room name to find directions from start room:\n")

        print("\n\tSearching Directions.")
        sleep(0.2)
        print("\n\tSearching Directions..")
        sleep(0.2)
        print("\n\tSearching Directions...")
        sleep(0.2)
        print("\n\tSearching Directions....")
        sleep(0.2)

        if(toFind in self.directArry.keys()):
            print("\n\tDirections Found! You have to take the following directions from Start Room:")
            print("\n\t{}".format(self.directArry[toFind]))
        else:
            print("\n\tError: Room does not exist\n")

        input("\n\tPress any key to continue...\n")



    def enterRoomWithDirection(self, dir):
        #the complexity for this would be O(1) since every line is executed once only

        compass = None
        if (dir=="n"):
            newRoom = self.currentRoom.north
            compass = "North"
        elif (dir=="s"):
            newRoom = self.currentRoom.south
            compass = "South"
        elif (dir=="e"):
            newRoom = self.currentRoom.east
            compass = "East"
        elif (dir=="w"):
            newRoom = self.currentRoom.west
            compass = "West"

        #print message
        self.enterRoomMsg(newRoom.name, compass)
        #change room
        self.currentRoom = newRoom
        #displayItems
        self.displayItemsInRoom()

    def displayItemsInRoom(self):
        clear_screen()
        print("Room: {}\t\tPlayer: {}".format(self.currentRoom.name, self.player.name))

        if (self.currentRoom.roomItems is None):
            input("\n\tInfo: The Room has no Items!!\n\tPress any key to continue..\n")
            return
        print("\n\n\tThe following items have been found in this room: ")
        # show all items list
        for it in self.currentRoom.roomItems:
            print("\t\t{}".format(it))
        input("\n\n\tPress any key to continue...")

    def exploreAllRooms(self):
        self.mainDisplay()

        print("\n\tYou are in self explore mode - This would take you through the following rooms:")
        for r in self.rooms:
            print("\t\t", r.name)
        input("\n\tPress any key to continue...")

        self.mainDisplay()

        self.currentRoom = self.start

        self.enterRoomWithDirection("s")
        self.enterRoomWithDirection("e")

        self.enterRoomWithDirection("n")
        self.enterRoomWithDirection("n")

        self.enterRoomWithDirection("s")
        self.enterRoomWithDirection("e")

        self.enterRoomWithDirection("w")
        self.enterRoomWithDirection("w")

        self.enterRoomWithDirection("n")
        self.enterRoomWithDirection("n")

        self.enterRoomWithDirection("s")
        self.enterRoomWithDirection("s")

        self.enterRoomWithDirection("w")
        self.enterRoomWithDirection("n")
        self.enterRoomWithDirection("s")
        self.enterRoomWithDirection("s")
        self.enterRoomWithDirection("n")
        self.enterRoomWithDirection("w")




    def enterRoomMsg(self,roomName, cdir):
        # the complexity for this would be O(1) since every line is executed once only

        input("\n\tPress any key to continue..")
        clear_screen()
        message = "\n\n\tYou are moving in {} direction.\n\tYou are leaving {} and entering {}.\n\tPress any key to continue..."
        message = message.format(cdir, self.currentRoom.name,roomName)
        input(message)


    def play(self, player):
        self.player = player

        while (True):
            #read player choice
            option = self.inGameMenu()

             #quit game
            if(option==0):
                break
            elif(option==1):
                self.enterRoom()
            elif(option==2):
                self.searchCurrentRoom()
            elif(option==3):
                self.searchSetOfRooms()
            elif(option==4):
                self.getDirectionsForRoom()
            elif(option==5):
                self.exploreAllRooms()

        return

def clear_screen():
    # the complexity for this would be O(1) since every line is executed once only
    system('cls' if name == 'nt' else 'clear')

if __name__ == '__main__':
    # the complexity for this would be O(1) since every line is executed once only

    # Setup the game board
    r = Room("StartRoom")
    g = Game(r)

    #take player name input
    pname = str(input("Enter Player Name:"))
    clear_screen()
    print("\t\tHi {}! \n\t\tWelcome to the game".format(pname))

    # Play as player
    p = Player(pname)
    input("\n\nPress Enter to continue...")
    sleep(0.5)

    clear_screen()


    g.play(p)


