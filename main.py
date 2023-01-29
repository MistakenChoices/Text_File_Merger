import os
import time

# Prompt user for folder path
print("WARNING: This will merge all the .txt files to the SAME directory as this python tool.")
folder_path = input("Path containing all the .txt files to merge: ")

# Get list of all .txt files in the folder
txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

# Create a new file to store the merged content
with open('merged_file.txt', 'w',encoding='utf-8') as outfile:
    start_time = time.time()
    try:
        for idx, fname in enumerate(txt_files):
            with open(os.path.join(folder_path, fname), 'rb') as infile:
                # read the file as bytes, then decode it as utf-8
                outfile.write(infile.read().decode('utf-8'))
                # Calculate ETA and print it
                elapsed_time = time.time() - start_time
                files_left = len(txt_files) - (idx + 1)
                eta = elapsed_time / (idx + 1) * files_left
                m, s = divmod(eta, 60)
                h, m = divmod(m, 60)
                print(f'ETA: {int(h)} hours, {int(m)} minutes, {int(s)} seconds')
        print("All .txt files from the folder has been merged into the merged_file.txt")
    except KeyboardInterrupt:
        # Handle keyboard interrupt (CTRL+C)
        print("\nMerging operation cancelled by user.")
