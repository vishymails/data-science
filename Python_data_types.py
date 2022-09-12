# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# LISTS

lst = list()


lst = ['Oracle', 'IBM', 'Microsoft', 100, 200, 300, 400]

print(lst)

print(len(lst))

lst.append('Dr.Rao')

lst.append(["Ram", "Raj"])

print(lst)


print(lst[6])

print(lst[1:6])


lst.insert(2, 'Rajesh')

print(lst)


lst.extend([90, 40])


print(lst)


print(lst.pop())


#sum()
#min()
#max()
#index()
#count()


# SETS 


set_var = set()

print(set_var)

print(type(set_var))


set_var={1,2,3,4,5,3,2,1}

print(set_var)


set_var={"Dr.Rao, Ram, Raj"}

print(set_var)

set_var.add("sushanth")


print(set_var)


set1 = {"Dr.Rao", "Ram", "Raj"}
set2 = {"sushanth", "mahanth", "Dr.Rao"}


set2.intersection_update(set1)


print(set2)

set1 = {"Dr.Rao", "Ram", "Raj"}
set2 = {"sushanth", "mahanth", "Dr.Rao"}

print(set2.intersection(set1))

set1 = {"Dr.Rao", "Ram", "Raj"}
set2 = {"sushanth", "mahanth", "Dr.Rao"}

print(set2.difference(set1))

print(set2)


#DICTIONARIES

dict ={}

print(type(dict))


my_dict = {"car1" : "xuv700", "car2" : "dzire", "car3" : "i10"}

print(my_dict)

print(my_dict['car1'])



for x in my_dict :
    print(x)


for x in my_dict.values() :
    print(x)



for x in my_dict.items() :
    print(x)
    
    
my_dict['car4'] = 'Audi 5.0';

print(my_dict)



#NESTED DICTIONARIES


car1_model={'xuv700': 2022}
car2_model={'dzire': 2008}
car3_model={'i10': 2014}


car_type = {'car1' : car1_model, 'car2' : car2_model, 'car3' : car3_model}

print(car_type)


print(car_type['car1'])




#TUPLES



my_tuple = tuple()

my_tuple = ()

print(type(my_tuple))

my_tuple = ("Dr.Rao", "Sushanth", "Mahanth")

print(my_tuple)

#count()
#index()

