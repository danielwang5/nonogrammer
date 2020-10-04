from bs4 import BeautifulSoup

def parse(source):
    soup = BeautifulSoup(source, 'html.parser')

    data = {
        'question': None,
        'answers': [],
    }