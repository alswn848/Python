s = []

for i in range(30):
    s.append(i+1)
for j in range(28):
    n = int(input())
    s.remove(n)

print(min(s))
print(max(s))