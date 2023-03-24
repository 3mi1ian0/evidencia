""" EQUIPO 7:
            EMILIANO MENDOZA NIETO - A01706083
            Juan Yael Ávalos Mayorga - A01276329
Tic Tac Toe

1. Modify the size and color of the "X" and "O" symbols and center them.
2. Validate if a box is already occupied.
"""

#Libraries
from turtle import hideturtle
from turtle import up
from turtle import goto
from turtle import down
from turtle import circle
from turtle import update
from turtle import setup
from turtle import tracer
from turtle import onscreenclick
from turtle import done
from turtle import color, pensize

from freegames import line


#Size correction
SIZE = 100
diff = 130 - SIZE  #Difference between grid and icon size


board = [False for i in range(9)] #Detect if the checkbox is already used


def grid(): #Define the grid
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y): #Draw the x
    """Draw X player."""
    pensize(10)
    color('red')
    line(x+diff, y + SIZE, x + SIZE, y+diff)
    line(x+diff, y+diff, x + SIZE, y + SIZE)


def drawo(x, y): #Draw the o
    """Draw O player."""
    up()
    pensize(10)
    color('blue')
    goto(x + 67, y + diff//2)
    down()
    circle(SIZE//2)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y): #User click location
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    
    #Index of the square pressed
    box_index = int((x+200)//133+(abs(y-66))//133*3)
    
    # Check if the box is occupied
    if not board[box_index]:
        board[box_index] = True
        player = state['player']
        draw = players[player]
        draw(x, y)
        update()
        state['player'] = not player


setup(420, 420, 370, 0) #Create the window
hideturtle()
tracer(False)
#Makes the grid
grid()
update()
onscreenclick(tap) #Detect the clicks
done()
