
import argparse
from datetime import date

# [ ] Write a program that reads a date from the command line as numbers (month  then day then year),
# if the date entered is in the past, a message saying "The date has passed" should be printed
# if the date is in the future the program should display the number of days remaining from today till that date,
# there should be an optional command line flag that displays the results in total number of seconds instead of days

# help message should look like:
'''
usage: day_counter.py [-h] [-s] month day year

positional arguments:
  month                Month as a number (1, 12)
  day                  Day as a number (1, 31) depending on the month
  year                 Year as a 4 digits number (2018)

optional arguments:
  -h, --help           show this help message and exit
  -s, --total_seconds  Show the time difference in total number of seconds
'''
def days(month, day, year, is_second):
    d = date(day = day, month = month, year = year)
    now = date.today()
    if (now > d):
        print("The date has passed!")
    else:
        diff = d - now
        if (is_second):
            print("Time remaining: ", diff.total_seconds(), " seconds")
        else:
            print("Time remaining: ", diff.days, " days")
            
parser = argparse.ArgumentParser()
parser.add_argument("month", help = "month of the year", type = int)
parser.add_argument("day", help = "day of the month", type = int)
parser.add_argument("year", help = "year", type = int)
parser.add_argument("-s","--total_seconds", help = "Difference in seconds", action = "store_true")

arguments = parser.parse_args()

days(arguments.month, arguments.day, arguments.year, arguments.total_seconds)