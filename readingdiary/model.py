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

    def add_note(self, text: str, page: int, date: datetime) -> bool:
        if page > self.pages:
            return False
        self.notes.append(Note(text, page, date))
        return True

    def set_rating(self, rating: int) -> bool:
        if rating not in(Book.EXCELLENT, Book.GOOD, Book.BAD, Book.UNRATED):
            return False
        self.rating = rating
        return True

    def get_notes_of_page(self, page: int) -> list[Note]:
        page_notes = []
        for note in self.notes:
            if note.page == page:
                page_notes.append(note)
        return page_notes

    def page_with_most_notes(self) -> int:
        if not self.notes:
            return -1

        count = {}

        for note in self.notes:
            if note.page in count:
                count[note.page] += 1
            count[note.page] += 1

            return max(count, key=count.get)

    def __str__(self) -> str:
        return (f"ISBN: {self.isbn}"
                f"Title: {self.title}"
                f"Author: {self.author}"
                f"Pages: {self.pages}"
                f"Rating: {self.rating}")

class ReadingDiary:
    def __init__(self):
        self.books: dict[str, Book] = {}

    def add_book(self, isbn: str, title: str, author: str, pages: int) -> bool:
        if isbn not in self.books:
            self.books[isbn] = Book(isbn, title, author, pages)
            return True
        else:
            return False

    def search_by_isbn(self, isbn: str) -> Book | None:
        if isbn in self.books:
            return self.books[isbn]
        else:
            return None

    def add_note_to_book(self, isbn: str, text: str, pages: int, date: datetime) -> bool:
        book = self.search_by_isbn(isbn)
        if book is None:
            return False

        return book.add_note(text, pages, date)


    def rate_book(self, isbn: str, rating: int) -> bool:
        book = self.search_by_isbn(isbn)
        if book is None:
            return False
        return book.set_rating(rating)


    def book_with_most_notes(self) -> Book | None:
        pass

