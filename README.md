# bandcamp-lyrics
Download Lyrics Albums on Bandcamp.

# Installation 
1. Clone the project, download [the zip file](https://github.com/grthigh/bandcamp-lyrics/archive/master.zip) or just download the script
2. Put it in whatever folder you like.
3. cd to the directory that contains bandcamp-lyrics.py file.
4. use 'pip -r requiremtents.txt' to download requirements of the package ( BeatifulSoup4 and Docopt ).

# Description 
This is an automated tool to download the album's lyrics of your choice from Bandcamp. It requires Python3 and an Internet connection of course :D

# Requiremtents 
   BeautifulSoup4
   
   Docopt
# Deatils
    Usage:
     bandcamp-lyrics.py <url> [--output=<folder>]
     bandcamp-lyrics.py (-h | --help)
     bandcamp-lyrics.py (--version)

    Options:
     -h --help                 Show this screen.
     -v --version              Show version.
     -o --output=<folder>      Store the lyrics in this folder.
# Dependencies

* [Python3](https://www.python.org/downloads/) - Python 3.2 or later
* [BeautifulSoup](https://pypi.python.org/pypi/beautifulsoup4) - For parsing the pages
* [Docopt](https://pypi.python.org/pypi/docopt) - For beautiful command-line interface

