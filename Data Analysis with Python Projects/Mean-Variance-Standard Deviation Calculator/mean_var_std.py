import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array([list[0:3],list[3:6],list[6:9]])

    mean = [[*arr.mean(0)],[*arr.mean(1)],arr.mean()]
    variance = [[*arr.var(0)],[*arr.var(1)],arr.var()]
    std = [[*arr.std(0)],[*arr.std(1)],arr.std()]
    max = [[*arr.max(0)],[*arr.max(1)],arr.max()]
    min = [[*arr.min(0)],[*arr.min(1)],arr.min()]
    sum = [[*arr.sum(0)],[*arr.sum(1)],arr.sum()]

    return {
        "mean" : mean,
        "variance" : variance,
        "standard deviation" : std,
        "max" : max,
        "min" : min,
        "sum" : sum}
