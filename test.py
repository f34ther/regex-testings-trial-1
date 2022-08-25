
# with open(r'regex_test') as f:
#     data = f.readlines()

names = ('Abraham Lincoln', 'Andrew P Garfield', 'Connor Milliken', 'Jordan Alexander', 'Williams Madonna',
         'programming is cool')

pattern = re.compile("([A-Z][a-z]+), ([A-Z][a-z])")

for person in data:
    match = pattern.search(person)
    if match:
        print('\nf"{match.group(1)} {match.group(2)}"')
