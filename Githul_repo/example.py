# Mathimatical operation

# print(50 + 50)
# print(20 + 20)
# print(60 - 50)
# print( -60 + 50)
# print( 50 / 3)
# print( 50 // 3) # floor division
# print(50.0 / 3.0)
# print( 50 / 10)
# print(50 % 10)
# print( 50 * 10)
# print(pow(2,4))
# print(2 ** 4)
'''
Order of operations
PEMDAS
Parenthises,Exponetionsion, multiplicaion, division,addition,
substraction
'''

# print((5+9 - 6 * (10 /20 )))

'''
Python variable
in computer programming, a variable is a storage location
(identified by a memory address) paired by an associated symbolic name
(an identifier)
which contains some know and unknown quantity of information 

'''
# myINt = 9 # = is assingment operator
# print(myINt) # no need to specfiy the data type

# variable not start with number or special character
# variable are case senstviv
# _age = 10 # Valied declearation
# age = .22 # invalid declaration
# 10age = 44 # invalid variable deceleration

# and = 54 # reserverd keyword invalied syntax

# myInt = 10
# print(myInt)
# myFloat = 20.5
# print(myFloat)
# mycomplex = 1j
# print(mycomplex)
# mynum = 5E5
# print(mynum)

# Reassingment
# myString = 'Max'
# print(myString)
# myFloat = myINt
# print(myFloat)

# converion integer vs float

# myFloat = float (myINt)
# print(myFloat)
#
# myINt = int (myFloat)
#
# print(myINt)
# type(myINt)
#
# print('Hello world') # passing arguments
# print(25)
# print(50 * 60)
#
# pass multiple arguments to print

# print('50 * 10 =', 50* 10)
# print('hello', 'world')
#
# x = 50
# y = 10
# print("+**********************")
# print('{0} * {1} = {2}'.format(x, y, x * y))
#
# print('hello','world',sep='^^^^^^^^^^^^^^')
#

# C-style string formatting

'''

%s -- string
%d -- integer
%f -- float
%2f --- limiting decemial point 
'''
# name = 'Max'
# print('hello %s' % name)
#
# age = 22
#
# print('Hello %s ! are %d years old'% (name, age))
# passing arguments inside the tuple

# marks = 92.6
#
# print('Marks = %f' %marks)
#
# marksa = 92.5
#
# print('marksa = %f.2' %marksa)
#
# print('marksa = %.2f' %marksa)

# value = input('enter some value:  ')
# print(value)
#
# value = int(input('enter some value:  '))


# python modules
# import math
# l = math.sqrt(100)
# print(l)

# excuting the python file
# x= float(input('Enter 1st numbaer: '))
# y= float(input('Enter 2st numbaer: '))
# z= float(input('Enter 3st numbaer: '))
#
# print('Sum of three values: ', max(x,y,z))
# print('Press any key to exit')

x = "Hello\" \\world"
y = 'Hello \world'
z = '   Hey dear  '
a = 'Hey, ram, krishna'

print(x)
print(y)

print(x.upper())
print(y.capitalize())
print(x.lower())
print(x[0])
print(x[0:4])
print(z.strip())  # strip function will remove the start/end space

print(z.lower())
print(z.replace('H', 'R '))
print(a.split())  # split into list of worlds
print(z, z, z)

# Boolean values
'''
Boolean values are two constant

True 
False
comparision operator:  

Logical operator: and or not

'''

# if else control loops

# x = - 100
#
# if x != 100:
#     print('x is =')
#     print(x)
#
# if x > 0:
#     print('x is positive')
# else:
#     print('x is negative ')
#
# print('Finished')

# name = input('Enter name :  ')
#
# if name == 'Max':
#     print('Name Entered is : ', name)
#
# elif name == 'Leo':
#     print('Name Entered is : ', name)
# elif name == 'Roy':
#     print('Name Entered is : ', name)
# elif name == 'Eli':
#     print('Name Entered is : ', name)
#
# else:
#     print('The name entered is invalid')

# nested if else condition loops

# x = 10
# if x < 0:
#     print('x is negative')
# else:
#     print('x is positive')
#     if x%2 ==0:
#         print('x is even number')
#     else:
#         print('x si odd number ')

# Nested if condition

# x = 10
# if x > 0:
#     print('x is negative')
#
#     if x % 2 == 0:
#         print('x is even number')
#     else:
#         print('x si odd number ')
#
# else:
#     print('x is positive')

# List in python

'''
is kind collection allows put many kind
ordered set of values which by index which start 0
inside the list called elemenets  
'''

# x = [3,4,5,9,6,47,8,56,]
# print(x)
# x[0]
# x[4]
# y = ['max',1,15,16.4,[3,2]]
# y[0]
# y[3]
# #y[100] # list index out of range
#
# len(x) # lenth of list
# '''
# Inserting elements inside list
# '''
#
# x.insert(2, 'Tom')
# print(x)

'''
remove elements in list
'''
# x.remove('Tom')
# print(x)
# #x.remove(100) # x not in list
#
# x.pop() # remove last element inside list
# print(x)
#
# z = [1,2,5,4]
# del z
#
# z = [1, 2, 5, 4]
# z.clear() # its empty the list
#
# x = [3,4,5,9]
# x.sort() # sorting asending ordre
# x.reverse() # sorting desending order
#
# x.append(10)
# print(x)
#
# x.append(10)
# x.append(10)
# print(x)
#
# s = x.copy()
# print(s)
#
# x.count(10)
# x.count(3)
# x.count(100)

'''
Tuples in python
it's similar like lists 
tuple are immutable. content con't be modify  
'''

x = (1, 2, 3, 4, 5, 8)  # both way we can define the tuples
x1 = 1, 2, 3, 4.5, 6, 7, 'word'
print(x1)
type(x1)
print(x[0])
print(x[4])
# print(x[100])
# x[4] =  9
x.count(8)
len(x)
y = (1, 'max', 1.6)
print(y)
'''
item assigment not possible in tuple
'''

z = x + y
print(z)

a = ('hi') * 5
print(a)

print(max(x))

del z

'''
python set:
No duplicate value
un order set elements 
No indexing 
'''

# A = {1,2,3,4,7,9,2}
# print(A) # remove the duplicate values and then save
# print(len(A))
# print(A.add(10))
# print(A.add(10)) # unique values is add
# print(A)
#
# A.update([12,23,45])# updating multiple values
# print(A)
#
# A.remove(12) # remove
# print(A)
#
# A.discard(23)#does't show error while elements not in the set
#
# print(A)
# print('@@@@@@@@@@@@')
# print(A.pop()) #Remove the random elements
# print(A)
#
# name = {'max','tom','Den'}
# name.clear()
# print(name)
# del name
# #print(name)
#
# name1 = set(('max','tom','Den'))
# print(name1)
#
# z = set([1,2,34.89])
# print(z)
# print(type(z))
#
# #Mathamatical operations
#
# a = set([1,2,3,4])
# b = set([3,4,5,6])
#
# a_union_b = a | b # union of a and b
# print(a_union_b)
# print(a.union(b))
#
# a_inter_b = a & b # interaction of a and b
# print(a_inter_b)
# print(a.intersection(b))
#
# a_differ_b = a - b# difference of a and b
# print(a_differ_b)
# print(a.difference(b))
# print(b.difference(a))
#
# a_symetric_b = a ^ b # symetric difference
# print(a_symetric_b)
# print(a.symmetric_difference(b))
# print(b.symmetric_difference(a))
# set are not indexed
# print(a[1]) set object does not support indexing

'''
Associative  list or map or pair
key value pair
'''
D = {'name': 'max', 'age': 14, 'year': 2004}
print(D)
print(D['name'])
print(D.items())
print(D.keys())
print(D.values())
print(D.get('year'))

d = {'name': 'Tom', 15: 15, 15.1: 15.3, 'Male': True, (2, 3): 5}
print(d)
print(d['Male'])
print(d[(2, 3)])
d['surname'] = 'Trump'
print(d)
print(len(d))

# print(d.pop())
# print(d.popitem())
# print(d.clear())
'''
update method will modify & appending  key, values pair in a dictionary
'''
print(d.update({'name': 'rajan', 'male': 'False', 'Occupation': 'tester'}))
print(len(d))

'''
Python slice and negative index
'''
# a = [0,1,2,3,4,5,6,7,8,9] # list
# b = (0,1,2,3,4,5,6,7,8,9) # tuple
# c = '0123456789' # string
# print(a)
# x = slice(0, 5)
# print(a[x])
# print(a[0:5])# short notation, start(0),end(5)
# print(a[-1])
# print(a[:-3:-1]) # end value (-3)
# print(a[-3::-1]) # start value (-3)
# #print(b[4:])
# #print(b[:4])
# print(c[:])
# print('*************')
# print(c[0:5]) #Here end point won't include in period
# print(a[0:9:2])
# print(a[0:9:3])
# print(a[0:9:4])  # start(0) , end (9) and step(4)
# print(a[::3]) # start and end with three step
# print(c[-1])
# print(c[-4])
#
# print(c[-1]) # negative index from right to left
# print(a[::-3]) # its from right to left
# print(a[:-2:-1])
#
# print(c)
# print(c[-10:-1]) #
# print(c[0:9]) # both are the same result

# Python tutorial for Benginners - while loop

# num = 1
# sum = 0
# print('Enter a Number. Please Enter zero(0) to exit')
# while num != 0:
#     num = float(input('Enter..? : '))
#     sum = sum + num
#     print('sum =', sum)
# else:
#     print('Finished sum')


# i = 0
# #while i < 5:
# while True:
#     print('the value of i is: ',i)
#     i = i + 1 # i += 1
# #    print('Finished while loop')
#
# else:
#     print('Fhinished while loop')
'''
Python tutorial for beginners - for loop
'''
z = [0, 1, 2, 3, 4, 5]
y = (0, 1, 2, 3, 4, 5)
x = {0, 1, 2, 3, 4, 5}
w = '012345'
v = {'name': 'max', 'age': 22}

print(0 in z)
print(0 in y)

for a in z:
    print(a)

print('************')
for b in x:
    print(b)

for c in v.values():
    print(c)

for key, value in v.items():
    print(key, ' ', value)

for x in range(6):  # last value in range it's not print
    print(x)  # it will print 0,1,2,3,4,5 only

'''
Range function will support (start,end,step)
'''

'''
Here else statement will execute after the 
for loop execution was completed
'''
# for x in range(2,30,2):
#     print(x)
#
# else:
#     print("finished")

'''
Python tutorial for beginners - break and continue
'''
a = [0, 1, 2, 3, 4, 5]
# for x in a:
#     if x == 3:
#         break
#     print(x)


print("################")
# i = 0
# while i < 5:
#     if i == 3:
#         break
#     print(i)
#     i += 1

# print('----------------')
#
# for x in a:
#     if x == 2:
#         continue
#     print(x)
#
# print('****************')
'''
Here once of the if statement execution stop
loop will break stop the IF loop
'''

