# TikTok Video Downloader

This Python script automates the process of downloading videos from a TikTok user's profile using Selenium and yt-dlp.

## Requirements

1. Python 3.x
2. Google Chrome
3. ChromeDriver
4. Python libraries: `selenium` and `yt-dlp`

## Setup Instructions

1. Install Python from [here](https://www.python.org/downloads/).
2. Install Google Chrome if you don't have it already.
3. Download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and add it to your system PATH.
4. Install the required Python libraries by running:

bash
   pip install selenium yt-dlp
   
## How to Use
Clone this repository or download the script.

Open the script and replace the TikTok URL with the username of the TikTok account you want to download videos from:

tiktok_url = "https://www.tiktok.com/@"  # Replace with the TikTok username

Run the script:

python tiktok_downloader.py

The script will open Google Chrome, scroll through the specified TikTok account's profile, and gather video links. These videos will be downloaded to a folder called videos in the same directory as the script.

Notes

Ensure you have the correct version of ChromeDriver that matches your version of Google Chrome.
The videos will be saved in .mp4 format with their original titles.
