from fastapi import FastAPI

app = FastAPI()


BOOKS = [
  {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "category": "Fiction"
  },
  {
    "title": "1984",
    "author": "George Orwell",
    "category": "Dystopian"
  },
  {
    "title": "A Brief History of Time",
    "author": "Stephen Hawking",
    "category": "Science"
  },
  {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "category": "Classic"
  },
  {
    "title": "The Pragmatic Programmer",
    "author": "Andrew Hunt and David Thomas",
    "category": "Technology"
  },
  {
    "title": "Sapiens: A Brief History of Humankind",
    "author": "Yuval Noah Harari",
    "category": "History"
  },
  {
    "title": "The Catcher in the Rye",
    "author": "J.D. Salinger",
    "category": "Coming-of-Age"
  },
  {
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "category": "Programming"
  },
  {
    "title": "Thinking, Fast and Slow",
    "author": "Daniel Kahneman",
    "category": "Psychology"
  },
  {
    "title": "The Art of War",
    "author": "Sun Tzu",
    "category": "Philosophy"
  }
]


@app.get("/api/books")
async def fisrt_api_fn():
    return BOOKS


@app.get("/api/books/{book_title}")
async def get_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
