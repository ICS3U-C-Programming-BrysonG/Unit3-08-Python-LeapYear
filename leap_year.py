#!/usr/bin/env python3
# Created By: Bryson Grant
# Date: 10 22, 2026
# This program gets a random year and tells you if it will
# be a leap year or not


def main():
    # Get year from the user
    year_string = input("Enter the year: ")
    try:
        year_int = int(year_string)
        if year_int % 4 == 0:
            if year_int % 100 == 0:
                if year_int % 400 == 0:
                    print("{} is a leap year".format(year_int))
                else:
                    print("{} is not a leap year".format(year_int))
            else:
                print("{} is a leap year".format(year_int))
        else:
            print("{} is not a leap year".format(year_int))
    except:
        print("{} is not a valid year".format(year_string))


if __name__ == "__main__":
    main()
