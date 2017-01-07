__author__ = 'Perkel'


# first class function

def print_text(text):
    print text

x = print_text

x('12')

# higher order function


def outer_function(tag):
    def inner_function(message):
        print '<'+tag+'>'+message+'</'+tag+'>'
    return inner_function


BOLD = outer_function('BOLD')
ITALIC = outer_function('ITALIC')

BOLD("Let's get down to business")
ITALIC("Let's get down to business")


# DECORATORS


def decorator_function(original_function):
    """
    This allows to add additional code inside premade function
    :param original_function: original function you want to change.
    :return: returns original function with new code in it.
    """
    def wrapper_function():
        # insert code here
        print 'TO BAD'

        # insert code here
        original_function()
    return wrapper_function

@decorator_function
def print_number():
    print '12'

print_number()

