import fileinput

week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

for line in fileinput.input():
    input = line.replace('\n', '').split(' ')

    print(input)
