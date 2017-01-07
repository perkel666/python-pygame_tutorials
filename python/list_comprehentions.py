__author__ = 'Perkel'

words = ['Adam', 'Eve', 'Willy', 'Adrian']


new_list = ['his name is: '+n for n in words if n != 'Adam']

print new_list