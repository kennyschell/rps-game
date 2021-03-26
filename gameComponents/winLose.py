from gameComponents import gameVars

#define a win / lose function and refer to it (invoke) in our game loop
def winorlose(status):
	if status == "won":
		pre_message = "You are the winner!"
	else:
		pre_message = "You are the loser!"

		print(pre_message + 'Would you like to play again?')

		choice = False

		while choice == False:
			choice = input("Y / N? ")

			if choice == "Y" or choice == "y":
				# reset the game loop and start over again

				gameVars.player_lives = gameVars.total_lives
				gameVars.computer_lives = gameVars.total_lives
				gameVars.player_choice = False
			elif choice == "N" or choice == "n":
				# exit message and quit
				print("You chose to quit, better luck next time!")
				exit()
			else:
				print("Make a valid choice - Y or N")
				choice = False