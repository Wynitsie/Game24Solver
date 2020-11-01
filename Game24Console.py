# =============================================================================
#  Name:            Game24Console
#  Purpose:         
#   
#  Author:          numberthreeox
#  Date Created:    10/26/2020
# =============================================================================
from CombinationGenerator import *

def Game24Console():
    """
    Starts a console program that takes in user inputs and determines solutions
    for a game of 24.
    """

    welcome_message = 'Hello! Welcome to the 24 Solver.'
    menu = 'What would you like to do next?\n'\
           'new = new game\n' \
           'num = number of solutions\n' \
           'full = full list of solutions\n' \
           'q = quit\n'

    print(welcome_message)
    status = 'new'

    while status != 'q':
        if status == 'new':
            a = input('Enter your 4 values! ')
            b = input('Good! Another! ')
            c = input('More please! ')
            d = input('Last one! ')

            #TESTING

            CombinationGenerator(a, b, c, d)
            # TODO look for solutions
            # TODO print out Y/N solvability

            # Ask user for next steps
            status = input(menu)

        elif status == 'num':
            #TODO print out number of solutions
            status = input(menu)

        elif status == 'full':
            #TODO print out full list of solutions
            status = input(menu)

Game24Console()

