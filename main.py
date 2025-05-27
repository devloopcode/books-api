from fastapi import Body, FastAPI
from models import Book
from validation import BookRequest

app = FastAPI()


BOOKS = [
    Book(1, "To Kill a Mockingbird", "Harper Lee", "A powerful story about racial injustice and moral growth in the American South.", 4),
    Book(2, "1984", "George Orwell", "A chilling vision of a totalitarian future under constant surveillance.", 4),
    Book(3, "Clean Code", "Robert C. Martin", "A guide to writing readable, maintainable, and efficient code.", 5),
    Book(4, "Sapiens: A Brief History of Humankind", "Yuval Noah Harari", "A sweeping narrative of human evolution, society, and culture.", 4),
    Book(5, "The Great Gatsby", "F. Scott Fitzgerald", "A critique of the American Dream set in the Roaring Twenties.", 4),
    Book(6, "Test", "George Orwell", "A chilling vision of a totalitarian future under constant surveillance.", 3),
]


@app.get("/api/books")
async def get_books():
    return BOOKS


@app.get("/api/books/{book_id}")
async def get_book_by_id(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book


@app.get("/api/books/")
async def get_books_by_rating(book_rating: int):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return    


@app.post("/api/books/create-book")
async def create_new_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))
    

@app.put("/api/books/update-book")
async def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book


@app.delete("/api/books/delete-book/{book_id}")
async def delete_book(book_id: int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book