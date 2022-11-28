from constants import *


def calculate_tax(an_inc: int, print_stats: bool =True):
    # Adjust personal allowance
    if an_inc >= personal_allowance_high_tr:
        bands.pop(0)
        bands.insert(0, (0, 0, 0, "_"))
    elif an_inc > personal_allowance_low_tr and an_inc < personal_allowance_high_tr:
        tmp_val = personal_allownace - (an_inc - personal_allowance_low_tr) / 2
        bands.pop(0)
        bands.insert(0, (0, round(tmp_val, ROUND_VAL), 0, "_"))

    if print_stats:
        print("Anual income:", an_inc)
        print("Personal Allowance:", bands[0][1])
        print("-----------")

    x = an_inc
    total_tax = 0
    done = False
    for band in bands:
        if x > band[1]:
            a = band[1] - band[0]
            t = round(a*(band[2]/100), ROUND_VAL)
            x = x - a
        else:
            t = round(x*(band[2]/100), ROUND_VAL)
            done = True
        total_tax += t
        if band[3] != "_" and print_stats:
            print(band[3], "tax:", t)
        if done:
            return round(total_tax, ROUND_VAL)