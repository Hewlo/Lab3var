# Set is the same as Tuple, but it's unordered, unindexed(no index like [1] or [3]) and must NOT HAVE DUPLICATE ELEMENTS.
# Note: Set elements are unchangeable, but you can remove items and add new elements.

# Below demonstrates usage of Set.
def set_basic_usage():
    age = {20,18,30,35,16}
    print(age)

'''
Adding elements to Set
'''
def set_add_elements():
    age = {20,18,30,35,16}
    age.add(40) #adds element 40 into Tuple age.
    print('ADD 40 =', age)

'''
Updating elements from Set
'''
def set_update_elements():
    age = {20,18,30,35,16}
    age.update({40,30,50}) #If there is an existing element (30 in this case), it won't override it and adds only the new elements.
    print('UPDATE {40,30,50} =', age)

'''
Removing elements from Set
'''
def set_remove_elements():
    age = {20,18,30,35,16}
    age.remove(30) #Removes the element 30 in Tuple age.
    print('REMOVE ELEMENT 30 =', age)

'''
Concatenating multiple Sets together

Set provide three methods to join two set together.
They are: union, intersection, difference

Union adds unique elements from first Set to second Set and removes duplicates according to the second Set.
Intersection keeps different elements and discards all unique elements.
Difference retains different elements from two sets.

'''
def set_concatenate():
    age1 = {20,18,30,35,16}
    age2 = {20,18,40,50,60}
    age_union = age1.union(age2)
    print('UNION =', age_union)
    age_intersect = age1.intersection(age2)
    print('INTERSECT =', age_intersect)
    age_difference = age1.difference(age2)
    print('DIFFERENCE =', age_difference)

print('SET\n'
      '------------------')
# Don't forget to comment out the functions below if you are overwhelmed!
set_basic_usage()
set_add_elements()
set_update_elements()
set_remove_elements()
set_concatenate()

print('\n')