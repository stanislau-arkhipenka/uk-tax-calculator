import sys

personal_allowance_low_tr = 100_000
personal_allowance_high_tr = 125_000

personal_allownace = 12_570
bands = [
    (0, personal_allownace, 0, "_"),
    (12_571, 50_270, 20, "Basic Rate"),
    (50_271, 150_000, 40, "Higher Rate"),
    (150_001, 9999999999, 45, "Additional Rate")
]

an_inc = float(sys.argv[1])

# Adjust personal allowance
if an_inc >= personal_allowance_high_tr:
    bands.pop(0)
    bands.insert(0, (0, 0, 0, "_"))
elif an_inc > personal_allowance_low_tr and an_inc < personal_allowance_high_tr:
    tmp_val = personal_allownace - (an_inc - personal_allowance_low_tr) / 2
    bands.pop(0)
    bands.insert(0, (0, round(tmp_val, 3), 0, "_"))

print("Anual income:", an_inc)
print("Personal Allowance:", bands[0][1])
print("-----------")

x = an_inc
total_tax = 0
done = False
for band in bands:
    if x > band[1]:
        a = band[1] - band[0]
        t = round(a*(band[2]/100),3)
        x = x - a
    else:
        t = round(x*(band[2]/100),3)
        done = True
    total_tax += t
    if band[3] != "_":
        print(band[3], "tax:", t)
    if done:
        print("-----------")
        print("Total anual tax:", round(total_tax,3))
        print("Total monthly tax:", round(total_tax/12,3))
        break

print("-----------")
while True:
    month_in = float(input("Month raw value:"))
    ratio = round(month_in / an_inc, 3)
    mt = total_tax * ratio
    print("Expected tax:", mt)