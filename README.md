# 📚 FastAPI 書籍管理系統

使用 Python FastAPI 製作的簡易 RESTful API 網站，實作書籍 CRUD 功能，包含 GET、POST、PUT、PATCH、DELETE 等操作，並使用 JSON 作為簡易資料儲存。

---

## 🚀 功能介紹

✅ 查詢書籍（全部或依條件）  
✅ 新增書籍  
✅ 修改書籍（PUT / PATCH）  
✅ 刪除書籍  
✅ JSON 資料儲存（無需資料庫）  
✅ 表單提交與 HTML 顯示（使用 Jinja2 模板）  
✅ 提供初始化與清除書籍功能

---

## 🖥️ 專案結構

fastapi-book-api/
├── main.py # FastAPI 主要路由與邏輯
├── schema.py # Pydantic 模型定義
├── db.py # 資料處理（載入、儲存、重置等）
├── book.json # 書籍資料檔案
├── templates/ # HTML 模板（index.html / result.html）
└── requirements.txt # 套件安裝清單


---
| 方法     | 路徑                 | 說明      |
| ------ | ------------------ | ------- |
| GET    | `/api/books`       | 查詢所有書籍  |
| GET    | `/api/books/{id_}` | 查詢單筆書籍  |
| POST   | `/api/books`       | 新增書籍    |
| PUT    | `/api/books/{id_}` | 完整更新書籍  |
| PATCH  | `/api/books/{id_}` | 局部更新書籍  |
| DELETE | `/api/books/{id_}` | 刪除書籍    |
| POST   | `/api/reset`       | 清空所有書籍  |
| POST   | `/api/init`        | 初始化預設資料 |


✅ 延伸目標（可選）
✅ 加入 SQLite 或 PostgreSQL 資料庫

✅ 部署到雲端（如 Vercel、Render、Railway）

✅ 加入登入驗證（JWT）

✅ 使用 Pytest 撰寫 API 單元測試
