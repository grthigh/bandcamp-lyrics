#!/usr/bin/python3
# Get Album lyrics from Bandcamp website and save 'em

"""Usage:
  bandcamp-lyrics.py <url> [--output=<folder>]
  bandcamp-lyrics.py (-h | --help)
  bandcamp-lyrics.py (--version)

Options:
  -h --help                 Show this screen.
  -v --version              Show version.
  -o --output=<folder>      Store the lyrics in this folder."""
from docopt import docopt
import os
import urllib.request
from bs4 import BeautifulSoup

def main(url):
    try:
        with urllib.request.urlopen(url) as response:
            soup = BeautifulSoup(response)
    except:
        print("Make sure your connection is working.")
        exit()
    url = url[:(url.index('.com') + 4)]
    for tag in soup.find_all('a'):
        link = tag.get('href')
        name = tag.get_text()
        if name == 'lyrics':
            link = url + link.replace('#lyrics', '')
            get_lyrics(link)

def get_lyrics(link):
    with urllib.request.urlopen(link) as response:
        soup = BeautifulSoup(response)
    lyrics_text = soup.find(class_='tralbumData lyricsText')
    text = lyrics_text.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    name = link[(link.index('track/') + 6):].replace('-', ' ').title()
    with open(name + '.txt', mode='w', encoding='utf-8') as f:
        f.write(text)
    print(('This lyrics track: {0} has been saved successfully.'.format(name)))

if __name__ == '__main__':
    arguments = docopt(__doc__, version='bandcamp-lyrics 2.3')
    url = arguments['<url>']
    if url.find('http') == -1:
        url = "http://" + url
    if arguments['--output']:
        if os.path.exists(arguments['--output']):
            os.chdir(arguments['--output'])
    else:
        os.makedirs('lyrics')
        os.chdir('lyrics')
    main(url)
    print("I have a good news:\n  All of the album lyrics  has been saved")
