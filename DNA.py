def nuclotides():
    A = 1
    G = -17
    C = -13
    T = -19
    global T, A, C
nuclotides()
def name_splitter():
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
        print sub
    sublist([T, A, C])
name_splitter()
