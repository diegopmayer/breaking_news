def scrap_link():

    """ Return Three lists, titles, links and imgs from 
        google trends page """
    
    import pandas as pd
    from requests import get, post
    from bs4 import BeautifulSoup as bs
    from selenium import webdriver 

    #---------------------------link from google trends daily
    url = 'https://trends.google.com.br/trends/trendingsearches/daily?geo=BR'

    #---------------------------Make parser and put to the soup
    browser = webdriver.Chrome()
    browser.get(url)
    soup = bs(browser.page_source, 'html.parser')
    browser.close()

    #---------------------------Get the title and links from google
    links, titles, imgs = [], [], []
    for getLink in soup.find_all('div', {'ng-if':"::imageUrl"}):
        title = getLink.find('a').get('title')
        linkHref = getLink.find('a').get('href')
        img = getLink.find('img').get('src')
        links.append(linkHref), titles.append(title), imgs.append(img)
    
    #---------------------------return a list of Links and Titles
    return titles, links, imgs