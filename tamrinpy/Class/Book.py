class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        return f"title = {self.title}, author = {self.author}, year = {self.year}"
    

book1 = Book("math","john","2024")
print(book1)