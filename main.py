#links: https://stackoverflow.com/questions/42710246/in-order-to-generate-all-combinations-of-1s-and-0s-we-use-a-simple-binary-tabl

def allBinaryPossiblities(maxLength, s=""):
    if len(s) == maxLength:
        return s
    else:
        temp = allBinaryPossiblities(maxLength, s + "0") + "\n"
        temp += allBinaryPossiblities(maxLength, s + "1")
        return temp

#this function will parse the input file and allow me to compare the numbers. Stored in list of pairs
#positive number for switch means down
#negative number means switch is up
def parse(input):
    x = 0
    my_list = []
    first = None
    str_len = len(input) #used in for loop takes length of input string
    for index in range(2,str_len):
        word = input[index].split()
        my_list.append((int(word[0]),int(word[1])))

    return my_list

        
        

def light_bulb(filePath):
    file = open(filePath, "r") 
    lines = file.readlines() #reads every line and creates list of every line
    print(lines)
    #print(allBinaryPossiblities(int(lines[0]))) #creates the table for switches based off how many switches is specified in file
    data = allBinaryPossiblities(int(lines[0]))
    final = data.splitlines() # contains list of each line in the switch matrix
    parsed_list= parse(lines) #returns list of all lightbulb combinations
    separated_string = data.splitlines() #splits up the combination of switch solutions so i can manipulate them better
    print(separated_string)
    test1 = True
    test2 = True
    for x in separated_string:
        for bulb in parsed_list:
            print(bulb)
            #following 2 else if statements check blah blah
            if x[abs(bulb[0]-1)] == "0":
                if bulb[0]-1 < 0: #if the switch in bulb is negative (switch is up)
                    test1 = True
                elif bulb[0]-1 > 0: #opposite case where first switch in bulb is positive (switch is down)
                    test1 = False
            elif x[abs(bulb[0]-1)] == "1":
                if bulb[0]-1 < 0: #if the switch in bulb is negative (switch is up)
                    test1 = False
                elif bulb[0]-1 > 0: #opposite case where first switch in bulb is positive (switch is down)
                    test1 = True
            if x[abs(bulb[1]-1)] == "0":
                if bulb[1]-1 < 0: #if the switch in bulb is negative (switch is up)
                    test2 = True
                elif bulb[1]-1 > 0: #opposite case where first switch in bulb is positive (switch is down)
                    test2 = False
            elif x[abs(bulb[1]-1)] == "1":
                if bulb[1]-1 < 0: #if the switch in bulb is negative (switch is up)
                    test2 = False
                elif bulb[1]-1 > 0: #opposite case where first switch in bulb is positive (switch is down)
                    test2 = True
            if test1 == False and test2 == False:
                break
            #need to come back, need to do for all bulbs now and find a way to determine a solution
                
            

                    

                
                

light_bulb("test.txt")