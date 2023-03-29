"""This module contains the basic QD calculation functions."""

import numpy as np

# TODO add the rest of the functions

# Define blast distance (BD) functions.
def bd1(q):
    """Returns BD1 blast distance from a given quantity (Q) in kg."""
    # import numpy as np
    # bd1 = np.where(q < 30_000, 0.35 * q ** (1/3), 0.44 * q ** (1/3))
    # return bd1
    if q < 30_000:
        bd1 = 0.35 * q ** (1/3) 
    else:
        bd1 = 0.44 * q ** (1/3)
    return bd1

def bd1_array(q):
    """Returns BD1 blast distance (as a numpy arrary for plotting) from a given quantity (Q) in kg."""
    bd1 = np.where(q < 30_000, 0.35 * q ** (1/3), 0.44 * q ** (1/3))
    return bd1