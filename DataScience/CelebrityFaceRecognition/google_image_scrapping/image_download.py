#!/usr/bin/env python3
"""Download image search results for the celebrity-classification dataset.

The scraper uses Selenium to collect image URLs and Pillow to validate and
store downloaded images. Only use it where automated image downloading is
permitted by the source website and applicable terms.
"""

import hashlib
import io
import os
import time
from pathlib import Path
from urllib.parse import quote_plus

import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


REQUEST_TIMEOUT = 10


def _build_driver(driver_path=None):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    if driver_path:
        return webdriver.Chrome(service=Service(driver_path), options=options)
    return webdriver.Chrome(options=options)


def fetch_image_urls(query, max_links_to_fetch, wd, sleep_between_interactions=1):
    """Collect up to ``max_links_to_fetch`` image URLs from image search."""
    if max_links_to_fetch <= 0:
        return set()

    search_url = (
        "https://www.google.com/search?tbm=isch&q=" + quote_plus(query)
    )
    wd.get(search_url)

    image_urls = set()
    previous_count = 0

    while len(image_urls) < max_links_to_fetch:
        thumbnails = wd.find_elements("css selector", "img")
        for thumbnail in thumbnails:
            src = thumbnail.get_attribute("src")
            if src and src.startswith("http"):
                image_urls.add(src)
                if len(image_urls) >= max_links_to_fetch:
                    break

        if len(image_urls) == previous_count:
            wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(sleep_between_interactions)
            thumbnails = wd.find_elements("css selector", "img")
            if len(thumbnails) <= previous_count:
                break
        previous_count = len(image_urls)
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_between_interactions)

    return set(list(image_urls)[:max_links_to_fetch])


def persist_image(folder_path, url):
    """Download, validate, and save one image. Return its path on success."""
    try:
        response = requests.get(
            url, timeout=REQUEST_TIMEOUT, headers={"User-Agent": "Mozilla/5.0"}
        )
        response.raise_for_status()
        image_content = response.content

        with Image.open(io.BytesIO(image_content)) as image:
            image = image.convert("RGB")
            filename = hashlib.sha1(image_content).hexdigest()[:10] + ".jpg"
            path = Path(folder_path) / filename
            path.parent.mkdir(parents=True, exist_ok=True)
            image.save(path, "JPEG", quality=85)

        print(f"SUCCESS - saved {url} - as {path}")
        return path
    except (requests.RequestException, OSError, ValueError) as exc:
        print(f"ERROR - could not save {url}: {exc}")
        return None


def search_and_download(search_term, driver_path=None, target_path="./datasets", number_images=50):
    """Search for a term and save the requested number of valid images."""
    target_folder = Path(target_path) / "_".join(search_term.lower().split())
    target_folder.mkdir(parents=True, exist_ok=True)

    with _build_driver(driver_path) as driver:
        urls = fetch_image_urls(search_term, number_images, driver)

    saved = 0
    for url in urls:
        if persist_image(target_folder, url):
            saved += 1

    print(f"Saved {saved} images for '{search_term}'.")
    return saved


if __name__ == "__main__":
    queries = ["Serena Williams"]
    for query in queries:
        search_and_download(query, "./chromedriver.exe", number_images=50)
