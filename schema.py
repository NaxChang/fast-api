from pydantic import BaseModel, Field, field_validator
from typing import Optional
import re


class BookInput(BaseModel):
    name: str
    publish: str
    type_: str
    isbn: Optional[str] = Field(default=None, description="書號格式必須為123-00006")
    price: Optional[float] = Field(default=None, description="價格不能為負數")

    @field_validator("isbn")
    def check_isbn(cls, v):
        if v is not None and not re.match(r"^\d{3}-\d{5}$", v):
            raise ValueError("isbn書號格式必須為123-00006")
        return v

    @field_validator("price")
    def check_price(cls, v):
        if v is not None and v < 0:
            raise ValueError("價格不能為負數!")
        return v

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


class BookPatchInput(BookInput):
    name: Optional[str] = Field(None, example="python新書")
    publish: Optional[str] = None
    type_: Optional[str] = None
    isbn: Optional[str] = None
    price: Optional[float] = Field(None, example=88.8)

    model_config = {
        "extra": "forbid",
        "json_schema_extra": {"example": {"name": "python新書", "price": 88.8}},
    }


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
        price=999,
    )
    print(book)
    # print(book.model_dump())
    # print(book.model_dump_json())
    # print(book.isbn)
    print(book.id_)
