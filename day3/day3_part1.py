file1 = open('test.txt','r')
Lines = file1.readlines()

master_control_count = 0

master_dict = {}
counter = 0
for line in Lines:
    
    #scan for nums and symbols (anything not a '.')
    clean_line = line.strip()

    list_line = clean_line.split('\.+')
    print(list_line)
    master_dict[counter] = list_line
    counter+=1

print(master_dict)

counter2 = 0
max_size = len(master_dict) - 1
print(max_size)
for item in master_dict:
    print('---------------------')

    if counter2 == 0:
        #don't look behind!
        #  
        print(master_dict[counter2])
        print(master_dict[counter2 + 1])
        counter2+=1
    elif counter2 == max_size:
        #don't look ahead!
        #
        print(master_dict[counter2 - 1])
        print(master_dict[counter2])
        counter2+=1
    else:
        print(master_dict[counter2 - 1])
        print(master_dict[counter2])
        print(master_dict[counter2 + 1])
        counter2+=1



    


