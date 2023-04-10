a = 8
b = 5
c = 7
d = 3

print()
print(a == 8)
print(b == 5)
print(c == 7)
print(d == 3)

print()
print(a > b)
print(a > c)
print(a > d)

print()
print(b < a)
print(b < c)
print(b > d)

print()
print(c < a)
print(c > b)
print(c > d)

print()
print(d < a)
print(d < b)
print(d < c)

print()
res = a > b and a > c
res = a > b and c
print(a > b or c)

print()
res = a > b and a > c and a > d
res = b < a and b < c and b > d
res = d < a and d < b and d < c
res = d < a or b or c
print(d < a or b or c)
print()

print()
a = abs(-8)
print(a)
d = abs(8-5)
print(d)




