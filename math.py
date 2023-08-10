class Math:
    def __init__(self,A,B):
        self.A = A
        self.B = B   
    def addition(self):
       return self.A+self.B
    def multiplication(self):
       return self.A*self.B
    def division(self):
       return self.A/self.B
    def subtraction(self):
       return self.A-self.B
ex1 = Math(4,8)
print(ex1.addition())
print(ex1.multiplication())
print(ex1.division())
print(ex1.subtraction())