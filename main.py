from fastapi import Body, FastAPI

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
    "title": "Animal Farm",
    "author": "George Orwell",
    "category": "Political Satire"
  },
  {
    "title": "A Brief History of Time",
    "author": "Stephen Hawking",
    "category": "Science"
  },
  {
    "title": "The Theory of Everything",
    "author": "Stephen Hawking",
    "category": "Science"
  },
  {
    "title": "Cosmos",
    "author": "Carl Sagan",
    "category": "Science"
  },
  {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "category": "Classic"
  },
  {
    "title": "This Side of Paradise",
    "author": "F. Scott Fitzgerald",
    "category": "Classic"
  },
  {
    "title": "The Pragmatic Programmer",
    "author": "Andrew Hunt and David Thomas",
    "category": "Technology"
  },
  {
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "category": "Programming"
  },
  {
    "title": "The Clean Coder",
    "author": "Robert C. Martin",
    "category": "Programming"
  },
  {
    "title": "Code Complete",
    "author": "Steve McConnell",
    "category": "Programming"
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
async def get_books():
    return BOOKS


@app.get("/api/books/")
async def get_book_by_category(category: str):
    books_to_returns = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_returns.append(book)
    return books_to_returns


@app.post("/api/books/create_book")
async def create_new_book(new_book = Body()):
    BOOKS.append(new_book)
    

@app.put("/api/books/update_book")
async def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == updated_book.get("title").casefold():
            BOOKS[i] = updated_book


@app.get("/api/books/{book_title}")
async def get_book_by_title(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book


@app.get("/api/books/{book_author}/")
async def get_book_by_author_category(book_author:str, category: str):
    books_to_returns = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold()  and book.get('author').casefold() == book_author.casefold():
            books_to_returns.append(book)
    return books_to_returns
