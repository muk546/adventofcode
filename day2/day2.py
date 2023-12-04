import re

file1 = open('game_input.txt','r')
Lines = file1.readlines()

input_red_count = 12
input_green_count = 13
input_blue_count = 14


#master count of the sum of game ids
master_control_count = 0

#read the game data
for game_line in Lines:
    #counter per game
    #master_red_count = 0
    #master_green_count = 0
    #master_blue_count = 0
    master_red_bool = True
    master_green_bool = True
    master_blue_bool = True

    #get current game id (always first number)
    match = re.search(r'\d+', game_line)
    matcher = match.group()
    current_game_id = int(matcher)
    print('XXXXXXXXXXXX current game id: ' + str(current_game_id))

    #clean up string 
    current_game_line = game_line[game_line.find(':'):]    
    #print('XXX: ' + current_game_line)
    #divide by game round
    round_list = current_game_line.split(';')
    #find the picked cubes
    for game_round in round_list:
            #master counts reset each round
        current_red_count = 0
        current_green_count = 0
        current_blue_count = 0

        check = game_round.split(',')
        for item in check:
            #print(item)
            match = re.search(r'\d+', item)
            matcher = match.group()

            current_val = int(matcher)
            
            if 'red' in item:#
               # print('current red val: ' + str(current_val))
                if current_val > input_red_count:
                    master_red_bool = False
            if 'green' in item:
                #print('current green val: ' + str(current_val))
                if current_val > input_green_count:
                    master_green_bool = False
            if 'blue' in item:
                #print('current blue val: ' + str(current_val))
                if current_val > input_blue_count:
                    master_blue_bool = False

        #now that the round is over check if it's real or not

            
    if master_red_bool & master_green_bool & master_blue_bool:
        print('vaild games: ' + str(current_game_id))
        master_control_count+=current_game_id

print(master_control_count)
