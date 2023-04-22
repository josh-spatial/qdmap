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

#BD2 function
def bd2(q):
    """Returns BD2 blast distance from a given quantity (Q) in kg."""
    # import numpy as np
    # bd1 = np.where(q < 30_000, 0.35 * q ** (1/3), 0.44 * q ** (1/3))
    # return bd1
    if q < 1_500:
        bd2 = 0.4 * q ** (1/3)
    else:
        bd2 = 0.6 * q ** (1/3)
    return bd2

#BD3 function
def bd3(q):
    """Returns BD3 blast distance from a given
      quantity (Q) in kg."""
    # import numpy as np
    # bd = np.where(q < 30_000, 0.35 * q ** (1/3), 0.44 * q ** (1/3))
    # return bd
    bd = 0.5 * q ** (1/3)
    return bd

#BD4 function
def bd4(q):
    """Returns BD4 blast distance from a given
      quantity (Q) in kg."""
    # import numpy as np
    # bd = np.where(q < 30_000, 0.35 * q ** (1/3), 0.44 * q ** (1/3))
    # return bd
    bd = 0.8 * q ** (1/3)
    return bd

#BD5 function
def bd5(q):
    """Returns BD5 blast distance from a given
      quantity (Q) in kg."""
    # import numpy as np
    # bd = np.where(q < 30_000, 0.35 * q ** (1/3), 0.44 * q ** (1/3))
    # return bd
    bd = 1.1 * q ** (1/3)
    return bd

#BD6 function
def bd6(q):
    """Returns BD6 blast distance from a given
      quantity (Q) in kg."""
    # import numpy as np
    # bd = np.where(q < 30_000, 0.35 * q ** (1/3), 0.44 * q ** (1/3))
    # return bd
    bd = 1.2 * q ** (1/3)
    return bd

#BD7 function
def bd7(q):
    """Returns BD7 blast distance from a given
      quantity (Q) in kg."""
    # import numpy as np
    # bd = np.where(q < 30_000, 0.35 * q ** (1/3), 0.44 * q ** (1/3))
    # return bd
    bd = 1.8 * q ** (1/3)
    return bd

#bd8 function
def bd8(q):
    """Returns BD8 blast distance from a given
      quantity (Q) in kg."""
    # import numpy as np
    # bd = np.where(q < 30_000, 0.35 * q ** (1/3), 0.44 * q ** (1/3))
    # return bd
    bd = 2.0 * q ** (1/3)
    return bd

#bd9 function
def BD9(q):
    """Returns bd9 blast distance from a given
      quantity (Q) in kg."""
    # import numpy as np
    # bd = np.where(q < 30_000, 0.35 * q ** (1/3), 0.44 * q ** (1/3))
    # return bd
    bd = 2.4 * q ** (1/3)
    return bd

#BD10 function
def bd10(q):
    """Returns BD10 blast distance from a given
      quantity (Q) in kg."""
    # import numpy as np
    # bd = np.where(q < 30_000, 0.35 * q ** (1/3), 0.44 * q ** (1/3))
    # return bd
    bd = 3.2 * q ** (1/3)
    return bd

#BD11 function
def bd11(q):
    """Returns BD11 blast distance from a given
      quantity (Q) in kg."""
    # import numpy as np
    # bd = np.where(q < 30_000, 0.35 * q ** (1/3), 0.44 * q ** (1/3))
    # return bd
    bd = 3.6 * q ** (1/3)
    return bd

#BD7 function
def bd12(q):
    """Returns BD12 blast distance from a given
      quantity (Q) in kg."""
    # import numpy as np
    # bd = np.where(q < 30_000, 0.35 * q ** (1/3), 0.44 * q ** (1/3))
    # return bd
    bd = 4 * q ** (1/3)
    return bd

def bd13(q):
    """Returns BD13 blast distance from a given
      quantity (Q) in kg."""
    # import numpy as np
    # bd = np.where(q < 30_000, 0.35 * q ** (1/3), 0.44 * q ** (1/3))
    # return bd
    bd = 4.4 * q ** (1/3)
    return bd

def bd14(q):
    """Returns BD14 blast distance from a given
      quantity (Q) in kg."""
    # import numpy as np
    # bd = np.where(q < 30_000, 0.35 * q ** (1/3), 0.44 * q ** (1/3))
    # return bd
    bd = 4.8 * q ** (1/3)
    return bd

def bd15(q):
    """Returns BD15 blast distance from a given
      quantity (Q) in kg."""
    # import numpy as np
    # bd = np.where(q < 30_000, 0.35 * q ** (1/3), 0.44 * q ** (1/3))
    # return bd
    bd = 6 * q ** (1/3)
    return bd

def bd16(q):
  """Returns BD16 blast distance from a given
      quantity (Q) in kg."""
    # import numpy as np
    # bd = np.where(q < 30_000, 0.35 * q ** (1/3), 0.44 * q ** (1/3))
    # return bd
  if q < 2_500:
      bd = 0.47 * q ** (2/3)
  elif q < 4_500:
      bd = 1.73 * q ** (1/2)
  else:
      bd = 7 * q ** (1/3)
  return bd


