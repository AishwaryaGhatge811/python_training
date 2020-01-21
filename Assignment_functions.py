#Assignments on functions

  
#Assignment 1
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
--------------------------------------------------------------------------------------------------------

#Assignment 2
def palindrome(str):   
    
    l = len(str)
    print("The Length of the given string is : " ,l)
    for i in range(0, l):  
        if (str[i] != str[l-i-1]): 
            return print("It is not a palindrome")
    return print("It is a palindrome")
  

a = input("Enter the String or number: ")
palindrome(a)

----------------------------------------------------------------------------------------------------------

#Assignment 3
"""def inner(d):
    for k,v in d.items() :
         for key in v :
             print(v[key])


d = {1:{"firstname":{"Aishwarya":"Ghatge"}}}
inner(d)"""

----------------------------------------------------------------------------------------------------------

#Assignment 4
def foo(s,a,b):
    return s(a,b)

def add(a,b):
    c = int(a + b)
    print("Addition of 2 numbers : ",c)

def sub(a,b): return a - b


def multi(a,b): return a * b


def division(a,b): return a / b

def power(a,b) : return a ** b

a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
s = input("Enter the operators(as add,sub,multi,div,power)which you want to peform: ")

if s == "add" :
    foo(add,a,b)
    
elif s == "sub" :
    print("Subtraction of 2 numbers: ", foo(sub,a,b))
    
elif s == "multi" :
    print("Multiplication of 2 numbers: ", foo(multi,a,b))
    
elif s == "div" :
    print("Division of 2 numbers: ", foo(div,a,b))
    
elif s == "power":
    print("Power of given numbers : ", foo(power,a,b))
    
else:
    print("Please enter valid operations")

----------------------------------------------------------------------------------------------------------

#Assignment 5

def sum(l):
    sum = 0
    flag = 0
    for x in l:
        if isinstance(x,str):
            flag = 1
            break
        else:
            sum = sum + x;
    if (flag == 0):
        print("The sum of the elements in the list are : ", sum)
    else:
        print("The given list contains string in it")
        
a = [1,2,3,4,5,"a","G"]
sum(a)








