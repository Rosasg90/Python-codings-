# Josue Rosas 
# Student ID: 877784637 
# Section: 08
# Module 7 Assignment 4

class NumCouple:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2 
    def minimum(self):
        return min(self.num1 ,self.num2)
    def maximum(self):
        return max(self.num1, self.num2)
    def product(self):
        return self.num1 * self.num2

class NumThruple(NumCouple):
    def __init__(self, num1, num2, num3):
        super().__init__(num1, num2)
        self.num3 = num3
    def minimum(self):
        couple_min = super().minimum()
        return min(couple_min, self.num3)
    def maximum(self):
        couple_max = super().maximum()
        return max(couple_max , self.num3) 
    def product(self):
        couple_product= super().product()
        return couple_product * self.num3






couple = NumCouple(4, 7)
print(f"The couples minimum is {couple.minimum()}")
print(f"The couples maximum is {couple.maximum()}")
print(f"The couples product is {couple.product()}")
thruple = NumThruple(3, 5, 2)
print(f"The thruples minimum is {thruple.minimum()}")
print(f"The thruples maximum is {thruple.maximum()}")
print(f"The thruples product is {thruple.product()}")