__author__ = 'Perkel'

import re

s = '[Event:23]'
start = "["
end = "]"

result = re.search(r'\[(.*)\]', s).group(1)
print result

