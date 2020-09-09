from leter_number import *
from the_name_list import big_name_list
real = big_name_list
test = 'JACK', 'DAN', 'RYAN'
dan = 'DAN'
def list_characters():
    starter_name = input() #imputs the name
    leter_by_leter = str(starter_name) #turns the name into a string
    global leter_by_leter #makes the varible usable in other functions
    print leter_by_leter
list_characters()

def number_per_character():
    a = leter_by_leter
    z = [] #creates empty list z
    sublist = []
    listsa = [] #creates empty list lista
    for i in a:
        z.append(i) #adds the elements from a into list z
    for letter in z: #takes the letters in list z
        convert_high = ord(letter) #runs the order command
        convert = convert_high - 64
        listsa.append(convert) #adds all order edited elements into list lista
        no_neg_with_comma = [x for x in listsa if x >= -20 ] #deletes negatives from the list (except for comma value of -20){is more or lest redundent shortens list to be used}
        #print(convert)             }
        #print(listsa)              test to see what printes
        print(no_neg_with_comma)
        global no_neg_with_comma
    #print sum(no_neg_with_comma) test for the sum [62] #test
number_per_character()

def adder():
    cool = [x + 1 for x in no_neg_with_comma if x >= -20 ]
    print cool
adder()

def name_splitter():
    def sublist(somelist):
        sub = []
        a = []
        for i in somelist:
            if i > 0:
                a.append(i)
            else:
                if a: # make sure a has something in it
                    sub.append(a)
                a = []
        if a: # if a is still accumulating elements
            sub.append(a)
        print sub
        global sub
    sublist(no_neg_with_comma)
name_splitter()


def small_list():
    x = 0
    mini_test = []
    while x <= 5 - 1:
        x += 1
        for i in range(1,8): # (_,+1 positioner_up_one number) ex 14,13
            mini_test.insert(i, x)
            #makes one massive list containing 6 copys of each number decending from 5000
            mini_test.sort() #reverses the order from 5000 ... 1 to 1 ... 5000
    global mini_test
    #print mini_test
small_list()

def listSplit():
    step_compensator = 1

    y = 1
    positioner_up_one = 0
    amount_of_seperators = 4*(1)
    #print positioner #test
    while positioner_up_one <= (amount_of_seperators * 7) - 1:
        step_compensator += 0
        #print step_compensator #test
        positioner_up_one += 29 + step_compensator #must be one below 30 if
        positioner = positioner_up_one -1
       #print positioner #test
        mini_test.insert(positioner,-10)
        #print mini_test # test
    def sublist(somelist):
        split = []
        r = []
        for i in somelist:
            if i > 0:
                r.append(i)
            else:
                if r: # make sure a has something in it
                    split.append(r)
                r = []
        if r: # if a is still accumulating elements
            split.append(r)
        #print split
        global split
    sublist(mini_test)
listSplit()

def multipier():
    multer = split
    sub_names = sub
    output = []
    for l1,l2 in zip(multer,sub_names):
        for a,b in zip(l1,l2):
            output.append(a*b)
    print output
    answer = sum(output)
    print answer
multipier()