# i = 0
# while i < 5:
#     if i == 2:
#         continue
#     print(i)
#     i += 1 #Iteration statement

print('-------------------')

'''
We can overcome problem with writing the iteration 
statement before if statement

output of below code was 0,1,3,4,5
'''
# i = 0
# while i < 5:
#     i += 1  # Iteration statement
#
#     if i == 2: # 2 won't print
#         continue
#     print(i)


'''
PYthon Functions 

function will complete one task at a time
print() 

Function decleration  

'''
# def nameoffunction(arg1,arg2,arg3):
#     print()
# print('-----Functions-------')
# def sum(arg1, arg2):
#
#     if type(arg1) != type(arg2):
#         print('Please give the args of same type')
#         return
#     print(arg1 + arg2)
#     return
# print('Function calling')
# a = sum(15, 60)
# print(a)
# print(sum('Hello','world'))
# print(sum(15.23,46.12))
# print(sum('hello',15)) #can only concatenate str(not 'int) to str
#
# print('==============')
# print('Second example')
# print('-------------')
'''
We can use defult values to argument passed
'''
# def student(name='Unknow_name',age = 0):
#     print('name',name)
#     print('age',age)
#
# student('Rajan',25)
# student('Puja')

'''
python tutorial for Beginners 
default arguments *args and *kwargs

*args --- assig multiple arguments(its support int,string)
    it's taking values as TUPLE


**kwargs --- assign multiple args as key pair manner(engish=35)
    it's take as dictionary


'''
print('Example for multiple argument passing (*args)')

# def Student(name,age,*marks):
#     '''
#     Note: Here in function only one (*args) should be
#     decleared
#     '''
#     print('name',name)
#     print('age', age)
# #    print('marks', marks)
#     for x in marks:
#         print(x)
# Student('juliana',35,56,89,90,100)
#
# print('____passing string as *args___________')
# def Student1(name,age,*friends):
#     '''
#     Note: Here in function only one (*args) should be
#     decleared
#     '''
#     print('name',name)
#     print('age', age)
#     print('marks', marks)
#     for friend in friends:
#         print(friend)


# print('******calling function**********')
# Student1('rama',36,'puja','kammala')
#
# print('=======**kwargs======explainstion')
#
# def SchoolStudent(name,age,**marks):
#     '''
#     Here with help of **kwargs. we can pass the key pair
#     argument of multiple one at time
#     **kwargs --- passing values as DICT{}
#     '''
#     print('name',name)
#     print('age', age)
#     print('marks', marks)
#     for key,value in marks.items():
#         print(key,' ', value,'\n')
#
# SchoolStudent('Samul',20,english=56,chemistray=44,physics=95)


print('*****OOPS*******', sep='\n')
'''
Objective oriented programming

class --blue print
method -- its a function which is inside the class
instance --
attributes -- (data members or attributes)

Data and method -- not separete in OOPs
'''

# class Car:
#     pass
# '''
# empty class
# '''
# #Attributes
# ford = Car()
# honda = Car()
# audi  = Car()
#
#
# ford.speed = 200
# honda.speed = 220
# audi.speed = 250
#
# ford.color = 'red'
# ford.color = 'blue'
# ford.color = 'black'
#
#
# print(ford.speed)
# print(ford.color)

# Changing the attributes values

# ford.speed = 300
# ford.color = 'Blue'
#
# print('\n')
#
# print(ford.speed)
# print(ford.color)
#
# print('*******new example****')

# class Rectangle:
#     pass
#
# rect1 = Rectangle()
# rect2 = Rectangle()
#
# rect1.height = 20
# rect2.height = 30
#
# rect1.width = 20
# rect2.width = 30
#
# print(rect1.height * rect1.width)
# print(rect2.height * rect2.width)

'''
How to use the __init__ method in python class

with self word
'''
# #class Car:
#     def __init__(abc,speed,color):# used as constructer
#         print(speed)
#         print(color)
#         abc.speed = speed
#         abc.color = color
#         print('the __init__ is called')
# #Attributes

# passing values to agruments
# ford = Car(200,'red')
# honda = Car(220,'blue')
# audi  = Car(250,'yellow')

# ford.speed = 200
# honda.speed = 220
# audi.speed = 250

# ford.color = 'red'
# ford.color = 'blue'
# ford.color = 'black'


# print(ford.speed)
# print(ford.color)

# Changing the attributes values

# ford.speed = 300
# ford.color = 'Blue'

# print('***Rectangle class')
#
# class Rectangle:
#     def __init__(self,height,width):
#         self.height = height
#         self.width = width
#
#
# rect1 = Rectangle(75,98)
# rect2 = Rectangle(20,40)
#
# rect1.height = 20
# rect2.height = 30
#
# rect1.width = 20
# rect2.width = 30

# print(rect1.height * rect1.width)
# print(rect2.height * rect2.width)

print('Brief explains')

# class Hello:
#     def __init__(self): pass
#     def __init__(self, name): pass
#
# hello = Hello('name')

'''
Here the below example reveals that 
in python class __init__ method will executes 
from top to bottom i.e in first line instance method

attributes igonre
def __init__(self, name): pass
def __init__(self): pass
as per theory last __init__method only valid

class Hello:
    def __init__(self, name): pass
    def __init__(self): pass
hello = Hello('name')

so in the second method their no arguments 
its reflect error  

TypeError: __init__() takes 1 positional argument but 2 were given
'''

# class Hello:
#
#     def __init__(self, name='max'):pass
#
# hello = Hello()
# hello = Hello('name')
#
# print('************8')
# class Hello:
#
#     def __init__(self, *args):pass
#
# hello = Hello()
# hello = Hello('name','yellow','greed')
#
# print('-------------')
# class Hello:
#
#     def __init__(self,*args, **kwargs):pass
#
# hello = Hello()
# hello = Hello('name','latha','friend','sujatha')

'''
Passing static values to the attribute without 
defining it in (__init__) instance method

Below example will explain about that
'''

# class Hello:
#     def __init__(self,name):
#         self.name = name
#         self.age = 20
#
# hello = Hello('name')
# print(hello.name)
# print(hello.age)

print('*************')
'''
Python encapsulation 
Avoid the tampering out code by the third person 


Implementing encapsulation
==========================

if you want to implement the encapsulation 
we have to create function called (__set__) and (__get__)


'''
# class Car:
#     def __init__(self,speed,color):
#         self.speed = speed
#         self.color = color
#
#
#     def set_speed(self,value):
#         self.speed = value
#
#
#     def __get_speed(self):
#         return self.speed


# ford = Car(200,'red')
# honda = Car(220,'blue')
# audi = Car(250,'black')
#
#
# ford.set_speed(300)
# ford.speed = 400

# By these we can't stop the tamparing
# not passible to make private data
# print(ford.speed)
# print(ford.color)

'''
BY using single & double underscore we achive the private method

self._b = 10 
self.__c (  ) make our attribute as private 

'''

# class Hello:
#     def __init__(self,name):
#         self.a = 10
#         self._b = 20 # technique to implement the encapsulation
#         self.__c = 40
#
#
# hello = Hello('name')
#
# print(hello.a)
# print(hello._b)
# print(hello.__c) # with help of these we make attributes as private


'''
Implementing the private method in class 
'''
# class Car:
#     def __init__(self,speed,color):
#         self.__speed = speed
#         self.__color = color
#
#     def set__speed(self,value):
#         self.speed = value
#
#     def get__speed(self):
#         return self.__speed
#
#     def set__color(self,value):
#         self.__color = value
#
#     def get__color(self):
#         return self.__color
#
# ford = Car(200,'red')
# honda = Car(220,'blue')
# audi = Car(250,'black')
#
# ford.set__speed(300)
# ford.__speed = 500
# ford.__color = 'mejento'
#
# print(ford.get__speed())
# print(ford.get__color())

'''
Here conclusion was the if you define the 
attributes with (double under score (__) then can't 
change the attributes values

additionally you have to define the functions 

def set__(self,value)
    self.__attributename = values
def get__(self) 

    :return name of attributes

'''

# By these we can't stop the tamparing
# not passible to make private data
# print(ford.__speed)
# print(ford.__color)


'''
We have to implement the private method to the
rectangle python file
'''

# class Rectangle:
#     def __init__(self, height, width):
#         self.__height = height
#         self.__width = width
#
#     def set__height(self, height):
#         self.__height = height
#
#     def get__height(self):
#         return self.__height
#
#     def set__width(self,width):
#         self.__width = width
#
#     def get__width(self):
#         return self.__width
#
#     def area(self):
#         return self.__height * self.__width
#
# rect1 = Rectangle(30, 52)
# rect2 = Rectangle(80, 50)
#
# print(rect1.area())
# print(rect2.area())

'''
private methods in python 

Following the above example we can't 
access the private variable out side of the functions

For overcoming the above problem By 
defining the Private & public variables in the 

function called PUBLIC_METHOD(SELF)
'''
# class Hello:
#     def __init__(self,name):
#         self.a = 10
#         self._b = 20
#         self.__c = 30
#
#     def public_method(self):
#         self.a
#         self._b
#         print(self.__c)
#         print('public')
#
# hello = Hello('name')
# print(hello.a)
# print(hello._b)
# print(hello.public_method())

'''
explaining the private methods

'''

# class Hello:
#     def __init__(self,name):
#         self.a = 10
#         self._b = 20
#         self.__c = 30
#
#     def public_method(self):
#         self.a
#         print(self.__c)
#         print('public')
#
#         self.__private_method()
#
#     def __private_method(self):
#         print('private')
#
# hello = Hello('name')
# print(hello.a)
# print(hello._b)
# hello.public_method()


print('Python inheritance', '\n')

'''
Python class inheritence 
parent class: -- super class
child class: -- sub class
'''

# class Polygon:
#     __width = None # Both are private members
#     __height = None

# ''''
# Here __private method won't access out side of function
# if you want to access __private method. we need to create
# other method Namely(def __set(), def __get())
# '''
#     def set_values(self, width, height):
#         self.__width = width
#         self.__height = height
#
#     def get_width(self):
#         return  self.__width
#
#     def get_height(self):
#         return  self.__height
#
#
# class Rectangle(Polygon):
#     def area(self):
#       return self.get_width() * self.get_width()
#
#
# class Triangle(Polygon):
#     def area(self):
#         return self.get_width() * self.get_height() / 2
#
#
# rect = Rectangle()
# tri = Triangle()
# rect.set_values(20, 30)
# tri.set_values(10, 20)
#
# print(rect.area())
# print(tri.area())

'''
Python Modules
module is nothing but python file
create our own module
'''
# import math

print('*******Python super()***********')
'''
here the inheritance from parent member to child class 
with help of super class or name of the superclass along with
init method 

ex: super().__init__('member value')

if importing more than one member we have to import 
each member of each parent class

example: parent.__init__(self,'value of  member')
         parentclassname.__init__(self, 'value of member'
Method resolution order: (__mro__)
it's dependent on order importing parent class inside of 
child class
'''

