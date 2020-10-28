from bangtal import *
from enum import Enum

setGameOption(GameOption.ROOM_TITLE, False)
setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

scene = Scene('오델로','images/background.png')

#상태함수
class State(Enum):
    BLANK = 0
    POSSIBLE = 1
    BLACK = 2
    WHITE = 3

#턴함수 
class Turn(Enum):
    BLACK = 1
    WHITE = 2
turn = Turn.BLACK

#상태함수
def setState(x,y,s):
    object = board[y][x]
    object.state = s
    if s == State.BLANK:
        object.setImage("images/blank.png")
    elif s == State.BLACK:
        object.setImage("images/black.png")
    elif s == State.WHITE:
        object.setImage("images/white.png")
    elif turn == Turn.BLACK:
        object.setImage("images/black possible.png")
    else:
        object.setImage("images/white possible.png")

#상태함수2
def stone_onMouseAction(x,y):
    global turn

    object = board[y][x]
    if object.state == State.POSSIBLE:
        if turn == Turn.BLACK:
            setState(x,y,State.BLACK)
            reverse_xy(x, y)
            turn = Turn.WHITE
        else:
            setState(x,y,State.WHITE)
            reverse_xy(x, y)
            turn = Turn.BLACK  
        
        if not setPossible():
            if turn == Turn.BLACK: turn = Turn.WHITE
            else: turn = Turn.BLACK

            if not setPossible():
                scorecheck(x,y)  
                if countB > countW:
                    showMessage("BLACK WIN")
                elif countB < countW:
                    showMessage("WHITE WIN")
                else:
                    showMessage("draw")
                
                
    

#놓을수 있는 경우의 수 체크
def setPossible_xy_dir(x, y, dx, dy):
    if turn == Turn.BLACK:
        mine = State.BLACK
        other = State.WHITE
    else:
        mine = State.WHITE
        other = State.BLACK

    possible = False
    while True:
        x = x + dx
        y = y + dy

        #보드에서 벗어나지 않게
        if x < 0 or x > 7: return False
        if y < 0 or y > 7: return False

        object = board[y][x]
        if object.state == other:
            possible = True
        elif object.state == mine:
            return possible
        else: 
            return False


##8방향체크
def setPossible_xy(x, y):
    object = board[y][x]
    if object.state == State.BLACK: return False
    if object.state == State.WHITE: return False
    setState(x, y, State.BLANK)

    if setPossible_xy_dir(x,y,0,1): return True
    if setPossible_xy_dir(x,y,1,1): return True
    if setPossible_xy_dir(x,y,1,0): return True
    if setPossible_xy_dir(x,y,1,-1): return True
    if setPossible_xy_dir(x,y,0,-1): return True
    if setPossible_xy_dir(x,y,-1,-1): return True
    if setPossible_xy_dir(x,y,-1,0): return True
    if setPossible_xy_dir(x,y,-1,1): return True
    return False

def reverse_xy_dir(x, y, dx, dy):
    if turn == Turn.BLACK:
        mine = State.BLACK
        other = State.WHITE
    else:
        mine = State.WHITE
        other = State.BLACK

    possible = False
    while True:
        x = x + dx
        y = y + dy

        #보드에서 벗어나지 않게
        if x < 0 or x > 7: return 
        if y < 0 or y > 7: return 

        object = board[y][x]
        if object.state == other:
            possible = True
        elif object.state == mine:
            if possible:
                while True:
                    x = x - dx
                    y = y - dy

                    object = board[y][x]
                    if object.state == other:
                        setState(x, y, mine)
                    else: return

        else: return
            


#뒤집기
def reverse_xy(x, y):
    reverse_xy_dir(x,y,0,1)
    reverse_xy_dir(x,y,1,1)
    reverse_xy_dir(x,y,1,0)
    reverse_xy_dir(x,y,1,-1)
    reverse_xy_dir(x,y,0,-1)
    reverse_xy_dir(x,y,-1,-1)
    reverse_xy_dir(x,y,-1,0)
    reverse_xy_dir(x,y,-1,1)



##체크
def setPossible():
    possible = False
    for y in range(8):
        for x in range(8):
            if setPossible_xy(x, y):
                setState(x,y,State.POSSIBLE)
                possible = True
    return possible 


