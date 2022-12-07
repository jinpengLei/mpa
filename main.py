# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from get_functions_details import get_functions_details
from mpa import Mpa
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    search_agents_no = 25
    max_iteration = 500
    function_name = "F1"
    [lb, ub, dim, fobj] = get_functions_details(function_name)
    [best_score, best_pos, convergence_curve] = Mpa(search_agents_no, max_iteration, lb, ub, dim, fobj)