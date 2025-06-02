from fastapi import FastAPI, Request, HTTPException, Form

# FastAPI 建立一個 API 應用程式的主入口物件,會用它來定義路由
# 代表使用者送來的 HTTP 請求
# 用來回傳 HTTP 錯誤
# 讓你從 HTML 表單（form）中接收資料，適用於表單格式提交
from db import load_book, save_book, reset_book

# 匯入自己在 db.py 模組中的三個函式
from schema import BookInput, BookOutput

# 匯入 schema.py 裡定義的資料模型：
from fastapi.templating import Jinja2Templates

#  Jinja2 模板系統，FastAPI 可以透過它渲染 HTML 頁面
from fastapi.responses import HTMLResponse

#  回傳內容的格式類型


templates = Jinja2Templates(directory="templates")


app = FastAPI()


@app.post("/submit", response_class=HTMLResponse)
def submit(
    request: Request,
    name: str = Form(...),
    publish: str = Form(...),
    type_: str = Form(...),
):
    books = load_book()
    max_id = max((b.id_ for b in books), default=0)
    new_id = max_id + 1
    if len(books) >= 10:
        return HTMLResponse(content="limit is 10", status_code=400)
    new_book = BookOutput(
        id_=new_id,
        name=name,
        publish=publish,
        type_=type_,
        isbn="",
        price=0.0,
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


@app.post("/api/books")
def add_book(book: BookInput) -> BookOutput:
    books = load_book()
    new_book = BookOutput(
        name=book.name,
        publish=book.publish,
        type_=book.type_,
        isbn=book.isbn,
        price=book.price,
        id_=len(books) + 1,
    )
    books.append(new_book)
    save_book(books)
    return new_book


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
        return [book for book in result if book.id_ == id_]
    return books


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
    return ["reset ok"]
