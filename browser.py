import sys
import os
import requests
from bs4 import BeautifulSoup
from collections import deque
from colorama import Fore, Style


def create_dir(dir_name):
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        print("Directory ", dir_name, " already exists")


def create_website_file(directory_name, url_site):
    current_dir = os.getcwd() + '\\' + directory_name
    file_name = url_site.strip(".com")
    website = scrap_website(url_site)
    with open(os.path.join(current_dir, file_name), 'w', encoding='utf-8') as f:
        f.write(website)


def read_website_file(directory_name, url_site):
    file_name = url_site.strip(".com")
    current_dir = os.getcwd() + '\\' + directory_name
    with open(os.path.join(current_dir, file_name), 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())


def scrap_website(url):
    base_url = 'https://'
    main_url = base_url + url
    print(main_url)
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    r = requests.get(main_url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    page_content = soup.get_text()
    return Fore.BLUE + page_content


# Get all the data arguments
args = sys.argv

viewed_tabs = deque()

if len(args) != 2:
    print("The script should be called with two arguments")
else:
    # Call to the create directory method
    create_dir(args[1])
    # Receive the name of the file
    while True:
        file = input().strip()
        if file[-4:] == '.com' or file[-4:] == '.org':
            create_website_file(args[1], file)
            read_website_file(args[1], file)
            viewed_tabs.append(file)
        elif file == 'back':
            if len(viewed_tabs) > 0:
                current_page = viewed_tabs.pop()
                read_website_file(args[1], viewed_tabs.pop())
                viewed_tabs.append(current_page)
        elif file == 'exit':
            break
        else:
            print("Error, the URL should include '.com' or '.org' at the end or be spelled correctly")


