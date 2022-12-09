

from get_functions_details import get_functions_details
from mpa import Mpa
if __name__ == '__main__':

    search_agents_no = 25
    max_iteration = 500
    function_name = "F2"
    [lb, ub, dim, fobj] = get_functions_details(function_name)
    [best_score, best_pos, convergence_curve] = Mpa(search_agents_no, max_iteration, lb, ub, dim, fobj)
    print(best_pos)
    print(best_score)
