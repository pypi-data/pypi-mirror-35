#!/usr/bin/env python
"""Compare the old and new rv precision."""

import pandas as pd

old_precision_file = "../data/precision_data_paper2015.txt"
df_old = pd.read_table(old_precision_file)
# df_old_corrected = ...

new_precision_file = "../data/new_precision_values.txt"
df_new = pd.read_table(new_precision_file)

# compare results 1 , 2 and 3
# count number of precision in cond 2 that decreased

# Combine the data frames together?

# Header names Simulation	RV_Cond_1[m/s]	RV_Cond_2[m/s]	RV_Cond_3[m/s]

# Might need to resort the table to have matching rows.
# This might be able to done when saving I think?

# Number_of cond2 that decrease
cond_2_lower = (df_old["RV_Cond_2[m/s]"] > df_new["RV_Cond_2[m/s]"]).sum()
percent_diff = (df_new["RV_Cond_2[m/s]"] - df_old["RV_Cond_2[m/s]"]) / df_old[
    "RV_Cond_2[m/s]"
]

print("Number of cond_2 precisions that were lower = {0:d}".format(cond_2_lower))
print("Percentage change in precision new-old/old")
for sim in df_new:
    print(sim, df_new[sim]["RV_Cond_2[m/s]"])
    # Calculate percentage difference inc precision of cond 1, 2, 3
    # With 1 and 3 testing the normalization.

    # Better as a Notebook.
