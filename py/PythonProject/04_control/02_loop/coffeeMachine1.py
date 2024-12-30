


cf = 5



while True:
    if cf == 0:
        print('커피가 없네요')
        break

    userm = int(input('돈 넣으세요.'))




    if userm > 300:
        print('커피 드세요')
        print('잔돈입니다. %d 원을 돌려드릴게요' % (userm % 300) )
        cf -= userm // 300
        print('남은 커피 개수: ', cf)

    elif userm == 300:
        print('커피 드세요')
        print('거스름돈은 없습니다.')
        cf -= 1
        print('남은 커피 개수: ', cf)

    else:
        print('금액이 부족합니다, 투입하신 %d 원을 돌려드릴게요' % userm)


