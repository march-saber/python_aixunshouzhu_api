import re


number = 'E4:34:93:5B:B9:C4|78:44:FD:A4:17:7B|02|0c|7|-43|hao123|1|0|0|1|1'
number2 = 'E4:34:93:5B:B9:C4|78:44:FD:A4:17:7B|01|0c|7|-43|hao123|1|0|0|1|0'

# p = "-[0-9]*"
p = "(-)[1-9]*"

m = re.search(p,number)
print(m)
g = m.group()
# print(m.group(1))
print(number.index('43'))
# print(number.replace(g,''))
print(re.sub(g,' ',number))



