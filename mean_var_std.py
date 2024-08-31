import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
        
    input_arr = np.array(list)
    matrix = input_arr.reshape(3,3)
    calculations = {}

    calculations['mean'] = [np.mean(matrix, axis=0), np.mean(matrix, axis=1), np.mean(input_arr)]
    calculations['variance'] = [np.var(matrix, axis=0), np.var(matrix, axis=1), np.var(input_arr)]
    calculations['standard deviation'] = [np.mean(matrix, axis=0), np.mean(matrix, axis=1), np.mean(input_arr)]
    calculations['max'] = [np.max(matrix, axis=0), np.max(matrix, axis=1), np.max(input_arr)]
    calculations['min'] = [np.min(matrix, axis=0), np.min(matrix, axis=1), np.min(input_arr)]
    calculations['sum'] = [np.sum(matrix, axis=0), np.sum(matrix, axis=1), np.sum(input_arr)]

    for key in calculations:
        to_format = calculations[key]
        regular_list = [item.tolist() for item in to_format]
        calculations[key] = regular_list    
    
    return calculations