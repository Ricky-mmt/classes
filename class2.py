class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def get_info(self):
        return f"'{self.title}' by {self.author}, published in {self.year}, Genre: {self.genre}"

    def read(self):
        print(f"Reading '{self.title}' by {self.author}.")

    def get_age(self):
        current_year = 2024
        return current_year - self.year

# Example usage
book1 = Book("1984", "George Orwell", 1949, "Dystopian")
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction")

print(book1.get_info())
print(book2.get_info())

book1.read()
print(f"'{book1.title}' is {book1.get_age()} years old.")