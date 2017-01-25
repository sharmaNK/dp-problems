import re

def comparator(item):
    num = re.findall('\d+', item)
    if len(num) > 0:
        return num[0]
    else:
        return item

data = ['boy1', 'boy3', 'boy2', 'girl']
sorted(data, key=comparator)
print data