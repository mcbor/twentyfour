# Twentyfour

RPN-based solver for twenty-four (and similair) puzzles, inspired by [The Universe of Discourse - Solving twenty-four puzzles](https://blog.plover.com/math/24-puzzle.html).

From a sequence of numbers (say 1, 2, 3, 4) the task is to combine them with simpel arithemtic operation (+, -, *, -) in any order to make the target number, typically 24. For example:

> ((1 + 2) + 3) * 4 = 24

or
	
> 4 * ((2 * 3) * 1) = 24

## Requirements

The following is required to run the script:

 * Python 3 (a recent Python 2 might also work)
 * [Click](http://click.pocoo.org/6)

[Pipenv](https://docs.pipenv.org) is highly recommended to set up a virtualenv and install all the required packages.

## Installation from Source

The script can be run as is, if all the required packages are installed. Otherwise you can install it as an editable package, letting `pip` take care of the dependencies:

	$ pip install -e .
	
Or globally (within or without a virtualenv):

	$ pip install twenty-four

## Usage

Run the script as follows:

	$ twenty-four --target 24 1 2 3 4
 
When no target is given, 24 is assumed. You can give as many numbers as required, but at least one.

By default, the solutions are printed in postfix form. To print them in infix form, use `--infix`, e.g.:

	$ twenty-four --infix 1 2 3 4
	
All possbible solutions are printed by default (which may take a long time, depending on how many numbers are supplied). To print only the first, use `--one`, e.g.:

	$ twenty-four --one 1 2 3 4
 

