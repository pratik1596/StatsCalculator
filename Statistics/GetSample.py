import random

def getSample(data, sample_size):
    random_values = random.choices(data, weights=None, cum_weights=None, k=sample_size)

    return random_values