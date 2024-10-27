n = 0
def A(I, P):
    global n 
    n = 3
    c = 3
    def B():
        print(I)
        a = 0
        print(a)
        print(c)
        print(n)
    if I > 1:
        P()
    else:
        n = 4
        c = 4
        A(2, B)
def C():
    pass
    
A(1, C)