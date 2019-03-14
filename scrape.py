import re
import requests
from bs4 import BeautifulSoup

writtenlinks = []
counter = 1

while True:
    src = requests.get('https://www.bing.com/search?q=https%3a%2f%2fanonfile.com%2f+site%3ahttps%3a%2f%2fanonfile.com%2f&first='+str(counter)+'&FORM=PERE', timeout=10).text
    links = src.split('<h2><a href="')[1:]
    for link in links:
        link = link.split('"')[0]
        if link in writtenlinks:
            continue
        else:
            handle = open('links.txt', 'a')
            handle.write(link+'\n')
            print(link)
            writtenlinks.append(link)
    src = requests.get('https://www.bing.com/search?q=https%3a%2f%2fanonfile.com%2f+site%3ahttps%3a%2f%2fanonfile.com%2f&first='+str(counter)+'&FORM=PERE2', timeout=10).text
    links = src.split('<h2><a href="')[1:]
    for link in links:
        link = link.split('"')[0]
        if link in writtenlinks:
            continue
        else:
            handle = open('links.txt', 'a')
            handle.write(link+'\n')
            print(link)
            writtenlinks.append(link)
    src = requests.get('https://www.bing.com/search?q=https%3a%2f%2fanonfile.com%2f+site%3ahttps%3a%2f%2fanonfile.com%2f&first='+str(counter)+'&FORM=PERE3', timeout=10).text
    links = src.split('<h2><a href="')[1:]
    for link in links:
        link = link.split('"')[0]
        if link in writtenlinks:
            continue
        else:
            handle = open('links.txt', 'a')
            handle.write(link+'\n')
            print(link)
            writtenlinks.append(link)
    src = requests.get('https://www.bing.com/search?q=https%3a%2f%2fanonfile.com%2f+site%3ahttps%3a%2f%2fanonfile.com%2f&first='+str(counter)+'&FORM=PERE4', timeout=10).text
    links = src.split('<h2><a href="')[1:]
    for link in links:
        link = link.split('"')[0]
        if link in writtenlinks:
            continue
        else:
            handle = open('links.txt', 'a')
            handle.write(link+'\n')
            print(link)
            writtenlinks.append(link)
    counter += 10
