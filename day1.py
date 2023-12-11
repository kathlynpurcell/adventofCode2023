data = open("day1_data.txt", "r")

str_numbers = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5",\
	"six":"6", "seven":"7", "eight":"8", "nine":"9"}

sum_of_dd = 0
dd_values = []
save_values = []

for line in data.readlines():
	#pt1
	numbers = "".join([n for n in line if n.isdigit()])
	sum_of_dd += int(numbers[0]+numbers[-1])
	
	#pt2
	str_values = [i for i in str_numbers.keys() if i in line]
	int_values = [i for i in str_numbers.values() if i in line]
	all_values = str_values+int_values

	# build the word from the string one letter at a time
	build_word=""
	for i in line:
		build_word+=i
		for item in all_values: 
			if item in build_word:
				dd_values.append(build_word)
				build_word=''
				break

	while dd_values[0] not in all_values: dd_values[0] = dd_values[0][1:]
	if dd_values[0] in str_numbers.keys(): dd = str_numbers[dd_values[0]]
	else: dd = dd_values[0]
	dd_values = []

	# build the last word to find the last number
	build_word=""
	for i in line[::-1]:
		build_word = i+build_word
		for item in all_values: 
			if item in build_word:
				dd_values.append(item)
				build_word=''
				break

	while dd_values[0] not in all_values: dd_values[0] = dd_values[0][1:]
	if dd_values[0] in str_numbers.keys(): dd += str_numbers[dd_values[0]]
	else: dd += dd_values[0]
	dd_values = []


	save_values.append(int(dd))




#pt1 - 55621
print(sum_of_dd)
#pt2 - 53592
print(sum(save_values))
