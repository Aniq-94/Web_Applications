# basic building blocks of python programs. Functions
# function can perform some actions on the input: side effect functions
# function that performs calc and returns a value
# function that performs some action w/out changing inputs or returning an output


#def <function name> (<....params>)

#def greet(first_name, last_name):
#    print(f'Hello, {first_name} {last_name}')



#arguments vs parameters
#variables that hold a function input are referred to as arguments
#var: first_name and last_name are arguments to the function greet

#greet('Aniq', 'Ali')


def favorite_fruit(fruits):
    for i in range(len(fruits)):
        if fruits[i] == 'apple':
            fruits[i] = 'APPLE'

fruits = ['apple','mango','banana']
print(fruits) #before function call
favorite_fruit(fruits)
print(fruits) #after fucntion call