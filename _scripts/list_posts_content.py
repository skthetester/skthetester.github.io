import os

POSTS_DIR = '_posts'

def list_files_with_content(directory):
    files = os.listdir(directory)
    result = []
    for file in files:
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            # Remove YAML front matter if present
            content_lines = []
            in_front_matter = False
            for line in lines:
                if line.strip() == '---':
                    in_front_matter = not in_front_matter
                    continue
                if not in_front_matter:
                    content_lines.append(line)
            # Join and strip whitespace
            display_content = ''.join(content_lines).strip()
            has_content = 'yes' if display_content else 'no'
            result.append({'name': file, 'has_content': has_content})
    return result

def main():
    results = list_files_with_content(POSTS_DIR)
    output_file = 'posts_content_report.txt'
    with open(output_file, 'w', encoding='utf-8') as out:
        for entry in results:
            out.write(f"{entry['name']}: {entry['has_content']}\n")
    print(f"Report written to {output_file}")

if __name__ == '__main__':
    main()
