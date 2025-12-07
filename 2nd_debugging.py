
""" Original (Incorrect) Code
import numpy as np

def swap(coords: np.ndarray):
   
       coords[:, 0], coords[:, 1], coords[:, 2], coords[:, 3] = coords[:, 1], coords[:, 1], coords[:, 3], coords[:, 2]
    return coords

# Test
coords = np.array([[10, 5, 15, 6, 0],
                   [11, 3, 13, 6, 0]])
print("Incorrect:", swap(coords)) """


""" 
Mistake 1: The columns are assigned
incorrectly (coords[:,1] is repeated).

Mistake 2: Without copy() or advanced indexing,
numpy may overwrite values unexpectedly.
"""





#ُSolution :

import numpy as np

def swap(coords: np.ndarray):
    """
    Swap x and y coordinates in a bounding box array of shape [n,5].
    """
    coords = coords.copy()  #  avoid modifying original array
    coords[:, [0, 1, 2, 3]] = coords[:, [1, 0, 3, 2]]  # correct swap
    return coords




# --- Test ---
coords = np.array([[10, 5, 15, 6, 0],
                   [11, 3, 13, 6, 0]])

swapped = swap(coords)
print(swapped)
# Expected output:
# [[ 5 10  6 15  0]
#  [ 3 11  6 13  0]]