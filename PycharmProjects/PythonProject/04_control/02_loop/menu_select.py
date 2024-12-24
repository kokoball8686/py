def add():
    print('ADD')

def delete():
    print('DEL')

def list():
    print('LIST')


prompt = """
    1. add
    2. del
    3. list
    4. quit
"""


while True:
    print(prompt)
    choice = input('Enter your number? (1|2|3|4): ')
    if choice == '1':
        add()
    elif choice == '2':
        delete()
    elif choice == '3':
        list()
    elif choice == '4':
        break
    else:
        print('돌아가~')
