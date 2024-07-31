from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
import os
import time
import math


class DownloadManager:

    def __init__(self):
            self.path_to_image = "D:\\wallpapers\\"
            self.path_to_video = "D:\\Videos\\"
            self.path_to_large_video = "C:\\Users\\LENOVO\\Videos\\Large_Video\\" # means movie
            self.path_to_song = "D:\\Music\\"
            self.path_to_pdf = "D:\\Documents\\PDF\\"
            self.path_to_exe_msi_zip = "D:\\Documents\\EXE_MSI_ZIP\\"
            self.path_to_txt = "D:\\Documents\\TXT\\"
            self.path_to_already = "D:\\Already Exist\\"  # already means this folder is used to move the already saved files

            self.file_type_map = {
                ".jpg": "image",
                ".jpeg": "image",
                ".png": "image",
                ".gif": "image",
                ".bmp": "image",
                ".tiff": "image",
                ".tif": "image",
                ".webp": "image",
                ".mp4": "video",
                ".avi": "video",
                ".mkv": "video",
                ".mov": "video",
                ".wmv": "video",
                ".flv": "video",
                ".webm": "video",
                ".mp3": "music",
                ".wav": "music",
                ".m4a": "music",
                ".flac": "music",
                ".aac": "music",
                ".ogg": "music",
                ".wma": "music",
                ".aiff": "music",
                ".aif": "music",
                ".pdf": "pdf",
                ".exe": "emz",
                ".zip": "emz",
                ".msi": "emz",   # emz means exe, msi, zip first letter of the extensions
            }


    def watcher(self):
        path = "D:\\Downloads"
        event_handler = FileSystemEventHandler()
        event_handler.on_created = self.on_create
        observer = Observer()
        observer.schedule(event_handler, path, recursive=True)
        observer.start()

        try:
            while observer.is_alive():
                observer.join(1)

        finally:
            observer.stop()    
            observer.join()
        

    def on_create(self, event):
        file_ext = os.path.basename(event.src_path)
        print(f"event : {event.event_type}, name : {file_ext}")
        file_ext = os.path.splitext(file_ext)[1]
        path = event.src_path
        if file_ext == ".crdownload":
            file_type = "nothing"
        else:
            file_type = self.file_type_map.get(file_ext, "unknown")

        if file_type == "video":
            time.sleep(1)
            size = os.path.getsize(path)
            size = math.ceil(size / (1024 * 1024))
            if size > 100:
                try:
                    shutil.move(path, self.path_to_large_video)
                    self.check(self.path_to_large_video, path)
                except shutil.Error as e:
                    shutil.move(path, self.path_to_already)
                    self.check(self.path_to_already, path)
            else:
                try:
                    shutil.move(path, self.path_to_video)
                    self.check(self.path_to_video, path) 
                except shutil.Error as e:
                    shutil.move(path, self.path_to_already)
                    self.check(self.path_to_already, path)

        elif file_type == "image":
            time.sleep(1)
            try:
                shutil.move(path, self.path_to_image)
                self.check(self.path_to_image,path)
            except shutil.Error as e:
                shutil.move(path, self.path_to_already)
                self.check(self.path_to_already, path)    

        elif file_type == "music":
            time.sleep(2)
            try:
                shutil.move(path, self.path_to_song)
                self.check(self.path_to_song, path)
            except shutil.Error as e:
                shutil.move(path, self.path_to_already)
                self.check(self.path_to_already, path)     

        elif file_type == "pdf":
            time.sleep(1)
            try:
                shutil.move(path, self.path_to_pdf)
                self.check(self.path_to_pdf, path)
            except shutil.Error as e:
                shutil.move(path, self.path_to_already)
                self.check(self.path_to_already, path)     

        elif file_type == "emz":
            time.sleep(1)
            try:
                shutil.move(path, self.path_to_exe_msi_zip)
                self.check(self.path_to_exe_msi_zip, path)
            except shutil.Error as e:
                shutil.move(path, self.path_to_already)
                self.check(self.path_to_already, path)    

        elif file_type == "unknown":
            time.sleep(1)
            try:
                shutil.move(path, "D:\\Unknown\\") 
                self.check("D:\\Unknown\\", path)  
            except shutil.Error as e:
                shutil.move(path, self.path_to_already)
                self.check(self.path_to_already, path)     


    def check(self,des, file_name):
        if os.path.exists(os.path.join(des, os.path.basename(file_name))):
            print("File moved successfully.")
        else:
            print("Failed to move file.") 



if __name__ == "__main__":
    obj = DownloadManager()
    obj.watcher()   