import numpy as np
def normalize(arr):
    mean = np.mean(arr)
    std_dev = np.std(arr)
    normalized = (arr - mean) / std_dev
    return normalized
sample_array = np.arange(10) 
print("Original Array:", sample_array)
normalized = normalize(sample_array)
print("Normalized Array:", normalized)
