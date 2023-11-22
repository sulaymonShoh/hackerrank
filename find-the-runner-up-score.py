n = int(input())
scores = sorted(list(map(int, input().split())))

print(scores[len(scores)-scores.count(max(scores))-1])
