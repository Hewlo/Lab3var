# Tuple is similar to List but elements inside CANNOT be changed.

# Below demonstrates usage of Tuple.
def tuple_basic_usage():
    age = (20, 18, 30, 35, 16)
    print(age)
    print('POS1 =', age[1])
    print('POS1 TO END =', age[1:])
    print('START TO POS3 =', age[:3])  # Print from the start to pos 2 (says :3 but its EXCLUSIVE, meaning it will STOP at 2 and EXCLUDE 3)
    print('POS2 TO POS4 =', age[2:4])  # Print from pos 2 to 3 (4 IS EXCLUSIVE ALSO!!!) in Tuple age

'''
Tuple concatenation
Yes, even if you can't change the elements inside Tuples, you can still join them together.
'''
def tuple_concatenate():
    age1 = (20, 18, 30, 35, 16)
    age2 = (20, 10, 25, 27, 45, 48)
    age = age1 + age2  # Combine Tuple age1 and age2 into age
    print('CONCATENATE =', age)

'''
Getting min and max values from Tuple
'''
def tuple_min_and_max():
    age1 = (20, 18, 30, 35, 16)
    age2 = (20, 10, 25, 27, 45, 48)
    age = age1 + age2  # Combine Tuple age1 and age2 into age
    min_value = min(age)  # Gets the minimum (smallest) value in Tuple age
    print('MAX AGE VALUE=', min_value)
    max_value = max(age)  # Gets the maximum (largest) value in Tuple age
    print('MAX AGE VALUE=', max_value)

print('TUPLE\n'
      '------------------')
# Don't forget to comment out the functions below if you are overwhelmed!
tuple_basic_usage()
tuple_concatenate()
tuple_min_and_max()

print('\n')