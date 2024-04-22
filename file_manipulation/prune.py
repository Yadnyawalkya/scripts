# Using file names find duplicates on target locations, keep files from higer size and delete lower size files
import os
import shutil
from multiprocessing import Pool

def find_files_recursive(directory):
    """
    Recursively finds all files in a directory and its subdirectories.
    """
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files

def check_and_move_file(args):
    source_file, source_dir, target_dir = args
    source_path = os.path.join(source_dir, source_file)
    target_files = find_files_recursive(target_dir)

    if any(os.path.basename(source_path) == os.path.basename(target_file) for target_file in target_files):
        for target_path in target_files:
            if os.path.basename(source_path) == os.path.basename(target_path):
                source_size = os.path.getsize(source_path)
                target_size = os.path.getsize(target_path)
                
                if source_size == target_size:
                    os.remove(source_path)
                    print(f"Deleted {source_file} from {source_dir}")
                elif source_size > target_size:
                    shutil.copy2(source_path, target_path)
                    os.remove(source_path)
                    print(f"Replaced {source_file} in {target_dir}")
                elif source_size < target_size:
                    os.remove(source_path)
                    print(f"Removed {source_file}; no need to change {target_dir}")
                break

def check_and_move_files(source_dir, target_dir):
    source_files = os.listdir(source_dir)
    args = [(file, source_dir, target_dir) for file in source_files]
    
    with Pool(processes=300) as pool:
        pool.map(check_and_move_file, args)

# Specify source and target directories
source_directory = '/all-photo'
target_directory = '/home/ytale/Music/aa_photos'

# Call function to check and move files
check_and_move_files(source_directory, target_directory)

