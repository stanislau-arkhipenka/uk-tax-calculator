from common import calculate_tax


if __name__ == "__main__":
    for i in range(10, 200):
        an_inc = i* 1000
        tax = calculate_tax(an_inc, print_stats=False)
        print(f"{an_inc},{an_inc-tax},{tax}")