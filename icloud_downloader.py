import os
import shutil
from datetime import datetime
import subprocess
import exiftool
import getpass

# Configuration
DOWNLOAD_DIR = os.path.join(os.getcwd(), "downloads")
EXIFTOOL_PATH = "exiftool.exe"  # Assumes exiftool is in the same directory; update if needed
ICLOUDPD_PATH = "icloudpd"      # Assumes icloudpd is in PATH; update if needed

def download_from_icloud(username):
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)
    print(f"\nDownloading for {username} to {DOWNLOAD_DIR}...")
    print(f"Note: Files already in {DOWNLOAD_DIR} will be skipped unless deleted or renamed.")
    password = getpass.getpass(f"Enter iCloud password for {username}: ")
    cmd = [
        ICLOUDPD_PATH,
        "--directory", DOWNLOAD_DIR,
        "--username", username,
        "--password", password,
        "--size", "original",
        "--set-exif-datetime",
        "--log-level", "info"
    ]
    try:
        print(f"Note: If 2FA is required, select a trusted device (e.g., '1' for iPhone) instead of SMS (e.g., '0') when prompted.")
        result = subprocess.run(cmd, check=True)
        print(f"Download completed successfully for {username}.")
        return True
    except FileNotFoundError:
        print(f"Error: {ICLOUDPD_PATH} not found. Ensure icloudpd is installed and in your PATH, or update the ICLOUDPD_PATH variable.")
        return False
    except subprocess.CalledProcessError as e:
        print(f"Error during download for {username}: {e}")
        return False
    except KeyboardInterrupt:
        print(f"Download interrupted by user for {username}. Restarting will skip already downloaded files.")
        return False

def get_file_date(filepath):
    try:
        with exiftool.ExifToolHelper(executable=EXIFTOOL_PATH) as et:
            metadata = et.get_metadata(filepath)[0]
            date_str = metadata.get("EXIF:DateTimeOriginal") or \
                       metadata.get("EXIF:CreateDate") or \
                       metadata.get("File:FileCreateDate")
            if date_str:
                return datetime.strptime(date_str.split('.')[0], "%Y:%m:%d %H:%M:%S")
    except Exception as e:
        print(f"Warning: Could not get EXIF date for {filepath}, using file timestamp: {e}")
        stat = os.stat(filepath)
        return datetime.fromtimestamp(stat.st_ctime)

def organize_files(username):
    print(f"Organizing new files for {username}...")
    base_dir = DOWNLOAD_DIR
    for filename in os.listdir(base_dir):
        filepath = os.path.join(base_dir, filename)
        if os.path.isfile(filepath):
            try:
                file_date = get_file_date(filepath)
                year = file_date.strftime("%Y")
                month = file_date.strftime("%m")
                day = file_date.strftime("%d")
                target_dir = os.path.join(DOWNLOAD_DIR, year, month, day)
                os.makedirs(target_dir, exist_ok=True)
                target_path = os.path.join(target_dir, filename)
                if filepath != target_path:
                    shutil.move(filepath, target_path)
                    print(f"Moved {filename} to {target_dir}")
                else:
                    print(f"Skipping {filename} - already in correct location")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

def clean_empty_dirs(username):
    print(f"Cleaning up empty directories for {username}...")
    for root, dirs, files in os.walk(DOWNLOAD_DIR, topdown=False):
        if not dirs and not files and root != DOWNLOAD_DIR:
            os.rmdir(root)
            print(f"Removed empty directory: {root}")

def main():
    print("Starting iCloud Photo Downloader...")
    username = input("Enter your iCloud email address: ")
    if not username:
        print("Error: No username provided. Exiting.")
        return
    if download_from_icloud(username):
        organize_files(username)
        clean_empty_dirs(username)
        print(f"All tasks completed for {username}!")
    else:
        print(f"Download failed or was interrupted for {username}. Restart to resume.")

if __name__ == "__main__":
    main()