# class Parent:
#     def __init__(self,name):
#         print('Parent __init__',name)
#
# class Parent2:
#     def __init__(self,name):
#         print('Parent2 __init__', name)
#
# #class Child(Parent,Parent2):
# class Child(Parent,Parent2):
#     def __init__(self):
#         print('Child __init__')
# #        super().__init__('name')
#         Parent2.__init__(self,'max') # importing parent member
#         Parent.__init__(self,'Hari')# importing another parent member
#
#
# child = Child()
# print(Child.__mro__)

'''
Concept of aggregation and composition

Aggregation : 
============
key word representation is HAS A
Here if want to import functionality with out the super() and
parent and child relationship.

we can share the member variable with help of composition 

composition is delegation of responsibily between the classes 

special praperties of aggregation:
i) class objects independent 
ii) Associated class have uni directional association


Composition:
===========
here both are the class interdependent 
members variable of classes are dependent each other  

key word representation is part of A

'''
# class Salary:
#     def __init__(self, pay, bonus):
#         self.pay = pay
#         self.bonus = bonus
#
#     def annual_salary(self):
#         return (self.pay * 12) + self.bonus


# class Employee:
#     def __init__(self,name,age,pay, bonus):
#          self.name = name
#          self.age = age
#          self.obj_salary = Salary(pay, bonus)
#
#     def total_salary(self):
#         return self.obj_salary.annual_salary()


# emp = Employee('max', 25, 15000, 10000)
# print(emp.total_salary())
#
# print('$$$$$$$ __Aggregation__$$$$$$$$$')

# class Salary:
#     def __init__(self, pay, bonus):
#         self.pay = pay
#         self.bonus = bonus
#
#     def annual_salary(self):
#         return  (self.pay * 12) + self.bonus

# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.obj_salary = salary
#
#     def total_salary(self):
#         return  self.obj_salary.annual_salary()
#
#
# salary = Salary(15000,10000)
# emp = Employee('tom', 25, salary)
# print(emp.total_salary())


print('@@@@@__Abstract class__@@@@@@@@@2')
'''
In some cases we must implemenet functionality 
someother class to completing the tasks 

i.e we have to abstract the main class to sub class. we can achive that by 

'''

# from abc import  ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self): pass
#
#     @abstractmethod
#     def perimeter(self): pass
#
#
# class Square(Shape):
#
#     def __init__(self, side):
#         self.__side = side
#
#     def area(self):
#         return self.__side * self.__side
#
#     def perimeter(self):
#         return self.__side * 4

# squre = Square(5)
# print(squre.area())
# print(squre.perimeter())


print('*****Exceptions**********')

''''
Here when python struck with invalid code 
it will simply stop the entire excution flow 

To overcome the above issue we have to implement the 
functions 

try: 
testing statements

except:

Error displaying statmenets 
Error revealing statements 
'''
# result = None
# a = input('Number 1:' ) # type error
# #a = float(input('Number 1:' )) #zerodivisonerror
# b = float(input('Number 2:' ))
#
# try:
#     result = a / b
# # except:
# #     print('float zero division error')
#
# # write generic exception class
#     '''
# Here Exception in except is the base class
#
# As it is Base class it can capature the all type of
# error
#
# Are Else we have to individually mentioned one by one
# each error
#     '''
#
# # except Exception as e:
# #     print('Error =', e)
#
# # except Exception as e:
# #     print('Error =', type(e))
#
#
# except ZeroDivisionError as e:
#     print('Error =', type(e))
#
# except TypeError as e:
#     print('Type Error :',type(e))
#
#
# print('Result =', result)
# print('End')

print("More about try/except/else/finally")

print('\n', '\n')
'''
More about the 

Try: testing code

Except:
 capaturing type of errors 
 Revealing about error information to developer 

else:

If except statement not excuted, next else statemenet will 
excute

Modifiying the code as after analysing the try block
Along  with except statemenet only else statement should use

Finally:
It will always excute,
irrespective of try/exception 

while opening closeing files and closing sql database

reconnection of data base file 

'''

# result = None
# a = float(input('Number 1: '))
# b = float(input('Number 2: '))
#
# try:
#     result = a / b
#
# except ZeroDivisionError as e:
#     print('Zerodivisionerror ',type(e))
#
# else:
#     print('__else__')
#
# finally:
#     print('__finally___')
#
# print('Resutl = ',result)
# print('End')


print('^^^^Python raise execption^^^^^^^^')
'''
Python raise exceptions
throw/raise the exceptions
'''

# class CoffeeCup:
#     def __init__(self, temperature):
#         self.__temperature = temperature
#
#     def drink_coffee(self):
#         if self.__temperature > 85:
#         #    print('Coffee Too Hot')
#             raise Exception('Coffee Too Hot')
#
#         elif self.__temperature < 65:
#         #   print('Coffee Too cold')
#         #    raise Exception('Coffee Too Cold')
#             raise ValueError('Coffee Too Cold')
#         else:
#             print('Coffee is ok Drink')
#
# cup = CoffeeCup(50)
# #cup = CoffeCup(115)
# print(cup.drink_coffee())


'''
Custom exception class
'''

# class CoffeeTooHotException(Exception):
#     def __init__(self,msg):
#         super().__init__(msg)


# class CoffeeTooColdException(Exception):
#     def __init__(self,msg):
#         super().__init__(msg)
#
#
# class CoffeeCup:
#     def __init__(self, temperature):
#         self.__temperature = temperature
#
#     def drink_coffee(self):
#         if self.__temperature > 85:
#             raise CoffeeTooHotException('Coffee Temperature:' + str(self.__temperature))
#
#         elif self.__temperature < 65:
#             raise CoffeeTooColdException('Coffee Too cold' + str(self.__temperature))
#
#         else:
#             print('Coffee ok to drink')
#
#
# cup = CoffeeCup(100)
# cup.drink_coffee()

'''
Importance of if __name__ = "__main__"

above function will limit the functionality or rest code which
in the importing file

instead of printing respones of the importing file code 
it will print only the Name of the imported module

In the same folder i created filename called add.py 
just import that file execute 
'''

# import add
#
# print(add.add(6, 7))


'''
Python reading and writing the file
'''

# fh = open('demo.txt','w')
# #fh.writelines('I wrote text data to file')
#
# for i in range(10):
#     fh.write('this is line no %d \n' %(i + 1))
#
# fh.close()
#
print('__File operation with append mode__')
# fh = open('demo1.txt','a')
# fh.writelines('I wrote text data to file')

# for i in range(10):
#     fh.write('this is line no %d \n' %(i + 1))
#
# fh.close()

print('*** mode (m+) ***')

fh = open('demo2.txt', 'w+')
# fh.writelines('I wrote text data to file')

for i in range(10):
    fh.write('this is line no %d \n' % (i + 1))

fh.close()

'''
Implemenet the try/finally
'''

fh = open('demo.txt', 'w')

# fh.writelines('I wrote text data to file')


# try:

#     for i in range(10):
#         fh.write('this is line no %d \n' %(i + 1))
#
# finally:
#     fh.close()

'''
Above the code written as well 
'''

# with open('demo.txt','w') as fh:
#
#     for i in range(10):
#
#         fh.write('This is line no {} \n'.format(i))

'''
Reading files in python 
'''
# fh = open('demo.txt')
# print(fh.read())
#
# fh.close()

fh = open('demo.txt')
# print(fh.read())
# print(fh.readline(5))
# print(fh.readlines()[4])
# print(fh.readlines()[5])


# for line in fh:
#     print(line)
#     print(len(line))# count the number characters in line
#     print(line.split()) # split the words in each line
#     print(len(line.split()))#count the words in each line
# fh.close()
#
#
# with open('demo.txt','r') as fh:
#     for line in fh:
#         print(line.split())


'''
working with JSON data in python
Java script object notation
'''
# import json
#
# a = {
#     'name':'max',
#     'age':22,
#     'marks' : [90,23,24,45],
#     'pass': True
# }
# print(json.dumps(a))
#
# print('\n', 'Data types which was supported by json')
#
# print(json.dumps({'name':'max','age':25}))
# print(json.dumps(['1','2']))
# print(json.dumps(('1', '2')))
# print(json.dumps('Hello world'))
# print(json.dumps(100))
# print(json.dumps(15.56))
# print(json.dumps(False))
# print(json.dumps([True]))
# print(json.dumps(None))
#
#
# a = {
#     'name':'max',
#     'age':22,
#     'marks' : [90,23,24,45],
#     'pass': True,
#     'object': {
#         'color':('red','blue')
#     }
# }
#
# with open('demo.json','w') as js:
#     js.write(json.dumps(a, indent=5))
#
# print(json.dumps(a, indent=5, separators= ('.', ' =')))

# print('\n', 'Read json file')
#
# import json
#
# with open('demo.json','r') as fh:
# #    print(fh.read())
#
# # assing json file content to variable
#     json_str = fh.read()
#     json_value = json.loads(json_str)
#     print(type(json_str))
#     print(type(json_value))
#     print(json_value['name'])
#     print(json_value['pass'])

'''
Itertoration in python
it is an object which can be interate over collection of elemenets inside a datatype
python have two type of iterations
i) __iter__()
ii) __next__()

'''

# class ListIterator:
#     def __init__(self, list):
#         self.__list = list
#         self.__index = -1
#
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.__index += 1
#
#         if self.__index >= len(self.__list):
#             raise StopIteration
#
#         return self.__list[self.__index]


# a = [1,2,3,6,5,4]
# mylist = ListIterator(a)
# it = iter(mylist)

print('\n', 'iteration')

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# insted of above interation we can you the for loop
# for i in it:
#     print(i)

'''
Python generators
Generators: it is the simple way of creating iterators

Generators automatically raise the exceptions
'''

# def my_func():
#     yield 'a'
#     yield 'b'
#     yield 'c'
#
# x = my_func()
#
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

print('\n', 'yield functionality')

# def my_yfunc():
#
#     n = 1
#     print('===========',n)
#     yield n
#
#     n += 1
#     print('----------',n)
#     yield n
#
#     n += 1
#     print('-----------',n)
#     yield n

# z = my_yfunc()
#
# print(next(z))
# print(next(z))
# print(next(z))

# print('\n', 'yield functionality with for loop')

# def myf_func():
#     for i in range(5):
#
#         print('----------',i)
#         yield i
#
# y = myf_func()
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
# #print(next(y))

'''
Generator function
'''
# def iter_iterator(list):
#     for i in list:
#         yield i
#
# a = [1,2,3,6,5,4]
# mylist = iter_iterator(a)
# print(next(mylist))
# print(next(mylist))
# print(next(mylist))
# print(next(mylist))
# print(next(mylist))

# print('\n', 'both above and below function have same')
#
# for x in mylist:
#     print(x)

# print('\n')
# print('\n')
# print('\n')

'''
command line arguments in python
it will be pass the arguments to python command line 
'''

