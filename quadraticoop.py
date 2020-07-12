import sys
from math import gcd

def print_info():
    """
    Print out the basic information for the user to use the program.
    """
    print("Solve your quadratic equation easily.")
    print("Write equation of form: ax2 + bx + c = 0")
    print("For example, x2 + 6x + 8 = 0")
    print("Note: DONT USE BRACKETS\n")


def take_input():
    """
    Take the equation and the method of solution as input and check if the input is valid.
    """
    # Take the equation and method of solution as input from user
    eq = input("Enter your Equation: ")
    print("Specify your method by which you want to solve your equation.\n1. 'quad' for Quadratic formula method\n2. 'midd' for Middle term break method\n3. 'sqre' for Completing square method")
    method = input("Enter you Method: ")

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

    def constants(self):
        """
        Take an equation of form: ax2 + bx + c = 0 and return the constants.
        Parameter: Equation
        Return: a, b, c
        """
        lhs, rhs = self.equation.split('=')
        if rhs.strip() == '0':
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
        else:
            print("Please type equation in the form:")
            print("ax2 + bx + c = 0")
        return a, b, c

    def print_coefficients(self):
        """
        This method prints out the coefficients and constant in the equation.
        """
        a, b, c = self.constants()
        print(f"The coefficient of x2 is {a}\nThe coefficient of x is {b}\nThe constant is {c}")

    def quad_method(self):
        pass

    def midd_method(self):
        pass

    def sqre_method(self):
        pass
        
    def solve(self):
        """
        Solve the quadratic equation with the specified method.
        """
        pass
        # if self.method == 'quad':
        #     quad_method()
        # elif self.method == 'midd':
        #     midd_method()
        # elif self.method == 'sqre':
        #     sqre_method()

def main():
    print('√') # √
    print_info()
    intention = 'y'
    while intention.lower().strip() == 'y':
        eq, var, method = take_input()
        equation = Quadratic_equation(eq, var, method)
        equation.solve()
        print("\nEnter 'y' to solve another, or 'q' for quit.")
        intention = input("y/q: ")
    sys.exit()


if __name__ == '__main__':
    main()
