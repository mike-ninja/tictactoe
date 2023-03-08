# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tictactoe.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbarutel <mbarutel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/08 17:10:50 by mbarutel          #+#    #+#              #
#    Updated: 2023/03/08 19:36:02 by mbarutel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from tkinter import *
import game_functions
import random

window = Tk()
window.title("Tic Tac Toe")
players = ["X", "O"]
player = random.choice(players)
buttons =  [[0, 0, 0],
			[0, 0, 0],
			[0, 0, 0]]

label = Label(text="Player " + player + " turn", font=("Consolas", 40))
label.pack(side="top")

reset_button = Button(text="Restart Game", font=("consolas", 20), highlightbackground='blue', padx=20, pady=10, command=game_functions.new_game)
reset_button.pack(side="bottom")

frame = Frame(window)
frame.pack()

for row in range(3):
	for col in range(3):
		buttons[row][col] = Button(frame, text="", font=("consolas", 40), width=5, height=3,
									command=lambda row=row, col=col: game_functions.next_turn(row, col))
		buttons[row][col].grid(row=row, column=col)

window.mainloop()