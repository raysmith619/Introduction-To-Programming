#savings_interest_with_addon.py 11Jan2022  crs, compound interest
# How long till principle rises to target
target = 100000
int_rate = .05
principle = 1000
add_on = 500
n_year = 0    # Number of years going
print("principle:", principle, "target:", target,
      "rate:",int_rate, "add_on:", add_on)
while principle < target:
    n_year += 1
    interest = principle * int_rate
    principle = principle + interest
    print("principle:", principle, "years:", n_year)
    principle += add_on
    
