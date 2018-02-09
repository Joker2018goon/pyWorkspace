import re

p = re.compile(r'(\w+) (?P<sign>.*)(\w+)', re.DOTALL)

print "p.pattern:", p.pattern
print "p.flags:", p.flags
print "p.groups:", p.groups
print "p.groupindex:", p.groupindex