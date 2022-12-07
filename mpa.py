import numpy as np
def Mpa(search_agents_no, max_iter, lb, ub, dim, fobj):
    top_predator_pos = np.zeros((1, dim))
    top_predator_fit = np.inf
    convergence_curve = np.zeros((1, max_iter))
    step_size = np.zeros((search_agents_no, dim))
    fitness = np.full((search_agents_no, 1), np.inf)
    prey = initialization(search_agents_no, dim, ub, lb)
