#!/usr/bin/env python3

# Created by Sean McLeod
# Created on December 2020
# This program calculates the square of each integer from 0 to the
#    accepted number


def main():
    # this program calculates the square of each integer from 0 to the
    #    accepted number

    print("This program can calculate the square of each integer from"
          " 0 to the number you type.")
    print("\n", end="")

    # input
    positive_integer_string = input("Enter in a positive integer: ")
    print("\n", end="")

    # process & output
    try:
        positive_integer = int(positive_integer_string)

        if positive_integer >= 0:
            for loop_counter in range(positive_integer + 1):
                squared = loop_counter**2
                print("{0}² = {1}".format(loop_counter, squared))
        else:
            print("This is a negative integer")

    except Exception:
        print("This is not an integer")


if __name__ == "__main__":
    main()
