import copy

a = [[1, 2], 2, 3]
b = a
c = [[1, 2], 2, 3]

# print(id(a))
# print(id(b))

print(id(a[0][0]))
print(id(b[0][0]))
print(id(c[0][0]))
