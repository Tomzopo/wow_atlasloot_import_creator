from bs4 import BeautifulSoup
import os
import requests


def create_list(items, filename):
    filename = filename.replace('https://tbc.wowhead.com/guides/', '')
    output_filename = "temp_files/item_lists/" + filename + ".txt"
    if os.path.exists(output_filename):
        os.remove(output_filename)
    file_output = open(output_filename, 'x')

    for item in items:
        file_output.write(item + '\n')

    file_output.close()


def get_input_files(file):

    urls = set(line.strip() for line in open(file))
    for url in urls:
        items = get_items(url)
        create_list(items, url)


def get_items(url):
    # url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")

    items = set()

    for table in soup.find_all('table'):
        for tr in table.find_all('tr'):
            for td in tr.find_all('td')[1:2]:
                for a in td.find_all('a'):
                    items.add(a['href'].replace('/item=', ''))

    return items
