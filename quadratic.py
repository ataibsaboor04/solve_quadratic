import sys
from math import gcd


def print_info():
    """
    Print out the basic information for the user to use the program.
    """
    print("Solve your quadratic equation easily.")
    print("Write equation of form: ax2 + bx + c = 0")
    print("For example, x2 + 6x + 8 = 0")
    print("Note: DONT USE BRACKETS")


def take_input():
    """
    Take the equation and the method of solution as input and check if the input is valid.
    """
    # Take the equation and method of solution as input from user
    eq = input("Enter your Equation: ")

    # Take the method of solving the equation
    methods = {'quad': "Quadratic Formula Method",
               'midd': "Middle Term Break Method",
               'sqre': "Completing Squares Method"}
    print("Specify your method by which you want to solve your equation.")
    for short in methods:
        print(f"'{short}' for '{methods[short]}'")
    inp = input("Enter you Method: ")
    method = methods[inp]

    # Conditions for input to be valid

    # check for brackets in the equation
    if "(" in eq or "{" in eq or "[" in eq:
        print("\nDON'T USE BRACKETS!!")
        take_input()

    # check if equation has more than one variable
    for i in eq:
        if i.isalpha():
            variable = i
            break
    for i in eq:
        if i.isalpha() and variable != i:
            print("\nENTER A QUADRATIC EQUATION!!")
            take_input()

    # check if its a equation
    if '+' not in eq and '-' not in eq:
        print("\nENTER A VALID QUADRATIC EQUATION!!")
        print_info()
        take_input()

    return eq, variable, method


class Quadratic_equation(object):
    """docstring for Quadratic."""

    def __init__(self, equation, variable, method):
        self.equation = equation
        self.variable = variable
        self.method = method

    def move_to_left(self, rhs):
        for t in rhs:
            if t == '+':
                pass
        # TODO: complete this function

    def constants(self):
        """
        Take an equation of form: ax2 + bx + c = 0 and return the constants.
        Parameter: Equation
        Return: a, b, c
        """
        # TODO: Update this function to also solve equations with '-' sign.

        # split the equation in right hand side and left hand side
        lhs, rhs = self.equation.split('=')

        if rhs.strip() != '0':
            move_to_left(rhs)
        vals = lhs.split('+')

        for x in vals:
            if 'x2' in x.strip():
                if len(x.strip()) == 2:
                    a = 1
                else:
                    a = int(x[:x.index('x2')])
            elif 'x' in x.strip():
                if len(x.strip()) == 1:
                    b = 1
                else:
                    b = int(x[:x.index('x')])
            elif x.strip().isnumeric():
                c = int(x)

        return a, b, c

    def print_coefficients_and_equation(self):
        """
        This method prints out the coefficients and constant in the equation.
        """
        a, b, c = self.constants()
        print("\n"+"-"*30+f"{self.method}")
        print(f"The coefficient of x2 is {a}\nThe coefficient of x is {b}\nThe constant is {c}")
        print(f"{a}{variable}2 ")  # TODO: complete this function to print pretty formatted equation

    def quad_method(self):
        """
        This method tries to solve the equation using Quadratic Formula Method.
        """
        self.print_coefficients_and_equation()

    def midd_method(self):
        """
        This method tries to solve the equation using Middle Term Break Method.
        """
        '√'
        self.print_coefficients_and_equation()

    def sqre_method(self):
        """
        This method tries to solve the equation using Completing Squares Method.
        """
        self.print_coefficients_and_equation()

    def solve(self):
        """
        Solve the quadratic equation with the specified method.
        """
        print("\n\nSOLUTION:")

        # if self.method == 'quad':
        #     quad_method()
        # elif self.method == 'midd':
        #     midd_method()
        # elif self.method == 'sqre':
        #     sqre_method()


def main():
    print_info()
    intention = 'y'
    while intention.lower().strip() == 'y':
        print()
        eq, var, method = take_input()
        equation = Quadratic_equation(eq, var, method)
        equation.solve()
        print("\nEnter 'y' to solve another, or 'q' for quit.")
        intention = input("y/q: ")
    sys.exit()


if __name__ == '__main__':
    main()
