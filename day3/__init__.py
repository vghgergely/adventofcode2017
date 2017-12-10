a = 265149

s = int(a**0.5)
if int(s) % 2 != 1:
    s -= 1

d = a - s**2
print(s)
#if d < (s-1):