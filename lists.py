# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from hmac import new


users = ['Sisovin', 'Viphop', 'Viphea', 'Vuddhi']

data = ['Sisovin', 52, True]

emptylist = []

print('Sisovin' in emptylist) #// Output: False
print('Sisovin' in users) # // Output: True
print(type(users)) # // Output: <class 'list'>
print(type(data)) # // Output: <class 'list'>
print(type[52] in data) # // Output: True
print(users[0]) # // Output: Sisovin
print(users[-2]) # // Output: Viphea
print(users[2]) # // Output: Viphea
print(users[1:3]) # // Output: ['Viphop', 'Viphea']
print(users[0:2]) # // Output: ['Sisovin', 'Viphop']
print(users[1:]) # // Output: ['Viphop', 'Viphea', 'Vuddhi']
print(users[:2]) # // Output: ['Sisovin', 'Viphop']
print(users[:]) # // Output: ['Sisovin', 'Viphop', 'Viphea', 'Vuddhi']
print(users[::2]) # // Output: ['Sisovin', 'Viphea']
print(users[-3:-1]) # // Output: ['Viphop', 'Viphea']

print(users.index('Vuddhi')) # // Output: 3
print(len(data)) # // Output: 3
users.append('Sovanny') # // Output: ['Sisovin', 'Viphop', 'Viphea', 'Vuddhi', 'Sovanny']
print(users) # // Output: ['Sisovin', 'Viphop', 'Viphea', 'Vuddhi', 'Sovanny']

users += ['John'] # // Output: ['Sisovin', 'Viphop', 'Viphea', 'Vuddhi', 'Sovanny', 'John']
print(users) # // Output: ['Sisovin', 'Viphop', 'Viphea', 'Vuddhi', 'Sovanny', 'John']

users.extend(['Robert', 'Smith']) # // Output: ['Sisovin', 'Viphop', 'Viphea', 'Vuddhi', 'Sovanny', 'John', 'Robert', 'Smith']
print(users) # // Output: ['Sisovin', 'Viphop', 'Viphea', 'Vuddhi', 'Sovanny', 'John', 'Robert', 'Smith']

users.extend(data[1:]) # // Output: ['Sisovin', 'Viphop', 'Viphea', 'Vuddhi', 'Sovanny', 'John', 'Robert', 'Smith', 52, True]
print(users) # // Output: ['Sisovin', 'Viphop', 'Viphea', 'Vuddhi', 'Sovanny', 'John', 'Robert', 'Smith', 52, True]

users.insert(0, 'Bob') # // Output: ['Bob', 'Sisovin', 'Viphop', 'Viphea', 'Vuddhi', 'Sovanny', 'John', 'Robert', 'Smith', 52, True]
print(users) # // Output: ['Bob', 'Sisovin', 'Viphop', 'Viphea', 'Vuddhi', 'Sovanny', 'John', 'Robert', 'Smith', 52, True]

users[2:2] = ['John', 'Robert'] # // Output: ['Bob', 'Sisovin', 'John', 'Robert', 'Viphop', 'Viphea', 'Vuddhi', 'Sovanny', 'John', 'Robert', 'Smith', 52, True]
print(users) # // Output: ['Bob', 'Sisovin', 'John', 'Robert', 'Viphop', 'Viphea', 'Vuddhi', 'Sovanny', 'John', 'Robert', 'Smith', 52, True]

users[1:3] = ['Robert', 'Smith'] # // Output: ['Bob', 'Robert', 'Smith', 'Robert', 'Viphop', 'Viphea', 'Vuddhi', 'Sovanny', 'John', 'Robert', 'Smith', 52, True]
print(users) # // Output: ['Bob', 'Robert', 'Smith', 'Robert', 'Viphop', 'Viphea', 'Vuddhi', 'Sovanny', 'John', 'Robert', 'Smith', 52, True]

