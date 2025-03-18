# iCloud Photo Downloader

A simple Python script to download photos and videos from your iCloud account and organize them into `Year/Month/Day` folders. It prompts for your iCloud email and password when run, and skips already downloaded files if restarted after an interruption.

## Features
- Downloads original-sized photos and videos from iCloud.
- Organizes files by date using EXIF metadata.
- Resumes downloads without re-downloading existing files.
- Handles two-factor authentication (2FA) interactively.

## Prerequisites
1. **Python 3.6+**: Install from [python.org](https://www.python.org).
2. **Python Packages**:
   - Listed in `requirements.txt` (install with `pip install -r requirements.txt`).
3. **ExifTool**: Download `exiftool.exe` from [exiftool.org](https://exiftool.org/), rename it from `exiftool(-k).exe` to `exiftool.exe`, and place it in the repository root or update `EXIFTOOL_PATH` in the script.

## Directory Structure
icloud-photo-downloader/
├── icloud_downloader.py    # Main script
├── README.md              # This file
├── requirements.txt       # Python dependencies
└── downloads/             # Created by script to store downloaded files


## Setup
1. **Clone the Repository**:
   git clone https://github.com/yourusername/icloud-photo-downloader.git
   cd icloud-photo-downloader

2.  **Install Dependencies**:
    pip install -r requirements.txt

3.  **Place exiftool.exe (optional)**:
    Put exiftool.exe in the same directory as icloud_downloader.py, or update EXIFTOOL_PATH in the script to its full path (e.g., C:\\Tools\\exiftool.exe).

4.  **Update ICLOUDPD_PATH (if needed)**:
    If icloudpd isn’t in your system PATH, set ICLOUDPD_PATH in the script to its full path (e.g., C:\\Python311\\Scripts\\icloudpd.exe).

## Usage
1.    **Run the script**:
    python icloud_downloader.py

## Steps
1.  **Enter Credentials**:
    Input your iCloud email address when prompted.
    Enter your iCloud password when prompted.

2.  **Handle 2FA (if enabled)**:
    Select a trusted device (e.g., 1 for iPhone) when prompted, then enter the OTP.

3.  **Download**:
    Files download to the downloads/ directory in the repository root.
    Organized into Year/Month/Day subfolders.

4.  **Resume**:
    If interrupted (e.g., Ctrl+C), restart the script. It skips files already in downloads/.

# Example Output
  Starting iCloud Photo Downloader...
  Enter your iCloud email address: yourname@example.com
  Downloading for yourname@example.com to /path/to/downloads...
  Note: Files already in /path/to/downloads will be skipped unless deleted or renamed.
  Enter iCloud password for yourname@example.com:
  Note: If 2FA is required, select a trusted device (e.g., '1' for iPhone) instead of SMS (e.g., '0') when prompted.
  [Downloading progress...]    

# Troubleshooting
  Files Re-Download: Ensure existing files remain in downloads/ and aren’t renamed or moved manually.
  ExifTool Error: Verify exiftool.exe is in the directory or update EXIFTOOL_PATH.
  iCloudPD Error: Ensure icloudpd is installed and in PATH, or update ICLOUDPD_PATH.  

# Customization
  Download Location: Change DOWNLOAD_DIR in the script (e.g., DOWNLOAD_DIR = "C:\\Photos").
  Tool Paths: Update EXIFTOOL_PATH or ICLOUDPD_PATH if they’re not in default locations.  