n = int(input())
scores = list(map(int, input().split()))
new_scores = []

m = max(scores)

for i in scores:
    new_scores.append(i/m*100)

print(sum(new_scores)/n)