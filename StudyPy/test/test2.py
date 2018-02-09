import re

# pattern=re.compile(r'hello')
# match=pattern.match('helloworldsjljjhello')
match=re.match(r'hello','helloworldsss')
if match:
    print match.group()
else:
    print('none')