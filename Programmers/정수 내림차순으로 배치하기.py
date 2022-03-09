def solution(n):
    nlist=list(str(int(n)))
    nlist.sort(reverse=True)
    return int("".join(nlist))
