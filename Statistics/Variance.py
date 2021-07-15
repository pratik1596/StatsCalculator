import math
from Statistics.Mean import mean
from Calculator.Addition import addition
from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Calculator.Square import square


def variance(data):
    numValues = len(data)
    if numValues == 0:
        raise Exception('empty list passed to list')

    meanValue = mean(data)

    total = 0
    for i in data:
        total = addition(total, square(subtraction(i,meanValue)))

    val = division(len(data)-1,total)
    return val