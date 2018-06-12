
import argparse
# [ ] The following program generates a staircase character art
# The `size` variable controls the number of steps
# The `base_shape` defines the characters used to generate the art
# Modify the program so the `size` is set as a positional command line argument, and base_shape as an optional 
# command line argument with a default value of `[]`

def gen_stairs(steps, base_shape):
    for row in range(steps):
        for col in range(steps):
            if(col <= row):
                print(base_shape, end = "")
        print()

# Generate a staircase with 6 steps using '[]` as a base shape               
parser = argparse.ArgumentParser()
parser.add_argument("size", type = int, help = "Number of rows should be used to display the character!")
parser.add_argument("-b", "--base_shape", default = '[]', help = "Character used for art!")
arguments = parser.parse_args()

gen_stairs(arguments.size, arguments.base_shape)