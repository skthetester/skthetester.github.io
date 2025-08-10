import os
import re

POSTS_DIR = os.path.join(os.path.dirname(__file__), '..', '_posts')
# This is the correct base path for images in your site
CORRECT_IMAGE_BASE = '/assets/img/posts/'

# Regex to find markdown image links with any path
IMAGE_LINK_REGEX = re.compile(r'(!\[[^\]]*\]\()([^)]*assets/img/posts/[^)]+)(\))')


def fix_image_links_in_post(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    updated = False
    def replacer(match):
        alt_text = match.group(1)
        img_path = match.group(2)
        closing = match.group(3)
        # Remove any leading URL or path before /assets/img/posts/
        idx = img_path.find('assets/img/posts/')
        if idx != -1:
            new_path = CORRECT_IMAGE_BASE + img_path[idx+len('assets/img/posts/'):]
            # Ensure it starts with /
            if not new_path.startswith('/'):
                new_path = '/' + new_path
            nonlocal updated
            updated = True
            return f'{alt_text}{new_path}{closing}'
        return match.group(0)
    new_content = IMAGE_LINK_REGEX.sub(replacer, content)
    if updated:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {filepath}")
    else:
        print(f"No changes: {filepath}")

def main():
    for fname in os.listdir(POSTS_DIR):
        if fname.endswith('.md'):
            fix_image_links_in_post(os.path.join(POSTS_DIR, fname))

if __name__ == '__main__':
    main()
