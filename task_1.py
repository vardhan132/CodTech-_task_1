import os
import hashlib

def calculate_hash(file_path):
    with open(file_path, 'rb') as f:
        file_data = f.read()
        return hashlib.sha256(file_data).hexdigest()

def store_hashes(directory, output_file):
    hashes = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            hashes[file_path] = calculate_hash(file_path)
    with open(output_file, 'w') as f:
        for path, hash_val in hashes.items():
            f.write(f"{path} {hash_val}\n")

def compare_hashes(directory, hash_file):
    with open(hash_file, 'r') as f:
        stored_hashes = {line.split()[0]: line.split()[1] for line in f}
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            current_hash = calculate_hash(file_path)
            if file_path in stored_hashes:
                if stored_hashes[file_path] != current_hash:
                    print(f"[MODIFIED] {file_path}")
            else:
                print(f"[NEW] {file_path}")