# import argparse
#
# if __name__ == '__main__':
#     # initailize the parser
#     parser = argparse.ArgumentParser(
#         description=' my script path'
#     )

# add the parameters positional/argmunts

# parser.add_argument('num1', help='number1: ', type=float)
# parser.add_argument('num2', help='number2: ', type=float)
# parser.add_argument('operation', help='operator')

# writing the postional arguments

# parser.add_argument('--num1', help='number1: ', type=float)
# parser.add_argument('--num2', help='number2: ', type=float)
# parser.add_argument('--operation', help='operator', default='+')


# optional parameters for short notation

# parser.add_argument('-n', '--num1', help='number1: ', type=float)
# parser.add_argument('-i', '--num2', help='number2: ', type=float)
# parser.add_argument('-k', '--operation', help='operator', default='+')
#
# # parse the arguments
# args = parser.parse_args()
# print(args)
#
# results = None
#
# if args.operation == '+':
#     results = args.num1 + args.num2
#
# if args.operation == '-':
#     results = args.num1 - args.num2
#
# if args.operation == '*':
#     results = args.num1 + args.num2
#
# if args.operation == 'pow':
#     results = pow(args.num1,args.num2)
#
#
# print('Results: ', results)


'''
Python lambda, map, reduce, filter functions 
lamdba x: x * 2 ---- its have variable and body 
lambad : in some situation we have to pass the function as argument(variable) in that 
circumstance we have use lambda function

MAP(function, iterable value)



'''
#
# def double(x):
#     return  x * 2
#
# def add(x, y):
#     return x + y
#
# def product(x, y , z):
#     return x * y * z
#
#
# a = lambda x: x * 2
# b = lambda x, y : x + y
# c = lambda x, y, z : x * y * z
#
# print('double: {} add: {} product: {}'.format(a(10),b(10,20),c(10,20,30)))
#
#
# # Demonstating the map functions
# mylist = [1,2,3,4,5,6]
#
# a = map(lambda x: x * 2,mylist)
# print(list(a))
#
# mylist = [1,2,3,4,5,6]
# mylist1 = [6,5,4,3,2,1]
#
# b = map(lambda x,y: x + y, mylist,mylist1)
#
# print(list(b))
#
# c = filter(lambda x: x%2==0,mylist)
# print(list(c))
#
# d = filter(lambda x: True if x >= 5 else False, mylist)
#
# print(list(d))
#
# from functools import reduce
#
# e = reduce(lambda x, y : x + y, mylist)
# e_sub = reduce(lambda x, y : x - y, mylist)
# e_mul = reduce(lambda x, y : x * y, mylist)
# print(e)
# print(e_sub)
# print(e_mul)

'''
Neasted functions && closere 

here outer function and inner functions 
'''

# def outerfun(text):
#     def innerfun():
#         print(text)
#     innerfun()
#
# outerfun('hello')
#
# print('\n')
#
#
# def pop(list):
#     def get_last_item(my_l):
#         return my_l[len(my_l) - 1]
#
#     list.remove(get_last_item(list))
#     return list
#
# a = [8,3,4,5,6,9]
#
# print(pop(a))
# print(pop(a))
# print(pop(a))

'''
Python closers

'''
# def outerfun(text):
#     def interfun():
#         print(text)
#     return interfun
#
# a = outerfun('hello')
# print('calling the outerfunction along with innerfunction')
# print(a())
# print('\n', 'Only calling the outerfun()')
# a()

'''
See here the magic 
even if you delete the value outer function the innerfunction can hold 
values 

Closers will remember the values which is outside the functions as well 
NOte: Here at return statement you should not writer peresenthises == ()
'''
# def outerfunction(text):
#     def innerfunctions():
#         print(text)
#
#     return innerfunctions

# b = outerfunction('Hello..! ')
#
# del outerfunction
# print('\n','calling the innerfunction after deleting the outerfunction')
# print(b())
# b()

'''
one more example to explaining the about the closers
'''

# def nth_power(exponent):
#     def pow_of(base):
#         return pow(base, exponent)
#
#     return pow_of

# square = nth_power(2)
# print(square(2))
# print(square(3))
# print(square(4))
#
# print('\n', 'explaining the remembering the values of which was  \''
#            'defined outsidef of the function')
#
# cube = nth_power(3)
# print(cube(2))
# print(cube(3))
# print(cube(4))

'''
Decorators: it is used calling the function as an argument 

'''

# def decorator_func(func):
#
#     def wrapper_func():
#
#         print('X' * 20)
#         func()
#         print('Y' * 20)
#
#     return wrapper_func
#
# def Say_hello():
#     print('Hello world')
#
#
# hello = decorator_func(Say_hello)
# hello()

'''
Here python will provide the simple to call decorator 
@decorator function name infort for where we have to user function 
'''

# def decorator_func(func):
#
#     def wrapper_func():
#
#         print('X' * 20)
#         func()
#         print('Y' * 20)
#
#     return wrapper_func
# @decorator_func
# def Say_hello():
#     print('Hello world')
#
# # we call directly as regular function call
# Say_hello()
#
# print('\n')
'''
More than one decorators 
order of decorator will change the execution 
'''

# def decorator_X(func):
#
#     def wrapper_func():
#
#         print('X' * 20)
#         func()
#         print('Y' * 20)
#
#     return wrapper_func
#
#
# def decorator_Y(func):
#
#     def wrapper_func():
#
#         print('X' * 20)
#         func()
#         print('Y' * 20)
#
#     return wrapper_func
#
# @decorator_X
# @decorator_Y
# def Say_hello():
#     print('Hello world')
#
# # we call directly as regular function call
# Say_hello()

# hello = decorator_X(decorator_Y(Say_hello))
# hello()

'''
calling the decorator as object

'''
# print('\n')
# def decorator_X(func):
#
#     def wrapper_func():
#
#         print('X' * 20)
#         func()
#         print('Y' * 20)
#
#     return wrapper_func
#
#
# def decorator_Y(func):
#
#     def wrapper_func():
#
#         print('X' * 20)
#         func()
#         print('Y' * 20)
#
#     return wrapper_func
#
# # @decorator_X
# # @decorator_Y
# def Say_hello():
#     print('Hello world')

# we call directly as regular function call
# Say_hello()

# hello = decorator_X(decorator_Y(Say_hello))
# hello()

'''
complex decorators 
'''

# def decorator_divide(func):
#     def wrapper_func(a, b):
#         print('divide', a, 'and',b)
#         if b == 0:
#             print('division with zero is not possible')
#             return b
#         return a / b
#     return wrapper_func
#
# @decorator_divide
#
# def divide(x, y):
#     return x / y
#
# print(divide(15, 5))
# print(divide(15, 0))

'''
Real world decorator examples
'''

# from time import time
# def timing(func):
#     def wrapper_func(*args, **kwargs):
#         start = time()
#         print('cacluation start at:', start)
#         results = func(*args, **kwargs)
#         end = time()
#         print('cacluation end at:', end)
#         print('Elapsed time: {}'.format(end - start))
#
#         return results
#     return wrapper_func
# @timing
#
# def my_func(num):
#     sum = 0
#
#     for i in range(num+1):
#
#         sum += 1
#
#
#     return sum
#
# print(my_func(200000000))

'''
Python operator overloaing 
# '''
# import math
#
# class Circle:
#     def __init__(self, radius):
#         self.__radius = radius
#
#     def setRadius(self, radius):
#         self.__radius = radius
#
#
#     def getRadius(self):
#         return self.__radius
#
#
#     def area(self):
#
#         return math.pi * self.__radius ** 2
#
#     def __add__(self, circle_object):
#        # self.__circle_object = circle_object
#
#         return Circle(self.__radius + circle_object.__radius)
#
#
#     def __le__(self, circle_object):
#        # self.__circle_object = circle_object
#
#         return self.__radius < circle_object.__radius
#
#
#     def __gt__(self, circle_object):
#      #   self.__circle_object = circle_object
#
#         return self.__radius > circle_object.__radius
#
#
#     def __str__(self):
#        # self.__circle_object = circle_object
#
#         return 'Circle area =  '+ str(self.area())
#
#
#
# c1 = Circle(2)
# c2 = Circle(3)
# c3 = c1 + c2
#
# print(c1.getRadius())
# print(c2.getRadius())
# print(c3.getRadius())
#
# print(c1 < c2)
# print(c2 > c1)
# print(c3 > c2)
#
# print(str(c1))
# print(str(c2))
# print(str(c3))


'''
Above two operator overloadding is confusing u have to know the 
what is what, u have to know each and every thing here 

'''

# import math
#
# class Circle:
#
#     def __init__(self, radius):
#         self.__redius = radius
#
#     def setRadius(self,radius):
#         self.__radius = radius
#
#     def getRadius(self):
#         return self.__redius
#
#     def area(self):
#         return math.pi * self.__redius ** 2
#
#     def __add__(self, circle_object):
#         return Circle(self.__redius + circle_object.__redius)
#
#     def __le__(self, circle_object):
#         return (self.__redius < circle_object.__redius)
#
#     def __gt__(self, circle_object):
#         return (self.__redius > circle_object.__redius)
#
#     def __str__(self):
#         return 'Circle area =' + str(self.area())
#
#
# c1 = Circle(2)
# c2 = Circle(3)
# c3 = c1 + c2
#
# print(c1.getRadius())
# print(c2.getRadius())
# print(c3.getRadius())
#
# print(c1 < c2)
# print(c2 > c1)
# print(c3 > c2)
#
# print(str(c1))
# print(str(c2))
# print(str(c3))

'''
Python debugger (pdb)

'''

# def add(x, y):
#     sum = x + y
#     return sum
#
# if __name__ == '__main__':
#     x = float(input('Num1: '))
#     y = float(input('Num1: '))
#
#     z = add(x, y)
#     print(z)

'''
Implement python debbuger inside the script
By importing the pdb module and set bread point
'''

# import  pdb
# def add(x, y):
#     sum = x + y
#     return sum
#
# if __name__ == '__main__':
#     x = float(input('Num1: '))
#     y = float(input('Num1: '))
#     pdb.set_trace()
#     z = add(x, y)
#     print(z)

'''
Another way of implementing python debbuging 

'''
# def add(x, y):
#     sum = x + y
#     return sum
#
# if __name__ == '__main__':
#     x = float(input('Num1: '))
#     y = float(input('Num1: '))
#     import pdb;pdb.set_trace()
#     z = add(x, y)
#     print(z)

'''
Using pdb in python console
'''

# def add(x, y):
#     sum = x + y
#
#     return sum
#
# def main():
#     x = float(input('Num1:  '))
#     y = float(input('Num2:  '))
#
#     z = add(x, y)
#     print(z)
#
# if __name__ == '__main__':
#     main()

'''
python global, local, nonlocal variables 
Global variable declear anywhere 
nonlocal: define in neasted function

local variable : inside the function 
'''


def func():
    global x
    print('1______', x)
    x = 'local'
    print('2______', x)


