# interest.py
# Calculate 5 years total interest on $1M, given an annual interest
# of two percent.
#
prin = 1.e6
apr = .02
int = prin * apr
print("principal:", prin, "apr:", apr, "interest:", int)

time = 10
int = prin * (1 + apr)**time - prin
print("principal:", prin, "apr:", apr, "time(yr):", time, "interest:", int)

time = 100
int = prin * (1 + apr)**time - prin
print("principal:", prin, "apr:", apr, "time(yr):", time, "interest:", int)