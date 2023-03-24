""" EQUIPO 7:
            EMILIANO MENDOZA NIETO - A01706083
            Juan Yael Ávalos Mayorga - A01276329
Tic Tac Toe

1. Modify the size and color of the "X" and "O" symbols and center them.
2. Validate if a box is already occupied.

3. Optionally, some improvements were made, to print a winner or tie.
The code can still be improved by, for example,
putting a match count and restarting the game every time there is a winner.
"""

# Libraries
from turtle import hideturtle, up, goto, down, circle, update, setup, tracer
from turtle import onscreenclick, done, color, pensize

from freegames import line


# Size correction
SIZE = 100
diff = 130 - SIZE  # Difference between grid and icon size


board = [False for i in range(9)]  # Detect if the checkbox is already used


def grid():  # Define the grid
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):  # Draw the x
    """Draw X player."""
    pensize(10)
    color('red')
    line(x+diff, y + SIZE, x + SIZE, y+diff)
    line(x+diff, y+diff, x + SIZE, y + SIZE)


def drawo(x, y):  # Draw the o
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
players = [drawx, drawo]  # Definition of players
moves_played = 0  # Keep track of the number of moves played


def tap(x, y):  # User click location
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    # Index of the square pressed
    box_index = int((x+200)//133+(abs(y-66))//133*3)
    # Check if the box is occupied
    if not board[box_index]:
        board[box_index] = True
        player = state['player']
        draw = players[player]
        draw(x, y)
        update()
        state['player'] = not player
        global moves_played
        moves_played += 1
        # Check for a tie game
        if moves_played == 9 and not check_winner():
            print("Tie game!")
        # Check for a winner
        elif check_winner():
            print(f"Player {int(not player) + 1} wins!")


def check_winner():
    """Check if there is a winner."""
    for i in range(3):
        # Horizontal check
        if (board[i*3] == board[i*3+1]) or (board[i*3] == board[i*3+2]):
            return True
        # Vertical check
        if (board[i] == board[i+3]) or (board[i] == board[i+6]):
            return True
    # Diagonal checks
    if (board[0] == board[4]) or (board[0] == board[8]):
        return True
    if (board[2] == board[4]) or (board[2] == board[6]):
        return True
    return False


setup(420, 420, 370, 0)  # Create the window
hideturtle()
tracer(False)
# Makes the grid
grid()
update()
onscreenclick(tap)  # Detect the clicks
done()
