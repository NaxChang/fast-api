from fastapi import FastAPI

app = FastAPI()

books = [
    {"id": 1, "書名": "Python超入門", "出版日期": "2021-06-15", "出版社": "小白出版社"},
    {
        "id": 2,
        "書名": "人生苦短用Python",
        "出版日期": "2020-11-03",
        "出版社": "快樂程式人",
    },
    {
        "id": 3,
        "書名": "資料科學不求人",
        "出版日期": "2022-03-28",
        "出版社": "資料人出版社",
    },
    {"id": 4, "書名": "機器學習小抄", "出版日期": "2019-09-12", "出版社": "技術宅出版"},
    {"id": 5, "書名": "AI到底是什麼", "出版日期": "2023-01-10", "出版社": "未來出版社"},
]


print(type(books))


@app.get("/api/books")
def get_books():
    return books


@app.get("/")
def hello_world():
    return {"Hello": "FastAPI"}


@app.get("/test")
def test():
    return {"Hello": "test"}
