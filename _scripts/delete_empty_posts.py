import os

POSTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), '_posts')
REPORT_FILE = os.path.join(os.path.dirname(__file__), 'posts_content_report.txt')

def delete_empty_posts(report_file, posts_dir):
    with open(report_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    deleted = []
    for line in lines:
        if line.strip().endswith(': no'):
            filename = line.split(':')[0].strip()
            file_path = os.path.join(posts_dir, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
                deleted.append(filename)
    return deleted

def main():
    deleted = delete_empty_posts(REPORT_FILE, POSTS_DIR)
    if deleted:
        print('Deleted files:')
        for f in deleted:
            print(f"  {f}")
    else:
        print('No files deleted.')

if __name__ == '__main__':
    main()
