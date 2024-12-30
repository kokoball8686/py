import sys

def communication(number):

    if number == '011':
        RET == 'SKT'
    elif number == '016':
        RET == 'KT'
    elif number == '019':
        RET == 'LGT'
    elif number == '010':
        RET == 'UNKOWN'
    else:
        RET == 'UNKOWN'

    return RET

phone_number = input("휴대전화번호 입력: ")
first = phone_number.split('-')[0]
comm = communication(first)

if   comm == 'SKT'   : print('당신은 %s 사용자입니다.' % comm)
elif comm == 'KT'    : print('당신은 %s 사용자입니다.' % comm)
elif comm == 'LGT'   : print('당신은 %s 사용자입니다.' % comm)
elif comm == 'UNKOWN': print('당신의 통신사는 알수 없습니다.')
else: sys.exit(1)