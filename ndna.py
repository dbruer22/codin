dna = "ACGT"
def nuclotides():
    A = 1
    C = -13
    G = -17
    T = -19
    #global T, A, C, G
nuclotides()

def list_characters():
    sequence_start = input() #imputs the name
    DNA_sequence = str(sequence_start) #turns the name into a string
    global DNA_sequence #makes the varible usable in other functions
    print DNA_sequence
    global sequence_start
list_characters()

def sequence_list():
    a = DNA_sequence
    letter_list = [] #creates empty list z
    sublist = []
    listsa = [] #creates empty list lista
    for i in a:
        letter_list.append(i) #adds the elements from a into list z
    print letter_list
    global letter_list
sequence_list()

def character_per_number():
    a = letter_list
    z = [] #creates empty list z
    sublist = []
    listsa = [] #creates empty list lista
    for i in a:
        z.append(i) #adds the elements from a into list z
    for number in z: #takes the letters in list z
        convert_high = ord(number) #runs the chr command
        convert = convert_high - 64
        listsa.append(convert) #adds all order edited elements into list lista
        number_list = [x for x in listsa if x >= 0 ] #deletes negatives from the list (except for comma value of -20){is more or lest redundent shortens list to be used}
        #print(convert)             }
        #print(listsa)              test to see what printes
        print(number_list)
        global number_list
    #print sum(no_neg_with_comma) test for the sum [62] #test
character_per_number()

def adder():
    a_fix = [x for x in number_list if x >= -20 ]
    print a_fix
    ag_fix = [x - 16 for x in a_fix if x >= 3 ]
    print ag_fix

adder()
