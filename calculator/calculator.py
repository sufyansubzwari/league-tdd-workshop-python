
class calculator:
    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    def factorial(n):
        if n == 0:
            return 1
        else:
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result