x = 'global'
func()
print('3_____', x)
# Mathimatical operation

# print(50 + 50)
# print(20 + 20)
# print(60 - 50)
# print( -60 + 50)
# print( 50 / 3)
# print( 50 // 3) # floor division
# print(50.0 / 3.0)
# print( 50 / 10)
# print(50 % 10)
# print( 50 * 10)
# print(pow(2,4))
# print(2 ** 4)
'''
Order of operations
PEMDAS 
Parenthises,Exponetionsion, multiplicaion, division,addition,
substraction
'''

# print((5+9 - 6 * (10 /20 )))

'''
Python variable
in computer programming, a variable is a storage location
(identified by a memory address) paired by an associated symbolic name
(an identifier)
which contains some know and unknown quantity of information 

'''
# myINt = 9 # = is assingment operator
# print(myINt) # no need to specfiy the data type

# variable not start with number or special character
# variable are case senstviv
# _age = 10 # Valied declearation
# age = .22 # invalid declaration
# 10age = 44 # invalid variable deceleration

# and = 54 # reserverd keyword invalied syntax

# myInt = 10
# print(myInt)
# myFloat = 20.5
# print(myFloat)
# mycomplex = 1j
# print(mycomplex)
# mynum = 5E5
# print(mynum)

# Reassingment
# myString = 'Max'
# print(myString)
# myFloat = myINt
# print(myFloat)

# converion integer vs float

# myFloat = float (myINt)
# print(myFloat)
#
# myINt = int (myFloat)
#
# print(myINt)
# type(myINt)
#
# print('Hello world') # passing arguments
# print(25)
# print(50 * 60)
#
# pass multiple arguments to print

# print('50 * 10 =', 50* 10)
# print('hello', 'world')
#
# x = 50
# y = 10
# print("+**********************")
# print('{0} * {1} = {2}'.format(x, y, x * y))
#
# print('hello','world',sep='^^^^^^^^^^^^^^')
#

# C-style string formatting

'''

%s -- string
%d -- integer
%f -- float
%2f --- limiting decemial point 
'''
# name = 'Max'
# print('hello %s' % name)
#
# age = 22
#
# print('Hello %s ! are %d years old'% (name, age))
# passing arguments inside the tuple

# marks = 92.6
#
# print('Marks = %f' %marks)
#
# marksa = 92.5
#
# print('marksa = %f.2' %marksa)
#
# print('marksa = %.2f' %marksa)

# value = input('enter some value:  ')
# print(value)
#
# value = int(input('enter some value:  '))


# python modules
# import math
# l = math.sqrt(100)
# print(l)

# excuting the python file
# x= float(input('Enter 1st numbaer: '))
# y= float(input('Enter 2st numbaer: '))
# z= float(input('Enter 3st numbaer: '))
#
# print('Sum of three values: ', max(x,y,z))
# print('Press any key to exit')

x = "Hello\" \\world"
y = 'Hello \world'
z = '   Hey dear  '
a = 'Hey, ram, krishna'

print(x)
print(y)

print(x.upper())
print(y.capitalize())
print(x.lower())
print(x[0])
print(x[0:4])
print(z.strip())  # strip function will remove the start/end space

print(z.lower())
print(z.replace('H', 'R '))
print(a.split())  # split into list of worlds
print(z, z, z)

# Boolean values
'''
Boolean values are two constant

True 
False
comparision operator:  

Logical operator: and or not

'''

# if else control loops

# x = - 100
#
# if x != 100:
#     print('x is =')
#     print(x)
#
# if x > 0:
#     print('x is positive')
# else:
#     print('x is negative ')
#
# print('Finished')

# name = input('Enter name :  ')
#
# if name == 'Max':
#     print('Name Entered is : ', name)
#
# elif name == 'Leo':
#     print('Name Entered is : ', name)
# elif name == 'Roy':
#     print('Name Entered is : ', name)
# elif name == 'Eli':
#     print('Name Entered is : ', name)
#
# else:
#     print('The name entered is invalid')

# nested if else condition loops

# x = 10
# if x < 0:
#     print('x is negative')
# else:
#     print('x is positive')
#     if x%2 ==0:
#         print('x is even number')
#     else:
#         print('x si odd number ')

# Nested if condition

# x = 10
# if x > 0:
#     print('x is negative')
#
#     if x % 2 == 0:
#         print('x is even number')
#     else:
#         print('x si odd number ')
#
# else:
#     print('x is positive')

# List in python

'''
is kind collection allows put many kind
ordered set of values which by index which start 0
inside the list called elemenets  
'''

# x = [3,4,5,9,6,47,8,56,]
# print(x)
# x[0]
# x[4]
# y = ['max',1,15,16.4,[3,2]]
# y[0]
# y[3]
# #y[100] # list index out of range
#
# len(x) # lenth of list
# '''
# Inserting elements inside list
# '''
#
# x.insert(2, 'Tom')
# print(x)

'''
remove elements in list
'''
# x.remove('Tom')
# print(x)
# #x.remove(100) # x not in list
#
# x.pop() # remove last element inside list
# print(x)
#
# z = [1,2,5,4]
# del z
#
# z = [1, 2, 5, 4]
# z.clear() # its empty the list
#
# x = [3,4,5,9]
# x.sort() # sorting asending ordre
# x.reverse() # sorting desending order
#
# x.append(10)
# print(x)
#
# x.append(10)
# x.append(10)
# print(x)
#
# s = x.copy()
# print(s)
#
# x.count(10)
# x.count(3)
# x.count(100)

'''
Tuples in python
it's similar like lists 
tuple are immutable. content con't be modify  
'''

x = (1, 2, 3, 4, 5, 8)  # both way we can define the tuples
x1 = 1, 2, 3, 4.5, 6, 7, 'word'
print(x1)
type(x1)
print(x[0])
print(x[4])
# print(x[100])
# x[4] =  9
x.count(8)
len(x)
y = (1, 'max', 1.6)
print(y)
'''
item assigment not possible in tuple
'''

z = x + y
print(z)

a = ('hi') * 5
print(a)

print(max(x))

del z

'''
python set:
No duplicate value
un order set elements 
No indexing 
'''

# A = {1,2,3,4,7,9,2}
# print(A) # remove the duplicate values and then save
# print(len(A))
# print(A.add(10))
# print(A.add(10)) # unique values is add
# print(A)
#
# A.update([12,23,45])# updating multiple values
# print(A)
#
# A.remove(12) # remove
# print(A)
#
# A.discard(23)#does't show error while elements not in the set
#
# print(A)
# print('@@@@@@@@@@@@')
# print(A.pop()) #Remove the random elements
# print(A)
#
# name = {'max','tom','Den'}
# name.clear()
# print(name)
# del name
# #print(name)
#
# name1 = set(('max','tom','Den'))
# print(name1)
#
# z = set([1,2,34.89])
# print(z)
# print(type(z))
#
# #Mathamatical operations
#
# a = set([1,2,3,4])
# b = set([3,4,5,6])
#
# a_union_b = a | b # union of a and b
# print(a_union_b)
# print(a.union(b))
#
# a_inter_b = a & b # interaction of a and b
# print(a_inter_b)
# print(a.intersection(b))
#
# a_differ_b = a - b# difference of a and b
# print(a_differ_b)
# print(a.difference(b))
# print(b.difference(a))
#
# a_symetric_b = a ^ b # symetric difference
# print(a_symetric_b)
# print(a.symmetric_difference(b))
# print(b.symmetric_difference(a))
# set are not indexed
# print(a[1]) set object does not support indexing

'''
Associative  list or map or pair
key value pair
'''
D = {'name': 'max', 'age': 14, 'year': 2004}
print(D)
print(D['name'])
print(D.items())
print(D.keys())
print(D.values())
print(D.get('year'))

d = {'name': 'Tom', 15: 15, 15.1: 15.3, 'Male': True, (2, 3): 5}
print(d)
print(d['Male'])
print(d[(2, 3)])
d['surname'] = 'Trump'
print(d)
print(len(d))

# print(d.pop())
# print(d.popitem())
# print(d.clear())
'''
update method will modify & appending  key, values pair in a dictionary
'''
print(d.update({'name': 'rajan', 'male': 'False', 'Occupation': 'tester'}))
print(len(d))

'''
Python slice and negative index
'''
# a = [0,1,2,3,4,5,6,7,8,9] # list
# b = (0,1,2,3,4,5,6,7,8,9) # tuple
# c = '0123456789' # string
# print(a)
# x = slice(0, 5)
# print(a[x])
# print(a[0:5])# short notation, start(0),end(5)
# print(a[-1])
# print(a[:-3:-1]) # end value (-3)
# print(a[-3::-1]) # start value (-3)
# #print(b[4:])
# #print(b[:4])
# print(c[:])
# print('*************')
# print(c[0:5]) #Here end point won't include in period
# print(a[0:9:2])
# print(a[0:9:3])
# print(a[0:9:4])  # start(0) , end (9) and step(4)
# print(a[::3]) # start and end with three step
# print(c[-1])
# print(c[-4])
#
# print(c[-1]) # negative index from right to left
# print(a[::-3]) # its from right to left
# print(a[:-2:-1])
#
# print(c)
# print(c[-10:-1]) #
# print(c[0:9]) # both are the same result

# Python tutorial for Benginners - while loop

# num = 1
# sum = 0
# print('Enter a Number. Please Enter zero(0) to exit')
# while num != 0:
#     num = float(input('Enter..? : '))
#     sum = sum + num
#     print('sum =', sum)
# else:
#     print('Finished sum')


# i = 0
# #while i < 5:
# while True:
#     print('the value of i is: ',i)
#     i = i + 1 # i += 1
# #    print('Finished while loop')
#
# else:
#     print('Fhinished while loop')
'''
Python tutorial for beginners - for loop
'''
z = [0, 1, 2, 3, 4, 5]
y = (0, 1, 2, 3, 4, 5)
x = {0, 1, 2, 3, 4, 5}
w = '012345'
v = {'name': 'max', 'age': 22}

print(0 in z)
print(0 in y)

for a in z:
    print(a)

print('************')
for b in x:
    print(b)

for c in v.values():
    print(c)

for key, value in v.items():
    print(key, ' ', value)

for x in range(6):  # last value in range it's not print
    print(x)  # it will print 0,1,2,3,4,5 only

'''
Range function will support (start,end,step)
'''

'''
Here else statement will execute after the 
for loop execution was completed
'''
# for x in range(2,30,2):
#     print(x)
#
# else:
#     print("finished")

'''
Python tutorial for beginners - break and continue
'''
a = [0, 1, 2, 3, 4, 5]
# for x in a:
#     if x == 3:
#         break
#     print(x)


print("################")
# i = 0
# while i < 5:
#     if i == 3:
#         break
#     print(i)
#     i += 1

# print('----------------')
#
# for x in a:
#     if x == 2:
#         continue
#     print(x)
#
# print('****************')
'''
Here once of the if statement execution stop
loop will break stop the IF loop
'''

