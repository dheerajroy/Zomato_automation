
import search
from time import sleep


class Main:
    def __init__(self):
        self.email = input('Enter your email address: ')
        self.pw = input('Enter your password: ')
        self.s = input('Enter the item: ')
        search.Search(self.s, self.email, self.pw)
        while True:
            pass


if __name__ == '__main__':
    obj = Main()
