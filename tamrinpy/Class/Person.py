# 1. Create a simple class
# Create a class called Person that contains properties called name and age.
# Create a method called introduce() in the class that prints the person information (name and age).
# Then create an object of this class and call the introduce() method.

class Person:
    def __init__(self,name,age): 
        self.name = name
        self.age = age
        
    def introduce(self):
        print(f"Hello My name is {self.name} and Im {self.age} years old! ")
        
person1 = Person("Ali", 25)
person1.introduce()


# توضیح کد:

# 1. تعریف کلاس Person:

# کلاس Person دو ویژگی (attribute) دارد: name و age. 
# این ویژگی‌ها برای هر فرد ذخیره می‌شوند.



# 2. متد init:

# در پایتون، متد سازنده (constructor) برای هر کلاس به اسم init نوشته می‌شود
# ، نه init. در این متد، نام و سن به عنوان ورودی به کلاس داده می‌شود و سپس در ویژگی‌های شی (object) ذخیره می‌شود.



# 3. متد introduce:

# این متد برای معرفی شخص به‌کار می‌رود.
# وقتی این متد اجرا می‌شود، پیام معرفی شخص با نام و سنش چاپ می‌شود.




