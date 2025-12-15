import csv
import numpy as np
from typing import Set,Tuple, List
import torch
import torch.utils
import torch.utils.data
import torch.nn as nn
import torchvision
NoneType = type(None)
import matplotlib.pyplot as plt
from IPython.display import display, clear_output
from PIL import Image
import torchvision.transforms.functional as TF
from torchvision.models import vgg11
from torchvision.models import mobilenet_v2
import torchvision.transforms as transforms
import time


"""def id_to_fruit(fruit_id: int, fruits: Set[str]) -> str:
    
    This method returns the fruit name by getting the string at a specific index of the set.

    :param fruit_id: The id of the fruit to get
    :param fruits: The set of fruits to choose the id from
    :return: The string corrosponding to the index ``fruit_id``

    **This method is part of a series of debugging exercises.**
    **Each Python method of this series contains bug that needs to be found.**

    | ``1   It does not print the fruit at the correct index, why is the returned result wrong?``
    | ``2   How could this be fixed?``

    This example demonstrates the issue:
    name1, name3 and name4 are expected to correspond to the strings at the indices 1, 3, and 4:
    'orange', 'kiwi' and 'strawberry'..

    >>> name1 = id_to_fruit(1, {"apple", "orange", "melon", "kiwi", "strawberry"})
    >>> name3 = id_to_fruit(3, {"apple", "orange", "melon", "kiwi", "strawberry"})
    >>> name4 = id_to_fruit(4, {"apple", "orange", "melon", "kiwi", "strawberry"})
    
    idx = 0
    for fruit in fruits:
        if fruit_id == idx:
            return fruit
        idx += 1
    raise RuntimeError(f"Fruit with id {fruit_id} does not exist")

name1 = id_to_fruit(1, {"apple", "orange", "melon", "kiwi", "strawberry"})
name3 = id_to_fruit(3, {"apple", "orange", "melon", "kiwi", "strawberry"})
name4 = id_to_fruit(4, {"apple", "orange", "melon", "kiwi", "strawberry"}) """






#ُSolution :
 
"""The returned result is incorrect because
the method iterates over a set.
In Python, a set is unordered, meaning its
elements do not have a fixed or predictable order.
Therefore, accessing an element by an index while
iterating over a set will not consistently return
the expected fruit, since the iteration order can 
change every time the program runs.
so
we can Replace the set with a list """


def id_to_fruit(fruit_id: int, fruits: list[str]) -> str:
    idx = 0
    for fruit in fruits:   
        if fruit_id == idx:
            return fruit
        idx += 1

    raise RuntimeError(f"Fruit with id {fruit_id} does not exist")





#Test
"""Inside the block:
- A list of fruits is defined with a fixed order.
- The `id_to_fruit` function is called with specific indices (1, 3, 4) to retrieve 
the corresponding fruits.
- The results are printed to the console to verify that the function 
returns the correct fruit for each index. """

if __name__ == "__main__":
    fruits = ["apple", "orange", "melon", "kiwi", "strawberry"]
    print(id_to_fruit(1, fruits))
    print(id_to_fruit(3, fruits))
    print(id_to_fruit(4, fruits))