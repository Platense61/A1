#links: https://stackoverflow.com/questions/42710246/in-order-to-generate-all-combinations-of-1s-and-0s-we-use-a-simple-binary-tabl

def allBinaryPossiblities(maxLength, s=""):
    if len(s) == maxLength:
        return s
    else:
        temp = allBinaryPossiblities(maxLength, s + "0") + "\n"
        temp += allBinaryPossiblities(maxLength, s + "1")
        return temp

#this function will parse the input file and allow me to compare the numbers. Stored in list of pairs
def parse(input):
    x = 0
    my_list = []
    first = None
    str_len = len(input) #used in for loop takes length of input string
    for index in range(2,str_len):
        word = input[index].split()
        my_list.append((int(word[0]),int(word[1])))

        
        

def light_bulb(filePath):
    file = open(filePath, "r") 
    lines = file.readlines() #reads every line and creates list of every line
    print(lines)
    #print(allBinaryPossiblities(int(lines[0]))) #creates the table for switches based off how many switches is specified in file
    data = allBinaryPossiblities(int(lines[0]))
    final = data.splitlines() # contains list of each line in the switch matrix
    parse(lines)

light_bulb("test.txt")
