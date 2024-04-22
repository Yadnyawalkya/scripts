# Find duplicate files using same file names and move it other dir
import os
import shutil
import concurrent.futures

def find_duplicates(root_dir):
    """Find duplicate files recursively in a directory."""
    duplicates = {}
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if filename in duplicates:
                duplicates[filename].append(file_path)
            else:
                duplicates[filename] = [file_path]

    return {k: v for k, v in duplicates.items() if len(v) > 1}

def move_file(file_path, dest_dir):
    """Move a file to the destination directory."""
    try:
        shutil.move(file_path, dest_dir)
        print(f"Moved file: {file_path}")
    except Exception as e:
        print(f"Error moving file {file_path}: {e}")

def move_duplicates(duplicates, dest_dir):
    """Move duplicate files to the destination directory."""
    with concurrent.futures.ThreadPoolExecutor(max_workers=300) as executor:
        futures = []
        for filename, file_paths in duplicates.items():
            for file_path in file_paths[1:]:  # Skip the first occurrence
                futures.append(executor.submit(move_file, file_path, dest_dir))
        for future in concurrent.futures.as_completed(futures):
            pass  # We wait for all tasks to complete

def main():
    root_dir = "/home/ytale/Music/aa_photos"
    dest_dir = "/home/ytale/Music/copy"
    
    duplicate_files = find_duplicates(root_dir)
    if duplicate_files:
        print("Duplicate files found:")
        for filename, file_paths in duplicate_files.items():
            print(f"Filename: {filename}")
            for file_path in file_paths:
                print(f"- {file_path}")
        move_duplicates(duplicate_files, dest_dir)
        print("Duplicate files moved to:", dest_dir)
    else:
        print("No duplicate files found.")

if __name__ == "__main__":
    main()
