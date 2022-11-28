import sys
from constants import *
from common import calculate_tax


if __name__ == "__main__":
    an_inc = float(sys.argv[1])

    total_tax = calculate_tax(an_inc)

    print("-----------")
    print("Total anual tax:", round(total_tax,3))
    print("Total monthly tax:", round(total_tax/12,3))

    print("-----------")
    while True:
        month_in = float(input("Month raw value:"))
        ratio = round(month_in / an_inc, 3)
        mt = total_tax * ratio
        print("Expected tax:", mt)