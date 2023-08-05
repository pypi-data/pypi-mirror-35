from bs4 import BeautifulSoup


def bs4_fix_html(html):
    soup = BeautifulSoup(html, 'fast')
    return soup.prettify()
