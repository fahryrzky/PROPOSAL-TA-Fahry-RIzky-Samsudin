import os
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

file_dir = 'File'
if os.path.exists(file_dir):
    print("Files in 'File' folder:")
    for f in os.listdir(file_dir):
        path = os.path.join(file_dir, f)
        size = os.path.getsize(path) if os.path.isfile(path) else 0
        is_dir = os.path.isdir(path)
        tag = "[DIR]" if is_dir else f"({size/1024:.1f} KB)"
        print(f" - {f} {tag}")
else:
    print("'File' directory does not exist")