# i = 0
# while i < 5:
#     if i == 2:
#         continue
#     print(i)
#     i += 1 #Iteration statement

print('-------------------')

'''
We can overcome problem with writing the iteration 
statement before if statement

output of below code was 0,1,3,4,5
'''
# i = 0
# while i < 5:
#     i += 1  # Iteration statement
#
#     if i == 2: # 2 won't print
#         continue
#     print(i)


'''
PYthon Functions 

function will complete one task at a time
print() 

Function decleration  

'''
# def nameoffunction(arg1,arg2,arg3):
#     print()
# print('-----Functions-------')
# def sum(arg1, arg2):
#
#     if type(arg1) != type(arg2):
#         print('Please give the args of same type')
#         return
#     print(arg1 + arg2)
#     return
# print('Function calling')
# a = sum(15, 60)
# print(a)
# print(sum('Hello','world'))
# print(sum(15.23,46.12))
# print(sum('hello',15)) #can only concatenate str(not 'int) to str
#
# print('==============')
# print('Second example')
# print('-------------')
'''
We can use defult values to argument passed
'''
# def student(name='Unknow_name',age = 0):
#     print('name',name)
#     print('age',age)
#
# student('Rajan',25)
# student('Puja')

'''
python tutorial for Beginners 
default arguments *args and *kwargs

*args --- assig multiple arguments(its support int,string)
    it's taking values as TUPLE


**kwargs --- assign multiple args as key pair manner(engish=35)
    it's take as dictionary


'''
print('Example for multiple argument passing (*args)')

# def Student(name,age,*marks):
#     '''
#     Note: Here in function only one (*args) should be
#     decleared
#     '''
#     print('name',name)
#     print('age', age)
# #    print('marks', marks)
#     for x in marks:
#         print(x)
# Student('juliana',35,56,89,90,100)
#
# print('____passing string as *args___________')
# def Student1(name,age,*friends):
#     '''
#     Note: Here in function only one (*args) should be
#     decleared
#     '''
#     print('name',name)
#     print('age', age)
#     print('marks', marks)
#     for friend in friends:
#         print(friend)


# print('******calling function**********')
# Student1('rama',36,'puja','kammala')
#
# print('=======**kwargs======explainstion')
#
# def SchoolStudent(name,age,**marks):
#     '''
#     Here with help of **kwargs. we can pass the key pair
#     argument of multiple one at time
#     **kwargs --- passing values as DICT{}
#     '''
#     print('name',name)
#     print('age', age)
#     print('marks', marks)
#     for key,value in marks.items():
#         print(key,' ', value,'\n')
#
# SchoolStudent('Samul',20,english=56,chemistray=44,physics=95)


print('*****OOPS*******', sep='\n')
'''
Objective oriented programming

class --blue print
method -- its a function which is inside the class
instance --
attributes -- (data members or attributes)

Data and method -- not separete in OOPs
'''

# class Car:
#     pass
# '''
# empty class
# '''
# #Attributes
# ford = Car()
# honda = Car()
# audi  = Car()
#
#
# ford.speed = 200
# honda.speed = 220
# audi.speed = 250
#
# ford.color = 'red'
# ford.color = 'blue'
# ford.color = 'black'
#
#
# print(ford.speed)
# print(ford.color)

# Changing the attributes values

# ford.speed = 300
# ford.color = 'Blue'
#
# print('\n')
#
# print(ford.speed)
# print(ford.color)
#
# print('*******new example****')

# class Rectangle:
#     pass
#
# rect1 = Rectangle()
# rect2 = Rectangle()
#
# rect1.height = 20
# rect2.height = 30
#
# rect1.width = 20
# rect2.width = 30
#
# print(rect1.height * rect1.width)
# print(rect2.height * rect2.width)

'''
How to use the __init__ method in python class

with self word
'''
# #class Car:
#     def __init__(abc,speed,color):# used as constructer
#         print(speed)
#         print(color)
#         abc.speed = speed
#         abc.color = color
#         print('the __init__ is called')
# #Attributes

# passing values to agruments
# ford = Car(200,'red')
# honda = Car(220,'blue')
# audi  = Car(250,'yellow')

# ford.speed = 200
# honda.speed = 220
# audi.speed = 250

# ford.color = 'red'
# ford.color = 'blue'
# ford.color = 'black'


# print(ford.speed)
# print(ford.color)

# Changing the attributes values

# ford.speed = 300
# ford.color = 'Blue'

# print('***Rectangle class')
#
# class Rectangle:
#     def __init__(self,height,width):
#         self.height = height
#         self.width = width
#
#
# rect1 = Rectangle(75,98)
# rect2 = Rectangle(20,40)
#
# rect1.height = 20
# rect2.height = 30
#
# rect1.width = 20
# rect2.width = 30

# print(rect1.height * rect1.width)
# print(rect2.height * rect2.width)

print('Brief explains')

# class Hello:
#     def __init__(self): pass
#     def __init__(self, name): pass
#
# hello = Hello('name')

'''
Here the below example reveals that 
in python class __init__ method will executes 
from top to bottom i.e in first line instance method

attributes igonre
def __init__(self, name): pass
def __init__(self): pass
as per theory last __init__method only valid

class Hello:
    def __init__(self, name): pass
    def __init__(self): pass
hello = Hello('name')

so in the second method their no arguments 
its reflect error  

TypeError: __init__() takes 1 positional argument but 2 were given
'''

# class Hello:
#
#     def __init__(self, name='max'):pass
#
# hello = Hello()
# hello = Hello('name')
#
# print('************8')
# class Hello:
#
#     def __init__(self, *args):pass
#
# hello = Hello()
# hello = Hello('name','yellow','greed')
#
# print('-------------')
# class Hello:
#
#     def __init__(self,*args, **kwargs):pass
#
# hello = Hello()
# hello = Hello('name','latha','friend','sujatha')

'''
Passing static values to the attribute without 
defining it in (__init__) instance method

Below example will explain about that
'''

# class Hello:
#     def __init__(self,name):
#         self.name = name
#         self.age = 20
#
# hello = Hello('name')
# print(hello.name)
# print(hello.age)

print('*************')
'''
Python encapsulation 
Avoid the tampering out code by the third person 


Implementing encapsulation
==========================

if you want to implement the encapsulation 
we have to create function called (__set__) and (__get__)


'''
# class Car:
#     def __init__(self,speed,color):
#         self.speed = speed
#         self.color = color
#
#
#     def set_speed(self,value):
#         self.speed = value
#
#
#     def __get_speed(self):
#         return self.speed


# ford = Car(200,'red')
# honda = Car(220,'blue')
# audi = Car(250,'black')
#
#
# ford.set_speed(300)
# ford.speed = 400

# By these we can't stop the tamparing
# not passible to make private data
# print(ford.speed)
# print(ford.color)

'''
BY using single & double underscore we achive the private method

self._b = 10 
self.__c (  ) make our attribute as private 

'''

# class Hello:
#     def __init__(self,name):
#         self.a = 10
#         self._b = 20 # technique to implement the encapsulation
#         self.__c = 40
#
#
# hello = Hello('name')
#
# print(hello.a)
# print(hello._b)
# print(hello.__c) # with help of these we make attributes as private


'''
Implementing the private method in class 
'''
# class Car:
#     def __init__(self,speed,color):
#         self.__speed = speed
#         self.__color = color
#
#     def set__speed(self,value):
#         self.speed = value
#
#     def get__speed(self):
#         return self.__speed
#
#     def set__color(self,value):
#         self.__color = value
#
#     def get__color(self):
#         return self.__color
#
# ford = Car(200,'red')
# honda = Car(220,'blue')
# audi = Car(250,'black')
#
# ford.set__speed(300)
# ford.__speed = 500
# ford.__color = 'mejento'
#
# print(ford.get__speed())
# print(ford.get__color())

'''
Here conclusion was the if you define the 
attributes with (double under score (__) then can't 
change the attributes values

additionally you have to define the functions 

def set__(self,value)
    self.__attributename = values
def get__(self) 

    :return name of attributes

'''

# By these we can't stop the tamparing
# not passible to make private data
# print(ford.__speed)
# print(ford.__color)


'''
We have to implement the private method to the
rectangle python file
'''

# class Rectangle:
#     def __init__(self, height, width):
#         self.__height = height
#         self.__width = width
#
#     def set__height(self, height):
#         self.__height = height
#
#     def get__height(self):
#         return self.__height
#
#     def set__width(self,width):
#         self.__width = width
#
#     def get__width(self):
#         return self.__width
#
#     def area(self):
#         return self.__height * self.__width
#
# rect1 = Rectangle(30, 52)
# rect2 = Rectangle(80, 50)
#
# print(rect1.area())
# print(rect2.area())

'''
private methods in python 

Following the above example we can't 
access the private variable out side of the functions

For overcoming the above problem By 
defining the Private & public variables in the 

function called PUBLIC_METHOD(SELF)
'''
# class Hello:
#     def __init__(self,name):
#         self.a = 10
#         self._b = 20
#         self.__c = 30
#
#     def public_method(self):
#         self.a
#         self._b
#         print(self.__c)
#         print('public')
#
# hello = Hello('name')
# print(hello.a)
# print(hello._b)
# print(hello.public_method())

'''
explaining the private methods

'''

# class Hello:
#     def __init__(self,name):
#         self.a = 10
#         self._b = 20
#         self.__c = 30
#
#     def public_method(self):
#         self.a
#         print(self.__c)
#         print('public')
#
#         self.__private_method()
#
#     def __private_method(self):
#         print('private')
#
# hello = Hello('name')
# print(hello.a)
# print(hello._b)
# hello.public_method()


print('Python inheritance', '\n')

'''
Python class inheritence 
parent class: -- super class
child class: -- sub class
'''

# class Polygon:
#     __width = None # Both are private members
#     __height = None

# ''''
# Here __private method won't access out side of function
# if you want to access __private method. we need to create
# other method Namely(def __set(), def __get())
# '''
#     def set_values(self, width, height):
#         self.__width = width
#         self.__height = height
#
#     def get_width(self):
#         return  self.__width
#
#     def get_height(self):
#         return  self.__height
#
#
# class Rectangle(Polygon):
#     def area(self):
#       return self.get_width() * self.get_width()
#
#
# class Triangle(Polygon):
#     def area(self):
#         return self.get_width() * self.get_height() / 2
#
#
# rect = Rectangle()
# tri = Triangle()
# rect.set_values(20, 30)
# tri.set_values(10, 20)
#
# print(rect.area())
# print(tri.area())

'''
Python Modules
module is nothing but python file
create our own module
'''
# import math

print('*******Python super()***********')
'''
here the inheritance from parent member to child class 
with help of super class or name of the superclass along with
init method 

ex: super().__init__('member value')

if importing more than one member we have to import 
each member of each parent class

example: parent.__init__(self,'value of  member')
         parentclassname.__init__(self, 'value of member'
Method resolution order: (__mro__)
it's dependent on order importing parent class inside of 
child class
'''

