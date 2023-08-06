#!/usr/bin/env python

'''
BUGS: 

TO DO:  - assign as metadata track number and album name if not originally assigned
        - change album folder name to "[year] artist - album"
        - add --hierarchy parameter and some useful hierarchy schemes (ex.: /artist/album/track,
        /artist/album/n. track, /artist - album/track, /artist - album/n. track
'''

import requests
import urllib
import os
from bs4 import BeautifulSoup

def get_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def download(url, directory):
    if(url.find("/track/") != -1 or url.find("/album/") != -1):
        download_tracks(url, directory) # Album and tracks HTMLs follow the same structure
    elif(url.find("/music") != -1):
        download_artist(url, directory)
    else:
        download_artist(url + "/music", directory)

def download_artist(url, directory):
    artist_soup = get_soup(url)
    links = artist_soup.find_all('a')
    album_links = []
    album_titles = []
    i = 0

    # Searches the tree finding albums and prints them in order
    # then, album links are stored in a list
    for link in links:

        # Albums have an 'href' attribute and 'album' string in it
        if (link.has_attr('href') and 'album' in link['href']) and not 'help/downloading' in link['href']:
            
            # In case album's url contains '.bandcamp.', it means that the path to the
            # album's page is not relative, becouse it is stored in another artist's profile
            if('.bandcamp.' in link['href']):
                # Albums's text contains some extra spaces and lines, this statement
                # deletes some of them making the print cleaner
                title = link.find('p').text.split('\n')[-3]
                album_titles.append(title[11:])
                album_links.append(link['href'])
            else:
                title = link.find('p').text.split('\n')[-3]
                album_titles.append(title[12:])
                album_links.append(url.split('/music')[0] + link['href'])
              
    for i in range (0, len(album_links)):
        print("ALBUM: " + album_titles[i])
        print(album_links[i])
        download_tracks(album_links[i], directory)

def download_tracks(url, directory):
    album_soup = get_soup(url)
    album = album_soup.prettify()

    # Album info starts in 'trackinfo' and ends with '}],'
    album_info_start = album.find('trackinfo: [')
    album_info_end = album.find('}],', album_info_start)
    album_info = album[album_info_start:album_info_end + 2]
    album_info = album_info.replace('trackinfo: ', '')

    # Although 'album_info' string is a JavaScript dict, we can make
    # some changes to it to make it legible as a Python dict
    album_info = album_info.replace('false', 'False').replace('true', 'True').replace('null', 'None')
    album_info = eval(album_info)
    urls = []
    track_names = []

    # Iterates album_info searching for urls and puts them into a list called 'urls'
    # Track names are stored in another list, download urls and names are in order
    for word in range(0, len(album_info)):
        urls.append(str(album_info[word]['file']['mp3-128']))
        track_names.append(album_info[word]['title'].replace('/', ' '))
    
    i = 0
    for url in urls:
        track_name = track_names[i]
        download_track(url, directory, track_name)
        i = i + 1
    print()

def download_track(url, directory, track_name):
    print('Downloading: ' + track_name)
    file_dir = directory + '/' + track_name + '.mp3'
    data = urllib.request.urlopen(url).read()
    mp3 = open(file_dir, 'wb')
    mp3.write(data)
    mp3.close()
