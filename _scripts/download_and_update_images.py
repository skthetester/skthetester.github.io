import os
import re
import requests
from urllib.parse import urlparse

POSTS_DIR = os.path.join(os.path.dirname(__file__), '..', '_posts')
ASSETS_DIR = os.path.join(os.path.dirname(__file__), '..', 'assets', 'img', 'posts')

os.makedirs(ASSETS_DIR, exist_ok=True)

IMAGE_REGEX = re.compile(r'!\[[^\]]*\]\((https?://[^)]+)\)')


def download_image(url, dest_folder):
    parsed = urlparse(url)
    filename = os.path.basename(parsed.path)
    local_path = os.path.join(dest_folder, filename)
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        with open(local_path, 'wb') as f:
            f.write(resp.content)
        return filename
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return None


def process_post(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    for match in IMAGE_REGEX.finditer(content):
        url = match.group(1)
        filename = download_image(url, ASSETS_DIR)
        if filename:
            new_link = f'./assets/img/posts/{filename}'
            new_content = new_content.replace(url, new_link)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {filepath}")
    else:
        print(f"No changes: {filepath}")


def main():
    for fname in os.listdir(POSTS_DIR):
        if fname.endswith('.md'):
            process_post(os.path.join(POSTS_DIR, fname))

if __name__ == '__main__':
    main()
