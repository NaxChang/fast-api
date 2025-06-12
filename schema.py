from pydantic import BaseModel, Field
from typing import Optional


class BookInput(BaseModel):
    name: str
    publish: str
    type_: str
    isbn: Optional[str] = None
    price: Optional[float] = None

    model_config = {
        "extra": "forbid",
        "json_schema_extra": {
            "example": {
                "name": "api",
                "publish": "Fastapi",
                "type_": "Python",
                "isbn": "123456",
                "price": 999,
            }
        },
    }

    # class Config:
    #     extra = "forbid"


class BookOutput(BookInput):
    id_: int

    model_config = {
        "extra": "forbid",
        "json_schema_extra": {
            "example": {
                "id": 1,
                "name": "api",
                "publish": "Fastapi",
                "type_": "Python",
                "isbn": "123456",
                "price": 999,
            }
        },
    }


if __name__ == "__main__":
    book = BookOutput(
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
