#math in python

# % - is a mod operator which returns the remainder in a division calculation
print(50 % 3)

#to check if a number is odd number we can use mod operator 'number % 2'
#if the remainder is 0, then it is even. if its other than 0, its odd number

print (2 ** 3) #2 to the power of 3

print (2 + 10* 10 +3) # runs in the order of math operation where multiplication happens before addition. 

print((2+10) * (10+3)) #putting brackets ensure math inside brackets gets calculated first, followed by the multiplication

my_income = 100
tax_rate = 0.1

my_taxes = my_income * tax_rate
print(my_taxes)


# Strings in python

print('hello \tworld') # \t denotes tab(forward slash)

print('hello \nworld') # \n denotes new line

print(len('I am Parsa')) #len provides the number of characters in a string including spaces

myString = 'Hello World'

print(myString[7]) #indexing
print(myString[-2]) #reverse indexing. -1 is always the last character
print(myString[2:]) #will start a 2 which is the 3rd char and will go till the end
print(myString[:4]) #will grab chars before index 4 but not including the 4th index
print(myString[2:5]) #starts at index 2 and stops before index 5

#steps
print(myString[::]) #prints out the whole string
print(myString[2:7:2]) #prints starting at index 2, not including index 7 in steps of 2
print(myString[::-1]) #prints everything in reverse order 

#String concatanation
#A
name = "sam"
last_letter = name[1:]
print(last_letter)
print("p" + last_letter)

#B
x = "hello world!"
y = " its beautiful outside!"
print(x+y)
x = x + y
print(x)

#C
letter = 'z' 
print(letter * 10)

#D
#string addition will return concatinated strings NOT an addition of the numbers
print('2' + '3')

#E
print(x.upper())
print(x.capitalize())
print(x.lower())
print(x.split())
print(x.split('i')) #list out of a string

#string interpolation is injecting an f string literal so variables can be accessed directly
print(f'Devs always use {x} in their codes')


#LISTS 
#slicing and indexing works just like strings
#lists can hold different datatypes
#lists are mutable

list = ["string", 7, 10.6]

my_list=['one', 'two', 'three']
another_list = ['four', 'five']
print(my_list + another_list) #generates a new list wihtout muttating the existing lists
new_list = my_list + another_list 
print(new_list)

new_list[0] = "ONE IN CAPS" #mutating a list
print(new_list)

new_list.append('six') #adds to the END of the list
print(new_list)

new_list.pop() #removes the last item from the list 
print(new_list)

print(new_list.pop(0)) #removes specific index 
print(new_list)

#sort
char_list = ['a', 'c', 'b', 'q', 'p', 'r']
num_list = [7, 3, 13, 10]

char_list.sort()
print
num_list.sort()

