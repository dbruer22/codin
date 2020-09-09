from leter_number import *
from the_name_list import big_name_list
real = big_name_list
test = 'JACK', 'DAN', 'RYAN'
dan = 'DAN'
dna = "ACGT"

def nuclotides():
    A = 1
    G = -17
    C = -13
    T = -19
    global T, A, C, G
nuclotides()

def list_characters():
    sequence_start = input() #imputs the name
    DNA_sequence = str(sequence_start) #turns the name into a string
    global DNA_sequence #makes the varible usable in other functions
    print DNA_sequence
    global sequence_start
list_characters()

def sequence_list():
    a = sequence_start
    letter_list = [] #creates empty list z
    sublist = []
    listsa = [] #creates empty list lista
    for i in a:
        letter.append(i) #adds the elements from a into list z
    print letter_list
    global letter_list
sequence_list()

def mRNA_switcher():
    def sublist(somelist):
        sub = []
        a = []
        for i in somelist:
            if i > -20:
                a.append(i)
            else:
                if a: # make sure a has something in it
                    sub.append(a)
                a = []
        if a: # if a is still accumulating elements
            sub.append(a)
        mRNA_numbers = sub + 20
        global mRNA_numbers
    sublist(low_sequence_num)
mRNA_switcher()

def character_per_number():
        a = mRNA_numbers
        z = [] #creates empty list z
        sublist = []
        listsa = [] #creates empty list lista
        for i in a:
            z.append(i) #adds the elements from a into list z
        for number in z: #takes the letters in list z
            convert_high = chr(number + 64) #runs the chr command
            convert = convert_high
            listsa.append(convert) #adds all order edited elements into list lista
            no_neg_with_comma = [x for x in listsa if x >= -20 ] #deletes negatives from the list (except for comma value of -20){is more or lest redundent shortens list to be used}
            #print(convert)             }
            #print(listsa)              test to see what printes
            print(no_neg_with_comma)
            global no_neg_with_comma
        #print sum(no_neg_with_comma) test for the sum [62] #test
character_per_number()
