from bs4 import BeautifulSoup


def parse(source):
    soup = BeautifulSoup(source, 'html.parser')

    data = {
        'question': None,
        'answers': [],
    }

    question = soup.find('div', {'id': 'question'})
    data['question'] = question.encode_contents().decode("cp1252")

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

def get_possible_answer_indices(source):
    soup = BeautifulSoup(source, 'html.parser')
    valid = []

    button_divs = soup.find_all('td', {'class': 'button'})
    for i,button in enumerate(button_divs):
        src = button.find('a').find('img')['src']
        if 'dim' not in src:
            valid.append(i)
    return valid