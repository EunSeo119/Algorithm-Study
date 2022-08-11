def solution(sizes):
    w_max=0
    h_max=0
    for i in sizes:
        w=i[0]
        h=i[1]
        if w>h:
            w,h=h,w
        w_max=max(w_max,w)
        h_max=max(h_max,h)
    return w_max*h_max
