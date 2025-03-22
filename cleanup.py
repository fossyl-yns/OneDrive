import os
import humanize

# Set your OneDrive folder path
onedrive_path = os.path.expanduser("~/OneDrive")  # Adjust if needed

# Function to get the largest files
def get_large_files(folder, limit=10):
    file_sizes = []
    for root, _, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                size = os.path.getsize(file_path)
                file_sizes.append((file_path, size))
            except OSError:
                pass
    file_sizes.sort(key=lambda x: x[1], reverse=True)
    return file_sizes[:limit]

# Find the largest files
large_files = get_large_files(onedrive_path)

# Show them
print("\nTop Large Files:")
for i, (path, size) in enumerate(large_files, 1):
    print(f"{i}. {path} - {humanize.naturalsize(size)}")

# Ask to delete
to_delete = input("\nEnter numbers to delete (comma-separated), or 'all' to remove everything: ").strip()
if to_delete.lower() == "all":
    for path, _ in large_files:
        os.remove(path)
        print(f"Deleted: {path}")
elif to_delete:
    numbers = [int(x.strip()) for x in to_delete.split(",") if x.strip().isdigit()]
    for i in numbers:
        if 1 <= i <= len(large_files):
            os.remove(large_files[i - 1][0])
            print(f"Deleted: {large_files[i - 1][0]}")
