# ========== Functions ==========

def Initialization():
    Doors = []
    for i in range(100):
        Doors.append(0)
    return Doors


def ToogleDoor(doors):
    step = 1
    while step <=100:
        for i in range(0, len(doors), step):
            if doors[i] == 0:
                doors[i] = 1
            else:
                doors[i] = 0
        step += 1
    return doors
    #print(doors)

def CountOpenDoors(doors):
    OpenDoors = []
    for i in range(len(doors)):
        if doors[i] == 1:
            OpenDoors.append(i)
    print("The following doors are open: ")
    for i in range(len(OpenDoors)):
        print(OpenDoors[i])



# ========== Main ==========

#Initialization()
CountOpenDoors(ToogleDoor(Initialization()))