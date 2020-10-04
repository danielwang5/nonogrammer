from bs4 import BeautifulSoup

def parse(source):
    soup = BeautifulSoup(source, 'html.parser')

    data = {'r':[], 'c':[]}

    # get row data
    task_row = soup.find('div', {'id': 'taskLeft'})
    rows = task_row.find_all('div', {'class': 'task-group'})
    for row in rows:
        r = []
        cells = row.find_all('div', {'class': 'task-cell'})
        for cell in cells:
            if len(cell.text) > 0:
                r.append(int(cell.text))
        data['r'].append(r)

    # get column data
    task_col = soup.find('div', {'id': 'taskTop'})
    cols = task_col.find_all('div', {'class': 'task-group'})
    for col in cols:
        c = []
        cells = col.find_all('div', {'class': 'task-cell'})
        for cell in cells:
            if len(cell.text) > 0:
                c.append(int(cell.text))
        data['c'].append(c)
    #print(data)

    return data
