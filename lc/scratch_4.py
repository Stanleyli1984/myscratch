__author__ = 'zhongqil'

def b_search(a, l, r, v):
    m = (l+r)/2
    while l < r - 1:
        m = (l+r)/2
        if a[m] < v:
            l = m
        else:
            r = m
    return r

print b_search([0,0,0,0,0,1,1,1],0, 6, 1)