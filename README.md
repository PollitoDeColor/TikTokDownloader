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
4. Install the required Python libraries by running: pip install selenium yt-dlp
   
## How to Use
Clone this repository or download the script.

Open the script and replace the TikTok URL with the username of the TikTok account you want to download videos from:

tiktok_url = "https://www.tiktok.com/@"  # Replace with the TikTok username

Run the script: python tiktok_downloader.py

The script will open Google Chrome, scroll through the specified TikTok account's profile, and gather video links. These videos will be downloaded to a folder called videos in the same directory as the script.

## Notes

Ensure you have the correct version of ChromeDriver that matches your version of Google Chrome.
The videos will be saved in .mp4 format with their original titles.



# Descargador de Videos de TikTok

Este script en Python automatiza el proceso de descargar videos del perfil de un usuario de TikTok utilizando Selenium y yt-dlp.

## Requisitos
Python 3.x
Google Chrome
ChromeDriver
Librerías de Python: selenium y yt-dlp
Instrucciones de Configuración
Instala Python desde aquí.

Instala Google Chrome si aún no lo tienes.

Descarga ChromeDriver desde aquí y agrégalo a tu PATH del sistema.

Instala las librerías de Python requeridas ejecutando: pip install selenium yt-dlp

## Cómo Usar
Clona este repositorio o descarga el script.

Abre el script y reemplaza la URL de TikTok con el nombre de usuario de la cuenta de TikTok desde la cual quieres descargar videos: tiktok_url = "https://www.tiktok.com/@"  # Reemplaza con el nombre de usuario de TikTok

Ejecuta el script: python tiktok_downloader.py

El script abrirá Google Chrome, desplazará hacia abajo el perfil del usuario de TikTok especificado y recopilará los enlaces de los videos. Estos videos se descargarán en una carpeta llamada videos en el mismo directorio que el script.

## Notas
Asegúrate de tener la versión correcta de ChromeDriver que coincida con tu versión de Google Chrome.
Los videos se guardarán en formato .mp4 con sus títulos originales.
