from selenium import webdriver

from parser import parse
from solver import NonogramSolver


def main():
    url = 'http://www.puzzle-nonograms.com/?size=1'

    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    driver.get(url)

    json = parse(driver.page_source)

    solver = NonogramSolver(json)
    solver.solve()
    solution = solver.result()


if __name__ == '__main__':
    main()