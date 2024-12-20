import curses
from random import randint

# setup window
screen = curses.initscr()
win = curses.newwin(20, 60, 0, 0)  # y, x
win.keypad(True)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(True)

# snake and food
snake_body = [(4, 10), (4, 9), (4, 8)]
food = (10, 20)

win.addch(food[0], food[1], "#")
# game logic
score = 0

ESC = 27
key = curses.KEY_RIGHT

while key != ESC:
    win.addstr(0, 2, f"Score: {score} ")
    # Adjust speed based on snake length
    win.timeout(max(50, 150 - (len(snake_body) // 5 + len(snake_body) // 10 % 120)))

    prev_key = key
    event = win.getch()
    key = event if event != -1 else prev_key

    if key not in [
        curses.KEY_LEFT,
        curses.KEY_RIGHT,
        curses.KEY_UP,
        curses.KEY_DOWN,
        ESC,
    ]:
        key = prev_key

    # Calculate the next head position
    head_y, head_x = snake_body[0]
    if key == curses.KEY_DOWN:
        head_y += 1
    elif key == curses.KEY_UP:
        head_y -= 1
    elif key == curses.KEY_LEFT:
        head_x -= 1
    elif key == curses.KEY_RIGHT:
        head_x += 1

    new_head = (head_y, head_x)
    snake_body.insert(0, new_head)

    # Check for collisions
    if (
        head_y == 0
        or head_y == 19
        or head_x == 0
        or head_x == 59
        or new_head in snake_body[1:]
    ):
        break

    # Check if food is eaten
    if new_head == food:
        score += 1
        while True:
            food = (randint(1, 18), randint(1, 58))
            if food not in snake_body:
                break
        win.addch(food[0], food[1], "#")
    else:
        # Move snake (remove tail)
        tail = snake_body.pop()
        win.addch(tail[0], tail[1], " ")

    # Render snake head
    win.addch(new_head[0], new_head[1], "*")

curses.endwin()
print(f"Final score = {score}")
