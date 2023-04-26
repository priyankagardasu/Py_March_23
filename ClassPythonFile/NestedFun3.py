def calculator(a,b):
    
    def addition(a):
        return a+10
    
    def mutliplication(a,b):
        return a*b
    
    add_ret = addition(a)
    mul_ret = mutliplication(a,b)
    
    return add_ret + mul_ret
    
ret = calculator(10,30)
    
print(ret)