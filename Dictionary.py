# Dictionary in Python is a collection of key:value pairs which
# unlike other data types, holds only a single value as an element.
# A dictionary is a collection which is ordered, changeable and do not allow duplicates.
# Dictionary are created with curly brackets similar to set but containing key:value pair instead.
# Key must be unique and cannot have duplicates.
# Last key value pair does not have a comma.

# Below demonstrates usage of Dictionary.
def dict_basic_usage():
    age_record = {'M1-John': 20, 'M2-Mary': 18, 'M3-Andy': 30, 'M4-Susie': 35, 'M5-Jay': 16}
    print(age_record)
    print('age_record[\'M1-John\'] =', age_record['M1-John'])  # Finds key 'M1-John' and print its value
    print('DICTIONARY KEYS =', age_record.keys())  # Prints all keys in Dict age_record
    print('DICTIONARY VALUES = ', age_record.values())  # Prints all values in Dict age_record

'''
Adding items into Dictionary
'''
def dict_add_items():
    age_record = {'M1-John': 20, 'M2-Mary': 18, 'M3-Andy': 30, 'M4-Susie': 35, 'M5-Jay': 16}
    age_record['M6-Jack'] = 25 #Adds new key 'M6-Jack' and value 25 into Dict age_record
    print(age_record)

'''
Updating items in Dictionary
'''
def dict_update_items():
    age_record = {'M1-John': 20, 'M2-Mary': 18, 'M3-Andy': 30, 'M4-Susie': 35, 'M5-Jay': 16}
    age_record['M1-John'] = 25  # Finds key 'M1-John' and update its value to 25
    print('UPDATE \'M1-John\' VALUE TO 25 =', age_record)

'''
Removing items from Dictionary
'''
def dict_remove_items():
    age_record = {'M1-John': 20, 'M2-Mary': 18, 'M3-Andy': 30, 'M4-Susie': 35, 'M5-Jay': 16}
    age_record.pop('M3-Andy')  # Remove key 'M3-Andy' and it's value from Dict age_record
    print('DICT POP \'M3-Andy\' =', age_record)
    age_record.clear()  # Clears EVERYTHING in Dict age_record
    print('DICT CLEAR =', age_record)

'''
Accessing keys based on values in Dictionary
'''
def dict_access_keys():
    age_record = {'M1-John': 20, 'M2-Mary': 18, 'M3-Andy': 30, 'M4-Susie': 35, 'M5-Jay': 16}
    key_list = list(age_record.keys())
    print('KEY LIST =', key_list)
    value_list = list(age_record.values()).index(16)  # Set variable value_list with converted List values of Dict age_record to the key that has the value 16 ('M5-Jay')
    print('VALUE LIST =', value_list)
    print('key_list([value_list]) =',
    key_list[value_list])  # prints specific key index of key_list with value_list as the key index

print('DICTIONARY\n'
      '------------------')
# Don't forget to comment out the functions below if you are overwhelmed!
dict_basic_usage()
dict_add_items()
dict_update_items()
dict_remove_items()
dict_access_keys()
