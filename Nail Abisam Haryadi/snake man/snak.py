from tkinter import *
import random
import tkinter as tk

GAME_WIDTH = 600
GAME_HEIGHT = 600
SPEED = 200
SPACE_SIZE = 15
BODY_PARTS = 1
SNAKE_COLOUR = "#00FF00"
FOOD_COLOUR = "#FF0000"
BACKGROUND_COLOUR = "#000000"


class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR, tag="snake")
            self.squares.append(square)


class Food:

    def __init__(self):
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOUR, tag="food")


def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == 'up':
        y -= SPACE_SIZE

    elif direction == 'down':
        y += SPACE_SIZE

    elif direction == 'left':
        x -= SPACE_SIZE

    elif direction == 'right':
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        label.config(text="Score: {}".format(score))

        canvas.delete("food")

        food = Food()

        SPEED - 6


    else:
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisons(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction

    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction

    if new_direction == 'up':
        if direction != 'down':
            direction = new_direction

    if new_direction == 'down':
        if direction != 'up':
            direction = new_direction


def check_collisons(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def game_over():
    # canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font=('consolas', 70), text="GAME OVER",
                       fill="red", tag="gameover")

    reset_button = Button(text="Restart", font=('consolas', 20), command=reset)
    canvas.create_window(300, 400, window=reset_button)


def reset():
    score = 0
    label.config(text="Score:{}".format(score))
    canvas.delete(ALL)

    snake = Snake()
    food = Food()
    next_turn(snake, food)

window1 = tk.Tk()
window1.geometry("600x600")
window1.title("Main")
window1.configure(bg='black')

window = tk.Toplevel(window1)
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOUR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()


window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()

food = Food()

next_turn(snake, food)



#projek = membuat ini dan membuat window awal mulai dan caramain,dan mempelajari koding ini untuk di presentasi I_+




def showup1():
    window.deiconify()
    window1.withdraw()

def showup2():
    window3.deiconify()
    window1.withdraw()

def showback():
    window1.deiconify()
    window3.withdraw()
    window.withdraw()

pic = tk.PhotoImage(file="snake1.png")
pic1 = tk.PhotoImage(file="lay.png")
smallpick = pic1.subsample(5,5)
pic2 = tk.PhotoImage(file="htp.png")


LP = tk.Label(window1, image=pic)
btn1 = tk.Button(window1,image=smallpick,command=showup1)
btn2 = tk.Button(window1,image=pic2,command=showup2)


LP.pack(pady=10)

btn1.pack(ipadx=50,ipady=20)
btn2.pack(ipadx=30,ipady=10,pady=20)







btn4 = tk.Button(window,text="Back",command=showback)


btn4.pack()



window3 = tk.Tk()
window3.geometry("600x600")
window3.title("Tutorial")

btn3 = tk.Button(window3,text="Back",command=showback)
lb1  = tk.Label(window3,text="kamu hanya perlu memakan buah untuk mendapatkan score dan jangan menabrak \ndinding atau ekormu dan dapatkanlah skor tertinggi mu")

btn3.pack()
lb1.pack()


window.withdraw()
window3.withdraw()

window1.mainloop()