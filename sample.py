
'''
1. Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and 
makes a new list of only the first and last elements of the given list. 
For practice, write this code inside a function.
'''

def list_end(a):
    return a[0], a[-1]

print(list_end(a = [5, 10, 15, 20, 25]))



# 2

def area(n):
    pi = 3.14
    area = n * pi**2
    return area

print(area(5))