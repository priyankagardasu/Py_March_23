def fun(num):
    if(num>0): #base condition
        fun(num-1)
        print(num ,end=" ")
        print("hello" *num)
        

        
#calling function        
fun(4)