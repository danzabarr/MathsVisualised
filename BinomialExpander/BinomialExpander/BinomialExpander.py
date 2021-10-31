from fractions import Fraction
import math

terms = 60

# Input binomial in the form
# (constant + x_coefficient * x)^exponent
# Example
# (4 + 3x)^3
constant = Fraction(input("Enter constant: "))
x_coefficient = Fraction(input("Enter x coefficient: "))
exponent = Fraction(input("Enter exponent: "))
x = Fraction(input("Enter a value for x: "))

# rearrange to the form:
# constant^exponent(1 + x_coefficient / constant * x)^exponent
# by factoring out the constant and applying law of indices (ab)^x = a^x * b^x
factor = constant ** exponent
coefficient = Fraction(x_coefficient, constant)

sum = 0

def prod(list):
    p = 1
    for x in list:
        p *= x
    return p

def format_fraction(fraction):
    if (fraction.numerator == fraction.denominator):
        return str(fraction.numerator)

    if (fraction.denominator == 1):
        return str(fraction.numerator)

    return f'{fraction.numerator}/{fraction.denominator}'

def format_fraction_exponent(fraction, exponent):

    if (exponent == 0):
        return format_fraction(fraction)
    
    if (exponent == 1):
        return f'({format_fraction(fraction)})x'
    
    return f'({format_fraction(fraction)})x^{exponent}'


print(f'({constant} + {x_coefficient}x)^{exponent}')
print(f'= {factor}(1 + {coefficient}x)^{exponent}')
print()

expansion = "= "

for t in range(0, terms):
    f = Fraction(1, math.factorial(t))
    list = [exponent - n for n in range(0, t)]
    xv = coefficient ** t
    value = factor * f * prod(list) * xv
    
    if (value == 0):
        break

    sum += value * x

    print("TERM #" + str(t + 1))

    line = ""

    if (f != 1):
        line += format_fraction(f)
    
    for i in list:
        line += f'({format_fraction(i)})'

    line += format_fraction_exponent(xv, t)
    
    if (factor != 1):
        line = f'{factor}({line})'

    print(line)
    term = format_fraction_exponent(value, t)
    print(term)
    if (t > 0):
        expansion += "+"
    expansion += term

    print()

print()
print(expansion)
print()
print(f'{format_fraction(sum)} where x = {x}')
print()