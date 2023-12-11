data = open("day4_data.txt", "r")
data = data.readlines()

total_card = 0
one_each = 0
how_many = {}

for i in range(len(data)):
    how_many[i]=1

for card in data:
    card_clean = card.replace(":", "|").replace("\n", "")
    number, wnum, tries = card_clean.split("|")
    points = [number for number in wnum.split(" ") if number in tries.split(" ")]
    while "" in points: points.remove("")
    # pt1
    if points: one_each += 2**(len(points)-1)
    # pt2
    if points:
        for add_card in range(len(points)):
            # game is base 1 index but how_many is 0 base
            current_card = int(number.split(" ")[-1])-1
            current_card_times = how_many[current_card]
            editing_card = current_card+add_card+1
            add_this = 1*current_card_times

            how_many[editing_card] += add_this

total_card = sum(how_many.values())

print(one_each)
print(total_card)
