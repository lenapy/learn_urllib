import re

example_string = 'Jessica is 15 years old, and Daniel is 27 years old.' \
                'Edward is 97, and his grandfather, Oscar, is 102.'

ages = re.findall(r'\d{1,3}', example_string)
names = re.findall(r'[A-Z][a-z]*', example_string)

data = dict(zip(names, ages))
print(data)

age_dict = {}
x = 0
for name in names:
    age_dict[name] = ages[x]
    x += 1
print(age_dict)

