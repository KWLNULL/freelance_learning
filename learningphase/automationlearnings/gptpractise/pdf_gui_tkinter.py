import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger
import subprocess
import os

# ---------- Backend Functions ----------
def merge_pdfs(file_list, output_path):
    merger = PdfMerger()
    for file in file_list:
        merger.append(file)
    merger.write(output_path)
    merger.close()

def compress_pdf(input_file, output_file):
    try:
        subprocess.run([
            "gs", "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.4",
            "-dPDFSETTINGS=/screen", "-dNOPAUSE", "-dQUIET", "-dBATCH",
            f"-sOutputFile={output_file}", input_file
        ], check=True)
        return True
    except Exception as e:
        messagebox.showerror("Compression Failed", str(e))
        return False

# ---------- GUI Logic ----------
def select_files():
    files = filedialog.askopenfilenames(
        title="Select PDF files",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if files:
        file_listbox.delete(0, tk.END)
        for f in files:
            file_listbox.insert(tk.END, f)

def start_merge():
    files = file_listbox.get(0, tk.END)
    if not files:
        messagebox.showwarning("No Files", "Please select PDF files first!")
        return

    output_file = output_entry.get().strip()
    if not output_file.endswith(".pdf"):
        output_file += ".pdf"

    try:
        merge_pdfs(files, output_file)
        status_label.config(text=f"✅ Merged {len(files)} PDFs into {output_file}")
        if compress_var.get():
            compressed_name = "compressed_" + os.path.basename(output_file)
            if compress_pdf(output_file, compressed_name):
                status_label.config(text=f"✅ Compressed file saved as {compressed_name}")
    except Exception as e:
        messagebox.showerror("Error", str(e))
        status_label.config(text="❌ Merge failed")

# ---------- UI Setup ----------
root = tk.Tk()
root.title("PDF Merger + Compressor")
root.geometry("600x400")
root.config(bg="#212121")

# File list
tk.Label(root, text="Selected PDFs", fg="white", bg="#212121", font=("Segoe UI", 11, "bold")).pack(pady=5)
file_listbox = tk.Listbox(root, width=70, height=10, selectmode=tk.MULTIPLE, bg="#333", fg="white")
file_listbox.pack()

# Buttons
tk.Button(root, text="Select Files", command=select_files, bg="#3f51b5", fg="white", width=15).pack(pady=5)

# Output entry
output_frame = tk.Frame(root, bg="#212121")
output_frame.pack(pady=5)
tk.Label(output_frame, text="Output File:", fg="white", bg="#212121").pack(side=tk.LEFT)
output_entry = tk.Entry(output_frame, width=40)
output_entry.insert(0, "merged_output.pdf")
output_entry.pack(side=tk.LEFT, padx=5)

# Compress option
compress_var = tk.BooleanVar()
tk.Checkbutton(root, text="Compress after merge", variable=compress_var, bg="#212121", fg="white").pack()

# Merge button
tk.Button(root, text="Merge PDFs", command=start_merge, bg="#4caf50", fg="white", width=15).pack(pady=10)

# Status label
status_label = tk.Label(root, text="", fg="lightgreen", bg="#212121", font=("Consolas", 10))
status_label.pack(pady=10)

root.mainloop()
