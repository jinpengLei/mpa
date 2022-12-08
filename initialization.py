import numpy as np

def initialization(search_agents_no, dim, ub, lb):
    boundary_no = 1
    if type(ub) == np.ndarray:
        boundary_no = ub.shape(0)
    if boundary_no == 1:
        positions = np.random.rand(search_agents_no, dim) * (ub - lb) + lb
    else:
        positions = np.zeros((search_agents_no, dim))
        for i in range(dim):
            ub_i = ub[i]
            lb_i = lb[i]
            positions[:, i] = np.random.rand(search_agents_no, ) * (ub_i - lb_i) + lb_i
    return positions




