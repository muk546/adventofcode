import re
file1 = open('test.txt','r')
Lines = file1.readlines()

master_control_count = 0

master_dict = {}
counter = 0
find_sp_chars_pattern = re.compile(r"[^a-zA-Z\d\.]")

for line in Lines:
    
    #scan for nums and symbols (anything not a '.')
    index = 0
    clean_line = line.strip()
    size = len(clean_line)
    
    for c in clean_line:
        result = find_sp_chars_pattern.findall(c)

        if(len(result) != 0):
            #print(c)
         print(result[0])
         master_dict[counter,index] = result[0]
        index+=1
    counter+=1

for line in Lines:
   

print(master_dict)



    


