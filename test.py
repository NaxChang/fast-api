def get_data() -> dict:
    return "hello"  # 錯誤：不是 dict


result = get_data()
print(result)  # 輸出 hello
print(type(result))  # <class 'str'>
