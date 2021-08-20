import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
text_holder = turtle.Turtle()
text_holder.penup()
text_holder.hideturtle()

count = 0
answer_list = []

data = pandas.read_csv("50_states.csv")
data_list = data["state"].tolist()

while count != 50:
    answer_state = screen.textinput(title=f"{count}/50 Correct Guess", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    elif answer_state in answer_list:
        continue
    else:
        if answer_state in data_list:
            count += 1
            ind = data_list.index(answer_state)
            x_cor = data["x"][ind]
            y_cor = data["y"][ind]
            text_holder.goto(x_cor, y_cor)
            text_holder.write(f"{answer_state}", align="center", )
        else:
            continue
    answer_list.append(answer_state)

states_to_guess = [states for states in data_list if (states in answer_list) == False]

final = pandas.DataFrame(states_to_guess)
final.to_csv("States_to_learn.csv")
