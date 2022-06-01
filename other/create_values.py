# this file is here because initially there is just one column with the name of the elements,
# but a combination of each element in the list is needed with a change propagation value in that relationship.
# At this initial stage the value is not important so I just create a cobination of all elements by pairs,
# not repeated, and assign a random value.

import pandas as pd

from itertools import combinations
import random

elements = pd.read_excel("data/Values.xlsx")
perms = combinations(elements["ELEMENT NAME"].to_list(), 2)
rand_cp = round(random.random(), 2)
elements_cp_values = [(*couple, round(random.random(), 2)) for couple in perms]

df_cp = pd.DataFrame(elements_cp_values)
df_cp.columns = ["Element 1", "Element 2", "Value"]
df_cp.to_excel("data/Values_2.xlsx", index=False)
