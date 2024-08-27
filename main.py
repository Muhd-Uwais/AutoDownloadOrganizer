from watchdog.observers import Observer  # For monitoring directory changes
from watchdog.events import FileSystemEventHandler  # For handling file system events
import shutil
import os
import time
import math

class DownloadManager:
    def __init__(self):
        # Define paths for organizing different types of files, replace with yours.
        self.path_to_image = "D:\\wallpapers\\"
        self.path_to_video = "D:\\Videos\\"
        self.path_to_large_video = "C:\\Users\\LENOVO\\Videos\\Large_Video\\"  # Path for large videos
        self.path_to_song = "D:\\Music\\"
        self.path_to_pdf = "D:\\Documents\\PDF\\"
        self.path_to_exe_msi_zip = "D:\\Documents\\EXE_MSI_ZIP\\"
        self.path_to_txt = "D:\\Documents\\TXT\\"
        self.path_to_already = "D:\\Already Exist\\"  # Path for already processed files

        # Map file extensions to categories
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
            ".msi": "emz",  # 'emz' stands for exe, msi, zip
        }

    def watcher(self):
        """
        Initialize the directory watcher for the Downloads folder.
        This method sets up the observer to monitor the specified directory.
        """
        path = "D:\\Downloads"  # Directory to monitor for new files, replace with yours.
        event_handler = FileSystemEventHandler()  # Create event handler
        event_handler.on_created = self.on_create  # Assign the handler function for file creation
        
        observer = Observer()
        observer.schedule(event_handler, path, recursive=True)  # Watch the directory recursively
        observer.start()

        try:
            while observer.is_alive():
                observer.join(1)  # Keep the observer running
        finally:
            observer.stop()  # Stop the observer
            observer.join()

    def on_create(self, event):
        """
        Handle file creation events.
        This method processes files based on their type and moves them to appropriate directories.
        """
        file_name = os.path.basename(event.src_path)
        print(f"Event: {event.event_type}, File: {file_name}")
        
        file_ext = os.path.splitext(file_name)[1]  # Extract file extension
        path = event.src_path
        
        if file_ext == ".crdownload":
            file_type = "nothing"  # Temporary file type for incomplete downloads
        else:
            file_type = self.file_type_map.get(file_ext, "unknown")

        # Process the file based on its type
        if file_type == "video":
            self._process_video(path)
        elif file_type == "image":
            self._process_image(path)
        elif file_type == "music":
            self._process_music(path)
        elif file_type == "pdf":
            self._process_pdf(path)
        elif file_type == "emz":
            self._process_emz(path)
        elif file_type == "unknown":
            self._process_unknown(path)

    def _process_video(self, path):
        """
        Process video files and move them based on size.
        """
        time.sleep(1)  # Wait for file to be fully created
        size = os.path.getsize(path)  # Get file size in bytes
        size_mb = math.ceil(size / (1024 * 1024))  # Convert size to MB

        if size_mb > 100:  # Move large videos to a specific folder
            dest_path = self.path_to_large_video
        else:
            dest_path = self.path_to_video

        self._move_file(path, dest_path)

    def _process_image(self, path):
        """
        Process image files and move them to the designated folder.
        """
        time.sleep(1)  # Wait for file to be fully created
        self._move_file(path, self.path_to_image)

    def _process_music(self, path):
        """
        Process music files and move them to the designated folder.
        """
        time.sleep(2)  # Wait for file to be fully created
        self._move_file(path, self.path_to_song)

    def _process_pdf(self, path):
        """
        Process PDF files and move them to the designated folder.
        """
        time.sleep(1)  # Wait for file to be fully created
        self._move_file(path, self.path_to_pdf)

    def _process_emz(self, path):
        """
        Process EXE, MSI, and ZIP files and move them to the designated folder.
        """
        time.sleep(1)  # Wait for file to be fully created
        self._move_file(path, self.path_to_exe_msi_zip)

    def _process_unknown(self, path):
        """
        Process unknown file types and move them to a specific folder.
        """
        time.sleep(1)  # Wait for file to be fully created
        self._move_file(path, "D:\\Unknown\\")

    def _move_file(self, path, dest_path):
        """
        Move file to the specified destination path and check if the move was successful.
        """
        try:
            shutil.move(path, dest_path)
            self.check(dest_path, path)
        except shutil.Error as e:
            print(f"Error moving file: {e}")
            shutil.move(path, self.path_to_already)
            self.check(self.path_to_already, path)

    def check(self, dest, file_path):
        """
        Verify if the file was moved successfully.
        """
        if os.path.exists(os.path.join(dest, os.path.basename(file_path))):
            print("File moved successfully.")
        else:
            print("Failed to move file.")

if __name__ == "__main__":
    obj = DownloadManager()
    obj.watcher()  # Start watching the Downloads folder
