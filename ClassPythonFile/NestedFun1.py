def outerFunction(text): 
    text = text + " World ,"
    
    def innerFunction(): 
        print(text * 10) 
    
    innerFunction() 
    

print('am in nested functions .... 1 ')
print("name value is", __name__)

if __name__ == '__main__':
    outerFunction('Hey !') 

# direct run __name__ --> __main__
# if you import or run indirectly from other file : __name__ ---> module-name(filename)