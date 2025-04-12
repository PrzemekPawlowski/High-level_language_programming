from typing import Dict, Optional

class Library:
    def __init__(self) -> None:
        self.books: Dict[str, str] = {} #ISBN

    def add_book(self, isbn: str, title: str) -> None:
        self.books[isbn] = title

    def find_book(self, isbn: str) -> Optional[str]:
        return self.books.get(isbn)

lib = Library()
lib.add_book("785-12-23-4523-1", "Lalka")
lib.add_book("785-14-2-1123-1", "Dziady")

print(lib.find_book("785-14-2-1123-1"))
print(lib.find_book("785-12-23-4523-1"))
