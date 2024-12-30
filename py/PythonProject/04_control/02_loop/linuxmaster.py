marks = [90, 25, 67, 45, 80]


number = 0

for i in marks:
    number += 1
    #print(i)
    if str(i) >= '60':
        print('%d 번 학생: ok' % number)
    else:
        print('%d 번 학생: fail' % number)