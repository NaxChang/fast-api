# 假設我們有一個書的清單，每本書是字典形式
books = [
    {"id_": 1, "name": "Python入門"},
    {"id_": 2, "name": "FastAPI指南"},
    {"id_": 3, "name": "資料科學"},
]

# 假設要刪除 id_ = 2 的書
id_to_delete = 2

# 找出符合的書
matches = [book for book in books if book["id_"] == id_to_delete]

if matches:
    # 從 books 移除符合的那一本書
    books.remove(matches[0])

print(books)


# 就是 books.remove(B)，把 B 從 books 裡刪掉

# def get_data() -> dict:
#     return "hello"  # 錯誤：不是 dict


# result = get_data()
# print(result)  # 輸出 hello
# print(type(result))  # <class 'str'>
