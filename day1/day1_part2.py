file1 = open('input.txt','r')
Lines = file1.readlines()

master_control_count = 0

enigma_machine = {'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5', 
			'six': '6', 
			'seven': '7', 
			'eight': '8', 
			'nine': '9'	}



enigma_search = ['one', 'two', 'three', 'four', 'five','six','seven','eight','nine']


for line in Lines:
		#part 2 translate the words into digits before running part1 
	clean_line = line.strip()
	for key, value in enigma_machine.items():
		clean_line2 = clean_line
		#build replacement str
		injected_num = key[:1] + value + key[1:]
		clean_line2 = clean_line.replace(key,injected_num)
		clean_line = clean_line2

	#for each line read every char set first num found as num1 and last as num2
	num1=None
	num2=None
	for char in clean_line:
		if(char.isnumeric()):
			if(num1 is None):
				num1 = char
			else:
				num2 = char		
	
	if(num2 is None):
		num2 = num1
	num3 = num1+num2
	print('{0} : {1}'.format(clean_line, num3))
	if((num1 is not None) & (num2 is not None)):
		master_control_count +=(int(num3))


print(master_control_count)
