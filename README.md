# AutoDownloadOrganizer

AutoDownloadOrganizer is a Python application that automatically organizes downloaded files into designated folders based on their type. It uses the `watchdog` library to monitor a specified directory for new files and categorizes them into folders for images, videos, music, PDFs, and other file types. Large video files are moved to a separate folder for better management. 

## Features

- Monitors a specified directory for new files.
- Categorizes files into folders based on their type (e.g., images, videos, music).
- Moves large video files to a designated folder for large videos.
- Handles and moves unknown file types to a separate folder.
- Provides logging of file processing and error handling.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Muhd-Uwais/AutoDownloadOrganizer.git
    ```

2. Navigate to the project directory:
    ```bash
    cd AutoDownloadOrganizer
    ```

3. Install the required dependencies:
    ```bash
    pip install watchdog
    ```

## Usage

1. Update the paths in the `DownloadManager` class in `main.py` to match your directory structure.

2. Run the script:
    ```bash
    python main.py
    ```

3. The script will start monitoring the specified directory and organize files as they are created.

## Configuration

- `self.path_to_image`: Directory for image files.
- `self.path_to_video`: Directory for regular video files.
- `self.path_to_large_video`: Directory for large video files.
- `self.path_to_song`: Directory for music files.
- `self.path_to_pdf`: Directory for PDF files.
- `self.path_to_exe_msi_zip`: Directory for executable, MSI, and ZIP files.
- `self.path_to_already`: Directory for files that could not be moved to their intended destination.
- `self.path_to_unknown`: Directory for unknown file types.

## Contributing

This project is in its early stages, and there are known flaws and areas for improvement. If you are interested in contributing, please feel free to submit a pull request with your enhancements or fixes. Your contributions are welcome, Thank You!

## Contact

For any questions or feedback, please reach out to [nox0389@gmail.com](mailto:nox0389@gmail.com).
