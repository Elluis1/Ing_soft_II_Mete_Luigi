class factorial_OOP():
    def __init__(self,min,max,):
        self.min = min
        self.max = max

    def run(min,max):
        if min | max < 0:
            print("Los numeros no pueden ser negativos")
        elif min == 0 & max == 0:
            return 1
        elif min == 0 & max > 0:
            min = 1
            fact = 1
            while(max > 1):
                fact *= max
                max -= 1
            return fact
        else: max == 0 & min > 0
        max = 1
        fact = 1
        while(min > 1):
            fact *= min
            min -= 1
        return fact