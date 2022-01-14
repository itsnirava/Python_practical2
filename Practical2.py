#Code written by 20CE072 NIRAVA PARIKH
#AIM: Study and Learn List, Tuple, Set and Dictionary


#Dictionary
print("Dictionary: ")
person={
    'fname':'Nirava',
    'lname':'Parikh',
    'age':'19'
}

#a. Write a Python script to check whether a given key already exists in a dictionary.
print("task a:")
print(person)
for key in person:
    if key=='fname':
        print("fname exists in dictionary person.")

#b. Write a Python script to merge two Python dictionaries.
print("task b:")
student={
    'ID':'20CE072',
    'Department':'CE',
    'Building':'CSPIT'
}
print(person)
print(student)
person.update(student)
print(person)

#c. Write a Python program to sum all the items in a dictionary.
print("task c:")
numbers = {
    'key1': 12,
    'key2': 78,
    'key3': 10
}
print(numbers)
sum=0
for i in numbers.values():
    sum = sum + i
print("Sum = {}".format(sum))

#d. Write a Python script to add a key to a dictionary.
print("task d:")
Sample_Dictionary= { 0: 10,1: 20 }
Sample_Dictionary[2]= 30
print("My Result:{}".format(Sample_Dictionary))
print("Expected Result : {0: 10, 1: 20, 2: 30}")

#e. Write a Python script to concatenate following dictionaries to create a new one.
print("task e:")
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dict4={} 
dict4.update(dic1)
dict4.update(dic2)
dict4.update(dic3)
print("My Result: {}".format(dict4))
print("Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}")
print()


#Tuple
print("Tuple: ")

#a. Write a Python program to create a tuple with different data types.
print("task a:")
tpl = ('Hello',56,'World',12.23)
print(tpl)

#b. Write a Python program to create a tuple with numbers and print one item.
print("task b:")
tpl1 = (12,45,67,32)
print(tpl1[0])

#c. Write a Python program to add an item in a tuple.
print("task c:")
lst = list(tpl) #converting tuple to list
lst.append('Python')
tpl = tuple(lst)
print(tpl)

#d. Write a Python program to convert a tuple to a string.
print("task d:")
tpl2 = ('n','i','r','a','v','a')
print(tpl2)
str = ''.join(tpl2)
print(str)

#e. Write a Python program to find the length of a tuple.
print("task e:")
print(tpl2)
print("Length: {}".format(len(tpl2)))
print()


#Set
print("Set: ")
#a. Write a Python program to add member(s) in a set and clear a set
print("task a:")
set1 = {'10','50','33'}
print(set1)
set1.add('49') #adding an element
print(set1)
set1.clear() #clearing a set
print(set1)

#b. Write a Python program to remove an item from a set if it is present in the set.
print("task b:")
set2 = {23,45,34,77}
print(set2)
try: set2.remove('89') 
except: print("Element does not exist in set1.")

#c. Write a Python program to create an intersection, Union, difference of sets.
print("task c:")
s1 = {'hello','python',23,45}
s2 = {'hello','world',23,56}
print("set1: {}".format(s1)) 
print("set2: {}".format(s2))
s_intersection = s1.intersection(s2)
print("Intersection: {}".format(s_intersection))
s_union = s1.union(s2)
print("Union: {}".format(s_union))
s_difference = s1.difference(s2)
print("Difference(set2-set1): {}".format(s_difference))
s_difference = s2.difference(s1)
print("Difference(set1-set2): {}".format(s_difference))
sys_diff = s1.symmetric_difference(s2)
print("Symmetric Difference: {}".format(sys_diff))

#d. Write a Python program to find maximum and the minimum value in a set.
print("task d:")
s3 = {34,41,67,22}
print(s3)
i=next(iter(s3))
for j in s3:
    if(i<j):
        i = j
print("Maximum Value: {}".format(i))
for j in s3:
    if(i<j):
        j=i
print("Minimum Value: {}".format(j))

#e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
print("task e:")
lst = [2,3,1,1,2,2,4]
print("List: {}".format(lst))
def most_frequent(List):
    counter = 0
    num = lst[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num
print("Most frequent element: {}".format(most_frequent(lst)))
tpl = (1,2,4,3,3,2,3)
print("Tuple: {}".format(tpl))
lst1 = list(tpl)
print("Most frequent element: {}".format(most_frequent(lst1)))
dict = {0:1,1:2,2:2,3:4}
from collections import Counter
list1 = dict.items()
list1 = list(list1)
print(list1)
b = Counter(list1)
print("", b.most_common(1))