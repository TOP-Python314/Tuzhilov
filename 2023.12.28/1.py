from pathlib import Path

def list_files(path_a: str) -> None | tuple: 
    base_dir = Path(path_a)
    if base_dir.is_dir():
        results = tuple(item.name for item in base_dir.iterdir() if item.is_file())
        return results
    else:
        return results
        return None

# C:\Users\user\Documents\Tuzhilov\2023.12.28>tree /f
# Структура папок тома SSD-Windows 10
# Серийный номер тома: 86CB-F1D5
# C:.
# │   # HW 2023.12.28.txt
# │   1.py
# │
# └───data
    # │   7MD9i.chm
    # │   conf.py
    # │   E3ln1.txt
    # │   F1jws.jpg
    # │   le1UO.txt
    # │   q40Kv.docx
    # │   questions.quiz
    # │   r62Bf.txt
    # │   vars.py
    # │   xcD1a.zip
    # │
    # ├───c14KE
    # │       5vsIh.dat
    # │       P2a91.dat
    # │
    # └───mXbd9
            # RoBjg.pt
            # z03EN.pt

# C:\Users\user\Documents\Tuzhilov\2023.12.28>python -i 1.py
# >>> list_files(r'c:\users\user\documents\tuzhilov\2023.12.28\data')
# ('7MD9i.chm', 'conf.py', 'E3ln1.txt', 'F1jws.jpg', 'le1UO.txt', 'q40Kv.docx', 'questions.quiz', 'r62Bf.txt', 'vars.py', 'xcD1a.zip')
