import xml.etree.ElementTree as ET
import frontmatter
import html2text
import os
import re

# Path to your WordPress XML export
WP_XML = './testingchief.WordPress.2025-08-09.xml'
# Output directory for Jekyll posts
OUTPUT_DIR = '_posts'

tree = ET.parse(WP_XML)
root = tree.getroot()

ns = {'wp': 'http://wordpress.org/export/1.2/', 'content': 'http://purl.org/rss/1.0/modules/content/', 'dc': 'http://purl.org/dc/elements/1.1/'}

for item in root.findall('./channel/item'):
    post_type = item.find('wp:post_type', ns)
    if post_type is not None and post_type.text == 'post':
        title = item.find('title').text or 'Untitled'
        date = item.find('wp:post_date', ns).text[:10]
        slug = item.find('wp:post_name', ns).text or re.sub(r'\W+', '-', title.lower())
        # Remove invalid filename characters for Windows
        slug = re.sub(r'[\\/:*?"<>|]', '', slug)
        content = item.find('content:encoded', ns).text or ''
        tags = [t.text for t in item.findall("category[@domain='post_tag']")]
        categories = [c.text for c in item.findall("category[@domain='category']")]

        # Convert HTML to Markdown
        md_content = html2text.html2text(content)

        # Build front matter
        post = frontmatter.Post(md_content)
        post['title'] = title
        post['date'] = date
        if tags:
            post['tags'] = tags
        if categories:
            post['categories'] = categories

        # Write to file
        filename = f"{date}-{slug}.md"
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(post))

print('Conversion complete!')