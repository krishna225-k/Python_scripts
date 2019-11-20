''' Source of this code from the youtube channel https://www.youtube.com/watch?v=DEwgZNC-KyE

Preparing for a Python Interview: 10 Things You Should Know

'''

#python flow control
# example for for loop

# for i in range(1,11):
#     print(i)

# while loop

# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1

#if else loop
#a = 30
# b = 20
#
# if a < b:
#     print("{} is less than {}".format(a,b))
#
# elif a == 20:
#     print('{} is equl to {}'.format(a,b))
#
# else:
#     print("{} is greater than {}".format(a,b))

# Preview experiance

# Finding list of files in folder

# import os,glob
#
# os.chdir("C:/Users/Hari/Desktop/")
#
# for file in glob.glob("*.txt"):
#     print(file)

#Fizz Buzz

# for num in range(1,101):
#     if num % 5 == 0 and num % 3 == 0:
#         print('FizzBuzz')
#
#     elif num % 5 == 0:
#         print('Fizz')
#
#     elif num % 3 == 0:
#         print('Buzz')
#
#     else:
#         print(num)

#Fibonacci Sequence
# a, b = 0, 1
#
# for i in range(0,10):
#     print(a)
#
#     a, b = b, a + b
# a is 0
# b is 1
# a + b is 1


# basic data types

# my_list
# my_list = [10,20,30,40,50]
#
# for i in my_list:
#     print(i)

# Tuple
#
# my_tuple = (1,2,3,4,5,6,7,8,9,10)
#
# for i in my_tuple:
#     print(i)

#My dictionaries

# my_dict = {'name':'Bronx','age':'24','occupation':'Corey dog'}
# for key,val in my_dict.items():
#      print("My {} is {}".format(key,val))


#Set

# my_set = {10,20,20,40,50,50,70,90,90,10 }
#
# for i in my_set:
#     print(i)

# list compression
# my_list = [1,2,3,4,5,6,7,8,9,10]
#
# squars = [num * num for num in my_list]
# print(squars)

# Generators
# def fib(num):
#     a, b = 0,1
#     for i in range(0, num):
#         yield "{} : {}".format(i + 1, a)
#         a, b = b, a + b
#
# for item in fib(10):
#     print(item)

#OOPs

# class Person():
#     def __init__(self,name):
#         self.name = name
#
#     def reveal_identity(self):
#         print('My name is {}'.format(self.name))


# class SuperHero(Person):
#     def __init__(self,name,hero_name):
#
#         super(SuperHero, self).__init__(name)
#         self.hero_name = hero_name
#
#     def reveal_identity(self):
#         super(SuperHero, self).reveal_identity()
#         print('....And I am{}'.format(self.hero_name))
#
# Hari = Person('Kumari rajni')
# Hari.reveal_identity()
#
# print('\n')
#
# Vander = SuperHero('kumarn', 'raja')
# Vander.reveal_identity()
#
# # Quetion number 9:
# ''' about working knoweldge on  like python2.7 and python 3.7'''
#
# # knowleged on different technologies
#
# ''' like the git hub version control'''


print('***************')
print('source code is from the whatsup group')
print('***************')
# write a program to wether the sentance contains given string or not

# string = 'this is orange juice'
# for i in range(0,len(string)):
#     if string[i] == 'o':
#         if (string[i + 1]+string[i + 2]+string[i + 3]+string[i + 4]+string[i + 5]) == 'range':
#         #if (string[i + (for i in range(5):)) == 'range':
#
#             print(True)
#             break

# program to convert full name to abbrivations
# fullname = input('Enter your fullname: ')
# index = []
# for i in range(0, len(fullname)):
#     if fullname[i] == ' ':
#         index.append(i)
#
# if len(index) == 0:
#     print(fullname)
#
# if len(index) >= 1:
#     abb = fullname[0] + '. '
#     j = 0
#     while j < len(index) - 1:
#         abb = abb + fullname[index[j] + 1] + '. '
#         j = j + 1
#     abb = abb + fullname[index[j] + 1:len(fullname)]
#     print(abb)

# program to return sum of cube of all numbers smaller than given input values

# number = int(input('Enter number: '))
# i = 0
# cube = 0
#
# while i < number:
#
#     cube =  cube + i ** 3
#     i = i + 1
#     print(cube)

#program to print first three characters with upper case

# string = input('Enter a word: ')
# if len(string) <= 3:
#     print(string.upper())
# else:
#     print(string[:3].upper())

#program to reverse the string
# string = input('Enter a word: ')
# if len(string)%3==0:
#     print(string[::-1])
# else:
#     print(string)

#program to find palindrom numbers

# sing = input('Enter a word: ')
# rev = ''
# for i in sing:
#     rev = i + rev
# if rev == sing:
#     print('Palindrome')
# else:
#     print('Not')

'''Program to test anagromas'''

str1 = input('Enter any string: ')
str2 = input('Enter second string: ')
#print(str1.sort)
if sorted(str1) == sorted(str2):
    print('anagrams')
else:
    print('not')




