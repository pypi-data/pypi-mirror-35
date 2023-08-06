import os








def read_all_text(file_path: str, encoding='UTF8') -> str:
    with open(file_path, 'r', encoding=encoding) as f:
        s = f.read()
        return s








def append_all_text(file_path: str, text: str, encoding='UTF8') -> str:
    with open(file_path, 'a', encoding=encoding) as f:
        f.write(text)








def write_all_text(file_path: str, file_content: str, encoding='UTF8'):
    with open(file_path, 'w', encoding=encoding) as f:
        f.write(file_content)
