from fractions import Fraction
import math


def prod(list):
    p = 1
    for x in list:
        p *= x
    return p

def format_fraction(fraction):
    fraction = Fraction(fraction)
    if (fraction.numerator == fraction.denominator):
        return str(fraction.numerator)

    if (fraction.denominator == 1):
        return str(fraction.numerator)

    return f'{fraction.numerator}/{fraction.denominator}'

def format_fraction_exponent(fraction, exponent):
    fraction = Fraction(fraction)

    if (exponent == 0):
        return format_fraction(fraction)
    
    if (exponent == 1):
        return f'({format_fraction(fraction)})x'
    
    return f'({format_fraction(fraction)})x^{exponent}'

# Input binomial in the form
# (constant + x_coefficient * x)^exponent
# Example
# (4 + 3x)^3
constant = Fraction(input("Enter constant: "))
x_coefficient = Fraction(input("Enter x coefficient: "))
exponent = Fraction(input("Enter exponent: "))
terms = int(input("Enter a maximum number of terms: "))
x = Fraction(input("Enter a value for x: "))

# rearrange to the form:
# constant^exponent(1 + x_coefficient / constant * x)^exponent
# by factoring out the constant and applying law of indices (ab)^x = a^x * b^x
factor = Fraction(constant ** exponent)
coefficient = Fraction(x_coefficient, constant)

print()
print("Binomial:")
print(f'({constant} + {x_coefficient}x)^{exponent}')
print()
print("Factorised:")
print(f'={factor}(1 + {coefficient}x)^{exponent}')
print()

def expand(terms, verbose):
    sum = 0
    expansion = "="
    for term in range(0, terms):
    
        one_over_n_factorial = Fraction(1, math.factorial(term))
        n_values = [exponent - n for n in range(0, term)]
        #Add to the sum where x = a value
        term_coefficient = factor * one_over_n_factorial * prod(n_values) * coefficient ** term
    
        #Break if the sequence terminates
        if (term_coefficient == 0):
            break

        sum += term_coefficient * (x ** term)
    
        if (verbose):
            print("TERM #" + str(term + 1))

            print("=", end='')

            if (factor != 1):
                print(f'{factor}(', end='')

            if (one_over_n_factorial != 1):
                print(format_fraction(one_over_n_factorial), end='')
    
            for i in n_values:
                print(f'({format_fraction(i)})', end='')

            print(format_fraction_exponent(coefficient ** term, term), end='')
    
            if (factor != 1):
                print(')', end='')

            print()

        term_string = format_fraction_exponent(term_coefficient, term)
        if (verbose):
            print('=' + term_string)

        if (term > 0):
            expansion += "+"
        expansion += term_string
        print()

    print("Expanded Polynomial: ")
    print(expansion)
    print()
    print(f"Sum (where x = {x}):")
    print(f'={format_fraction(sum)} ({sum.numerator / sum.denominator})')
    print()

#for n in range(1, terms):
expand(terms, True)

