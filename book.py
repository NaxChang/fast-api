from fastapi import FastAPI, Request, HTTPException, Form
from collections import OrderedDict

# FastAPI 建立一個 API 應用程式的主入口物件,會用它來定義路由
# 代表使用者送來的 HTTP 請求
# 用來回傳 HTTP 錯誤
# 讓你從 HTML 表單（form）中接收資料，適用於表單格式提交
from db import load_book, save_book, reset_book, init_book, find_smallest_missing_id

# 匯入自己在 schema.py 模組中的三個函式
from schema import BookInput, BookOutput, BookPatchInput

# 匯入 schema.py 裡定義的資料模型：
from fastapi.templating import Jinja2Templates

#  Jinja2 模板系統，FastAPI 可以透過它渲染 HTML 頁面
from fastapi.responses import HTMLResponse, JSONResponse


#  回傳內容的格式類型


templates = Jinja2Templates(directory="templates")


app = FastAPI(title="BOOK_API")


# patch
@app.patch("/api/books/{id_}")
def patch_book(id_: int, update_data: BookPatchInput) -> BookOutput:
    books = load_book()
    matches = [book for book in books if book.id_ == id_]
    if not matches:
        raise HTTPException(status_code=404, detail=f"no book with id_ = {id_}")
    book = matches[0]
    update_dict = update_data.model_dump(exclude_unset=True)
    for field, value in update_dict.items():
        setattr(book, field, value)
    save_book(books)
    return book


# update_data = BookPatchInput(name="Python新書", price=88.8)
# patch_book(1, update_data)


@app.post("/submit", response_class=HTMLResponse)
def submit(
    request: Request,
    name: str = Form(...),
    publish: str = Form(...),
    type_: str = Form(...),
    isbn: str = Form(""),
    price: float = Form(0.0),
):
    books = load_book()
    # new_id = max((b.id_ for b in books), default=0) + 1
    if len(books) >= 10:
        return HTMLResponse(content="limit is 10", status_code=400)
    new_id = find_smallest_missing_id(books)
    new_book = BookOutput(
        id_=new_id,
        name=name,
        publish=publish,
        type_=type_,
        isbn=isbn,
        price=price,
    )
    books.append(new_book)
    save_book(books)
    return templates.TemplateResponse(
        "result.html",
        {"request": request, "id_": new_id},
    )


@app.get("/", response_class=HTMLResponse)
def form_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# books = load_book()
# if books:
#     id_list = []
#     for b in books:
#         id_list.append(b.id_)
#     max_id = max(id_list)
#     new_id = max_id + 1
# else:
#     new_id = 1
# # 建立新書
# new_book = Book(id_=new_id, **book.model_dump())
# books.append(new_book)
# save_book(books)
# return {"message": f"新增成功,id = {new_id}", "id_": new_id}


# 改為BookOutput
@app.get("/api/books")
def get_books(type_: str | None = None, id_: int | None = None) -> list[BookOutput]:
    books = load_book()
    result = books
    if type_:
        result = [book for book in books if book.type_ == type_]
    if id_:
        result = [book for book in result if book.id_ == id_]
    ordered_result = [
        OrderedDict(
            [
                ("id_", book.id_),
                ("name", book.name),
                ("publish", book.publish),
                ("type_", book.type_),
                ("isbn", book.isbn),
                ("price", book.price),
            ]
        )
        for book in result
    ]
    return JSONResponse(content=ordered_result)


@app.post("/api/books")
def add_book(book: BookInput) -> BookOutput:
    books = load_book()
    if len(books) >= 10:
        raise HTTPException(status_code=400, detail="Limit is 10 books.")
    new_id = find_smallest_missing_id(books)
    new_book = BookOutput(
        name=book.name,
        publish=book.publish,
        type_=book.type_,
        isbn=book.isbn,
        price=book.price,
        id_=new_id,
    )
    books.append(new_book)
    save_book(books)
    return new_book


# 改為BookOutput
@app.get("/api/books/{id_}")
def get_books_id(id_: int) -> BookOutput:
    books = load_book()
    result = [book for book in books if book.id_ == id_]
    if result:
        return result[0]
    raise HTTPException(status_code=404, detail=f"no book with id_ = {id_}")


@app.post("/api/reset")
def reset_book_data():
    reset_book()
    return {"message": "reset ok"}


@app.post("/api/init")
def init_book_data():
    init_book()
    return {"message": "init ok"}


# delete
@app.delete("/api/books/{id_}")
def delete_book(id_: int):
    books = load_book()
    matches = [book for book in books if book.id_ == id_]
    if matches:
        books.remove(matches[0])
        save_book(books)
    else:
        raise HTTPException(status_code=404, detail=f"no book with id_ = {id_}")


# put
@app.put("/api/books/{id_}")
def update_book(id_: int, new_book: BookInput) -> BookOutput:
    books = load_book()
    matches = [book for book in books if book.id_ == id_]
    if matches:
        book = matches[0]
        book.name = new_book.name
        book.publish = new_book.publish
        book.type_ = new_book.type_
        book.isbn = new_book.isbn
        book.price = new_book.price
        save_book(books)
        return book
    else:
        raise HTTPException(status_code=404, detail=f"no book with id_ = {id_}")
