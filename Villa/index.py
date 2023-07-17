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


from selenium import webdriver
# مسیر فایل درایور مرورگر را تعیین کنید
driver_path = '/home/siyamak/Documents/Python-Course/Villa/chromedriver_linux64/chromedriver'
# ایجاد نمونه از مرورگر Chrome با استفاده از درایور مرورگر
driver = webdriver.Chrome(driver_path)
# آدرس وبسایت مورد نظر را تعیین کنید
website_url = 'http://villaarzan.com'
# باز کردن صفحه وب در مرورگر
driver.get(website_url)
# یافتن تمام تگ‌های img در صفحه
img_tags = driver.find_elements_by_tag_name('img')
# استخراج لینک‌های عکس
image_links = []
for img_tag in img_tags:
    src = img_tag.get_attribute('src')
    if src:
        image_links.append(src)
# نمایش لینک‌های عکس
for image_link in image_links:
    print(image_link)
    with open("vlilla.log", "a") as file:
        file.write(image_link)
# بستن مرورگر
driver.quit()