#보드, 돌 위치
board = []
for y in range(8):
    board.append([])
    for x in range(8):
        object = Object("images/blank.png")
        object.locate(scene, 40 + x * 80,40 + y * 80)
        object.show()
        object.onMouseAction = lambda mx, my, action, ix = x, iy = y: stone_onMouseAction(ix, iy)
        object.state = State.BLANK
        board[y].append(object)
       
setState(3, 3,State.BLACK)
setState(4, 4,State.BLACK)
setState(3, 4,State.WHITE)
setState(4, 3,State.WHITE)

setPossible()

#점수
score1 = Object("images/L0.png")
score2 = Object("images/L0.png")
score3 = Object("images/L0.png")
score4 = Object("images/L0.png")

countB,countW= 0,0
countB = int(countB)
countW = int(countW) 



def setScore1(s):
    if s == 0:
        score1.setImage("images/L0.png")
    elif s == 1:
        score1.setImage("images/L1.png")
    elif s == 2:
        score1.setImage("images/L2.png")
    elif s == 3:
        score1.setImage("images/L3.png")
    elif s == 4:
        score1.setImage("images/L4.png")
    elif s == 5:
        score1.setImage("images/L5.png")
    elif s == 6:
        score1.setImage("images/L6.png")
    elif s == 7:
        score1.setImage("images/L7.png")
    elif s == 8:
        score1.setImage("images/L8.png")
    elif s == 9:
        score1.setImage("images/L9.png")

def setScore2(s):
    if s == 0:
        score2.setImage("images/L0.png")
    elif s == 1:
        score2.setImage("images/L1.png")
    elif s == 2:
        score2.setImage("images/L2.png")
    elif s == 3:
        score2.setImage("images/L3.png")
    elif s == 4:
        score2.setImage("images/L4.png")
    elif s == 5:
        score2.setImage("images/L5.png")
    elif s == 6:
        score2.setImage("images/L6.png")
    elif s == 7:
        score2.setImage("images/L7.png")
    elif s == 8:
        score2.setImage("images/L8.png")
    elif s == 9:
        score2.setImage("images/L9.png")

def setScore3(s):
    if s == 0:
        score3.setImage("images/L0.png")
    elif s == 1:
        score3.setImage("images/L1.png")
    elif s == 2:
        score3.setImage("images/L2.png")
    elif s == 3:
        score3.setImage("images/L3.png")
    elif s == 4:
        score3.setImage("images/L4.png")
    elif s == 5:
        score3.setImage("images/L5.png")
    elif s == 6:
        score3.setImage("images/L6.png")
    elif s == 7:
        score3.setImage("images/L7.png")
    elif s == 8:
        score3.setImage("images/L8.png")
    elif s == 9:
        score3.setImage("images/L9.png")

def setScore4(s):
    if s == 0:
        score4.setImage("images/L0.png")
    elif s == 1:
        score4.setImage("images/L1.png")
    elif s == 2:
        score4.setImage("images/L2.png")
    elif s == 3:
        score4.setImage("images/L3.png")
    elif s == 4:
        score4.setImage("images/L4.png")
    elif s == 5:
        score4.setImage("images/L5.png")
    elif s == 6:
        score4.setImage("images/L6.png")
    elif s == 7:
        score4.setImage("images/L7.png")
    elif s == 8:
        score4.setImage("images/L8.png")
    elif s == 9:
        score4.setImage("images/L9.png")
    

def scorecheck(x,y):
    global countB
    global countW
    for y in range(8):
        for x in range(8):
            object = board[y][x]
            if object.state == State.BLACK:
                countB+=1
            else:
                countW+=1
    
    if countB < 10:
        for i in range(10):
            if countB == i:
                setScore1(countB)
                score1.locate(scene, 750, 220)
                score1.show()
           
    elif countB >= 10:
        for i in range(10):
            if countB//10 == i:
                setScore1(countB//10)
                score1.locate(scene, 750, 220)
                score1.show()
            
        for i in range(10):
            if countB%10 == i:
                setScore2(countB%10)
                score2.locate(scene, 830, 220)
                score2.show()
            
    if countW < 10:
        for i in range(10):
            if countW == i:
                setScore3(countW)
                score3.locate(scene, 1070, 220)
                score3.show()
           
    elif countW >= 10:
        for i in range(10):
            if countW//10 == i:
                setScore3(countW//10)
                score3.locate(scene, 1070, 220)
                score3.show()
           
        for i in range(10):
            if countW%10 == i:
                setScore4(countW%10)
                score4.locate(scene, 1150, 220)
                score4.show()
            



startGame(scene)
