class Person:
    # fname = ''
    # lname = ''   # 어짜피 비어있어서 주석하나 안하나 노상관

    def __init__(self, fname, lname):
        self.fname = fname        #  위에서 지은 이름은 fname, lname 에 집어넣는다
        self.lname = lname



    def printname(self):
        print(self.fname, self.lname)

xman = Person('jw', 'hong')

xman.printname()