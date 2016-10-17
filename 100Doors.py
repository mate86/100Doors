# ========== Functions ==========

# Create an list with the close doors (0: closed, 1: opened)
def Initialization():
    Doors = []
    for i in range(100):
        Doors.append(0)                     # All doors are closed
    return Doors

# If the door is open/close, the function close/open it
def ToogleDoor(doors):
    for i in range(1, 101):
        for j in range(0, len(doors)):
            if (j+1)%i == 0:                # If the list element is divisible by "i", then test its status
                if doors[j] == 0:           # If the door is close, the function open it
                    doors[j] = 1
                else:
                    doors[j] = 0
    return doors

# Count the open doors, and stores its index in a list
def CountOpenDoors(doors):
    OpenDoorsIndex = []
    for i in range(len(doors)):
        if doors[i] == 1:
            OpenDoorsIndex.append(str(i+1))
    print("The following doors are open: " + ", ".join(OpenDoorsIndex))     # It prints the list elements without brackets

# ========== Main ==========

CountOpenDoors(ToogleDoor(Initialization()))                                # Calling the functions
