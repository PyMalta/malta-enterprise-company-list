import requests
import time
import os

# About 2 requests per second
delay = 0.5

# Create the directory to hold the HTML files if it does not exist
if not os.path.isdir('pages'):
    os.mkdir('pages')

with open('links.txt', 'r', encoding='utf-8') as links_file:
    # for each link,
    for link in links_file:
        # Remove the new line
        link = link.strip()
        print('Downloading HTML for link: {}'.format(link))
        # Get the page contents
        response = requests.get(url=link)
        company_id = link.replace('http://mim.maltaenterprise.com/default.asp?page=companyb&show=', '')
        with open('pages/{}.html'.format(company_id), 'w', encoding='utf-8') as html_file:
            html_file.write(response.text.strip())
        time.sleep(delay)
