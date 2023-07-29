import os
import shutil

download_path = ('/Users/luanho/Desktop')
photos_path = ('/Users/luanho/Desktop/Photos')

with os.scandir(download_path) as entries:
    for entry in entries:
        print(entry.name)

for filename in os.listdir(download_path):
    if filename.lower().endswith(('.png', '.jpeg', '.jpg')):
        file_path = os.path.join(download_path, filename)
        shutil.move(file_path, photos_path)