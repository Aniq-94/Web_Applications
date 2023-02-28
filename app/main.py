import sys

from app.utils import utils as u


def main():
    greeting: str = u.greet('Johh','Doe')
    print(greeting)

if __name__ =='main':
    main()