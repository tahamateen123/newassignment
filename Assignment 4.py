#!/usr/bin/env python
# coding: utf-8

# In[2]:


obj = {
    "first_name" : "Jamil",
    "last_name," : "Ahmed",
    "age":"25",
    "city" : "Karachi"
}

for i in obj.values():
    print(i)

obj.update({"qualification":"Matric"})

print(obj["qualification"])

obj["qualification"] = "Bsc"
print("fter update Qualification ",obj["qualification"])

del obj["qualification"]

print(obj)


# In[3]:


city ={
    "karachi" : {
        "country": "Pakistan",
        "approximate_population":"14.91 million",
        "fact":"Karachi is the Capital of the Pakistani province od Sindh it is the most populous city in Pakistan and fifth-most-populous city proper in the world"
    },
    "Dubai" : {
        "country": "UAE",
        "approximate_population":"3.137 million approx",
        "fact":"Dubai is a city & emirate in the United Arab Emirates known for luxury shopping, ultramodren architecture and a lively nightlife scene"
    },
    "paris" : {
        "country": "France",
        "approximate_population":"2.141 million approx",
        "fact":"Paris, France's capital, is a major European city and a global center for art, fashion gastronomy and culture"
    }
}
    
for i in city.keys():
    print("Name of city is ", i)
    print("Country Name is : " , city[i]["country"])
    print("Approximate population is : " , city[i]["approximate_population"])
    print("Fact of the city is : " , city[i]["fact"])
    print("===================================================================================================================")


# In[4]:


print("Welcome To Movie Theater")
persons = int(input("Enter the no. of Person : "))

total_price = 0

for i in range(1,persons+1):
    age = int(input("Enter The Age Of Person: "))
    if age <= 3:
        print("Your Ticket is Free! Enjoy Your Movie")
    elif age <= 12:
        print("Your Ticket price will be 10$")
        total_price +=10
    else:
        print("Your Ticket price will be 15$")
        total_price +=15

print("Total Amount = ",total_price," $ Enjoy Your Movie")


# In[5]:


def favorite_book(book_name):
    print("One of my favorite books is ",book_name)
    
title=input("Enter The Bookk Title: ")

favorite_book(title)


# In[6]:


import random

random_number = random.randrange(1,30)

flag = False

for i in range(1,4):
    guess = int(input("Guess the number between 1 to 30 : "))
    if guess == random_number:
        flag = True 
        break
    elif guess < random_number:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
        
if flag:
    print("Congratulation you Win!!")
else:
    print("You Loose")
    print("Correct Number is ", random_number)


# In[ ]:




