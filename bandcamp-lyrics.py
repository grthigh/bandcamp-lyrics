#!/usr/bin/python3
# Get Album lyrics from Bandcamp website and save 'em

"""bandcamp-lyrics
Usage:
  bandcamp-lyrics.py <url> [--output=<folder>]
  bandcamp-lyrics.py (-h | --help)
  bandcamp-lyrics.py (--version)

Options:
  -h --help                 Show this screen.
  -v --version              Show version.
  -o --output=<folder>      Store the lyrics in this folder.
"""
from docopt import docopt
import os
import urllib.request
from bs4 import BeautifulSoup

def get_database(url):
    links = []
    urls = []
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
    except:
        print("Make sure your connection is working.")
        exit()
    index = url.index('.com') + 4
    url = url[:index]
    soup = BeautifulSoup(data)
    for tag in soup.find_all('a'):
        link = tag.get('href')
        name = tag.get_text()
        if name == 'lyrics':
            link = link.replace('#lyrics', '')
            links.append(link)
    for link in links:
        urls.append(url + link)
    return urls

def get_page(link):
    with urllib.request.urlopen(link) as response:
        page = response.read()
    soup = BeautifulSoup(page)
    for tag in soup():
        for attribute in ["class", "id", "name", "style"]:
            del tag[attribute]
    for script in soup(["script", "style"]):
        script.extract()
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    text.encode('utf-8')
    return text

def save_lyrics(text):
    start_with = text.find('lyrics')
    start_with += 7  # Avoid typing lyrics itslef
    end_with = text.find('credits')
    lyrics = text[start_with:end_with]
    with open(name + '.txt', mode='w', encoding='utf-8') as f:
        f.write(lyrics)
    print(('This lyrics track: {0} has been saved successfully.'.format(name)))

if __name__ == '__main__':
    arguments = docopt(__doc__, version='bandcamp-lyrics 2.1')
    url = arguments['<url>']
    handle_url = url.find('http')
    if handle_url == -1:
        url = "http://" + url
    urls = get_database(url)
    if arguments['--output']:
        if os.path.exists(arguments['--output']):
            os.chdir(arguments['--output'])
    else:
        os.makedirs('lyrics')
        os.chdir('lyrics')
        print("The lyrics folder has been created to store the lyrics there")
    for link in urls:
        text = get_page(link)
        index = link.index('track/') + 6
        name = link[index:].replace('-', ' ').title()
        save_lyrics(text)
    print("I have a good news:\n  All of the album lyrics  has been saved")

