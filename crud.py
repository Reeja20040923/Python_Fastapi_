from fastapi import FastAPI,status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

books = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960
    },
]

app = FastAPI()

@app.get("/books")
def get_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id:int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Book not found")
        
class Book(BaseModel):
    id: int
    title:str
    author:str
    publish_date:str

@app.post("/books")
def create_book(Book: Book):
    new_book = Book.model_dump()
    books.append(new_book)


class Book_Update(BaseModel):
    title:str
    author:str
    publish_date:str    
@app.put("/books/{book_id}")
def update_book(book_id:int,book_update: Book_Update):
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_update.title
            book["author"] = book_update.author
            book["publish_date"] = book_update.publish_date
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.delete("/books/{book_id}")
def delete_book(book_id:int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"Message": "Book deleted successfully"}
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Book not found")
    