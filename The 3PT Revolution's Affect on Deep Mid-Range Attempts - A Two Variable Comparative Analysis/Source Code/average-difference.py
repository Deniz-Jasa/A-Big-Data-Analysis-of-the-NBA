# One Variable Assignment - Deniz Jasarbasic
import numpy as np

# Data sets:
list_central_tendency_a = [20.038, 19.9, 20.2]
list_central_tendency_b = [30.111, 30.05, 26.1]

# Calculations:
diffs_a = np.array(list_central_tendency_a)
diffs_b = np.array(list_central_tendency_b)

np.diff(diffs_a)
np.diff(diffs_b)

# Output:
print(np.diff(diffs_a))
print(np.sum(np.diff(diffs_a))/(len(diffs_a)))

print(np.diff(diffs_b))
print(np.sum(np.diff(diffs_b))/(len(diffs_b)))