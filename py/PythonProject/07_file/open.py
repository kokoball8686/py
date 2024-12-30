file = 'filename.txt'

content = """Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!"""

fd = open(file, 'w')
fd.write(content)
fd.close()

fd = open(file)
lines = fd.readlines()

fd.close()

for line in lines:
    print(line, end = '')