print("=============================")
users.remove('Bob') # // Output: ['Bob', 'Smith', 'Robert', 'Viphop', 'Viphea', 'Vuddhi', 'Sovanny', 'John', 'Robert', 'Smith', 52, True]
print(users) # // Output: ['Bob', 'Smith', 'Robert', 'Viphop', 'Viphea', 'Vuddhi', 'Sovanny', 'John', 'Robert', 'Smith', 52, True]

users.remove('Robert') # // Output: ['Bob', 'Smith', 'Robert', 'Viphop', 'Viphea', 'Vuddhi', 'Sovanny', 'John', 'Robert', 'Smith', 52, True]
print(users) # // Output: ['Bob', 'Smith', 'Robert', 'Viphop', 'Viphea', 'Vuddhi', 'Sovanny', 'John', 'Robert', 'Smith', 52, True]

print(users.pop()) # // Output: ['Bob', 'Smith', 'Robert', 'Viphop', 'Viphea', 'Vuddhi', 'Sovanny', 'John', 'Robert', 'Smith', 52]
print(users) # // Output: ['Bob', 'Smith', 'Robert', 'Viphop', 'Viphea', 'Vuddhi', 'Sovanny', 'John', 'Robert', 'Smith']

print("=============================")
del users[0] # // Output: ['Smith', 'Robert', 'Viphop', 'Viphea', 'Vuddhi', 'Sovanny', 'John', 'Robert', 'Smith']

print("=====================Delete Data=============================")
# del data
data.clear() # // Output: []
print(data) # // Output: []

users[1:2] = ['Sisovin']
print(type(users)) # // Output: <class 'list'>
users.remove(52)
print(users) # // Output: ['Smith', 'Sisovin', 'Viphop', 'Viphea', 'Vuddhi', 'Sovanny', 'John', 'Robert', 'Smith']
users.sort()
print(users) # // Output: ['John', 'Robert', 'Smith', 'Sisovin', 'Sovanny', 'Viphop', 'Viphea', 'Vuddhi']

users.sort(key=str.lower)
print(users) # // Output: ['John', 'Robert', 'Smith', 'Sisovin', 'Sovanny', 'Viphop', 'Viphea', 'Vuddhi']

nums = [4, 52, 78, 1, 5]
nums.reverse()
print(nums) # // Output: [5, 1, 78, 52, 4]

nums.sort(reverse=True)
print(nums) # // Output: [78, 52, 5, 4, 1]

print("=====================Copy Data=============================")
print(sorted(nums, reverse=True)) # // Output: [78, 52, 5, 4, 1]
print(nums) # // Output: [78, 52, 5, 4, 1]

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy) # // Output: [78, 52, 5, 4, 1]
print(mynums) # // Output: [78, 52, 5, 4, 1]
mycopy.sort()
print(mycopy) # // Output: [1, 4, 5, 52, 78]
print(nums) # // Output: [78, 52, 5, 4, 1]

print(type(nums)) # // Output: <class 'list'>

mylist = list([1, "Neil", True])
print(mylist) # // Output: [1, 'Neil', True]

print("=====================Tuples=============================")
# Tuples
mytuple = tuple(("Sisovin", 52, True))

anothertuple = (1, 4, 2, 8, 2, 2)

print(mytuple) # // Output: ('Sisovin', 52, True)
print(type(mytuple)) # // Output: <class 'tuple'>
print(type(anothertuple)) # // Output: <class 'tuple'>

newlist = list(mytuple) # // Output: ['Sisovin', 52, True]
newlist.append(['Sovanny', 51, True])
newtuple = tuple(newlist) # // Output: ('Sisovin', 52, True, 'Sovanny')
print(newtuple) # // Output: ('Sisovin', 52, True, 'Sovanny')

(one, *two, hey) = anothertuple
print(one) # // Output: 1
print(two) # // Output: [4, 2, 8, 2]
print(hey) # // Output: 2

print(anothertuple.count(2)) # // Output: 3
