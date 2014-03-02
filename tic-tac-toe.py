'''
Name: Kush Patel

Purpose:
To use the minimax rule to write the AI for Tic Tac Toe.

GUI Details:

# cell 0 is from range 105 <= x <= 195 and 305 <= y <= 395.
# cell 1 is from range 205 <= x <= 295 and 305 <= y <= 395.
# cell 2 is from range 305 <= x <= 395 and 305 <= y <= 395.
#
# cell 3 is from range 105 <= x <= 195 and 205 <= y <= 295.
# cell 4 is from range 205 <= x <= 295 and 205 <= y <= 295.
# cell 5 is from range 305 <= x <= 395 and 205 <= y <= 295.
#
# cell 6 is from range 105 <= x <= 195 and 105 <= y <= 195.
# cell 7 is from range 205 <= x <= 295 and 105 <= y <= 195.
# cell 8 is from range 305 <= x <= 395 and 105 <= y <= 195.
#
# Play Again button is from range 450 <= x <= 550 and 100 <= y <= 200.
#
#
# The First Vertical line for the play grid starting from the left is from range
#   195 < x < 205 and 100 < y < 400.
#
# The Second Vertical line for the play grid starting from the left is from range
#   295 < x < 305 and 100 < y < 400.
#
# The Top Horizontal line for the play grid is from range
#   100 < x < 400 and 295 < y < 305.
#
# The Bottom Horizontal line for the play grid is from range
#   100 < x < 100 and 195 < y < 205.
#

Data Model:
A *state* is a list of nine strings, each of whose members is either
'x', 'o', or 'e'. The state S is visualized as a board configuration
in which the contects of cell i is S[i] for 0<=i<9. For example, the
state ['x', 'e', 'e', 'e', 'o', 'e', 'e', 'e', 'x'] can be visualized as
follows:

    x| |
    -----
     |o|
    -----
     | |x

A *point* is a pair (x,y) of integers where 0<=x<=600 and 0<=y<=500.
Points are interpreted as points in a graphics window 600 pixels wide
by 500 pixels high, with (0,0) in the lower left corner, x increasing
to the right and y increasing upward

A *position* is an integer in the interval [0,11). Position 0 to 8
inclusive represent squares on the tic tac toe board as pictured below:

    0|1|2
    -----
    3|4|5
    -----
    6|7|8

position 9 represents the "play again" button and position 10 represents
the area that player cannot interact with.
     ______________________________
    |                              |
    |                              |
    |                              |
    |         0|1|2          10    |
    |         -----                |
    |         3|4|5                |
    |         -----                |
    |         6|7|8                |
    |                     _____    |
    |                    |__9__|   |
    |                              |
    |                              |
    |                              |
    |______________________________|

    
A *letter* is a string, it can be either 'x' or 'o'.

A *generalList* is a list of four integers. A generalList can be a list of 
corner positions of the game board: [0,2,6,8] or generalList can be a list of positions: [1,3,5,7]

A *line segment* is a 4-tuple (x1,y1,x2,y2) of integers where 0 ≤ x1, x2 ≤ 600 and 0≤ y1, y2≤ 500. Intuitively, it is the line segment connecting the points (x1,y1) and (x2,y2) in the coordinate system whose origin is the lower left corner of the display screen. 

A *Circle* is a triple (x,y,R) where (x,y) is a point and R is an integer. It is thought of as the circle whose center is (x,y) and whose radius is R, in the coordinate system whose origin is the lower left corner of the display screen. 

A *displayText* is 4-tuple (c,x,y,s) where c is a string, x and y are nonnegative integers, and s is an integer in the interval [5,37). Intuitively, displayText (c,x,y,s) is the image of a text string, centered at point (x,y) of height s in pixels.

An *image* is a line segment, a circle, or a displayText. 

An *imageList* is a list of images.

A *bestValue* is the best possible value of the move that 'o' makes based on the minimax rule.

A *bestMove* is the cell prescribed for 'o' based on the minimax rule.

A *value* can be either 0,1, or 2.


'''

import random

# initialState: state
# initialState() is the state corresponding to an empty board.
def initialState():
    state = ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']
    return state

# successor: state*point -> state
# if S is a state and p is a point,  then successor(S,p) is the
# game state resulting from clicking point p in game state S.
def successor(state, point):
    position = checkPointPosition(point)
    if position == 10:
        return state
    
    if isWinner(state, 'x') or isWinner(state, 'o') or boardFull(state):
        if position == 9:
            state = initialState()
        return state
        
    elif (position >= 0 and position <= 8):
        if state[position] == 'e':
            state[position] = 'x'     
            if (not isWinner(state, 'x') and (not boardFull(state))):            
                state = isComputerTurn(state)            
        return state
        
    elif position == 9:
        state = initialState()
        return state
    
