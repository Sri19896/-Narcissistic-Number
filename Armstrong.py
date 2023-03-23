def narcissistic(n):
    n = str(n)
    l = len(n)
    s = 0
    for i in n:
        t = int(i) ** l
        s = s+t
    return(s == int(n))


print(narcissistic(7))
