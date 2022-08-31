#!/usr/bin/env python3

class LiarDiceRound:
	## Constructor Method
	def __init__(self, list_of_players,init_player_health_bar):
		self.players = list_of_players
		self.player_health = [init_player_health_bar]*len(list_of_players)
		self.declared_score = 0
		self.five_aces = False
		self.challenge = False
		self.roller = list_of_players[0]
		self.challenger = list_of_players[1]

	## Roll Dice
	def roll_dice(self,dice, players=[]):
		from random import randint
		side = randint(1,6)
		return dice[side]

	## Take user input for Declared Score
	def declared_score(self):
		##TODO: check that input is valid
		self.declared_score = input(self.roller,', what is the score you saw?\n')
	
	def get_declared_score(self):
		return self.declared_score

	## is Declared Score = 5 Aces
	def is_declared_score_5_aces(self):
		if self.get_declared_score() == '5A':
			self.five_aces = True
		return

	def challenge_or_accept(self, players=[]):
		challenge = input("f{self.challenger}, do you wish to challenge this score? (Y,yes/N,No)\n")
		if challenge in ['N','n','No','no', 0, False]:
			print(self.challenger,' did not challenge, please roll.')
			self.change_roller_challenger()
			challenge = False
		else:
			challenge = True
		return challenge
	
	def change_roller_challenger(self):
		pass

def main():
	##from random import randint
	dice = {
		1:"9",
		2:"10",
		3:"J",
		4:"Q",
		5:"K",
		6:"A"
	}
	## Input players in order 
	players = ['Ivan', 'Larry']

	## Initialize Gameplay - Determine how many lives to start with
	game = LiarDiceRound(players,init_player_health_bar=5)
	game.roll_dice(dice)

	game.challenge_or_accept(players)
	## Results of Gameplay
	#print(game.player_health)
	#print(game.roll_dice(dice))
	print("Player:", players[0],
		"\nhas declared a score of ... ",game.declared_score())

if __name__ == '__main__':
	main()