def bd17(q):
    """Returns BD17 blast distance from a given quantity (Q) in kg."""
    bd = 7.2 * q ** (1/3)
    return bd

def bd18(q):
    """Returns BD18 blast distance from a given quantity (Q) in kg."""
    bd = 8 * q ** (1/3)
    return bd

def bd19(q):
    """Returns BD19 blast distance from a given quantity (Q) in kg."""
    if q < 2_500:
        bd = 0.61 * q ** (2/3)
    elif q < 4_500:
        bd = 2.23 * q ** (1/2)
    else:
        bd = 9 * q ** (1/3)
    return bd

def bd20(q):
    """Returns BD20 blast distance from a given quantity (Q) in kg."""
    if q < 2_500:
        bd = 0.63 * q ** (2/3)
    elif q < 4_500:
        bd = 2.30 * q ** (1/2)
    else:
        bd = 9.3 * q ** (1/3)
    return bd

def bd21(q):
    """Returns BD21 blast distance from a given quantity (Q) in kg."""
    bd = 9.6 * q ** (1/3)
    return bd

def bd22(q):
    """Returns BD22 blast distance from a given quantity (Q) in kg."""
    if q < 2_500:
        bd = 0.75 * q ** (2/3)
    elif q < 4_500:
        bd = 2.75 * q ** (1/2)
    else:
        bd = 11.1 * q ** (1/3)
    return bd

def bd23(q):
    """Returns BD23 blast distance from a given quantity (Q) in kg."""
    if q < 2_500:
        bd = 0.81 * q ** (2/3)
    elif q < 4_500:
        bd = 2.97 * q ** (1/2)
    else:
        bd = 12 * q ** (1/3)
    return bd

def bd24(q):
    """Returns BD24 blast distance from a given quantity (Q) in kg."""
    bd = 13 * q ** (1/3)
    return bd

def bd25(q):
    """Returns BD25 blast distance from a given quantity (Q) in kg."""
    if q < 2_500:
        bd = 0.95 * q ** (2/3)
    elif q < 4_500:
        bd = 3.47 * q ** (1/2)
    else:
        bd = 14 * q ** (1/3)
    return bd

def bd26(q):
    """Returns BD26 blast distance from a given quantity (Q) in kg."""
    if q < 2_500:
        bd = 1 * q ** (2/3)
    elif q < 4_500:
        bd = 3.6 * q ** (1/2)
    else:
        bd = 14.8 * q ** (1/3)
    return bd

def bd27(q):
    """Returns BD27 blast distance from a given quantity (Q) in kg."""
    bd = 16 * q ** (1/3)
    return bd

def bd28(q):
    """Returns BD28 blast distance from a given quantity (Q) in kg."""
    if q < 2_500:
        bd = 1.22 * q ** (2/3)
    elif q < 4_500:
        bd = 4.46 * q ** (1/2)
    else:
        bd = 18 * q ** (1/3)
    return bd

def bd29(q):
    """Returns BD29 blast distance from a given quantity (Q) in kg."""
    bd = 20 * q ** (1/3)
    return bd

def bd30(q):
    """Returns BD30 blast distance from a given quantity (Q) in kg."""
    bd = 22.2 * q ** (1/3)
    return bd

def bd31(q):
    """Returns BD31 blast distance from a given quantity (Q) in kg."""
    if q < 2_500:
        bd = 1.5 * q ** (2/3)
    elif q < 4_500:
        bd = 5.5 * q ** (1/2)
    else:
        bd = 22.2 * q ** (1/3)
    return bd

def bd32(q):
    """Returns BD32 blast distance from a given quantity (Q) in kg."""
    bd = 25 * q ** (1/3)
    return bd

def bd33(q):
    """Returns BD33 blast distance from a given quantity (Q) in kg."""
    if q < 2_500:
        bd = 1.89 * q ** (2/3)
    elif q < 4_500:
        bd = 6.94 * q ** (1/2)
    else:
        bd = 28 * q ** (1/3)
    return bd

def bd34(q):
    """Returns BD34 blast distance from a given quantity (Q) in kg."""
    if q < 2_500:
        bd = 2.43 * q ** (2/3)
    elif q < 4_500:
        bd = 8.92 * q ** (1/2)
    else:
        bd = 36 * q ** (1/3)
    return bd

def bd35(q):
    """Returns BD35 blast distance from a given quantity (Q) in kg."""
    bd = 44.4 * q ** (1/3)
    return bd

def bd36(q):
    """Returns BD34 blast distance from a given quantity (Q) in kg."""
    if q < 2_500:
        bd = 3 * q ** (2/3)
    elif q < 4_500:
        bd = 11 * q ** (1/2)
    else:
        bd = 44.4 * q ** (1/3)
    return bd