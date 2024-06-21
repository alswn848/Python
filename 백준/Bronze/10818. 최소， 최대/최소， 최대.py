N = int(input())
A = list(map(int, input().split()))
num = list()
for i in A:
        num.append(i)
print(min(num), max(num))