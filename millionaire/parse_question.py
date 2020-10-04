from bs4 import BeautifulSoup


def parse(source):
    soup = BeautifulSoup(source, 'html.parser')

    data = {
        'question': None,
        'answers': [],
    }

    question_div = soup.find('div', {'id': 'question'})
    question = question_div.find('p')
    data['question'] = question.text

    answer_divs = soup.find_all('td', {'class': 'text'})
    for answer_div in answer_divs:
        answer = answer_div.find('a')
        data['answers'].append(answer.text)

    return data


# check if the website says its correct
def check_correct(source):
    soup = BeautifulSoup(source, 'html.parser')

    quit = soup.find('div', {'id': 'quit'})
    quit_a = quit.find('a')
    quit_a_img = quit_a.find('img')
    text = quit_a_img['alt']

    if text == 'Play again!':
        return False
    return True