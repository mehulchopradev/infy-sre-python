n = int(input('Enter n: '))

# n = 8 - 0 1 1 2 3 5 8 13
a, b = 0, 1
print(a)
print(b)

i = 3
while i <= n:
    c = a + b
    print(c)
    a, b = b, c

    i = i + 1