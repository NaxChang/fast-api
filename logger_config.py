# project/logger_config.py

import logging
import os


def setup_logger(name=None, level=logging.INFO):
    # 取得或建立 logger 實例，名稱為 name（模組名稱或自訂名稱）
    logger = logging.getLogger(name)

    # 如果 logger 已經有 handler，代表已設定過，直接回傳避免重複添加
    if logger.handlers:
        return logger

    # 設定 logger 的最低紀錄層級（例如 INFO，過濾掉 DEBUG）
    logger.setLevel(level)

    # 定義日誌輸出格式，包含時間、日誌等級、訊息內容
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # 建立一個輸出到終端機的 handler（管道）
    console_handler = logging.StreamHandler()

    # 將格式應用到終端機 handler
    console_handler.setFormatter(formatter)

    # ➤ 將「終端機輸出管道」加到 logger（讓 log 可以顯示在畫面上）
    logger.addHandler(console_handler)

    # ➤ 確保 logs 資料夾存在（若不存在就自動建立）
    os.makedirs("logs", exist_ok=True)

    # ➤ 建立一個「寫入檔案的處理器」，log 會輸出到 logs/app.log，使用 UTF-8 編碼

    file_handler = logging.FileHandler("logs/app.log", encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

