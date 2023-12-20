import urllib
import urllib.request, urllib.parse, urllib.error 
from bs4 import BeautifulSoup

# x =urllib.open("https://www.ngkntk.co.jp").read()
x = urllib.request.urlopen("https://querycode.ir")
y = BeautifulSoup(x , "html.parser")


for link in y.find_all("a"):
    z = link.get("href")
    print(z)
    print("================================================")
# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>

# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>

# <p class="story">...</p>
# """
# from bs4 import BeautifulSoup

# soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())

# soup.title



#######################################3333333333
# import requests
# import time
# time .sleep(5)
# x = requests.get ("https://iplocation.com",proxies=dict(https='socks5://1.2.3.4:8080'))
# # Proxy setting: http://username:pass#123@proxy:8080

# print(x.content)




