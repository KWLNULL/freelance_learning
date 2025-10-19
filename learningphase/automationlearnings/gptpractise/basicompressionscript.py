import pikepdf
import os

def compress_pdf(input_file, output_file, quality="default"):
    pdf = pikepdf.open(input_file)
    
    # Save with optimization
    pdf.save(output_file, linearize=True)
    pdf.close()
    
    original = os.path.getsize(input_file) / 1024
    compressed = os.path.getsize(output_file) / 1024
    
    print(f"✅ Compression done!")
    print(f"Original: {original:.2f} KB → Compressed: {compressed:.2f} KB")

if __name__ == "__main__":
    compress_pdf("merged_basic.pdf", "merged_compressed.pdf")
