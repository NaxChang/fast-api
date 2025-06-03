import json
from schema import BookOutput
from typing import List

BOOK_FILE = "book.json"


# 讀取
def load_book() -> List[BookOutput]:
    try:
        with open(BOOK_FILE, "r", encoding="utf8") as file:
            books = json.load(file)
            return [BookOutput(**book) for book in books]
    except FileNotFoundError:
        print(f"Error:{BOOK_FILE}was not found")
        return []
    except json.JSONDecodeError:
        print(f"Error:{BOOK_FILE}contains invalid")
        return []
    except Exception as e:
        print("Error", e)
        return []


if __name__ == "__main__":
    loaded_book = load_book()
    print(loaded_book)
    print(type(loaded_book))


# 寫入
def save_book(books: List[BookOutput]) -> None:
    with open(BOOK_FILE, "w", encoding="utf8") as file:
        json.dump(
            [book.model_dump() for book in books],
            file,
            ensure_ascii=False,
            indent=4,
        )


# 重置,清除
def reset_book() -> None:
    with open(BOOK_FILE, "w", encoding="utf8") as file:
        json.dump([], file, ensure_ascii=False, indent=4)
        print("reset to empty.")


# init , 初始化
def init_book() -> None:
    with open(BOOK_FILE, "w", encoding="utf8") as file:
        json.dump(original_books, file, ensure_ascii=False, indent=4)
        print("init ok.")


original_books = [
    {
        "id_": 1,
        "name": "Python超入門",
        "publish": "小白出版社",
        "type_": "python",
        "isbn": "123-00001",
        "price": 85,
    },
    {
        "id_": 2,
        "name": "人生苦短用Python",
        "publish": "快樂程式人",
        "type_": "python",
        "isbn": "123-00002",
        "price": 92,
    },
    {
        "id_": 3,
        "name": "資料科學不求人",
        "publish": "資料人出版社",
        "type_": "科學",
        "isbn": "123-00003",
        "price": 78,
    },
    {
        "id_": 4,
        "name": "機器學習小抄",
        "publish": "技術宅出版",
        "type_": "AI",
        "isbn": "123-00004",
        "price": 65,
    },
    {
        "id_": 5,
        "name": "AI到底是什麼",
        "publish": "未來出版社",
        "type_": "AI",
        "isbn": "123-00005",
        "price": 90,
    },
    {
        "id_": 6,
        "name": "數學解密",
        "publish": "數字出版社",
        "type_": "數學",
        "isbn": "123-00006",
        "price": 88,
    },
    {
        "id_": 7,
        "name": "統計入門",
        "publish": "數據之家",
        "type_": "統計",
        "isbn": "123-00007",
        "price": 80,
    },
    {
        "id_": 8,
        "name": "演算法圖鑑",
        "publish": "程式圖書",
        "type_": "演算法",
        "isbn": "123-00008",
        "price": 95,
    },
]
