# browser_config.py

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def configurar_driver():
    # Configurar carpeta de descargas
    download_dir = os.path.abspath("downloads")
    os.makedirs(download_dir, exist_ok=True)

    # Opciones de Chrome
    options = Options()
    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": True,
        "profile.default_content_settings.popups": 1,
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--start-maximized")

    return webdriver.Chrome(options=options)