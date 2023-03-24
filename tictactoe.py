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

SIZE = 100

diff = 130 - SIZE

def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    pensize(10)
    color('red')
    line(x+diff, y + SIZE, x + SIZE, y+diff)
    line(x+diff, y+diff, x + SIZE, y + SIZE)


def drawo(x, y):
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


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
