import math

def mean(data):
    if len(data) == 0:
        raise ValueError("The dataset cannot be empty")
    return sum(data) / len(data)

def median(data):
    sorted_data = sorted(data)
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return sorted_data[mid]

def mode(data):
    from collections import Counter
    count = Counter(data)
    return count.most_common(1)[0][0]

def standard_deviation(data):
    if len(data) == 0:
        raise ValueError("The dataset cannot be empty")
    
    # Calculate the mean
    data_mean = mean(data)
    
    # Calculate the variance
    variance = sum((x - data_mean) ** 2 for x in data) / len(data)
    
    # Return the square root of the variance (standard deviation)
    return math.sqrt(variance)
