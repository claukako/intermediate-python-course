import random
def main():
	dicerolls = int(input('How many dice would you like to roll? '))
	dice_size = int(input('How many sides are the dice? '))
	dicesum = 0
	for i in range(0, dicerolls):
		roll = random.randint(1, 6)
		dicesum += roll
		if roll == 1:
			print(f'you rolled a {roll}! Critical fail!')
		elif roll == dice_size:
			print(f'you rolled a {roll}! Critical success!')
		else:
			print(f'you rolled a {roll}')
	print(f'you rolled a total of {dicesum}')
if __name__=="__main__":
	main()
