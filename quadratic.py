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
    Take the equation and the method of solution as input and check if the input
    is valid.
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
    inp = ""
    while inp not in methods:
        inp = input("Enter your Method: ")
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

    # check if its an equation
    if '+' not in eq and '-' not in eq:
        print("\nENTER A VALID QUADRATIC EQUATION!!\n")
        print_info()
        take_input()

    return eq, variable, method


class Quadratic_equation(object):
    """
    Solve Quadratic Equations by creating the instance of this class as
    quadratic equation and use its method named solve.
    """

    def __init__(self, equation, variable, method):
        self.equation = equation
        self.variable = variable
        self.method = method
        self.lhs, self.rhs = self.equation.strip().split('=')

    def sort_vals(self, lst_vals):
        """
        Sorts the list of values in an equation.
        Parameters: List of values
        Returns: Sorted list of values
        """
        values = []
        for val in lst_vals:
            if f"{self.variable}2" in val:
                values.insert(0, val)
            elif f"{self.variable}" in val:
                values.insert(1, val)
            elif val.isnumeric():
                values.insert(2, val)
        return values

    def separate_pos_n_neg_vals(self, eq):
        """
        Separate positive and negative values in an equation.
        Parameters: One side of the equation.
        Returns: Three Lists of all values, positive values and negative values.
        """

        all_values = []
        for val in eq.split('+'):
            if '-' in val:
                lst = val.split('-')
                all_values += [v.strip() for v in lst]
            else:
                all_values += [val.strip()]

        if len(all_values) > 3 or len(all_values) < 2:
            print("\nENTER SIMPLIFIED AND VALID EQUATION\n")
            main()

        # sort the values of all_values
        values = self.sort_vals(all_values)

        positive_values = []
        negative_values = []

        equ = self.equation[self.equation.index(values[0])+len(values[0])-1:]

        # separate positive and negative values
        for val in values[1:]:
            ind = equ.index(val)
            for i in range(ind, 0, -1):
                c = equ[i]
                if c == '+':
                    positive_values.append(val)
                    break
                elif c == '-':
                    print(val)
                    negative_values.append(val)
                    break

        return values, positive_values, negative_values

    def move_to_left(self):
        """
        If the equation has values on the right hand side it moves them to the left hand side

        """
        ar, pr, nr = separate_pos_n_neg_vals(self.rhs)
        al, pl, nl = separate_pos_n_neg_vals(self.lhs)

        values = self.sort_vals(list(ar+al))
        positive_values = self.sort_vals(list(pl+nr))
        negative_values = self.sort_vals(list(nl+pr))

        return values, positive_values, negative_values
        # TODO: complete this function

    def vals_with_signs(self, values, positive_values, negative_values):
        """
        Create list of values with there respective signs.
        """
        sign_values = [values[0]]
        for val in values[1:]:
            if val in positive_values:
                sign_values.append(' +' + val)
            elif val in negative_values:
                sign_values.append(' -' + val)
            else:
                print("Something went wrong on line no. 163")

        return sign_values

    def correct_the_equation(self):
        """
        Correct the equation if its not in the correct syntax
        """

        if self.equation.strip()[0] == '-':
            sign_values = vals_with_signs(self.move_to_left())
        else:
            sign_values = vals_with_signs(separate_pos_n_neg_vals(self.lhs)) + " = 0"
        self.equation = sign_values.join("") + " = 0"
        self.lhs, self.rhs = self.equation.strip().split('=')

    def constants(self):
        """
        Take an equation of form: ax2 + bx + c = 0 and return the constants.
        Parameters: Equation
        Returns: a, b, c
        """
        # TODO: Update this function to also solve equations with '-' sign.

        # split the equation in right hand side and left hand side

        # if self.rhs.strip() != '0':
        #     move_to_left(rhs)

        self.correct_the_equation()
        vals = self.lhs.split('+')

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
        print(self.equation)
        print(f"The coefficient of x2 is {a}\nThe coefficient of x is {b}\nThe constant is {c}")
        # self.equation = f"{a}{variable}2 "
        # TODO: complete this function to print pretty formatted equation

    def quad_method(self):
        """
        This method tries to solve the equation using Quadratic Formula Method.
        """
        '√'
        self.print_coefficients_and_equation()

    def midd_method(self):
        """
        This method tries to solve the equation using Middle Term Break Method.
        """
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
        self.print_coefficients_and_equation()
        # if self.method == 'quad':
        #     quad_method()
        # elif self.method == 'midd':
        #     midd_method()
        # elif self.method == 'sqre':
        #     sqre_method()


# def main():
#     print_info()
#     intention = 'y'
#     while intention.lower().strip() == 'y':
#         eq, var, method = take_input()
#         equation = Quadratic_equation(eq, var, method)
#         equation.separate_pos_n_neg_vals(equation.lhs)
#         equation.solve()
#         print("\nEnter 'y' to solve another, or 'q' for quit.")
#         intention = input("y/q: ")
#         if intention != 'y' and intention != 'q':
#             intention = input("'y' for yes 'q' for quit: ")
#     sys.exit()

def main():
    print_info()
    intention = 'y'
    while intention.lower().strip() == 'y':
        eq, var, method = take_input()
        equation = Quadratic_equation(eq, var, method)
        equation.solve()
        print("\nEnter 'y' to solve another, or 'q' for quit.")
        intention = input("y/q: ")
        if intention != 'y' and intention != 'q':
            intention = input("'y' for yes 'q' for quit: ")
    sys.exit()


if __name__ == '__main__':
    main()
