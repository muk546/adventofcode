import re

file1 = open('game_input.txt','r')
Lines = file1.readlines()


master_red_count = 0
master_green_count = 0
master_blue_count = 0

#master count of the sum of game ids
master_control_count = 0

#read the game data
for game_line in Lines:
    #counter per game
    game_count = 0
    #master counts reset each round
    current_red_count = 1
    current_green_count = 1
    current_blue_count = 1



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

        check = game_round.split(',')
        for item in check:
            
            match = re.search(r'\d+', item)
            matcher = match.group()

            current_val = int(matcher)
            if 'red' in item:
               # print('current red val: ' + str(current_val))
                if current_val > current_red_count:
                    current_red_count = current_val
            if 'green' in item:
                #print('current green val: ' + str(current_val))
                if current_val > current_green_count:
                    current_green_count = current_val
            if 'blue' in item:
                #print('current blue val: ' + str(current_val))
                if current_val > current_blue_count:
                    current_blue_count = current_val
    print(current_red_count)
    print(current_green_count)
    print(current_blue_count)

        #now that the round is over check if it's real or not
    game_count = (current_red_count * current_blue_count * current_green_count)
    print(game_count)        
    master_control_count += game_count

print(master_control_count)
