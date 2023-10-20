#not me doing this again :)
import curses
import random
from tkinter import Canvas, Label, Tk
from turtle import window_height, window_width

GAMEWIDTH=1000
GAMEHEIGHT=800
SPEED=300
SPACE_SIZE=50
BODYPARTS=10
SNACKCOLORS="#00FF00"
FOODCOLOR="#FF0000"
BACKGROUNDCOLOR="#000000"

class Snack:
    def __init__(self) :
        self.body_size=BODYPARTS
        self.coordinates=[]
        self.squares=[]

        for i in range(0,BODYPARTS):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            squar=canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNACKCOLORS,tag="snake")
            self.squares.append(squar)
import random

class Food:
    def __init__(self, canvas, GAMEWIDTH, GAMEHEIGHT, SPACE_SIZE, FOODCOLOR):
        x = random.randint(0, (GAMEWIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAMEHEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOODCOLOR, tag="food")

def next_turn(snake, food):
    global direction, score

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE

    if x == food.coordinates[0] and y == food.coordinates[1]:
        score += 1
        label.config(text="Score: {}".format(score))
        canvas.delete("food")
        food = Food(canvas, GAMEWIDTH, GAMEHEIGHT, SPACE_SIZE, FOODCOLOR)
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    
    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNACKCOLORS)
    snake.squares.insert(0, square)
    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)


def change_direction(new_sdirection):
    global direction

    if new_sdirection=='left':
        if direction!='right':
            direction= new_sdirection
    elif new_sdirection=='right':
        if direction!='left':
            direction= new_sdirection
    elif new_sdirection=='up':
        if direction!='down':
            direction= new_sdirection
    elif new_sdirection=='down':
        if direction!='up':
            direction= new_sdirection

def check_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAMEWIDTH or y < 0 or y >= GAMEHEIGHT:
        print("GAME OVER")
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print("GAME OVER")
            return True

    return False

    
def game_over():
    canvas.delete(all)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=('consolas',70),text="GAME OVER",fill="red",tags="gme")

window=Tk()
window.title("snack game")
window.resizable(False,False) 

score=0
direction='down'
label=Label(window,text="score:{}".format(score),font=('consolas',40))
label.pack()

canvas=Canvas(window,bg=BACKGROUNDCOLOR,height=GAMEHEIGHT,width=GAMEWIDTH,)
canvas.pack()

window.update()

window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

x=int((screen_width/2) - (window_width/2))
y=int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.bind('<Left>',lambda event: change_direction('left'))
window.bind('<Right>',lambda event: change_direction('right'))
window.bind('<Down>',lambda event: change_direction('down'))
window.bind('<Up>',lambda event: change_direction('up'))

snake=Snack()
food=Food(canvas, GAMEWIDTH, GAMEHEIGHT, SPACE_SIZE, FOODCOLOR)

next_turn(snake,food)

window.mainloop()