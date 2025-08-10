import os
import re

POSTS_DIR = os.path.join(os.path.dirname(__file__), '..', '_posts')

OLD_DOMAIN = 'testingchief.com'
NEW_DOMAIN = 'skthetester.github.io'
TWITTER_OLD = 'twitter.com'
TWITTER_NEW = 'x.com'

def replace_domain_in_post(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    updated = False
    new_content = content
    if OLD_DOMAIN in new_content:
        new_content = new_content.replace(OLD_DOMAIN, NEW_DOMAIN)
        updated = True
    if TWITTER_OLD in new_content:
        new_content = new_content.replace(TWITTER_OLD, TWITTER_NEW)
        updated = True
    if updated:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {filepath}")
    else:
        print(f"No changes: {filepath}")

def main():
    for fname in os.listdir(POSTS_DIR):
        if fname.endswith('.md'):
            replace_domain_in_post(os.path.join(POSTS_DIR, fname))

if __name__ == '__main__':
    main()
