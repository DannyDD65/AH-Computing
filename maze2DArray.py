import numpy as np

room = 0

roomList = [[-1, 1, -1, -1], [-1, 2, 4, 0], [-1, -1, 5, 1],
            [-1, 4, 6, -1], [1, -1, -1, 3], [2, -1, -1, -1],
            [3, 7, -1, -1], [-1, 8, -1, 6], [-1, -1, -1, 7]]
validInputs = ["w", "a", "s", "d"]

print("You are in a maze 3x3 large. Starting in room 0, you must make your way to room 8.")
print(" the maze is set up such that room 0, 1, and 2 are in the top row, 3, 4, and 5 are in the middle row and so on.")
print("Use W to move up, A to move left, D to move right, and S to move down")

def move(playerInput):
    if playerInput.lower() not in validInputs:
        return
    global room
    if playerInput.lower() == "w":
        newRoom = roomList[room][0]
    elif playerInput.lower() == "a":
        newRoom = roomList[room][3]
    if playerInput.lower() == "s":
        newRoom = roomList[room][2]
    elif playerInput.lower() == "d":
        newRoom = roomList[room][1]
    if newRoom == -1:
        print("You hit a wall")
    else: 
        room = newRoom

while room != 8:
    print("You are in room " + str(room))
    move(input("What direction to move: "))

print("You reached the Exit!!! Well Done!!")
exit()