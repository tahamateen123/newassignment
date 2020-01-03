#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('''The concept of OOP is focuses on creating reusable code. 
This concept is also known as DRY (Don't Repeat Yourself). 
there are four Pillars of OOP which are : 
Inheritance. Encapsulation , Polymorphism and Abstraction''')


# In[2]:


print('''
    OOP based code ko maintain karna asan hota hai 
    OOP based code re-useable hota hai 
    OOP ka code module base hota hai like tree structure ''')


# In[3]:


print('Funtion')
print('''if we have to use a task again and again we write that task in a function and call it when we need it.
    we can pass arguments when calling a funtion if it takes parameters .
    in function you have to pass class attributes as parameters else you can use them in function. ''')
print('Method')
print('''
Methods are same as functions there are very few differece in methods and functions which are:
    1) methods are written in the scope of class
    2) methods take "self" as first parameter , then you know that its a method
    3) self in method takes all the attributes which are defined in class and u can use the attributes 
    in method using self keyword .
    ''')


# In[4]:



print('''
1. Class
2. Object
3. Attribute
4. Behavior


    
    
    OOPS me class ek blueprint ka kaam karti it's like defining data structure using 
    attributes which are basically variables. we define methods and functions in class
    kuch behaviours k liye Example:
                    #class its like a box which have many things inside it, which are  attributes methods functons etc ...
                     class Soccerplayer:
                     #object , class is a blueprint of this object , in this object we have all those things which i defined in class lines 
                         def __init__(self,playername,number,position)
                         
                         #attribute are variables , means address to memory loction of the value which these variables have
                        self.name = playername
                        self.number = number
                        self.position = position
                        
                        
                        #method For defining players who are better in dribbling then most players 
                        #methods can only be defined in the class scope ,its perform a task when we call it.
                        # this method will print the player name which will be passed as argument when calling this method ,
                        #printing is this methods behavior
                        def specialists(self):
                        print(self.name, " is better in dribbble then other soccerPlayers")
                        
                        #function is different then methods you can define funtion in and out of the class
                        def run(name):
                        print(name,"runs fast")
                        
                        
                         ''')


# In[5]:


class Car:
    def __init__(self,model,color,name,company,number):
        self.model=model
        self.color=color
        self.name=name
        self.company=company
        self.number=number
        
    def print_name(self):
        print("this car name is : ",self.name)
            
    def print_UPdatecompany(self):
        self.company="Suzuki"
        print(self.company)
            
    def print_number(self):
        print(self.number)
            
car1=Car('2019','Black','Corolla','Toyota','Abx-2132')
car2=Car('2018','white','VIGO','Toyota','Xayz-212')
car3=Car('2017','Red','land Cruiser','Toyota','cda-132')
car4=Car('2016','Blue','Civic','Honda','zzw-32')
car5=Car('2015','mate Black','City','Honda','Ax-22')



car1.print_name()
car2.print_UPdatecompany()
car2.print_number()


# In[ ]:




