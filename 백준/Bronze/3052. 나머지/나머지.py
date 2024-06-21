a = set()
for i in range(10):
    n = int(input())
    a.add(n%42)

result = 10-len(a)
print(10-result)