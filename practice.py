#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

num1=int(input("input first number:"))
num2=int(input("input second number:"))

pro=num1*num2
addition=num1+num2

if pro <=1000:
    print(pro)
    
else:
    print(addition)



# In[ ]:


#Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.


previous_num=0

for i in range(10):
    Addition=previous_num+i
    
    print(f"Current num is: {i} previous num is {previous_num} and sum is{Addition}")
    




# In[ ]:


#Print characters from a string that are present at an even index number


given_str=input("write your string:")

length=len(given_str)

#print(length)


for i in range(0,length):
    if i%2==0:
        print(given_str[i])
        


# In[ ]:


#Remove first n characters from a string

some_str="Saurabhthakar"

length=(len(some_str))

n=int(input("number of initial characters you want to remove:"))


#print(some_str.replace("Sau"," "))


ek_str=some_str[:n]

print(some_str.replace(ek_str," "))


# In[ ]:


#Check if the first and last number of a list is the same

some_list=[1,2,3,4,5,6,7,8,9,6,5,4,3,4,5,6,7]

first_item=some_list[0]

#print(first_item)


last_item=some_list[-1]

#print(last_item)


if first_item==last_item:
    print(f"first element is {first_item} and last element is {last_item} and hence it is equal ")
    
else:
    print(f"first element is {first_item} and last element is {last_item} and hence it is unequal")


# In[ ]:


#Display numbers divisible by 5 from a list

Given=[10, 20, 33, 46, 55,4555,234234,4,54234,242,543,534,53,4532,53,45,35,345,435,345,35,3,45]


for every in Given:
    if every%5==0:
        print(every)


# In[ ]:


#Return the count of a given substring from a string

#Count number of times Ema appeared in the string

stringa="Emma is good developer. Emma is a writer"

num_count=stringa.count("Emma")

print(f"Emma appeared {num_count} times in the string")


# In[ ]:


#Check Palindrome Number


given_str=("567")


empty_str=""

i=0

length=len(given_str)

mod_len=length-1
while i<length:
    
    empty_str=empty_str.join(given_str[mod_len-i])
    
    
    #print(rev_str)
    print(given_str)
    print(empty_str)
    i+=1
    
#reversed the string but not able to get elements in single list or tuple


# In[ ]:


'''Given a two list of numbers,write a program to create a new list such that the new list should contain odd 
numbers from the first list and even numbers from the second list.'''

list1 = [10, 20, 25, 30, 35]
list2=[40, 45, 60, 75, 90]
list3=[]
for every in list1:
    if every%2!=0:
        list3.append(every)
    else:
        pass
    
for nevery in list2:
    if nevery%2==0:
        list3.append(nevery)
    else:
        pass
    
print(list3)


# In[ ]:


#Print multiplication table form 1 to 10


for every in range(1,11):
    print(" ")
    for nevery in range(1,11):
        print(every*nevery, end=" ")
    


# In[ ]:




