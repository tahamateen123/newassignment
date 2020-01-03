#!/usr/bin/env python
# coding: utf-8

# In[1]:


def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)
number=int(input("Enter a number to calculate the factiorial : "))
print(factorial(number))


# In[2]:


def string_test(s):
    value={"UPPER_CASE":0, "LOWER_CASE":0}
     
    for c in s:
        if c.isupper():
           value["UPPER_CASE"]+=1
        elif c.islower():
           value["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", value["UPPER_CASE"])
    print ("No. of Lower case Characters : ", value["LOWER_CASE"])

print(string_test(s = input('Enter a string value with lower and uppercase letters :')))


# In[3]:


def even_num(l):
    even = []
    for n in l:
        if n % 2 == 0:
            even.append(n)
    return even
print(even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# In[4]:


def is_palindrome(string):
    left = 0
    right = len(string) - 1
    while right >= left:
        if not string[left] == string[right]:
            return False
        else:
            left += 1
            right -= 1
            return True
print(is_palindrome('madam'))


# In[5]:


num = int(input("Enter a number: "))  
  
if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0:  
           print(num,"is not a prime number")  
           print(i,"times",num//i,"is",num)  
           break  
   else:  
       print(num,"is a prime number")  
         
else:  
   print(num,"is not a prime number")


# In[6]:


def shoping(*items):
    for item in items:
        print(" You Slected",item)
        
shoping('mango','banana','apple')


# In[ ]:




