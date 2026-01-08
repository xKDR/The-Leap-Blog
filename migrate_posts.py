import os
import shutil
import re
import yaml

# Source and destination
SOURCE_DIR = "posts"
PROJECT_ROOT = "."
METADATA_FILE = os.path.join(SOURCE_DIR, "_metadata.yml")

# Regex to parse folder name: YYYY-MM-DD-slug
folder_pattern = re.compile(r"(\d{4})-(\d{2})-(\d{2})-(.+)")

def migrate():
    if not os.path.exists(SOURCE_DIR):
        print(f"Source directory {SOURCE_DIR} does not exist.")
        return

    # Read the metadata content to copy later
    metadata_content = ""
    if os.path.exists(METADATA_FILE):
        with open(METADATA_FILE, "r") as f:
            metadata_content = f.read()

    # Iterate over items in posts/
    for item in os.listdir(SOURCE_DIR):
        item_path = os.path.join(SOURCE_DIR, item)
        
        if not os.path.isdir(item_path):
            continue
            
        match = folder_pattern.match(item)
        if match:
            year, month, day, slug = match.groups()
            
            # Destination path: YYYY/MM/
            dest_dir = os.path.join(PROJECT_ROOT, year, month)
            os.makedirs(dest_dir, exist_ok=True)
            
            # Ensure metadata exists in the year folder (e.g., 2025/_metadata.yml)
            # Actually, proper place is usually the directory containing the qmds. 
            # If we have 2025/12/slug.qmd, metadata in 2025/_metadata.yml applies!
            year_metadata = os.path.join(PROJECT_ROOT, year, "_metadata.yml")
            if not os.path.exists(year_metadata) and metadata_content:
                with open(year_metadata, "w") as f:
                    # Fix relative paths in metadata
                    # ../_ejs/similar.ejs becomes ../../_ejs/similar.ejs if deep?
                    # No, _metadata in 2025/ applies to 2025/12/post.qmd.
                    # 2025/ is at root. _ejs is at root. So path is ../_ejs/similar.ejs
                    f.write(metadata_content)

            # Move and rename index.qmd
            src_file = os.path.join(item_path, "index.qmd")
            if os.path.exists(src_file):
                dest_file = os.path.join(dest_dir, f"{slug}.qmd")
                shutil.move(src_file, dest_file)
                print(f"Moved {src_file} -> {dest_file}")
            else:
                print(f"No index.qmd found in {item_path}")
                
    # Optional: Clean up empty posts folders
    # shutil.rmtree(SOURCE_DIR) 
    print("Migration complete.")

if __name__ == "__main__":
    migrate()
