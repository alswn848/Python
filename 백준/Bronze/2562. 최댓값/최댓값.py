a = []
for i in range(9):
    n = int(input())
    a.append(n)

m = max(a)

print(m)
print(a.index(m)+1)