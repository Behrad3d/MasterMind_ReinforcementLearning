import numpy as np



class MasterMind(object):

	def __init__(self, slot_size = 4, peg_colors =  ['G','W','B','K','R','G','O']):
		self.peg_colors = peg_colors
		self.slot_size = slot_size
		self.selected_code = None
		self.guess_list = []
		self.stepScores = []
		self.totalScore = 0
		self.attempt = 0

		self.MAX_ATTEMPTS = 10
		self.STEP_SCORE_REDUCTION = 20

		self.CORRECT_GUESS_SCORE  = 4
		self.CORRECT_COLOR_SCORE  = 1

		self.WIN_GUESS_SCORE  = self.CORRECT_GUESS_SCORE * self.slot_size

		self.GAMESTATUS_START = 0
		self.GAMESTATUS_ONGOING = 1
		self.GAMESTATUS_WON = 2
		self.GAMESTATUS_LOST = 3

		self.gameStatus = self.GAMESTATUS_START


	def reset(self):
		self.selected_code = None
		self.guess_list = []
		self.stepScores = []
		self.totalScore = 0
		self.gameStatus = self.GAMESTATUS_START
		self.attempt = 0 

	def int2str(self, codes):
		output = [self.peg_colors[x] for x in codes]
		return output 
	def startGame(self,chosenCode = None):

		self.reset()

		if chosenCode is None:
			self.selected_code = np.random.choice(len(self.peg_colors), self.slot_size)
		else:
			self.selected_code = chosenCode

		self.gameStatus = self.GAMESTATUS_ONGOING
		print("Game Started\nTarget:\t", self.int2str(self.selected_code))



	def assessInput(self,index, guess):
		output = 0
		if guess == self.selected_code[index]:
			output = 4
		elif guess in self.selected_code:
			output = 1

		return output


	def user_guess(self, guess):
		if not(len(guess) == self.slot_size):
			print("WRONG GUESS FORMAT")
			return [], self.gameStatus

		output = [0 for _ in range(self.slot_size)]
		stepScore = 0

		for i in range(self.slot_size):
			itemScore = self.assessInput(i,guess[i])
			stepScore += itemScore
			output[i] = itemScore

		self.attempt += 1

		if stepScore == self.WIN_GUESS_SCORE:
			self.gameStatus = self.GAMESTATUS_WON
			self.totalScore = (self.MAX_ATTEMPTS + 1 - self.attempt) * self.STEP_SCORE_REDUCTION 
		else:
			if self.attempt == self.MAX_ATTEMPTS:
				self.gameStatus = self.GAMESTATUS_LOST

		
		self.stepScores.append(stepScore)
		self.guess_list.append(guess)	

		return output, self.gameStatus






