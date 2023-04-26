count = 0
def fun_name(fname,lname): #declaration
    print(fname+' '+lname)
    global count
    count+=1
    print(count)
    fun_name('Akumar' , "K") #recursive call

    
fun_name('Kumar','R') #calling 
print(count)