import requests
import time

from bs4 import BeautifulSoup

# About 2 requests per second
delay = 0.5

list_url = 'http://mim.maltaenterprise.com/default.asp?page=list&show=0&disp={}'
start_number = 11
current_number = start_number


def get_a_tags(number):
    response = requests.get(url=list_url.format(number))
    soup = BeautifulSoup(response.text, 'lxml')
    content_td = soup.find_all('td', {'class': 'content'})[2]
    content_table = content_td.find('table', {'width': '100%'})
    return content_table.find_all('a')

a_tags = get_a_tags(current_number)
# if there is nothing in the tbody, then there are no companies listed
while len(a_tags) > 0:
    print('Scraping Page: {}'.format(current_number // 10))
    # get all hrefs from the a tags
    hrefs = [a_tag['href'] for a_tag in a_tags]
    # write the links to a file
    with open('links.txt', 'a', encoding='utf-8') as links_file:
        for href in hrefs:
            links_file.write('{}{}\n'.format('http://mim.maltaenterprise.com/', href))
    # add on 10 to the current number and get the next page
    current_number += 10
    a_tags = get_a_tags(current_number)
    time.sleep(delay)
