#savings_interest.py 11Jan2022  crs, compound interest
# How long till principal rises to target
target = 2000
int_rate = .05
principal = 1000
n_year = 0    # Number of years going
print("principal:", principal, "target:", target,
      "rate:",int_rate)
while principal < target:
    n_year += 1
    interest = principal * int_rate
    principal = principal + interest
    print("principal:", principal, "years:", n_year)    
    
