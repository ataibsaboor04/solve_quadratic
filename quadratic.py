import sys
import math
import sympy
from sympy import pretty_print as pprint


def take_input():
    print("Enter the variable, coefficients and the constant.")
    v = input("variable: ")
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    if a < 0:
        return -a, -b, -c, v
    elif a == 0:
        print("Its not a quadratic equation.")
        sys.exit()
    return a, b, c, v


def take_solution_method():
    methods = {'quad': "Quadratic Formula Method",
               'midd': "Middle Term Break Method",
               'sqre': "Completing Squares Method"}
    print("\nSpecify your method by which you want to solve your equation.")
    # print available methods
    for short in methods:
        print(f"'{short}' for '{methods[short]}'")
    method = ""
    while method not in methods:
        method = input("\nMethod: ")
    return method


def firststring(f, var=""):
    if var=="":
        return f
    if f > 0:
        fstr = f"{f}{var}"
        if f == 1:
            fstr = f"{var}"
    elif f < 0:
        fstr = f"- {-f}{var}"
        if f == -1:
            fstr = f"- {var}"
    return fstr


def astring(a, var):
    if a == 1:
        astr = f"{var}2"
    else:
        astr = f"{a}{var}2"
    return astr


def bstring(b, var):
    if b > 0:
        bstr = f"+ {b}{var}"
        if b == 1:
            bstr = f"+ {var}"
    elif b < 0:
        bstr = f"- {-b}{var}"
        if b == -1:
            bstr = f"- {var}"
    else:
        bstr = "\b"
    return bstr


def cstring(c):
    if c > 0:
        cstr = f"+ {c}"

    elif c < 0:
        cstr = f"- {-c}"

    else:
        cstr = "\b"
    return cstr


def make_strings(a, b, c, var):
    astr = astring(a, var)
    bstr = bstring(b, var)
    cstr = cstring(c)
    return astr, bstr, cstr


def print_equation(a, b, c, var):
    astr, bstr, cstr = make_strings(a, b, c, var)
    print(astr, bstr, cstr, "= 0")


def split_middle_term(a, b, c):
    for i in range(50):
        for j in range(20):
            if i*j == abs(a*c):
                if b > 0 and c > 0:
                    if i+j == b:
                        return i, j
                    # elif i-j == b:
                    #     return i, -j
                    # elif j-i == b:
                    #     return -i, j
                elif b < 0 and c < 0:
                    if i-j == b:
                        return i, -j
                    elif j-i == b:
                        return -i, j
                elif b > 0 and c < 0:
                    if i-j == b:
                        return i, -j
                    elif j-i == b:
                        return -i, j
                elif b < 0 and c > 0:
                    if -i-j == b:
                        return -i, -j
                    elif i+j == b:
                        return i, j
    return False


def take_common(p, q):
    common = math.gcd(p, q)
    p = int(p/common)
    q = int(q/common)
    if p < 0:
        return -common, -p, -q
    return common, p, q


def quad_method(a, b, c, var):
    """
    This method tries to solve the equation using Quadratic Formula Method.
    """
    """     √ chr(8730s)
            ± chr(177)
    """
    print("-"*50 + "\nQuadratic Formula Method\n" + "-"*50)
    print_equation(a, b, c, var)

    # Quadratic Formula
    # aq, bq, cq = sympy.symbols('a b c')
    # pprint((-bq + - sympy.sqrt(bq**2 - 4aq cq))/2aq))


def midd_method(a, b, c, var):
    """
    This method tries to solve the equation using Middle Term Break Method.
    """
    print("-"*50 + "\nMiddle Term Break Method\n" + "-"*50)

    astr, bstr, cstr = make_strings(a, b, c, var)

    print()
    print_equation(a, b, c, var)

    # a2 + 2ab + b2 = (a+b)2
    if c > 0:
        if int(2*math.sqrt(a)*math.sqrt(c)) == b:
            print()
            s, t = '-', '\b'
            if b > 0:
                s, t = '+', '-'
            ar, cr = firststring(int(math.sqrt(a)), var), int(math.sqrt(c))
            print(f"({ar})2 {s} 2({ar})({cr}) + ({cr})2 = 0")
            print()
            print(f"({ar} {s} {cr})2 = 0")
            print()
            print(" "*3, "Taking Root On Both Sides")
            print()
            print(f"{ar} {s} {cr} = 0")
            print()
            print(f"{ar} = {t} {cr}")

            if int(math.sqrt(a)) == 1:
                sys.exit()
            else:
                print()
                print(f"{var} = {t} {cr}/{int(math.sqrt(a))}")
                sys.exit()

    # Split middle Term
    if split_middle_term(a, b, c) is False:
        print("Can't break the middle term.")
        sys.exit()
    b1, b2 = split_middle_term(a, b, c)
    b1str, b2str = bstring(b1, var), bstring(b2, var)

    # Step 1
    print()
    print(astr, b1str, b2str, cstr, "= 0")

    # Step 2
    print()
    common1, acommon, b1common = take_common(a, b1)
    common1str, acommonstr, b1commonstr = firststring(
        common1, var), firststring(acommon, var), cstring(b1common)
    common2, b2common, ccommon = take_common(b2, c)
    common2str, b2commonstr, ccommonstr = cstring(
        common2), firststring(b2common, var), cstring(ccommon)
    print(f"{common1str}({acommonstr} {b1commonstr})",
          f"{common2str}({b2commonstr} {ccommonstr})", "= 0")
    if f"({acommonstr} {b1commonstr})" != f"({b2commonstr} {ccommonstr})":
        print("Can't solve by Middle Term Break Method")
        sys.exit()

    # Step 3
    print()
    print(f"({acommonstr} {b1commonstr}).({common1str} {common2str})", "= 0")

    # Step 4
    print()
    print("Either".rjust(12), end="")
    print("Or".rjust(28))
    print()
    print(" "*3, f"{acommonstr} {b1commonstr} = 0".ljust(30), end="")
    print(f"{common1str} {common2str} = 0")

    # Step 5
    print()
    b1commonstr, common2str = firststring(-b1common), firststring(-common2)
    print(" "*3, f"{acommonstr} = {b1commonstr}".ljust(30), end="")
    print(f"{common1str} = {common2str}")
    if acommon == 1 and common1 == 1:
        sys.exit()

    # Step 6
    print()
    if acommon == 1:
        s = ""
    else:
        s = f"/{acommon}"
    if common1 == 1:
        t = ""
    else:
        t = f"/{common1}"

    print(" "*3, f"{var} = {b1commonstr}{s}".ljust(30), end="")
    print(f"{var} = {common2str}{t}")


def sqre_method(a, b, c, var):
    """
    This method tries to solve the equation using Completing Squares Method.
    """
    print("-"*50 + "\nCompleting Squares Method\n" + "-"*50)

    astr, bstr, cstr = make_strings(a, b, c, var)

    print()
    print_equation(a, b, c, var, '= 0')


def solve():
    """
    Solve the quadratic equation with the specified method.
    """
    a, b, c, var = take_input()
    method = take_solution_method()
    print("\n\nSOLUTION:\n")
    if method == 'quad':
        quad_method(a, b, c, var)
    elif method == 'midd':
        midd_method(a, b, c, var)
    elif method == 'sqre':
        sqre_method(a, b, c, var)


if __name__ == '__main__':
    solve()
