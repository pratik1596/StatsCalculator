import random
from random import uniform

def RandomInt(low, high):
    return random.randint(low, high)

def RandomFloat(low, high):
    return uniform(low, high)

def IntSeed(low, high, seed):
    random.seed(seed)
    return RandomInt(low, high)

def RandomIntegers(low, high, seed, total):
    data = []
    for i in range(total):
        random.seed(seed)
        data.append(random.randint(low, high))
    return data

def RandomFloats(low, high, seed, total):
    data = []
    for i in range(total):
        random.seed(seed)
        data.append(RandomFloat(low, high))
    return data