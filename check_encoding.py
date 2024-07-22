import os

def is_utf8(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            f.read()
        return True
    except UnicodeDecodeError:
        return False

project_path = "E:/Haidar/aic/music-analyzer"
non_utf8_files = []

for root, dirs, files in os.walk(project_path):
    for file in files:
        filepath = os.path.join(root, file)
        if not is_utf8(filepath):
            non_utf8_files.append(filepath)

if non_utf8_files:
    print("Non-UTF-8 encoded files found:")
    for file in non_utf8_files:
        print(file)
else:
    print("All files are UTF-8 encoded.")
