file1 = open('input.txt','r')
Lines = file1.readlines()

master_control_count = 0

for line in Lines:
	clean_line = line.strip()
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
	#print('{0} : {1} + {2}'.format(clean_line, num1, num2))
	if((num1 is not None) & (num2 is not None)):
		master_control_count +=(int(num3))

print(master_control_count)
