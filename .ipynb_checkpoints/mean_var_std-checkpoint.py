import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers")
        
    input_arr = np.array(list)
    matrix = input_arr.reshape(3,3)
    calculations = dict()

    calculations['mean'] = [np.mean(matrix, axis=0), np.mean(matrix, axis=1), np.mean(input_arr)]

    return calculations