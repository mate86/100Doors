# ========== Functions ==========

# Create an list with the close doors (0: closed, 1: opened)
def Initialization():
    Doors = []
    for i in range(100):
        Doors.append(0)    # All doors are closed
    return Doors

# If the door is open/close, the function close/open it
def ToogleDoor(doors):
    for step in range(1, len(doors)):    # This loop changes the step
        for i in range(step, len(doors), step):
            if doors[i] == 0:   # If the door is close, opens it
                doors[i] = 1
            else:
                doors[i] = 0    # If the door is open, close it
    return doors

# Count the open doors, and stores its index in a list
def CountOpenDoors(doors):
    OpenDoorsIndex = []
    for i in range(len(doors)):
        if doors[i] == 1:
            OpenDoorsIndex.append(str(i))
    print("The following doors are open: " + ", ".join(OpenDoorsIndex))    # It prints the list elements without brackets

# ========== Main ==========

# Calling the functions
CountOpenDoors(ToogleDoor(Initialization()))