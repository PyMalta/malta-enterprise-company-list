import json
import os

from bs4 import BeautifulSoup

html_files = os.listdir('pages')
print('Parsing {} HTML files'.format(len(html_files)))
all_content = []
for file in html_files:
    with open('pages/{}'.format(file), 'r', encoding='utf-8') as html_file:
        data = html_file.read()
    print('Reading data for: {}'.format(file))
    soup = BeautifulSoup(data, 'lxml')
    content_td = soup.find_all('td', {'class': 'content'})[2]
    data_rows = content_td.find_all('tr')
    title = data_rows[0].text.strip()
    address = '{}\n{}\n{}'.format(
        data_rows[1].find_all('td')[1].text.strip(),
        data_rows[2].find_all('td')[1].text.strip(),
        data_rows[3].find_all('td')[1].text.strip()
    )
    content = {
        'title': title,
        'address': address,
        'id': file.replace('.html', '')
    }
    # gather the rest dynamically as they vary
    # some companies don't have a website listed for example
    for i in range(4, len(data_rows)):
        tds = data_rows[i].find_all('td')
        # skip sectors data for now
        if tds[0].text.strip() == 'List of sectors':
            break
        key = tds[0].text.strip()
        value = tds[1].text.strip()
        content[key] = value
    all_content.append(content)

# write all the content to a json file
with open('all_data.json', 'w', encoding='utf-8') as data_file:
    data_file.write(json.dumps(all_content))
