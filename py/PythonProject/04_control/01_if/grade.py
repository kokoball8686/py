import sys


score = int(input('Score: '))
if 100 >= score >= 81:
    print('grade is A')
elif 80 >= score >= 61:
    print('grade is B')
elif 60 >= score >= 41:
    print('grade is C')
elif 40 >= score >= 21:
    print('grade is D')
elif 20 >= score >= 0:
    print('grade is E')
else:
    print('fail 끄세요')
    sys.exit(1)