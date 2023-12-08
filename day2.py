# get the data
data = open("day2_data.txt", "r")


limits = {'red':12, 'green':13, 'blue':14}
possible_numbers = []
game_powers = []

for line in data.readlines():
	game = line.split(":")[1]
	game_number = int(line.split(":")[0][5:])
	handfuls =  {'red':0, 'green':0, 'blue':0}
	possible = 1
	for grab in game.split(";"):
		for handful in grab.split(","):
			nothing, number, color = handful.split(" ")
			color = color.strip("\n")
			if int(number) > limits[color]: possible = 0
			if int(number) > handfuls[color]: handfuls[color] = int(number)
	if possible == 1: 
		possible_numbers.append(game_number)
	game_powers.append(handfuls["red"]*handfuls["blue"]*handfuls["green"])

#pt1: 2406
print(sum(possible_numbers))
# pt2: 78375
print(sum(game_powers))
