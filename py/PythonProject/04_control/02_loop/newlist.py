file_lists = ['hello.py', 'ex01.py', 'ex02.py', 'ch02.py', 'intro.hwp']






output_lists = []

for file in file_lists:
    output_lists.append(''.join(file.split('.')[:-1]))

print(output_lists)