# class Parent:
#     def __init__(self,name):
#         print('Parent __init__',name)
#
# class Parent2:
#     def __init__(self,name):
#         print('Parent2 __init__', name)
#
# #class Child(Parent,Parent2):
# class Child(Parent,Parent2):
#     def __init__(self):
#         print('Child __init__')
# #        super().__init__('name')
#         Parent2.__init__(self,'max') # importing parent member
#         Parent.__init__(self,'Hari')# importing another parent member
#
#
# child = Child()
# print(Child.__mro__)

'''
Concept of aggregation and composition

Aggregation : 
============
key word representation is HAS A
Here if want to import functionality with out the super() and
parent and child relationship.

we can share the member variable with help of composition 

composition is delegation of responsibily between the classes 

special praperties of aggregation:
i) class objects independent 
ii) Associated class have uni directional association


Composition:
===========
here both are the class interdependent 
members variable of classes are dependent each other  

key word representation is part of A

'''
# class Salary:
#     def __init__(self, pay, bonus):
#         self.pay = pay
#         self.bonus = bonus
#
#     def annual_salary(self):
#         return (self.pay * 12) + self.bonus


# class Employee:
#     def __init__(self,name,age,pay, bonus):
#          self.name = name
#          self.age = age
#          self.obj_salary = Salary(pay, bonus)
#
#     def total_salary(self):
#         return self.obj_salary.annual_salary()


# emp = Employee('max', 25, 15000, 10000)
# print(emp.total_salary())
#
# print('$$$$$$$ __Aggregation__$$$$$$$$$')

# class Salary:
#     def __init__(self, pay, bonus):
#         self.pay = pay
#         self.bonus = bonus
#
#     def annual_salary(self):
#         return  (self.pay * 12) + self.bonus

# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.obj_salary = salary
#
#     def total_salary(self):
#         return  self.obj_salary.annual_salary()
#
#
# salary = Salary(15000,10000)
# emp = Employee('tom', 25, salary)
# print(emp.total_salary())


print('@@@@@__Abstract class__@@@@@@@@@2')
'''
In some cases we must implemenet functionality 
someother class to completing the tasks 

i.e we have to abstract the main class to sub class. we can achive that by 

'''

# from abc import  ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self): pass
#
#     @abstractmethod
#     def perimeter(self): pass
#
#
# class Square(Shape):
#
#     def __init__(self, side):
#         self.__side = side
#
#     def area(self):
#         return self.__side * self.__side
#
#     def perimeter(self):
#         return self.__side * 4

# squre = Square(5)
# print(squre.area())
# print(squre.perimeter())


print('*****Exceptions**********')

''''
Here when python struck with invalid code 
it will simply stop the entire excution flow 

To overcome the above issue we have to implement the 
functions 

try: 
testing statements

except:

Error displaying statmenets 
Error revealing statements 
'''
# result = None
# a = input('Number 1:' ) # type error
# #a = float(input('Number 1:' )) #zerodivisonerror
# b = float(input('Number 2:' ))
#
# try:
#     result = a / b
# # except:
# #     print('float zero division error')
#
# # write generic exception class
#     '''
# Here Exception in except is the base class
#
# As it is Base class it can capature the all type of
# error
#
# Are Else we have to individually mentioned one by one
# each error
#     '''
#
# # except Exception as e:
# #     print('Error =', e)
#
# # except Exception as e:
# #     print('Error =', type(e))
#
#
# except ZeroDivisionError as e:
#     print('Error =', type(e))
#
# except TypeError as e:
#     print('Type Error :',type(e))
#
#
# print('Result =', result)
# print('End')

print("More about try/except/else/finally")

print('\n', '\n')
'''
More about the 

Try: testing code

Except:
 capaturing type of errors 
 Revealing about error information to developer 

else:

If except statement not excuted, next else statemenet will 
excute

Modifiying the code as after analysing the try block
Along  with except statemenet only else statement should use

Finally:
It will always excute,
irrespective of try/exception 

while opening closeing files and closing sql database

reconnection of data base file 

'''

# result = None
# a = float(input('Number 1: '))
# b = float(input('Number 2: '))
#
# try:
#     result = a / b
#
# except ZeroDivisionError as e:
#     print('Zerodivisionerror ',type(e))
#
# else:
#     print('__else__')
#
# finally:
#     print('__finally___')
#
# print('Resutl = ',result)
# print('End')


print('^^^^Python raise execption^^^^^^^^')
'''
Python raise exceptions
throw/raise the exceptions
'''

# class CoffeeCup:
#     def __init__(self, temperature):
#         self.__temperature = temperature
#
#     def drink_coffee(self):
#         if self.__temperature > 85:
#         #    print('Coffee Too Hot')
#             raise Exception('Coffee Too Hot')
#
#         elif self.__temperature < 65:
#         #   print('Coffee Too cold')
#         #    raise Exception('Coffee Too Cold')
#             raise ValueError('Coffee Too Cold')
#         else:
#             print('Coffee is ok Drink')
#
# cup = CoffeeCup(50)
# #cup = CoffeCup(115)
# print(cup.drink_coffee())


'''
Custom exception class
'''

# class CoffeeTooHotException(Exception):
#     def __init__(self,msg):
#         super().__init__(msg)


# class CoffeeTooColdException(Exception):
#     def __init__(self,msg):
#         super().__init__(msg)
#
#
# class CoffeeCup:
#     def __init__(self, temperature):
#         self.__temperature = temperature
#
#     def drink_coffee(self):
#         if self.__temperature > 85:
#             raise CoffeeTooHotException('Coffee Temperature:' + str(self.__temperature))
#
#         elif self.__temperature < 65:
#             raise CoffeeTooColdException('Coffee Too cold' + str(self.__temperature))
#
#         else:
#             print('Coffee ok to drink')
#
#
# cup = CoffeeCup(100)
# cup.drink_coffee()

'''
Importance of if __name__ = "__main__"

above function will limit the functionality or rest code which
in the importing file

instead of printing respones of the importing file code 
it will print only the Name of the imported module

In the same folder i created filename called add.py 
just import that file execute 
'''

# import add
#
# print(add.add(6, 7))


'''
Python reading and writing the file
'''

# fh = open('demo.txt','w')
# #fh.writelines('I wrote text data to file')
#
# for i in range(10):
#     fh.write('this is line no %d \n' %(i + 1))
#
# fh.close()
#
print('__File operation with append mode__')
# fh = open('demo1.txt','a')
# fh.writelines('I wrote text data to file')

# for i in range(10):
#     fh.write('this is line no %d \n' %(i + 1))
#
# fh.close()

print('*** mode (m+) ***')

fh = open('demo2.txt', 'w+')
# fh.writelines('I wrote text data to file')

for i in range(10):
    fh.write('this is line no %d \n' % (i + 1))

fh.close()

'''
Implemenet the try/finally
'''

fh = open('demo.txt', 'w')

# fh.writelines('I wrote text data to file')


# try:

#     for i in range(10):
#         fh.write('this is line no %d \n' %(i + 1))
#
# finally:
#     fh.close()

'''
Above the code written as well 
'''

# with open('demo.txt','w') as fh:
#
#     for i in range(10):
#
#         fh.write('This is line no {} \n'.format(i))

'''
Reading files in python 
'''
# fh = open('demo.txt')
# print(fh.read())
#
# fh.close()

fh = open('demo.txt')
# print(fh.read())
# print(fh.readline(5))
# print(fh.readlines()[4])
# print(fh.readlines()[5])


# for line in fh:
#     print(line)
#     print(len(line))# count the number characters in line
#     print(line.split()) # split the words in each line
#     print(len(line.split()))#count the words in each line
# fh.close()
#
#
# with open('demo.txt','r') as fh:
#     for line in fh:
#         print(line.split())


'''
working with JSON data in python
Java script object notation
'''
# import json
#
# a = {
#     'name':'max',
#     'age':22,
#     'marks' : [90,23,24,45],
#     'pass': True
# }
# print(json.dumps(a))
#
# print('\n', 'Data types which was supported by json')
#
# print(json.dumps({'name':'max','age':25}))
# print(json.dumps(['1','2']))
# print(json.dumps(('1', '2')))
# print(json.dumps('Hello world'))
# print(json.dumps(100))
# print(json.dumps(15.56))
# print(json.dumps(False))
# print(json.dumps([True]))
# print(json.dumps(None))
#
#
# a = {
#     'name':'max',
#     'age':22,
#     'marks' : [90,23,24,45],
#     'pass': True,
#     'object': {
#         'color':('red','blue')
#     }
# }
#
# with open('demo.json','w') as js:
#     js.write(json.dumps(a, indent=5))
#
# print(json.dumps(a, indent=5, separators= ('.', ' =')))

# print('\n', 'Read json file')
#
# import json
#
# with open('demo.json','r') as fh:
# #    print(fh.read())
#
# # assing json file content to variable
#     json_str = fh.read()
#     json_value = json.loads(json_str)
#     print(type(json_str))
#     print(type(json_value))
#     print(json_value['name'])
#     print(json_value['pass'])

'''
Itertoration in python
it is an object which can be interate over collection of elemenets inside a datatype
python have two type of iterations
i) __iter__()
ii) __next__()

'''

# class ListIterator:
#     def __init__(self, list):
#         self.__list = list
#         self.__index = -1
#
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.__index += 1
#
#         if self.__index >= len(self.__list):
#             raise StopIteration
#
#         return self.__list[self.__index]


# a = [1,2,3,6,5,4]
# mylist = ListIterator(a)
# it = iter(mylist)

print('\n', 'iteration')

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# insted of above interation we can you the for loop
# for i in it:
#     print(i)

'''
Python generators
Generators: it is the simple way of creating iterators

Generators automatically raise the exceptions
'''

# def my_func():
#     yield 'a'
#     yield 'b'
#     yield 'c'
#
# x = my_func()
#
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

print('\n', 'yield functionality')

# def my_yfunc():
#
#     n = 1
#     print('===========',n)
#     yield n
#
#     n += 1
#     print('----------',n)
#     yield n
#
#     n += 1
#     print('-----------',n)
#     yield n

# z = my_yfunc()
#
# print(next(z))
# print(next(z))
# print(next(z))

# print('\n', 'yield functionality with for loop')

# def myf_func():
#     for i in range(5):
#
#         print('----------',i)
#         yield i
#
# y = myf_func()
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
# #print(next(y))

'''
Generator function
'''
# def iter_iterator(list):
#     for i in list:
#         yield i
#
# a = [1,2,3,6,5,4]
# mylist = iter_iterator(a)
# print(next(mylist))
# print(next(mylist))
# print(next(mylist))
# print(next(mylist))
# print(next(mylist))

# print('\n', 'both above and below function have same')
#
# for x in mylist:
#     print(x)

# print('\n')
# print('\n')
# print('\n')

'''
command line arguments in python
it will be pass the arguments to python command line 
'''

