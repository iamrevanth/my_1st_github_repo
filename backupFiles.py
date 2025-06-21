import os
import sys
import shutil
from datetime import datetime

def backup_files(src_dir, dest_dir):
    if not os.path.isdir(src_dir):
        print(f"Error: Source directory '{src_dir}' does not exist.")
        return
    if not os.path.isdir(dest_dir):
        print(f"Error: Destination directory '{dest_dir}' does not exist.")
        return

    for filename in os.listdir(src_dir):
        src_file = os.path.join(src_dir, filename)
        if os.path.isfile(src_file):
            dest_file = os.path.join(dest_dir, filename)
            if os.path.exists(dest_file):
                name, ext = os.path.splitext(filename)
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                new_filename = f"{name}_{timestamp}{ext}"
                dest_file = os.path.join(dest_dir, new_filename)
            try:
                shutil.copy2(src_file, dest_file)
                print(f"Copied: {src_file} -> {dest_file}")
            except Exception as e:
                print(f"Failed to copy {src_file}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
        sys.exit(1)
    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]
    backup_files(source_directory, destination_directory)