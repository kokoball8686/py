import os


ttt = '/home/soldesk/PycharmProjects/PythonProject/07_file/test/'

if not os.path.isdir(ttt):
    os.mkdir(ttt)


ttext = '''
반갑습니다. 
python 개발자 여러분 한살 더 드셨죠!
올 한해는... 행복한 가득한 한해가 되었으면 합니다.
'''

fd = open('test/test.txt', 'w')
fd.write(ttext)
fd.close


fd = open('test/test.txt', 'r')
print(fd.read())