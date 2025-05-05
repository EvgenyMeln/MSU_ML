import numpy as np
import statistics as st

numbers = np.array([1, 2, 3, 4, 5])
print(numbers)
numbers_mean = st.mean(numbers)
numbers_std = np.std(numbers)
numbers_scaled = (numbers - numbers_mean)/numbers_std
print(numbers_scaled)
