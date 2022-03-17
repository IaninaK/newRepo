h = int(input())
a = int(input())
b = int(input())
rate = a - b
h2 = h - a
day_night = h2 // rate
extra_day = 1 - 0**(h2 % rate)
print(day_night + extra_day + 1)
