"""Write a function which accept list of numbers and
return the prime numbers for that list"""

def primenumber(l):

    prime = []
    for i in l:
        flag = 0
        for j in range(2,i):
            if(i % j == 0):
                flag = 1
                break
        if flag == 0:
            prime.append(i)
    print("The Prime numbers are :" , prime)


lst = []   
n = int(input("Enter number of elements : ")) 
  

for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele) 
      
print("The inserted list of elements are : ", lst) 
primenumber(lst)
