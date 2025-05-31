from pydantic import BaseModel
from typing import Optional


class Book(BaseModel):
    id_: int
    name: str
    publish: str
    type_: str
    isbn: Optional[str] = None
    price: Optional[float] = None


class BookCreate(BaseModel):
    name: str
    publish: str
    type_: str
    isbn: str
    price: float


if __name__ == "__main__":
    book = Book(
        id_=9,
        name="nameless",
        publish="school",
        type_="python",
        isbn="123-00009",
        price="999",
    )
    print(book)
    # print(book.model_dump())
    # print(book.model_dump_json())
    # print(book.isbn)
    print(book.id_)
