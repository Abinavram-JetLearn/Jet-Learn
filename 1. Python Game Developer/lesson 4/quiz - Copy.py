import pgzrun, random

WIDTH = 962
HEIGHT = 500
title = Rect(0,0,962,50)
title2 = Rect(0,0,962,50)

question = Rect(6.25,75,650,50)

ans1 = Rect(12.5,150,250,150)
ans2 = Rect(12.5,325,250,150)
ans3 = Rect(406.25,150,250,150)
ans4 = Rect(406.25,325,250,150)

timer = Rect(700,75,100,200)
restart = Rect(700,287.5,250,200)
skip = Rect(850,75,100,100)

score = 0
answerboxes = [ans1, ans2, ans3, ans4]

time_que = 10
game_state = True
titletext = "Hello Welcome to this very cool quiz"
questions = []

def read_question():
    global questions
    file = open("1. Python Game Developer\lesson 4\questions.txt", "r", encoding="utf-8")
    for q in file:
        questions.append(q.strip())
    random.shuffle(questions)
    q = questions.pop(0).split("|")
    return q

cur_question = read_question()

def timer_reduce():
    global time_que, game_state, cur_question
    if time_que > 0:
        time_que -= 1
    else:
        game_state = False
        time_que = 0
        cur_question = [f"Game Over You scored {score} point(s)!", "-", "-", "-", "-", "-", 5]
        time_que = 0

def draw():
    global time_que, titletext, question, score

    screen.fill("magenta3")
    screen.draw.filled_rect(title,"magenta2")
    screen.draw.filled_rect(title2,"magenta2")
    screen.draw.textbox(f"{titletext}, Score: {score}", title, color = "violet red")
    screen.draw.filled_rect(question,"magenta2")
    screen.draw.textbox(cur_question[0], question, color = "violet red")
    screen.draw.filled_rect(ans1,"magenta2")
    screen.draw.textbox(cur_question[1], ans1, color = "violet red")
    screen.draw.filled_rect(ans2,"magenta2")
    screen.draw.textbox(cur_question[2], ans2, color = "violet red")
    screen.draw.filled_rect(ans3,"magenta2")
    screen.draw.textbox(cur_question[3], ans3, color = "violet red")
    screen.draw.filled_rect(ans4,"magenta2")
    screen.draw.textbox(cur_question[4], ans4, color = "violet red")
    screen.draw.filled_rect(skip,"magenta2")
    screen.draw.textbox("Skip", skip, color = "violet red")
    screen.draw.filled_rect(restart,"magenta2")
    screen.draw.textbox("Restart", restart, color = "violet red")
    screen.draw.filled_rect(timer,"magenta2")
    screen.draw.textbox(f"{time_que}", timer, color = "violet red")

def update():
    global titletext
    if game_state == False:
        titletext = "GAME OVER"
    if title.right < 0:
        title.left = WIDTH
    else:
        title.x -= 10
def on_mouse_down(pos):
    global time_que, cur_question, score, questions, game_state, titletext
    index = 1
    if game_state == True:
        for box in answerboxes:
            if box.collidepoint(pos):
                if index == int(cur_question[5]):
                    score += 1
                    if questions:
                        cur_question = read_question()
                        time_que = 10
                else:
                    cur_question = [f"Game Over You scored {score} point(s)!", "-", "-", "-", "-", "-", 5]
                    time_que = 0
            index += 1
    if skip.collidepoint(pos):
        if questions:
            if game_state == True:
                cur_question = read_question()
                time_que = 10
                if score > 0:
                    score -= 1
                else:
                    cur_question = [f"Game Over You (skipped) scored {score} point(s)!", "-", "-", "-", "-", "-", 5]
                    time_que = 0
    if restart.collidepoint(pos):
        questions = []
        cur_question = read_question()
        score = 0
        time_que = 10
        game_state = True
        titletext = "Hello Welcome to this very cool quiz"

clock.schedule_interval(timer_reduce,1)
pgzrun.go()