from MasterMind_class import MasterMind 
import numpy as np 

def main():
	
	gameEngine = MasterMind()
	gameEngine.startGame()
	while gameEngine.gameStatus < gameEngine.GAMESTATUS_WON:
		#inputValue = input()
		#theInput = inputValue.upper().split(',')
		theInput = np.random.choice(len(gameEngine.peg_colors),gameEngine.slot_size)

		feedback, status = gameEngine.user_guess(theInput)
		print("Guess:\t", gameEngine.int2str(theInput), "\tfeedback:\t" , feedback)

	if (gameEngine.gameStatus == gameEngine.GAMESTATUS_WON):
		print("You WON, Total Score", gameEngine.totalScore)
	else:
		print("YOU LOST, Total Score", gameEngine.totalScore)

	



main()