# boardFull: state -> bool
# if S is a state, then boardFull(S) is True when there is no 'e' in S.
def boardFull(state):
    if 'e' in state:
        return False
    return True

# checkPointPosition: point -> position
# if p is a point, then checkPointPosition(p) is the position of p on the game area. 
def checkPointPosition(point):
    x = point[0]
    y = point[1]
    position = 10
    
    #check if point is in the play grid
    if (x >= 100 and x <= 400 and y >= 100 and y <= 400):
        if(105 <= x <= 195 and 305 <= y <= 395):
            position = 0
        # Cell 1 Click
        elif(205 <= x <= 295 and 305 <= y <= 395):
            position = 1
        # Cell 2 Click
        elif(305 <= x <= 395 and 305 <= y <= 395):
            position = 2
        # Cell 3 Click
        elif(105 <= x <= 195 and 205 <= y <= 295):
            position = 3
        # Cell 4 Click
        elif(205 <= x <= 295 and 205 <= y <= 295):
            position = 4
        # Cell 5 Click
        elif(305 <= x <= 395 and 205 <= y <= 295):
            position = 5
        # Cell 6 Click
        elif(105 <= x <= 195 and 105 <= y <= 195):
            position = 6
        # Cell 7 Click
        elif(205 <= x <= 295 and 105 <= y <= 195):
            position = 7
        # Cell 8 Click
        elif(305 <= x <= 395 and 105 <= y <= 195):
            position = 8
    # Play Again Click
    elif(450 <= x <= 550 and 100 <= y <= 200):
        position = 9
    
    else:
        position = 10
        
    return position

# isComputerTurn: state->state
# if S is a state, then isComputerTurn(S) returns the state after 'o'(the computer) makes the best available move. 
def isComputerTurn(state):
    position,value = max_move(state)
    state[position] = 'o'
    return state

# min_move: state->bestMove,bestValue
# if S is a valid state and it is 'o' move in S, then min_move(S) returns the bestMove and bestValue for 'o' in state S based on the minimax rule.
def min_move(state):
    bestValue = None
    bestMove = None
    
    for i in range(0,9):
        if state[i] == 'e':
            state[i] = 'x'
            if isWinner(state,'x') or isWinner(state,'o') or boardFull(state):
                value = getValue(state)
            else:
                position,value = max_move(state)
            state[i] = 'e'
        
            if bestValue == None or value < bestValue:
                bestValue = value
                bestMove = i
                
    return bestMove, bestValue

# max_move: state->bestMove,bestValue
# if S is a valid state, then max_move(S) returns the bestMove and bestValue for 'o' in S based on the minimax rule.
def max_move(state):
    bestValue = None
    bestMove = None
    for i in range(0,9):
        if state[i] == 'e':
            state[i] = 'o'
            if isWinner(state,'x') or isWinner(state,'o') or boardFull(state):
                value = getValue(state)
            else:
                position,value = min_move(state)
            state[i] = 'e'

            if bestValue == None or value > bestValue:
                bestValue = value
                bestMove = i
            
    return bestMove, bestValue


# getValue: state->value
# if S is a valid state, getValue(S) is the value of S to player 'o' and a minimax rule using the full game tree.
def getValue(state):
    if isWinner(state,'x'):
        return 0
    elif boardFull(state):
        return 1
    elif isWinner(state,'o'):
        return 2

# isWinner: state*letter->bool
# if S is a state and l is a letter, then isWinner(S,l) returns True if l reaches a winning state, False otherwise. 
def isWinner(state, letter):
    if ((state[0] == state[1] == state[2] == letter) or (state[3] == state[4] == state[5] == letter) or (state[6] == state[7] == state[8] == letter) or
        (state[0] == state[3] == state[6] == letter) or (state[1] == state[4] == state[7] == letter) or (state[2] == state[5] == state[8] == letter) or (state[0] == state[4] == state[8] == letter) or (state[2] == state[4] == state[6] == letter)):        
        return True
    return False


# displayImages: gameState -> ImageList
# if S is a gameState
# then displayImages(S) is a list containing the images to be displayed on the sceen
#   in program state S. 
def displayImages(S):
    return background() + showMove(S)


