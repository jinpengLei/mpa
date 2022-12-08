import numpy as np
from initialization import initialization
from levy import levy
def Mpa(search_agents_no, max_iter, lb, ub, dim, fobj):
    top_predator_pos = np.zeros((1, dim))
    top_predator_fit = np.inf
    convergence_curve = np.zeros((max_iter, ))
    step_size = np.zeros((search_agents_no, dim))
    fitness = np.full((search_agents_no, 1), np.inf)
    prey = initialization(search_agents_no, dim, ub, lb)
    print(prey.shape)
    x_min = np.tile(np.ones(dim, ) * lb, (search_agents_no, 1))
    x_max = np.tile(np.ones(dim, ) * ub, (search_agents_no, 1))
    iter = 0
    FADs = 0.2
    P = 0.5
    while iter < max_iter:
        for i in range(prey.shape[0]):
            flag_ub = np.where(prey[i, :] > ub, 1, 0)
            flag_lb = np.where(prey[i, :] < lb, 1, 0)
            flag = flag_ub + flag_lb
            prey[i, :] = prey[i, :] * np.where(flag != 0, 0, 1) + ub * flag_ub + lb * flag_lb

            fitness[i, 0] = fobj(prey[i, :])
            if fitness[i, 0] < top_predator_fit:
                top_predator_fit = fitness[i, 0]
                top_predator_pos = prey[i, :]
        if iter == 0:
            fit_old = fitness
            prey_old = prey

        inx = np.where(fit_old < fitness, 1, 0)
        indx = np.tile(inx, (1, dim))
        prey = indx * prey_old + np.where(indx != 0, 0, 1) * prey
        fitness = inx * fit_old + np.where(inx != 0, 0, 1) * fitness
        fit_old = fitness
        prey_old = prey

        elite = np.tile(top_predator_pos, (search_agents_no, 1))
        CF = (1 - iter / max_iter) ** (2 * iter / max_iter)

        RL = 0.05 * levy(search_agents_no, dim, 1.5)
        RB = np.random.randn(search_agents_no, dim)

        for i in range(prey.shape[0]):
            for j in range(prey.shape[1]):
                R = np.random.rand()
                if iter < max_iter / 3:
                    step_size[i, j] = RB[i, j] * (elite[i, j] - RB[i, j] * prey[i, j])
                    prey[i, j] = prey[i, j] + P * R * step_size[i, j]
                elif max_iter / 3 <= iter < 2 * max_iter / 3:
                    if i > prey.shape[0] / 2:
                        step_size[i, j] = RB[i, j] * (RB[i, j]*elite[i, j]-prey[i, j])
                        prey[i, j] = elite[i, j] + P * CF * step_size[i, j]
                    else:
                        step_size[i, j] = RL[i, j] * (elite[i, j] - RL[i, j] * prey[i, j])
                        prey[i, j] = prey[i, j] + P * R * step_size[i, j]
                else:
                    step_size[i, j] = RL[i, j] *(RL[i, j] * elite[i, j] - prey[i, j])
                    prey[i, j] = elite[i, j] + P * CF * step_size[i, j]

        for i in range(prey.shape[0]):
            flag_ub = np.where(prey[i, :] > ub, 1, 0)
            flag_lb = np.where(prey[i, :] < lb, 1, 0)
            flag = flag_ub + flag_lb
            prey[i, :] = prey[i, :] * np.where(flag != 0, 0, 1) + ub * flag_ub + lb * flag_lb

            fitness[i, 0] = fobj(prey[i, :])
            if fitness[i, 0] < top_predator_fit:
                top_predator_fit = fitness[i, 0]
                top_predator_pos = prey[i, :]

        if iter == 0:
            fit_old = fitness
            prey_old = prey

        inx = np.where(fit_old < fitness, 1, 0)
        indx = np.tile(inx, (1, dim))
        prey = indx * prey_old + np.where(indx != 0, 0, 1) * prey
        fitness = inx * fit_old + np.where(inx != 0, 0, 1) * fitness
        fit_old = fitness
        prey_old = prey

        if np.random.rand() < FADs:
            U = np.where(np.random.rand(search_agents_no, dim) < FADs, 1, 0)
            prey = prey + CF * ((x_min + np.random.rand(search_agents_no, dim) * (x_max - x_min)) * U)
        else:
            r = np.random.rand()
            Rs = prey.shape[0]
            step_size = (FADs * (1 - r) + r) * (prey[np.random.permutation(Rs), :] - prey[np.random.permutation(Rs), :])
            prey = prey + step_size

        convergence_curve[iter] = top_predator_fit
        iter = iter + 1

    return [top_predator_fit, top_predator_pos, convergence_curve]





