import os

def ensure_dir(directory):
    """Ensure that a directory exists."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def read_file(file_path):
    """Reads a file and returns its content."""
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    """Writes content to a file."""
    with open(file_path, 'w') as file:
        file.write(content)
