personal_allowance_low_tr = 100_000
personal_allowance_high_tr = 125_000

personal_allownace = 12_570
bands = [
    (0, personal_allownace, 0, "_"),
    (12_571, 50_270, 20, "Basic Rate"),
    (50_271, 150_000, 40, "Higher Rate"),
    (150_001, 9999999999, 45, "Additional Rate")
]

ROUND_VAL = 3