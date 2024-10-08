import math
from collections import Counter

def mean(data):
    if len(data) == 0:
        raise ValueError("The dataset cannot be empty")
    return sum(data) / len(data)

def median(data):
    if len(data) == 0:
        raise ValueError("The dataset cannot be empty")
    
    sorted_data = sorted(data)
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return sorted_data[mid]

def mode(data):
    if len(data) == 0:
        raise ValueError("The dataset cannot be empty")
        
    count = Counter(data)
    modes = count.most_common()  # Get all elements with their counts
    
    max_count = modes[0][1]  # The highest count
    modes_with_max_count = [num for num, freq in modes if freq == max_count]
    
    if len(modes_with_max_count) == 1:
        return modes_with_max_count[0]  # Return the single mode
    else:
        return modes_with_max_count  # Return all modes if there are multiple

def standard_deviation(data):
    if len(data) == 0:
        raise ValueError("The dataset cannot be empty")
    
    # Calculate the mean
    data_mean = mean(data)
    
    # Calculate the variance
    variance = sum((x - data_mean) ** 2 for x in data) / len(data)
    
    # Return the square root of the variance (standard deviation)
    return math.sqrt(variance)
