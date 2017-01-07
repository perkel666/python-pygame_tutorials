__author__ = 'Perkel'


from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])

color1 = Color(100, 200, 100)
color2 = Color(20, 20, 20)
color3 = Color(10, 10, 10)

print color1.green
print color2.red
print color3.blue