# def fibonnaci (a):
#     if a <= 1:
#         return a
#     else:
#         return(fibonnaci((a-1) + fibonnaci(a-2)))


def fib (a, b, n, d):
    n -= 1
    c = b+a
    a = b
    b = c
    print(d)
    if (n == 0):
        return 0
    else:
        d.append(c)
        return fib(a, b, n, d)
    
a = [0,1]
fib (a[0],a[1],10, a)


