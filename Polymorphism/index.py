# در پایتون،
#  polymorphism 
# یکی از اصول اصلی شی گرایی است
#  Polymorphism 
# به معنای این است که اشیای مختلف می‌توانند با استفاده از یک رابط یا نحوه کارکرد مشابه با یکدیگر همکاری کنند، بدون اینکه برای هر کدام یک روش خاص ایجاد شود

# به طور مثال، در پایتون می‌توانید از پلی مورفیسم با استفاده از مفهوم شی گرایی بهره ببرید. شما می‌توانید یک متد را در یک کلاس ایجاد کنید و سپس در کلاس‌های دیگر این متد را با ویژگی‌ها و عملکرد متفاوتی مجدداً تعریف کنید. به این ترتیب، می‌توانید از یک رابط مشترک بین کلاس‌های مختلف استفاده کنید و بدون نیاز به تعریف روش‌های مختلف برای هر کلاس، از همه آن‌ها به یک شیء استفاده کنید.

# برای مثال، در کد زیر، دو کلاس پدر با نام Shape و Rectangle تعریف شده‌اند. هر دو کلاس یک متد با نام area دارند که برای محاسبه مساحت شکل‌ها استفاده می‌شود. کلاس Square هم از کلاس Shape ارث‌بری می‌کند و متد area را با توجه به شکل مربع به‌روزرسانی می‌کند.

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

r = Rectangle(2, 3)
print(r.area())
s = Square
print(s.area())