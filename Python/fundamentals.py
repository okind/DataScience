#Complete Python Developer in 2022: Zero to Mastery
#-------------------------------------Fundamental data types-------------------------------------
print(2+4)
print(2-4)
print(2*4)
print(type(2/4))
print(type(0.555))
print( 2**3) #=8, power of
print(5//4) # = 1
print(5%4) #= 1, modulo

#math functions
print(round(3.9))
print(abs(-20))

iq=190
print(iq)

#Int variables
user_id = 19
_user_id = 15
a,b,c = 1,2,3
#constant
PI = 3.14

#Augmented assignment operator
some_value=5
some_value= some_value + 2
some_value+= 2

#---------------------------------------String variables------------------------------------------
username='string text'
username="string text"
long_string = '''
Asgaw
Asea
Fawef
'''
#- to use quotes inside string
weather = "It\'s \" kind of sunny"
#- \t is tab
weather ="\t happy"
# - formatted string
name='Olga'
age='36'
print(f'hi {name}. You are old {age}')
#Type conversion
a = str(100)
b=int(a)
new_string='I am happy'
#[start:stop:step_over]
print(new_string[5:10:2])
print(new_string[5:])
print(new_string[-1]) #starts from the end of the string
#reverse the String
print(new_string[::-1])

quote = 'text to format'
print(quote.capitalize())
print(quote.upper())
print(quote.find('to', 0,len(quote)))
print(quote.replace('to', 'ya')) #creating a new string

name = 'Andrei'
is_cool=False
is_cool=True
print(bool(1)) #True

birth_year = input('what year were you born')
print(2019 - int(birth_year))

print('*' * 10)

#------------------------------------------Lists like arrays--------------------------------
li = [1, 2, 3, 4]
li2 = ['f','g','h']
li3 = [1, 2,'a', True]

print(li[0])
#List slicing [start:stop:step_over]
print(li[1:3:1]) #with slicing we create a new list

li[0]='a'
print(len(li))

#Matrix
matrix = [
[1, 2, 3], #0 element
[2, 4, 6], #1 element
[7, 8, 9] #2 element
]
a = matrix[0][2] #=3
print(a)

li = [1, 2, 3, 4]
li.append(5) #insert value in brackets to the end
print(li)
li.insert(3,100) #insert value 100 to position 3
print(li)
li.extend([105,106]) #insert list values to the end
print(li)

new_list=li
li.pop() #removes last elements
print(li)
li.remove(3) #remove value 3
print(li)
li.clear() #remove all elements
print(li)

basket = ['a', 'b', 'c', 'd', 'e']
print(basket.index('a')) #returns index by list_value
print(basket.count('c')) # how many time value occures
basket.sort() #sorts the list
sorted(basket) #produces new array
basket.reverse()
basket[::-1] #same as reverse, creates new list
print(basket[:]) #copy basket

print(list(range(1,100))) # crates a list with elements from 1 to 99
new_sentence = ','.join(['my', 'name', 'is', 'Olga']) #creates string from the list with ','' as a separator
print(new_sentence)

#List unpacking
a,b,c, *other, d=[1,2,3,4,5,6,7,8]
print(a) #equal 1
print(b) #2
print(c) #3
print(other) #[4,5,6,7]
print(d) #8
#Null is absence of value, same is None
value=None
print(value)

#---------------------------Dictionary-key-value data structure--------------------------------------------------
#unordered key-value pair, key must be unique, key-value is a tuple, if key doenst exist it throws an error
#tuple can be used as a key in dictionary, because it is immutable
dictionary = {
'a':10,
(1,2,10):['a','b','x'],
'b':True,
'c':'hellow'
}
print(dictionary['c'])
print(dictionary[(1,2,3)])

print(dictionary.get('b')) #returns None if key does not exist

print(dictionary.get('d', 55)) #return default value if key doesn't exist

dictionary2 = dict(neme='Olga') #another way to create a dictionary2
print(dictionary2)

print('abc' in dictionary) #returns True or false
print(dictionary.keys())
print(dictionary.items())
#dictionary.clear() #in place removes all the elements from the dictionary, empty dictionary returns None
dictionary.pop('a') #removes element, key-value
dictionary.update({'d':'hi hi'}) #can update value by its key, if key doesn't exist add new key-value pair

#---------------------------Tuples---------------------------
#immutable lists, can't modify, change values, can't sort or reverse

my_tuple = (1,2,3,4,5)
print(my_tuple[1])

print(my_tuple.count(1)) #count how many times value appeares in a Tuple

print(my_tuple.index(3)) #get index by value

print(len(my_tuple))
