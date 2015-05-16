#!/usr/bin/python3
# Get Album lyrics from Bandcamp website and save 'em

import urllib.request
from bs4 import BeautifulSoup
import argparse
import os

def get_database(url):
    links = []
    urls = []
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
    except:
        print("Make sure you're connection is working.")
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
    info = "Download Album lyrics from bandcamp."
    parser = argparse.ArgumentParser(description=info)
    parser.add_argument("url", help="The url of the album")
    parser.add_argument("-o", type=str, help="Save they lyrics in this folder")
    args = parser.parse_args()
    url = args.url
    output_folder = args.o
    handle_url = url.find('http')
    if handle_url == -1:
        url = "http://" + url
    urls = get_database(url)
    if not args.o:
        os.makedirs('lyrics')
        os.chdir('lyrics')
        print("The lyrics folder has been created to store the lyrics there")
    elif os.path.exists(output_folder):
        os.chdir(output_folder)
    else:
        print(("You didn't specify a valid folder. I'll set one for you on" +
                " The same folder as this script. "))
    for link in urls:
        text = get_page(link)
        index = link.index('track/') + 6
        name = link[index:]
        name = name.replace('-', ' ').title()
        save_lyrics(text)
    print("I have a good news:\n  All of the Album lyricses  has been saved :)")

