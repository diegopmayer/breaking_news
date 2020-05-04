def scrap_link():

    """ Return Three lists, titles, links and imgs from 
        google trends page """
    
    import pandas as pd
    from requests import get, post
    from bs4 import BeautifulSoup as bs
    from selenium import webdriver 
    from webdriver_manager.chrome import ChromeDriverManager

    #---------------------------link from google trends daily
    url = 'https://trends.google.com.br/trends/trendingsearches/daily?geo=BR'

    #---------------------------Make parser and put to the soup
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(url)
    soup = bs(browser.page_source, 'html.parser')
    browser.close()

    #---------------------------Get the title and links from google
    #links, titles, imgs = [], [], []
    posts = []
    for getLink in soup.find_all('div', {'ng-if':"::imageUrl"}):
        title = getLink.find('a').get('title')
        linkHref = getLink.find('a').get('href')
        img = getLink.find('img').get('src')
        posts.append(
            {'title':title,
            'link':linkHref,
            'img':img,
            })
    
    #---------------------------return a list of Links and Titles
    return posts