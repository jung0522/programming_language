class PrintStr:
    def __init__(self):
        self.n = 3;
        self.s = "abc";
        
    def __str__(self):
        return "n = " + str(self.n) + ", s = " + self.s;
        
a = PrintStr()
print(a)