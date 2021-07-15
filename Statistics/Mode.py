from Calculator.Addition import addition

def mode(data):
    numValues = len(data)
    if numValues == 0:
        raise Exception('Error! List is empty.')
    data.sort()

    list1 = []

    i = 0
    while i < len(data) :
        list1.append(data.count(data[i]))
        i = addition(i,1)

    d1 = dict(zip(data, list1))
    d2=[k for (k,v) in d1.items() if v == max(list1)]
    d2.sort()
    return d2[0]