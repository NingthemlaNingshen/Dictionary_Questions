# Write a program to print the top 3 highest values of a given dictionary.

# Input :-
# my_dict = {
#  'a':50, 
#  'b':58, 
#  'c':56,
#  'd':40, 
#  'e':100, 
#  'f':20
#  }
# Visualize
# Output :-
# [58,56,100]

my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
a=[]
max1=0
max2=0
max3=0
for i in my_dict.values():
    if i>max1:
        max1=i
        
    elif i>max2 and max2<max1:
        max2=i
        
    elif  max3<max1 and max3<max2 and i>max3:
        max3=i
a.append(max1)
a.append(max2)
a.append(max3)
print(a)








# Write a program to print the top 3 highest values of a given dictionary.

# Example :-
# my_dict = {
#  'a':50, 
#  'b':58,
#  'c': 56,
#  'd':40,
#  'e':100, 
#  'f':20
#  }
# Visualize
# Output :-
# expect result:-['e','b','c']

my_dict = {'a':50, 'b':58,'c': 56,'d':40,'e':100, 'f':20}
list=[]
i=0
max1=0
max2=0
max3=0
for key in my_dict:
    for value in my_dict:
        if my_dict[key]>max1:
           max1=my_dict[key]
           b=key
        elif max1>my_dict[value]and max2<my_dict[value]:
           max2= my_dict[key]
           e=key
        elif max2>my_dict[value]and max3<my_dict[value]:
           max3=my_dict[key]
           c=key
list.append(b)
list.append(e)
list.append(c)
print(list)