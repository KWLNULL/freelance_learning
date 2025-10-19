import os

def merge_text_files(input_files, output_file):
    """Merge multiple text files into one output file."""
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for file in input_files:
            if os.path.exists(file):
                with open(file, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read().strip() + "\n\n")
            else:
                print(f"[!] File not found: {file}")
    print(f"✅ Merged {len(input_files)} files into {output_file}")

if __name__ == "__main__":
    files = ["sample1.txt", "sample2.txt", "sample3.txt"]
    for i, name in enumerate(files, start=1):
        with open(name, "w") as f:
            f.write(f"This is file {i}")
    merge_text_files(files, "merged_output.txt")
