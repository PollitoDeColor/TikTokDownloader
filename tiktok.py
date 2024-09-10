from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import yt_dlp
import os

# Function to download a video using yt-dlp
def download_video(url):
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',  # Save with the video title
        'format': 'mp4',  # Download format
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print(f'Downloading: {url}')
            ydl.download([url])
        except Exception as e:
            print(f"Error downloading {url}: {e}")

# Selenium configuration
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)

# TikTok account URL
tiktok_url = "https://www.tiktok.com/@"  # Replace with the TikTok username
driver.get(tiktok_url)

# Create a folder for videos if it doesn't exist
if not os.path.exists("videos"):
    os.mkdir("videos")

# Scroll down the page to load more videos
SCROLL_PAUSE_TIME = 2
last_height = driver.execute_script("return document.body.scrollHeight")
videos = set()

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

    # Find all video elements and get the links
    video_elements = driver.find_elements(By.XPATH, '//a[contains(@href, "/video/")]')
    for video in video_elements:
        video_link = video.get_attribute('href')
        if video_link and video_link not in videos:
            videos.add(video_link)

# Download the videos
for i, video_link in enumerate(videos):
    print(f"Downloading video {i + 1}: {video_link}")
    
    download_video(video_link)

# Close the browser
driver.quit()