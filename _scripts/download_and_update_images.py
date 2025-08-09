import os
import re
import requests
import csv
from urllib.parse import urlparse

POSTS_DIR = os.path.join(os.path.dirname(__file__), '..', '_posts')
ASSETS_DIR = os.path.join(os.path.dirname(__file__), '..', 'assets', 'img', 'posts')
REPORT_CSV = os.path.join(os.path.dirname(__file__), 'image_download_report.csv')

os.makedirs(ASSETS_DIR, exist_ok=True)


# This regex will match image links even if the URL is broken by newlines (greedy match inside parentheses)
IMAGE_REGEX = re.compile(r'!\[[^\]]*\]\((https?://[\s\S]*?)\)', re.MULTILINE)


def download_image(url, dest_folder):
	# Remove any line breaks and whitespace from the URL
	clean_url = url.replace('\n', '').replace('\r', '').replace(' ', '')
	parsed = urlparse(clean_url)
	filename = os.path.basename(parsed.path)
	local_path = os.path.join(dest_folder, filename)
	try:
		resp = requests.get(clean_url, timeout=10)
		resp.raise_for_status()
		with open(local_path, 'wb') as f:
			f.write(resp.content)
		return filename, 'Downloaded'
	except Exception as e:
		print(f"Failed to download {clean_url}: {e}")
		return None, f'Failed: {e}'


def process_post(filepath, report_rows):
	with open(filepath, 'r', encoding='utf-8') as f:
		content = f.read()

	new_content = content
	updated = False
	post_name = os.path.basename(filepath)
	for match in IMAGE_REGEX.finditer(content):
		url = match.group(1)
		# Clean the URL for download and for replacement
		clean_url = url.replace('\n', '').replace('\r', '').replace(' ', '')
		filename, status = download_image(url, ASSETS_DIR)
		if filename:
			new_link = f'./assets/img/posts/{filename}'
			# Replace the possibly broken URL (with newlines) with the new local path
			new_content = new_content.replace(url, new_link)
			updated = True
			report_rows.append([post_name, url, new_link, status])
		else:
			report_rows.append([post_name, url, '', status])

	if updated:
		with open(filepath, 'w', encoding='utf-8') as f:
			f.write(new_content)
		print(f"Updated: {filepath}")
	else:
		print(f"No changes: {filepath}")

def main():
	report_rows = [['Post Name', 'Original Image URL', 'New Image Path', 'Status']]
	for fname in os.listdir(POSTS_DIR):
		if fname.endswith('.md'):
			process_post(os.path.join(POSTS_DIR, fname), report_rows)
	with open(REPORT_CSV, 'w', newline='', encoding='utf-8') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerows(report_rows)
	print(f"CSV report generated at: {REPORT_CSV}")

if __name__ == '__main__':
	main()
