from bs4 import BeautifulSoup
import os
from selenium import webdriver


def create_list(items, filename):
    filename = filename.replace('https://tbc.wowhead.com/guides/', '')
    output_filename = "temp_files/item_lists/" + filename + ".txt"

    if os.path.exists(output_filename):
        os.remove(output_filename)

    os.makedirs(os.path.dirname(output_filename), exist_ok=True)
    file_output = open(output_filename, 'x')

    for item in items:
        file_output.write(item + '\n')

    file_output.close()

    print("Completed: " + output_filename)


def get_input_files(file):
    urls = set(line.strip() for line in open(file))
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    browser = webdriver.Chrome(executable_path='vendor/chromedriver.exe', options=options)

    for url in urls:
        browser.get(url)
        items = get_items(browser)
        create_list(items, url)

    browser.quit()


def get_items(browser_source):
    html_content = browser_source.page_source
    soup = BeautifulSoup(html_content, "html.parser")

    items = set()

    for table in soup.find_all('table', class_="grid max-width"):
        # print(table)
        for tr in table.find_all('tr'):
            for td in tr.find_all('td')[1:2]:
                for a in td.find_all('a', href=True):
                    if 'https://tbc.wowhead.com/item=' in a['href']:
                        item_id = a['href'].split('/')[3].split('=')[1]
                        items.add(item_id)
                    else:
                        items.add(a['href'].replace('/item=', ''))
    return items
