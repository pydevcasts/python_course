import urllib
import urllib.request, urllib.parse, urllib.error 
from bs4 import BeautifulSoup

# x =urllib.open("https://www.ngkntk.co.jp").read()
x = urllib.request.urlopen("https://academybime.com")
# y = BeautifulSoup(x , "html.parser")


# for link in y.find_all("a"):
    # z = link.get("href")
    # print(z)
    # print("================================================")
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

soup = BeautifulSoup(x, 'html.parser')

print(soup.prettify())

soup.title



#######################################3333333333
# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin

# # آدرس وبسایت مورد نظر را تعیین کنید
# website_url = 'http://villaarzan.com'

# # ارسال درخواست GET به سایت
# response = requests.get(website_url)

# # بررسی موفقیت درخواست
# if response.status_code == 200:
#     # تبدیل محتوای صفحه به شیء BeautifulSoup
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # یافتن تمام لینک‌های صفحه
#     img_tags = soup.find_all('img')

#     # استخراج لینک‌های فایل
#     image_links = []
#     for img_tag in img_tags:
#         src = img_tag.get('src')
#         if src:
#             image_links.append(src)

#     # نمایش لینک‌های عکس
#     for image_link in image_links:
#         print(image_link)
# else:
#     print('خطا:', response.status_code)
