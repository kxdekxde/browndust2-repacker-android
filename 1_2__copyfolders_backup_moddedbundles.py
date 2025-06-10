import os
import shutil

# Get the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define paths
backup_folder = os.path.join(script_dir, "Backup")
modded_bundles_folder = os.path.join(script_dir, "Modded Bundles")

def copy_subfolders(src, dst):
    """Copy all subfolders from src to dst"""
    if not os.path.exists(src):
        print(f"Error: Source folder '{src}' does not exist")
        return False
    
    if not os.path.exists(dst):
        os.makedirs(dst)
    
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        if os.path.isdir(src_path):
            dst_path = os.path.join(dst, item)
            
            # Remove destination folder if it exists
            if os.path.exists(dst_path):
                try:
                    shutil.rmtree(dst_path)
                    print(f"Removed existing folder: {dst_path}")
                except Exception as e:
                    print(f"Error removing {dst_path}: {e}")
                    continue
            
            # Copy the folder
            try:
                shutil.copytree(src_path, dst_path)
                print(f"Copied: {src_path} → {dst_path}")
            except Exception as e:
                print(f"Error copying {src_path}: {e}")
    
    return True

if __name__ == "__main__":
    print("Starting folder copy operation...")
    print(f"Source: {backup_folder}")
    print(f"Destination: {modded_bundles_folder}")
    
    if copy_subfolders(backup_folder, modded_bundles_folder):
        print("\nOperation completed successfully!")
    else:
        print("\nOperation failed with errors.")