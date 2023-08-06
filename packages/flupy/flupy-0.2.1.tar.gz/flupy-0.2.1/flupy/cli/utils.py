import os

def walk_files(path):
    """Yield files recursively starting from *path"""
    for d, dirs, files in os.walk(path):
        for x in files:
            yield os.path.join(d, x)

def walk_folders(path):
    """Yield files recursively starting from *path"""
    for d, _, _ in os.walk(path):
        yield d

