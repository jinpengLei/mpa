import numpy as np

def F1(x):
    return np.sum(np.power(x, 2), axis=0)
def F2(x):
    return np.prod(np.abs(x), axis=0) + np.sum(np.abs(x), axis=0)
def F3(x):
    return np.max(np.abs(x), axis=0)


def get_functions_details(function_name):
    fobj = F1
    lb = -100
    ub = 100
    dim = 50
    if function_name == 'F1':
        fobj = F1
        lb = -100
        ub = 100
        dim = 50
    elif function_name == 'F2':
        fobj = F2
        lb = -10
        ub = 10
        dim = 50
    elif function_name == 'F3':
        fobj = F3
        lb = -100
        ub = 100
        dim = 50
    return [lb, ub, dim, fobj]