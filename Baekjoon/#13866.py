A=list(map(int, input().split()))
high=max(A)
low=min(A)
team1=high+low
A.remove(high)
A.remove(low)
team2=sum(A)
print(abs(team1-team2))
