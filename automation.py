import os
import shutil
import time

desktop_path = ('/Users/luanho/Desktop')
photos_path = ('/Users/luanho/Desktop/Photos')

if not os.path.exists(photos_path):
    os.makedirs(photos_path)
    
# lists all files in desktop
with os.scandir(desktop_path) as entries:
    for entry in entries:
        print(entry.name)

while True:
    # for all files in the desktop, if they are a picture, move them into photos
    for filename in os.listdir(desktop_path):
        if filename.lower().endswith(('.png', '.jpeg', '.jpg')):
            file_path = os.path.join(desktop_path, filename)
            shutil.move(file_path, photos_path)
    print("This code is running")
    time.sleep(1)