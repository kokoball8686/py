


cf = 5
cfm = 300


while True:
    userm = input('돈 넣으세요.')
    if userm >= 300:
        print('일단패스')
        #!
        #!
    elif userm < 300:
        print('금액이 부족합니다')
        print('%d 원을 돌려드릴게요' % (300 - userm))

    else
