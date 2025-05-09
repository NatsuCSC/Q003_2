N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
voter = []

for i in range(N):
    if A[i] == B[i]:
        voter.append(i+1)
else:
    if voter == []:
        print(0)
    else:
        print(*voter)
