from .links import Links
from .elements import Elements
import nltk
nltk.download('punkt')


def execute(f_query):
    link = Links(f_query)
    link.get_links()
    links = link.results
    elements = Elements(links, 10)
    text = elements.parsing()
    res = ''
    for p in text:
        res += f'{p} \n'
    res += f'\n \n'
    for l in links:
        res += f'{l} \n'
    return res