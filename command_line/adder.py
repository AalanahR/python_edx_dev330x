
import argparse
# [ ] Write a program that reads an unspecified number of integers from the command line,
# then prints out the sum of all the numbers
# the program should also have an optional argument to show the product of the numbers (in addition to the sum)


# help message should look like:
'''
usage: adder.py [-h] [-p] [numbers [numbers ...]]

positional arguments:
  numbers        numbers to be added (or multiplied)

optional arguments:
  -h, --help     show this help message and exit
  -p, --product  show the product of the numbers (in addition to the displayed
                 sum)
'''

def result(lst, product):
    if (product):
        value=1
        for l in lst:
            value *= l
    else:
        value = 0
        for l in lst:
            value += l
    return (value)

parser = argparse.ArgumentParser()
parser.add_argument("numbers", nargs = "*", help = "numbers to be added (or multiplied)", type = float)
parser.add_argument("-p", "--product", action = "store_true", help = "show the product of the numbers (in addition to the displayed sum)")
args = parser.parse_args()

print("Result: ", result(args.numbers, args.product))