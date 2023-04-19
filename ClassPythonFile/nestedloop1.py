"""
# simple  for loop
n = int(input("enter the number: "))

for i in range(1,n+1,1):
    if i%2 == 0:
        print(i , end = ' ')


print()

# while loop 
s = 0
while s<=n:
    if s%2 == 1:
        print(s , end=" ")
    s+=1


print()

# print base for loop
studentNames = ["prakash","kuma","lavanya","manoj"]
for name in studentNames:
    print(name)

"""


#nested loop
# for i in range(1,5):
#     for j in range(1,3):
#         print(i,j)
#     print()


# nested loop2
for i in range(0,6):
    if i%2 == 0:
        for j in range(0,i+1):
            print(j , end=" ")
        print()