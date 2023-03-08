# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game_functions.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbarutel <mbarutel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/08 19:33:52 by mbarutel          #+#    #+#              #
#    Updated: 2023/03/08 19:41:41 by mbarutel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def next_turn(row, col):
	
	global player

	if buttons[row][col]['text'] == "" and check_win() is False:
		
		if player == players[0]:
			
			buttons[row][col]['text'] = player
			if check_win() is False:
				player = players[1]
				label.config(text="Player " + players[1] + " turn")
				
			elif check_win() is True:
				label.config(text="Player " + players[0] + " wins!")
				
			elif check_win() == "Tie":
				label.config(text="It's a tie!")
		
		else:
		
			buttons[row][col]['text'] = player

			if check_win() is False:
				player = players[0]
				label.config(text="Player " + players[0] + " turn")
				
			elif check_win() is True:
				label.config(text="Player " + players[1] + " wins!")
				
			elif check_win() == "Tie":
				label.config(text="It's a tie!")
	
def check_win():
	
	for row in range(3):
		if buttons[row][0]['text'] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
			buttons[row][0].config(highlightbackground='green')
			buttons[row][1].config(highlightbackground='green')
			buttons[row][2].config(highlightbackground='green')
			return True
		
	for col in range(3):
		if buttons[0][col]['text'] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
			buttons[0][col].config(highlightbackground='green')
			buttons[1][col].config(highlightbackground='green')
			buttons[2][col].config(highlightbackground='green')
			return True
	
	if buttons[0][0]['text'] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
		buttons[0][0].config(highlightbackground='green')
		buttons[1][1].config(highlightbackground='green')
		buttons[2][2].config(highlightbackground='green')
		return True

	elif buttons[2][0]['text'] == buttons[1][1]["text"] == buttons[0][2]["text"] != "":
		buttons[2][0].config(highlightbackground='green')
		buttons[1][1].config(highlightbackground='green')
		buttons[0][2].config(highlightbackground='green')
		return True

	elif empty_cells() is False:
		for row in range(3):
			for col in range(3):
				buttons[row][col].config(highlightbackground='orange')
		return "Tie"
	
	else:
		return False

def empty_cells():

	spaces = 9
	
	for row in range(3):
		for col in range(3):
			if buttons[row][col]['text'] != "":
				spaces -= 1
	if spaces == 0:
		return False
	else:
		return True

def new_game():
	
	global player

	player = random.choice(players)
	label.config(text="Player " + player + " turn")			
	for row in range(3):
		for col in range(3):
			buttons[row][col].config(text="", highlightbackground="#F0F0F0")