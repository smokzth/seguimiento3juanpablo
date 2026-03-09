from datetime import datetime

class Note:
    def __init__(self, text: str, page: str, date: datetime):
        self.text = text
        self.page = page
        self.date : datetime = date

    def __str__(self) -> str:
        return f"{self.date} - page {self.page}: {self.text}"

class Book:
    EXCELLENT: int = 3
    GOOD: int = 2
    BAD: int = 1
    UNRATED: int = -1
    def __init__(self, isbn: str, title: str, author: str, pages: str):
        self.isbn: str = isbn
        self.title: str = title
        self.author: str = author
        self.pages: str = pages
        self.rating : int = Book.UNRATED
        self.notes : list[Note] = []

    def add_note


