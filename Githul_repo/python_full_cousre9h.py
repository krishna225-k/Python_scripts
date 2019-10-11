"""
%s --> represent the strings
%d --> represent the intigers
%f --> represent the float points

"""
# name = 'max'
# age = 22
# marks = 95.5
# print('Hello %s! '%(name))
# print('Hello %s! , are you %d years old' %(name,age))
# print('marks = %f' %marks)
# print('marks= %2f' %marks)
# print('marks = %.2f' %marks)
# print('marks = %f2' %marks)
# " User input "
# values = input('Enter a value: ')
# print('your enter values is : ',values)
#
# values1 = int(input('Please enter a values: '))
# print('enter a values is: ',values1)
#
# value3 = float(input('please enter values:'))
# print('your entered float values is: ', value3)
max_value = max(1,4,5,7,9,10)
print(max_value)
#Built moduls
import math
y = math.sqrt(100)
print(y)

#BUiltin string methods
x = 'Hello worldhari'
print(x.capitalize())
print(x.strip('Hello')) # input the word to need to remove
print(x.replace('H','l'))

# Boolean values
" True - 1, False - 0"

"List methods in python "
" python tuples"
m = (1,2,3,4,'hari')
n = ('word','lord',4,5)

a = m + n;print(a)

#" python sets"

" no indexing"
" no duplicates elements "
"Unorder set of elements"

'''b = {1,2,3,4,7,2,5}
b.update([12,13,14]) # should pass as list
b.add(10)
b.remove(1)
b.discard(5) # both discard and remove will give the result
b.clear()
print(b)'''

"""
name = ['max','tom','den']
print(name)
name.clear()
print(name)
del name
print(name)
"""
"Create a set with set constructer"
# print(name)
# name =set(('max','job','lil'))
"mathamatical operation with sets"
A = set({3,4,7,8})
B = set({1,2,9,6})
#Union operation
y = A | B; print(y)
A_inter_B = A&B;print(A_inter_B) # no common values in both sets
A.intersection(B)
A.symmetric_difference(B)
A_diff_B = A -B;print(A_diff_B)