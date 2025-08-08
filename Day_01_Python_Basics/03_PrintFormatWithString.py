#String Formatting Examples


# String formatting lets you inject items into a string rather than chaining them with concatenation.

# Oldest method: placeholders with % operator
print("I'm going to inject %s here." % 'something')

# Multiple items using tuple
print("I'm going to inject %s text here, and %s text here." % ('some', 'more'))

# Using variables
x, y = 'some', 'more'
print("I'm going to inject %s text here, and %s text here." % (x, y))

# %s vs %r for string representations
print('He said his name was %s.' % 'Fred')
print('He said his name was %r.' % 'Fred')

# Escape characters with %r
print('I once caught a fish %s.' % 'this \tbig')
print('I once caught a fish %r.' % 'this \tbig')

# %s converts to string, %d converts to integer (truncates floats)
print('I wrote %s programs today.' % 3.75)
print('I wrote %d programs today.' % 3.75)

# Padding and precision for floats: %5.2f
print('Floating point numbers: %5.2f' % (13.144))
print('Floating point numbers: %1.0f' % (13.144))
print('Floating point numbers: %1.5f' % (13.144))
print('Floating point numbers: %10.2f' % (13.144))
print('Floating point numbers: %25.2f' % (13.144))

# Multiple formatting types in one print
print('First: %s, Second: %5.2f, Third: %r' % ('hi!', 3.1415, 'bye!'))

# Using .format() method
print('This is a string with an {}'.format('insert'))

# .format() method advantages:
# 1. Insert objects by index
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))

# 2. Insert objects by keywords
print('First Object: {a}, Second Object: {b}, Third Object: {c}'.format(a=1, b='Two', c=12.3))

# 3. Reusing inserted objects
print('A %s saved is a %s earned.' % ('penny', 'penny'))
print('A {p} saved is a {p} earned.'.format(p='penny'))

# Alignment, padding, and precision with .format()
print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:9}'.format('Apples', 3.))
print('{0:8} | {1:9}'.format('Oranges', 10))

# Alignment options: < left, ^ center, > right
print('{0:<8} | {1:^8} | {2:>8}'.format('Left', 'Center', 'Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11, 22, 33))

# Padding with characters
print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left', 'Center', 'Right'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11, 22, 33))

# Field widths and float precision with .format()
print('This is my ten-character, two-decimal number:%10.2f' % 13.579)
print('This is my ten-character, two-decimal number:{0:10.2f}'.format(13.579))

# Formatted string literals (f-strings) - Python 3.6+
name = 'Fred'
print(f"He said his name is {name}.")
print(f"He said his name is {name!r}")

# Float formatting with f-strings
num = 23.45678
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")

num = 23.45
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")

# Using .format() syntax inside f-strings for precision
num = 23.45
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:10.4f}")

