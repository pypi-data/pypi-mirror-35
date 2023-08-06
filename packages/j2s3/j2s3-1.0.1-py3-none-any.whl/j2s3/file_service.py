def get_file_content(path):
    with open(path, 'r') as file:
        return file.read().replace('\n', '')

def write_file_content(path, content):
    with open(path, 'w') as file:
        file.write(content)