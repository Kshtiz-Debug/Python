import sys
class prime:
    def __init__(self,number):
        self.number=number

    def check(self):
        for i in range(2,self.number//2):
            if self.number%i==0:
                return "It is not a prime number"
                break
            else:
                return "It is a prime number"

N1=prime(101337133147572225)
x=prime.check(N1)
print(x)