# import argparse
#
# if __name__ == '__main__':
#     # initailize the parser
#     parser = argparse.ArgumentParser(
#         description=' my script path'
#     )

# add the parameters positional/argmunts

# parser.add_argument('num1', help='number1: ', type=float)
# parser.add_argument('num2', help='number2: ', type=float)
# parser.add_argument('operation', help='operator')

# writing the postional arguments

# parser.add_argument('--num1', help='number1: ', type=float)
# parser.add_argument('--num2', help='number2: ', type=float)
# parser.add_argument('--operation', help='operator', default='+')


# optional parameters for short notation

# parser.add_argument('-n', '--num1', help='number1: ', type=float)
# parser.add_argument('-i', '--num2', help='number2: ', type=float)
# parser.add_argument('-k', '--operation', help='operator', default='+')
#
# # parse the arguments
# args = parser.parse_args()
# print(args)
#
# results = None
#
# if args.operation == '+':
#     results = args.num1 + args.num2
#
# if args.operation == '-':
#     results = args.num1 - args.num2
#
# if args.operation == '*':
#     results = args.num1 + args.num2
#
# if args.operation == 'pow':
#     results = pow(args.num1,args.num2)
#
#
# print('Results: ', results)


'''
Python lambda, map, reduce, filter functions 
lamdba x: x * 2 ---- its have variable and body 
lambad : in some situation we have to pass the function as argument(variable) in that 
circumstance we have use lambda function

MAP(function, iterable value)



'''
#
# def double(x):
#     return  x * 2
#
# def add(x, y):
#     return x + y
#
# def product(x, y , z):
#     return x * y * z
#
#
# a = lambda x: x * 2
# b = lambda x, y : x + y
# c = lambda x, y, z : x * y * z
#
# print('double: {} add: {} product: {}'.format(a(10),b(10,20),c(10,20,30)))
#
#
# # Demonstating the map functions
# mylist = [1,2,3,4,5,6]
#
# a = map(lambda x: x * 2,mylist)
# print(list(a))
#
# mylist = [1,2,3,4,5,6]
# mylist1 = [6,5,4,3,2,1]
#
# b = map(lambda x,y: x + y, mylist,mylist1)
#
# print(list(b))
#
# c = filter(lambda x: x%2==0,mylist)
# print(list(c))
#
# d = filter(lambda x: True if x >= 5 else False, mylist)
#
# print(list(d))
#
# from functools import reduce
#
# e = reduce(lambda x, y : x + y, mylist)
# e_sub = reduce(lambda x, y : x - y, mylist)
# e_mul = reduce(lambda x, y : x * y, mylist)
# print(e)
# print(e_sub)
# print(e_mul)

'''
Neasted functions && closere 

here outer function and inner functions 
'''

# def outerfun(text):
#     def innerfun():
#         print(text)
#     innerfun()
#
# outerfun('hello')
#
# print('\n')
#
#
# def pop(list):
#     def get_last_item(my_l):
#         return my_l[len(my_l) - 1]
#
#     list.remove(get_last_item(list))
#     return list
#
# a = [8,3,4,5,6,9]
#
# print(pop(a))
# print(pop(a))
# print(pop(a))

'''
Python closers

'''
# def outerfun(text):
#     def interfun():
#         print(text)
#     return interfun
#
# a = outerfun('hello')
# print('calling the outerfunction along with innerfunction')
# print(a())
# print('\n', 'Only calling the outerfun()')
# a()

'''
See here the magic 
even if you delete the value outer function the innerfunction can hold 
values 

Closers will remember the values which is outside the functions as well 
NOte: Here at return statement you should not writer peresenthises == ()
'''
# def outerfunction(text):
#     def innerfunctions():
#         print(text)
#
#     return innerfunctions

# b = outerfunction('Hello..! ')
#
# del outerfunction
# print('\n','calling the innerfunction after deleting the outerfunction')
# print(b())
# b()

'''
one more example to explaining the about the closers
'''

# def nth_power(exponent):
#     def pow_of(base):
#         return pow(base, exponent)
#
#     return pow_of

# square = nth_power(2)
# print(square(2))
# print(square(3))
# print(square(4))
#
# print('\n', 'explaining the remembering the values of which was  \''
#            'defined outsidef of the function')
#
# cube = nth_power(3)
# print(cube(2))
# print(cube(3))
# print(cube(4))

'''
Decorators: it is used calling the function as an argument 

'''

# def decorator_func(func):
#
#     def wrapper_func():
#
#         print('X' * 20)
#         func()
#         print('Y' * 20)
#
#     return wrapper_func
#
# def Say_hello():
#     print('Hello world')
#
#
# hello = decorator_func(Say_hello)
# hello()

'''
Here python will provide the simple to call decorator 
@decorator function name infort for where we have to user function 
'''

# def decorator_func(func):
#
#     def wrapper_func():
#
#         print('X' * 20)
#         func()
#         print('Y' * 20)
#
#     return wrapper_func
# @decorator_func
# def Say_hello():
#     print('Hello world')
#
# # we call directly as regular function call
# Say_hello()
#
# print('\n')
'''
More than one decorators 
order of decorator will change the execution 
'''

# def decorator_X(func):
#
#     def wrapper_func():
#
#         print('X' * 20)
#         func()
#         print('Y' * 20)
#
#     return wrapper_func
#
#
# def decorator_Y(func):
#
#     def wrapper_func():
#
#         print('X' * 20)
#         func()
#         print('Y' * 20)
#
#     return wrapper_func
#
# @decorator_X
# @decorator_Y
# def Say_hello():
#     print('Hello world')
#
# # we call directly as regular function call
# Say_hello()

# hello = decorator_X(decorator_Y(Say_hello))
# hello()

'''
calling the decorator as object

'''
# print('\n')
# def decorator_X(func):
#
#     def wrapper_func():
#
#         print('X' * 20)
#         func()
#         print('Y' * 20)
#
#     return wrapper_func
#
#
# def decorator_Y(func):
#
#     def wrapper_func():
#
#         print('X' * 20)
#         func()
#         print('Y' * 20)
#
#     return wrapper_func
#
# # @decorator_X
# # @decorator_Y
# def Say_hello():
#     print('Hello world')

# we call directly as regular function call
# Say_hello()

# hello = decorator_X(decorator_Y(Say_hello))
# hello()

'''
complex decorators 
'''

# def decorator_divide(func):
#     def wrapper_func(a, b):
#         print('divide', a, 'and',b)
#         if b == 0:
#             print('division with zero is not possible')
#             return b
#         return a / b
#     return wrapper_func
#
# @decorator_divide
#
# def divide(x, y):
#     return x / y
#
# print(divide(15, 5))
# print(divide(15, 0))

'''
Real world decorator examples
'''

# from time import time
# def timing(func):
#     def wrapper_func(*args, **kwargs):
#         start = time()
#         print('cacluation start at:', start)
#         results = func(*args, **kwargs)
#         end = time()
#         print('cacluation end at:', end)
#         print('Elapsed time: {}'.format(end - start))
#
#         return results
#     return wrapper_func
# @timing
#
# def my_func(num):
#     sum = 0
#
#     for i in range(num+1):
#
#         sum += 1
#
#
#     return sum
#
# print(my_func(200000000))

'''
Python operator overloaing 
# '''
# import math
#
# class Circle:
#     def __init__(self, radius):
#         self.__radius = radius
#
#     def setRadius(self, radius):
#         self.__radius = radius
#
#
#     def getRadius(self):
#         return self.__radius
#
#
#     def area(self):
#
#         return math.pi * self.__radius ** 2
#
#     def __add__(self, circle_object):
#        # self.__circle_object = circle_object
#
#         return Circle(self.__radius + circle_object.__radius)
#
#
#     def __le__(self, circle_object):
#        # self.__circle_object = circle_object
#
#         return self.__radius < circle_object.__radius
#
#
#     def __gt__(self, circle_object):
#      #   self.__circle_object = circle_object
#
#         return self.__radius > circle_object.__radius
#
#
#     def __str__(self):
#        # self.__circle_object = circle_object
#
#         return 'Circle area =  '+ str(self.area())
#
#
#
# c1 = Circle(2)
# c2 = Circle(3)
# c3 = c1 + c2
#
# print(c1.getRadius())
# print(c2.getRadius())
# print(c3.getRadius())
#
# print(c1 < c2)
# print(c2 > c1)
# print(c3 > c2)
#
# print(str(c1))
# print(str(c2))
# print(str(c3))


'''
Above two operator overloadding is confusing u have to know the 
what is what, u have to know each and every thing here 

'''

# import math
#
# class Circle:
#
#     def __init__(self, radius):
#         self.__redius = radius
#
#     def setRadius(self,radius):
#         self.__radius = radius
#
#     def getRadius(self):
#         return self.__redius
#
#     def area(self):
#         return math.pi * self.__redius ** 2
#
#     def __add__(self, circle_object):
#         return Circle(self.__redius + circle_object.__redius)
#
#     def __le__(self, circle_object):
#         return (self.__redius < circle_object.__redius)
#
#     def __gt__(self, circle_object):
#         return (self.__redius > circle_object.__redius)
#
#     def __str__(self):
#         return 'Circle area =' + str(self.area())
#
#
# c1 = Circle(2)
# c2 = Circle(3)
# c3 = c1 + c2
#
# print(c1.getRadius())
# print(c2.getRadius())
# print(c3.getRadius())
#
# print(c1 < c2)
# print(c2 > c1)
# print(c3 > c2)
#
# print(str(c1))
# print(str(c2))
# print(str(c3))

'''
Python debugger (pdb)

'''

# def add(x, y):
#     sum = x + y
#     return sum
#
# if __name__ == '__main__':
#     x = float(input('Num1: '))
#     y = float(input('Num1: '))
#
#     z = add(x, y)
#     print(z)

'''
Implement python debbuger inside the script
By importing the pdb module and set bread point
'''

# import  pdb
# def add(x, y):
#     sum = x + y
#     return sum
#
# if __name__ == '__main__':
#     x = float(input('Num1: '))
#     y = float(input('Num1: '))
#     pdb.set_trace()
#     z = add(x, y)
#     print(z)

'''
Another way of implementing python debbuging 

'''
# def add(x, y):
#     sum = x + y
#     return sum
#
# if __name__ == '__main__':
#     x = float(input('Num1: '))
#     y = float(input('Num1: '))
#     import pdb;pdb.set_trace()
#     z = add(x, y)
#     print(z)

'''
Using pdb in python console
'''

# def add(x, y):
#     sum = x + y
#
#     return sum
#
# def main():
#     x = float(input('Num1:  '))
#     y = float(input('Num2:  '))
#
#     z = add(x, y)
#     print(z)
#
# if __name__ == '__main__':
#     main()

'''
python global, local, nonlocal variables 
Global variable declear anywhere 
nonlocal: define in neasted function

local variable : inside the function 
'''


def func():
    global x
    print('1______', x)
    x = 'local'
    print('2______', x)


x = 'global'
func()
print('3_____', x)
