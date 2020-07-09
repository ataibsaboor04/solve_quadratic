import sys
from math import gcd

print("Type your quadratic equation")
print("Write equation of form: ax2 + bx + c = 0")
print("For example, x2 + 2x + 7 = 0")
eq = input("Equation: ")

def find_const(eq):
    """
    Take an equation of form: ax2 + bx + c = 0 and return the constants.
    Input: Equation
    Returns: a, b, c
    """
    lhs, rhs = eq.split('=')
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

a, b, c = find_const(eq)
s, t = a, b
if a == 1: s = ''
if b == 1: t = ''

print(f"\n{s}x2 + {t}x + {c} = 0")
def split_middle_term(a, b, c):
    for i in range(20):
        for j in range(20):
            if i*j == a*c and i+j == b:
                b1 = i
                b2 = j
                return b1, b2

try:
    b1, b2 = split_middle_term(a, b, c)
    t1 = b1
    t2 = b2
except:
    print("I can't solve your equation. Sorry!!")
    sys.exit()

if b1 == 1: t1 = ''
if b2 == 1: t2 = ''

print(f"\n{s}x2 + {t1}x + {t2}x + {c} = 0")

n1 = gcd(a, b1)
n2 = gcd(c, b2)

s1 = int(a/n1)
s2 = int(b1/n1)
t1 = int(b2/n2)
t2 = int(c/n2)

if n1 == 1: n1 = ''
if n2 == 1: n2 = ''
if s1 == 1: s1 = ''
if s2 == 1: s2 = ''
if t1 == 1: t1 = ''
if t2 == 1: t2 = ''

print(f"\n{n1}x({s1}x + {s2}) + {n2}({t1}x + {t2}) = 0")
