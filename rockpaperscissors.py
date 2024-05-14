from tkinter import *
import random
def play_game(user_choice):
    choices = ["rock","paper","scissors"]
    computer_choice = random.choice(choices) 
    l2.config(text="Computer choose: " + computer_choice)
    if user_choice == computer_choice:
        result = "It's a tie!"
  
    elif user_choice == "rock":
        if computer_choice == "scissors":
            result = "YaY You Win!"
        else:
            result = "Computer wins!"

    elif user_choice == "paper":
        if computer_choice == "rock":
            result = "YaY You Win!"
        else:
            result = "Computer wins!"

    elif user_choice == "scissors":
        if computer_choice == "paper":
            result = "YaY You Win!"
        else:
           result = "Computer wins!"
    l3.config(text=result)
    play_again_button.pack()

def play_again():
    l2.config(text="")
    l3.config(text="")
    play_again_button.pack_forget()

parent = Tk()
parent.title("Rock Paper Scissors Game")
label = Label(parent, text="Choose:")
label.pack()
b1 = Button(parent, text="rock", command=lambda: play_game("rock"))
b1.pack(side="left")
b2 = Button(parent, text="paper", command=lambda: play_game("paper"))
b2.pack(side="right")
b3 = Button(parent, text="scissors", command=lambda: play_game("scissors"))
b3.pack(side="top")
l2 = Label(parent, text="")
l2.pack()
l3 = Label(parent, text="")
l3.pack()
play_again_button = Button(parent, text="Play Again", command=play_again)
parent.mainloop()