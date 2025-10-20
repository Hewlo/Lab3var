# Below demonstrates usage of List.
def list_basic_usage():
    wallet = ['receipt', 5, 0.35, True]  # Store String, Integer, Float and Boolean value
    print(wallet)
    print('POS0 =', wallet[0])  # Get item from position 0
    print('POS3 =', wallet[3])  # Get item from position 3
    print('POS1 TO END =', wallet[1:])  # Print item from pos 1 to the end. (Slice)
    print('START TO POS3 (EXCLUSIVE) =', wallet[:3])  # Print item from starting to the end, EXCLUDING the provided value at the right (3)

'''
Basic manipulation of List (append, assignment, insert and delete)
'''
def list_manipulation():
    wallet = ['receipt', 5, 0.35, True]
    wallet.append('nameCard')  # Adds element 'nameCard' to the end of the List, NOT REPLACE!!!
    wallet.insert(1, 'photo')  # Insert 'photo' inbetween position 1
    print('INSERT PHOTO INBETWEEN POS1 =', wallet)
    wallet[1] = 8  # Assign Integer '8' to wallet's position 1
    print('ASSIGN 1 TO POS1 ELEMENT:', wallet)
    wallet[2:3] = [0.8, False]  # Lab says this replaces index 2:3 with the two values, but it replaces ONLY pos 2 and inserts a new False between pos 3 instead
    print('ASSIGN [0.8, False] TO POS2 AND POS3 =', wallet)
    del wallet[2]  # Delete element at position 2
    print('DELETE POS2 =', wallet)
    wallet.clear()  # Clears EVERYTHING in List wallet
    print('CLEAR WALLET =', wallet)

'''
List sorting
'''
def list_sorting():
    age = [20, 18, 30, 35, 16]
    age.sort()  # Smallest to Largest
    print('AGE SORT =', age)

    country = ['Malaysia', 'Indonesia', 'Philippine', 'Singapore', 'Vietname', 'Thailand', 'Cambodia']
    country.sort()  # A to Z
    print('COUNTRY SORT:', country)

    '''
    By doing explicit attribute assignment, you are only assigning values to that attribute
    regardless of the class constructor's order (__init__(self, a1,a2,a3) etc...).
    Below shows explicit attribute assignment by setting specific attribute reverse to value of True instead of just True.
    '''
    age = [20, 18, 30, 35, 16]
    age.sort(reverse=True) # Reverse numerical order
    print('REVERSED AGE SORT:', age)

    country = ['Malaysia', 'Indonesia', 'Philippine', 'Singapore', 'Vietnam', 'Thailand', 'Cambodia']
    country.sort(reverse=True) # Reverse alphabetical order
    print('REVERSED COUNTRY SORT:', country)

'''
List concatenation (AKA combination in simpler terms)
'''
def list_concatenate():
    age1 = [20, 18, 30, 35, 16]
    age2 = [20, 10, 25, 27, 45, 48]
    age = age1 + age2  # Combines List age1 and age2 into List age
    print('COMBINED AGE LIST=', age)

    country1 = ['Malaysia', 'Indonesia', 'Philippine', 'Singapore', 'Vietname', 'Thailand', 'Cambodia']
    country2 = ['Myanmar', 'Laos']
    country = country1 + country2  # Combines List country1 and country2 into List country
    print('CONCATENATE =', country)

'''
Getting min and max elements from List
'''
def list_min_and_max():
    age1 = [20, 18, 30, 35, 16]
    age2 = [20, 10, 25, 27, 45, 48]
    age = age1 + age2
    min_value = min(age)  # Gets the minimum (smallest) value in List age
    print('MIN AGE VALUE =', min_value)
    max_value = max(age)  # Gets the maximum (largest) value in List age
    print('MAX AGE VALUE=', max_value)

print('LIST\n'
      '------------------')
# Don't forget to comment out the functions below if you are overwhelmed!
list_basic_usage()
list_manipulation()
list_sorting()
list_concatenate()
list_min_and_max()

print('\n')