def sum(n, x, m):
    for i in range(x):
        n = n + (m  / (2 ** i))
    return n

print(sum(0.25, 0, 0.125))
print(sum(0.25, 1, 0.125))
print(sum(0.25, 2, 0.125))

# print(sum(0.6, 1))
# print(sum(0.6, 2))
# print(sum(0.6, 3))
# print(sum(0.6, 4))
