#Fundamental data types
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

#String variables
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

#immutability
