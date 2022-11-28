from constants import *


def calculate_tax(an_inc: int, print_stats: bool = True):
    # Adjust personal allowance
    pa = personal_allownace
    if an_inc >= personal_allowance_high_tr:
        pa = 0
    elif an_inc > personal_allowance_low_tr and an_inc < personal_allowance_high_tr:
        tmp_val = pa - (an_inc - personal_allowance_low_tr) / 2
        pa = round(tmp_val, ROUND_VAL)

    total_tax = 0
    tmp_an_inc = max(an_inc - pa, 0)
    for band in bands_2:
        if band[0] > 0:
            taxible = min(band[0], tmp_an_inc)
        else:
            taxible = tmp_an_inc
        tax = round(taxible*band[1]/100, ROUND_VAL)

        if print_stats:
            print(band[2], "tax", tax)

        total_tax += tax
        tmp_an_inc -=taxible 
        if tmp_an_inc <= 0:
            break
        
    return total_tax