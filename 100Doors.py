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
    print(doors)


# ========== Main ==========

#Initialization()
ToogleDoor(Initialization())