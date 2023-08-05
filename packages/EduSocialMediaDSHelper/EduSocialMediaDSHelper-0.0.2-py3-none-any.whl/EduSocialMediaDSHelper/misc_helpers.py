# Likely imports for all functions below
import numpy as np
import matplotlib.pyplot as plt

# Example Likert distributions with various centers and outlier capability
# Returns an array of ints of a given size
def ExLikertDist(size=1000, center=None, outlier=False):

    l_choices = [1, 2, 3, 4, 5]

    if center == 'left':
        l_probs = [0.40, 0.35, 0.15, 0.05, 0.05]
    elif center == 'right':
        l_probs = [0.05, 0.05, 0.15, 0.35, 0.40]
    elif center == 'bimodal':
        l_probs = [0.35, 0.125, 0.05, 0.125, 0.35]
    elif center == 'center':
        l_probs = [0.05, 0.15, 0.60, 0.15, 0.05]
    else:
        l_probs = [0.2, 0.2, 0.2, 0.2, 0.2]

    a = np.random.choice(l_choices, p=l_probs, size=size)

    if outlier:
        a = np.concatenate([a, [8]*int(round(size/100))])

    return a