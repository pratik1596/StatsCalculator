from Statistics.Variance import variance
from Calculator.SquareRoot import sroot

def standardDeviation(data):
    numValues = len(data)
    if numValues == 0:
        raise Exception('Error! List is empty.')
    return sroot(variance(data))