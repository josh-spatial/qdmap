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
  """Returns BD17 blast distance from a given
      quantity (Q) in kg."""
    # import numpy as np
    # bd = np.where(q < 30_000, 0.35 * q ** (1/3), 0.44 * q ** (1/3))
    # return bd
  bd = 7.2 * q ** (1/3) 
  return bd


