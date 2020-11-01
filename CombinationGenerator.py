# =============================================================================
#  Name:            CombinationGenerator
#  Purpose:         
#   
#  Author:          Winnie Ding
#  Date Created:    10/29/2020
# =============================================================================

import itertools

def CombinationGenerator(a, b, c, d):
    """
    Takes 4 values and generates every combination to test in
    reverse polish notation
    """

    values_list = [a, b, c, d]
    operators_list = ['+', '-', '*', '/']

    #Generate permutations of 4 numbers
    values_perms = []
    for perm in itertools.permutations(values_list,4):
        values_perms.append(perm)

    #Generate combinations of 3 operators
    operators_combs = []
    for comb in itertools.combinations_with_replacement(operators_list,3):
        operators_combs.append(comb)

    #Generate orders of values vs operators
    full_combinations = []
    for values_row in values_perms:
        for operators_row in operators_combs:
            # We have exactly 4 operands, so there are limited ways
            # to arrange them into a valid expression.
            # Hard-coding the 5 possible orders of operands and operators:
            #[v,v,v,v,o,o,o]
            full_combinations.append(values_row+operators_row)
            #[v,v,v,o,v,o,o]
            full_combinations.append(values_row[:-1]+(operators_row[0],
                                     values_row[-1])+operators_row[1:])
            #[v,v,v,o,o,v,o]
            full_combinations.append(values_row[:-1] + operators_row[0:2]
                                     + (values_row[-1], operators_row[-1]))
            #[v,v,o,v,v,o,o]
            full_combinations.append(values_row[:-2] + (operators_row[0],)
                                     + values_row[-2:] + operators_row[-2:])
            #[v,v,o,v,o,v,o]
            full_combinations.append(values_row[:-2] + (operators_row[0],
                                     values_row[-2], operators_row[-2],
                                     values_row[-1], operators_row[-1]))
    for p in full_combinations:
        print(p)

