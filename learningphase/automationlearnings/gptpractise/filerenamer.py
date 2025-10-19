import os

# Change this to your test folder path
folder_path = r"C:\Users\KIIT\Desktop\test_folder"

for count, filename in enumerate(os.listdir(folder_path)):
    # Get file extension
    ext = os.path.splitext(filename)[1]
    # Create new name
    if ext=='.jpg':
        new_name = f"photo_{count+1}.jpg"
    elif ext=='.pdf':
        new_name = f"pdf_{count+1}.pdf"
    else:
        new_name = f"file_{count+1}.txt"
    # Build full paths
    src = os.path.join(folder_path, filename)
    dst = os.path.join(folder_path, new_name)
    # Rename
    os.rename(src, dst)

print("✅ Files renamed successfully!")
