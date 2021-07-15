from Calculator.Addition import addition
from Calculator.Division import division

def mean(data):
    numValues = len(data)
    if numValues == 0:
        raise Exception('Error! List is Empty')

    total = 0
    for num in data:
        if isinstance(num, str):
            raise Exception('Error! List does not have numbers')
        total = addition(total, num)
    return division(numValues,total)