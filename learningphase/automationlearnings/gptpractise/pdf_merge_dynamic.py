import os
from PyPDF2 import PdfMerger, PdfReader
from PyPDF2.errors import PdfReadError
from datetime import datetime

def is_valid_pdf(file_path):
    """Check if file is a valid, readable PDF."""
    try:
        reader = PdfReader(file_path)
        _ = len(reader.pages)
        return True
    except (PdfReadError, Exception):
        return False

def merge_all_pdfs(input_dir, output_file):
    merger = PdfMerger()
    merged_files = []
    skipped_files = []

    for file in os.listdir(input_dir):
        if file.lower().endswith(".pdf"):
            full_path = os.path.join(input_dir, file)
            if is_valid_pdf(full_path):
                try:
                    merger.append(full_path)
                    merged_files.append(file)
                    print(f"✅ Merged: {file}")
                except Exception as e:
                    skipped_files.append((file, str(e)))
                    print(f"⚠️ Skipped (merge error): {file} — {e}")
            else:
                skipped_files.append((file, "Invalid PDF"))
                print(f"❌ Skipped invalid PDF: {file}")

    merger.write(output_file)
    merger.close()

    log_summary(output_file, merged_files, skipped_files)

def log_summary(output_file, merged_files, skipped_files):
    """Write a merge summary log."""
    log_file = "merge_log.txt"
    with open(log_file, "w", encoding="utf-8") as f:
        f.write(f"Merge Summary ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})\n")
        f.write(f"Output file: {output_file}\n\n")
        f.write("Merged files:\n")
        for m in merged_files:
            f.write(f"  ✅ {m}\n")
        f.write("\nSkipped files:\n")
        for s, reason in skipped_files:
            f.write(f"  ❌ {s} — {reason}\n")
    print(f"\n📄 Log saved to {log_file}")

if __name__ == "__main__":
    merge_all_pdfs("testpdfs", "merged_dynamic.pdf")
