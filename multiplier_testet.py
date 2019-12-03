def small_list():
    x = 0
    mini_test = []
    while x <= 3 - 1:
        x += 1
        for i in range(0,6):
            mini_test.insert(i, x)
            #makes one massive list containing 6 copys of each number decending from 5000
            mini_test.sort() #reverses the order from 5000 ... 1 to 1 ... 5000

    #n_posit_mult = [posit_mult] #makes one massive list containing 6 copys of each number decending from 5000
    global mini_test
    print mini_test
    #print posit_mult # was to make sure was going in asending order
small_list()
def sublist_mult():
    x = 0
    posit_mult = []
    while x <= 5000 - 1:
        x += 1
        for i in range(0,6):
            posit_mult.insert(i, x)
            #makes one massive list containing 6 copys of each number decending from 5000
            posit_mult.sort() #reverses the order from 5000 ... 1 to 1 ... 5000

    #n_posit_mult = [posit_mult] #makes one massive list containing 6 copys of each number decending from 5000
    global posit_mult
    #print posit_mult # was to make sure was going in asending order
sublist_mult()

def listSplit(list):
    splitList = []
    for item in range(0,6):
        splitList.append(list[item])
        list.remove(item)
    return splitList

def multipier():
    multer = [mini_test, [1,1,1,1,1,1], [1,1,1,1,1,1], [1,1,1,1,1,1]]
    sub_names=[[10, 1, 3, 11],[4, 1, 14],[18 , 25, 1, 14]]
    output = []
    for l1,l2 in zip(multer,sub_names):
        for a,b in zip(l1,l2):
            output.append(a*b)
    print output
multipier()
