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