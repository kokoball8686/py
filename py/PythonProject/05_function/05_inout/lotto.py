import random


lotto_numbers = []
for i in range(1, 46):
    lotto_numbers.append(i)




def lotto_number(num):
    # input: int(num)
    # output: 숫자 6개(1~45 사이)
    # function: 로또 번호 생성기



    choiced_num = []
    for i in range(num):


        # 1. 번호 섞기
        random.shuffle(lotto_numbers)
        #print(lotto_numbers)

        # 2. 뽑을려는 숫자
        max = len(lotto_numbers)
        choice = random.randint(0, max-1)
        #print(choice)



        # 3. 번호 추출하기
        lotto_num = lotto_numbers.pop(choice)
        # print(lotto_num)
        choiced_num.append(lotto_num)
    print(''.join(str(choiced_num)))


def main():
    lotto_number(6)



main()