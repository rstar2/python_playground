from string import Template

# The format uses placeholder names formed by $ with valid Python identifiers
#  (alphanumeric characters and underscores).
# Surrounding the placeholder with braces allows it to be followed
# by more alphanumeric letters with no intervening spaces.
# Writing $$ creates a single escaped $:
t = Template('${village}folks send $$10 to $cause.')

x = t.substitute(village='Nottingham', cause='the ditch fund')

print(x)

t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
#  this will raise KeyError: 'owner' exception
# t.substitute(d)

t.safe_substitute(d) # will return 'Return the unladen swallow to $owner.'
