import requests
import time

# x = requests.get("http://www.parsiankhazar.ir", timeout=10)
# # print(x.status_code)
# # print(x.url)
# # for key,values  in x.headers.items():
# #     print(key +" = "+ values)
# # print(x.text)
# # print(x.content)
# print(x.cookies)


# y = requests.put("http://parsiankhazar.com/get")
# y = requests.options("http://parsiankhazar.com/get")
# print(id(y))
# # for key, values in y.headers.items():
# #     print(key + " " +  values)
# # print(y.cookies)
# print(y.headers)



# params
# paylod={"key":"value","key2":"value2"}
# x = requests.get("http://parsiankhazar.com", params = paylod)
# print(x.url)


# paylod= {'key1': 'value1', 'key2': ['value2', 'value3']}
# x = requests.get("http://academybime.com", params = paylod)
# print(x.url)
# print(x.encoding)
# x.encoding='ISO-8859-1'
# print(x.encoding)
# y = x.headers

# print(y)


# r = requests.get('https://api.github.com/events', stream=True)
# print(r.row)


# data = {"email":"test@gmail.com",
#         "password":"12345"}
# s = requests.post("http://shalishomal.ir", params=data)
# print(s.status_code)

########################################################################
import requests
import urllib

req = urllib.request.urlopen('https://academybime.com/')
print(req.status)




#  imagefile
# url = 'https://www.python.org/static/opengraph-icon-200x200.png'
# urllib.request.urlretrieve(url, "image-urllib.png")
# با استفاده از request

# url = 'https://www.python.org/static/opengraph-icon-200x200.png'
# x = requests.get(url)
# with open("poing.png", "wb") as file:
#     file.write(x.content)

# PDF
# url = 'https://media.readthedocs.org/pdf/urllib3/latest/urllib3.pdf'
# urllib.request.urlretrieve(url, "pdf-urllib.pdf")



# url = 'https://media.readthedocs.org/pdf/urllib3/latest/urllib3.pdf'
# s = requests.get(url)
# with open("poing2.pdf", "wb") as filezip:
#     filezip.write(s.content)


# FILEZIPE
 
url = 'https://docs.python.org/2/archives/python-2.7.14-docs-pdf-a4.zip'
urllib.request.urlretrieve(url, "zip-urllib.zip")
######################################################################################
import requests

session = requests.session()


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0',
           'Accept': '*/*'}

username = input('  Enter username $ ')
password = input('  Enter Password $ ')

login_go = 'https://shalishomal.ir/wp-login.php'

Check_wordpress = session.get(login_go, timeout=50)
cookies = dict(Check_wordpress.cookies)
if 'Powered by WordPress' in Check_wordpress.text:

    post_data = {'log': str(username),
                 'pwd': str(password),
                 'wp-submit': 'ورود',
                 'redirect_to': 'https://shalishomal.ir/wp-admin.php',
                 'testcookie': '1'}

    Get_login = session.post(login_go, data=post_data, headers=headers, cookies=cookies, timeout=50)


    if '<li id="wp-admin-bar-logout">' in Get_login.text:
        print(' yeah, we login Successfully!')
        print(cookies)
        with open('result.html', 'a') as x:
            x.write(Get_login.text)
    else:
        print('maybe username and password is wrong! try again')
else:
    print(' wordpress login page Not Found !')







# در اولین خط ما ماژول Requests رو فراخوانی کردیم سپس یک session ایجاد کردیم تا بعد از login شدن اطلاعات پایدار باشند
# در خط بعدی یک Header تعریف کردیم سپس از کاربر خواستیم تا username و password را برای ورود به سایت وارد کند
# سپس یک متغیری با نام login_go ایجاد کردیم تا از آن برای ارسال درخواست استفاده کنیم
# در خط بعدی متغیری برای چک کردن این که آیا سایت مورد نظر Wordpress است یا خیر ایجاد کردیم با نام Check_wordpress و مقدار آن را اینگونه وارد کردیم session.get(login_go, timeout=10) سپس متغیری از نوع dict ( واژه نامه یا دیکشنری)برای دریافت کوکی ایجاد کردیم تا کوکی استفاده شده در آن ذخیره شود
# در خط بعد با یک دستور شرطی گفتیم که : اگر مقدار 'Powered by WordPress' در Check_wordpress.text بود برای ما کار های زیر را انجام بده در غیر این صورت پیام : 'wordpress login page Not Found !' را چاپ کن

# سپس برای ارسال با متد POST یک متغیری با نام post_data ایجاد کردیم تا data خودمان را در آن قرار دهیم ! ( به شما توضیح میدم چطوری data رو از source پیدا کنید )


# سپس متغیری با نام Get_login ایجاد میکنیم و مقدار session.post(login_go, data=post_data, headers=headers, cookies=cookies, timeout=10) را در آن قرار میدهیم
# در خط بعد میگویم : اگر مقدار '<li id="wp-admin-bar-logout">' در Get_login.text موجود بود کارهای زیر رو انجام بده در غیراینصورت برای ما مقدار 'maybe username and password is wrong! try again' چاپ کن.
# اگر برنامه با موفقیت به مرحله بعد برسد برای ما مقدار ' yeah, we login Successfully!' را نمایش میدهد در غیراینصورت پیام مرحله قبل نمایش داده خواهد شد,
# برای فهم بهتر من مقدار cookie استفاده شده را هم نمایش دادم تا شما بهتر متوجه شوید
# و در مرحله اخر گفتم که یک فایل با نام result.html ایجاد کنه و Get_login.text را در آن قرار دهد !


