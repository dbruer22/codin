def sublist(somelist):
    result = []
    a = []
    for i in somelist:
        if i > 0:
            a.append(i)
        else:
            if a: # make sure a has something in it
                result.append(a)
            a = []
    if a: # if a is still accumulating elements
        result.append(a)
    print result
sublist(input())