# background: ImageList
# background() is a list containing the images to display the board and the play again button.
def background():
    VL1 = (196,400,196,100)
    VL2 = (204,400,204,100)
    VL3 = (296,400,296,100)
    VL4 = (304,400,304,100)

    HL1 = (100,196,400,196)
    HL2 = (100,204,400,204)
    HL3 = (100,296,400,296)
    HL4 = (100,304,400,304)

    PA1 = (450,100,450,200)
    PA2 = (450,100,550,100)
    PA3 = (550,100,550,200)
    PA4 = (450,200,550,200)
    PAT = ("Play Again", 500, 150, 16)

    return [VL1,VL2,VL3,VL4,HL1,HL2,HL3,HL4,PA1,PA2,PA3,PA4,PAT]


# showMove: gameState -> ImageList
# if S is a gameState
# then showMove(S) is a list containing the images for X and O to be displayed on the sceen.
def showMove(S):
    imageList = []
    if S[0] == 'x':
        imageList.append((125,375,175,325))
        imageList.append((125,325,175,375))
    elif S[0] == 'o':
        imageList.append((150,350,25))
        
    if  S[1] == 'x':
        imageList.append((225,375,275,325))
        imageList.append((225,325,275,375))
    elif  S[1] == 'o':
        imageList.append((250,350,25))

    if  S[2] == 'x':
        imageList.append((325,375,375,325))
        imageList.append((325,325,375,375))
    elif  S[2] == 'o':
        imageList.append((350,350,25))

    if  S[3] == 'x':
        imageList.append((125,275,175,225))
        imageList.append((125,225,175,275))
    elif  S[3] == 'o':
        imageList.append((150,250,25))

    if  S[4] == 'x':
        imageList.append((225,275,275,225))
        imageList.append((225,225,275,275))
    elif S[4] == 'o':
        imageList.append((250,250,25))

    if  S[5] == 'x':
        imageList.append((325,275,375,225))
        imageList.append((325,225,375,275))
    elif  S[5] == 'o':
        imageList.append((350,250,25))

    if  S[6] == 'x':
        imageList.append((125,175,175,125))
        imageList.append((125,125,175,175))
    elif S[6] == 'o':
        imageList.append((150,150,25))

    if  S[7] == 'x':
        imageList.append((225,175,275,125))
        imageList.append((225,125,275,175))
    elif  S[7] == 'o':
        imageList.append((250,150,25))

    if  S[8] == 'x':
        imageList.append((325,175,375,125))
        imageList.append((325,125,375,175))
    elif  S[8] == 'o':
        imageList.append((350,150,25))
        
    
    return imageList


######################################################################
######################################################################
# TPGE GAME ENGINE
#

# displaySize() is the size of the display window, (width, height)

def displaySize() : return (600,500)
from graphics import *

# If x is an image, imageKind(x) is the type of image x is:
# 'circle', 'text', or 'lineSegment'

def imageKind(x):
    if len(x)==3 : return 'circle'
    elif type(x[0])== str :return 'text'
    else : return 'lineSegment'

    
# If x is an image, convert(x) is the corresponding image in the
# graphics.py library. We turn the screen upside down so that the origin
# is in the lower left corner, so it matches what they learn in algebra
# class.

def convert(x):
    if imageKind(x)=='circle': return convertCircle(x)
    elif imageKind(x)=='lineSegment': return convertLine(x)
    elif imageKind(x)=='text' : return convertText(x)


def convertLine(x):
    (W,H) = displaySize()
    P1 = Point(x[0],H - x[1])
    P2 = Point(x[2],H - x[3])
    return Line(P1,P2)

def convertText(x):
    (W,H) = displaySize()
    center = Point(x[1],H-x[2])
    string = x[0]
    size = x[3]
    T = Text(center,string)
    T.setSize(size)
    return T

def convertCircle(x):
    (W,H) = displaySize()
    center = Point(x[0],H-x[1])
    radius = x[2]
    return Circle(center,radius)

# Create a window to play in
display = GraphWin("My game", displaySize()[0], displaySize()[1])


# The main loop
#
# Set the state, draw the display, get a mouse click, set the new state,
# and repeat until the user closes the window.

S = initialState()
images = [convert(x) for x in displayImages(S)]

while(True):
    for x in images: x.draw(display)
    c = display.getMouse()
    click = (c.getX(),displaySize()[1] - c.getY())
    S = successor(S,click)
    for I in images: I.undraw()
    images = [convert(x) for x in displayImages(S)]
      
        
    
    
