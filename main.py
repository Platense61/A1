#links: https://stackoverflow.com/questions/42710246/in-order-to-generate-all-combinations-of-1s-and-0s-we-use-a-simple-binary-tabl
def allBinaryPossiblities(maxLength, s=""):
    if len(s) == maxLength:
        return s
    else:
        temp = allBinaryPossiblities(maxLength, s + "0") + "\n"
        temp += allBinaryPossiblities(maxLength, s + "1")
        return temp

#this function will parse the input file and allow me to compare the numbers. Stored in list of pairs
#positive number for switch means down 0
#negative number means switch is up 1
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
    #print(allBinaryPossiblities(int(lines[0]))) #creates the table for switches based off how many switches is specified in file
    data = allBinaryPossiblities(int(lines[0]))
    final = data.splitlines() # contains list of each line in the switch matrix
    parsed_list= parse(lines) #returns list of all lightbulb combinations
    separated_string = data.splitlines() #splits up the combination of switch solutions so i can manipulate them better

    #the following 2 if statements determines if we have less or more switches than bulbs. If we dont do this we get index error
    sub = 1
    #if int(lines[0]) < int(lines[1]):
        #sub = 2

    counter= 0
    flag = False
    for x in separated_string:
        for bulb in parsed_list:
            test1 = True
            test2 = True
            print(abs(bulb[1]-sub))
            #following 2 else if statements check blah blah
            if x[abs(bulb[0])-sub] == "0":
                if bulb[0] < 0: #if the switch in bulb is negative (switch is up)
                    test1 = True
                elif bulb[0] > 0: #opposite case where first switch in bulb is positive (switch is down)
                    test1 = False
            elif x[abs(bulb[0])-sub] == "1":
                if bulb[0] < 0: #if the switch in bulb is negative (switch is up)
                    test1 = False
                elif bulb[0] > 0: #opposite case where first switch in bulb is positive (switch is down)
                    test1 = True
            if x[abs(bulb[1])-sub] == "0":
                if bulb[1] < 0: #if the switch in bulb is negative (switch is up)
                    test2 = True
                elif bulb[1] > 0: #opposite case where first switch in bulb is positive (switch is down)
                    test2 = False
            elif x[abs(bulb[1])-sub] == "1":
                if bulb[1] < 0: #if the switch in bulb is negative (switch is up)
                    test2 = False
                elif bulb[1] > 0: #opposite case where first switch in bulb is positive (switch is down)
                    test2 = True
            if test1 == False and test2 == False:
                break
            counter = counter + 1
        
        if counter == int(lines[1]):
            solution = []
            itr = 1
            #This for loop just turns the solution of 0s and 1s into positive and negative switch configurations
            for var in x:
                if var == "0":
                    solution.append(itr)

                else:
                    solution.append(itr*-1)
                
                itr = itr+1

            flag = True
            print("Solution: ", solution)
            break

        counter = 0
    
    if flag == False:
        print("No Solution")
                
                

light_bulb("instance1.txt")