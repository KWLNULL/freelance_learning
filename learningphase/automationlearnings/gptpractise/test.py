import os

# User input
folder_path = input("Enter folder path: ")
prefix = input("Enter prefix for files: ")

try:
    files = os.listdir(folder_path)
    for count, filename in enumerate(files):
        # Get file extension (lowercase)
        ext = os.path.splitext(filename)[1].lower()

        # Create new name
        new_name = f"{prefix}_{count+1}{ext}"

        # Full paths
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_name)

        # Avoid overwrite
        if os.path.exists(dst):
            dst = os.path.join(folder_path, f"{prefix}_{count+1}_new{ext}")

        # Rename
        os.rename(src, dst)
        print(f"Renamed: {filename} → {new_name}")

    print("✅ Files renamed successfully!")

except FileNotFoundError:
    print("❌ Error: Folder not found.")
