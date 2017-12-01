#!/usr/bin/env python3
"""
    twentyfour
    ~~~~~~~~~~
    RPN-based solver for twenty-four (and similair) puzzles.

    :copyright: (c) 2017 by Martin Bor.
    :license: MIT, see LICENSE for more details.
"""

import click
import operator
from numbers import Number
from itertools import permutations, chain, product

ops = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul,
       '/': operator.truediv}

priority = {'+': 2,
            '-': 2,
            '*': 1,
            '/': 1}

# Easy:
# numbers = [1, 2, 3, 4]
# target = 24

# Hard, as you need fractions
# numbers = [2, 5, 6, 6]
# target = 17

# numbers = [2,3,5,7]
# target = 41

# numbers = [4, 6, 6, 6]
# target = 24


def precedence(subexpr):
    if isinstance(subexpr, Number):
        return 0
    return max(priority[x] for x in subexpr[1::2])


def parenthesize(subexpr, token):
    if isinstance(subexpr, Number) or \
            precedence(subexpr) > priority[token]:
        return [subexpr]
    return subexpr


def toinfix(program):
    stack = []
    for token in program:
        if isinstance(token, Number):
            stack.append(token)
        else:
            y = parenthesize(stack.pop(), token)
            x = parenthesize(stack.pop(), token)
            stack.append(x + [token] + y)
    assert len(stack) == 1
    return stack[0]


def toinfixstring(expr):
    parts = []
    for subexpr in expr:
        if isinstance(subexpr, list):
            parts.append('(' + toinfixstring(subexpr) + ')')
        else:
            parts.append(str(subexpr))
    return " ".join(parts)


def tostring(s, infix=False):
    """Convert a solution into a string.

    :s: solution list
    :infix: iff true, string format is infix, else postfix
    """
    if infix:
        expr = toinfix(s)
        return toinfixstring(expr)
    return " ".join(map(str, s))


def evaluate(program):
    stack = []
    for token in program:
        if isinstance(token, Number):
            stack.append(token)
        elif token in ops:
            if len(stack) < 2:
                return None
            y = stack.pop()
            x = stack.pop()
            try:
                r = ops[token](x, y)
            except Exception as e:
                return None
            stack.append(r)
        else:
            # not a token we recognize
            raise RuntimeError(f"unknown token '{token}'")
    if len(stack) > 1:
        return None
    return stack[0]


def solve(numbers, target, one=False):
    tried = set()
    solutions = set()
    for s in product(ops.keys(), repeat=len(numbers) - 1):
        for p in permutations(chain(numbers, s)):
            if p in tried:
                continue
            tried.add(p)
            r = evaluate(p)
            if r == target:
                solutions.add(p)
                if one:
                    return solutions
    return solutions


@click.command()
@click.argument('numbers', type=int, nargs=-1)
@click.option('--target', type=int, default=24,
              help="target number.")
@click.option('--infix', is_flag=True,
              help="Print solutions in infix notation")
@click.option('--one', is_flag=True,
              help="Print the first solution and exit.")
def main(target, numbers, infix, one):
    if len(numbers) == 0:
        raise click.UsageError('need at least one number')
    solutions = solve(numbers, target, one)
    if solutions:
        click.echo('solutions:')
        for nr, solution in enumerate(solutions, 1):
            s = tostring(solution, infix)
            click.echo("{:>3}: {}".format(nr, s))
    else:
        click.echo("No solutions found.")


if __name__ == '__main__':
    main()
