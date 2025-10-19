import pikepdf
import os

def compress_pdf(input_file, output_file):
    pdf = pikepdf.open(input_file)
    pdf.save(output_file, linearize=True)
    pdf.close()

    original = os.path.getsize(input_file) / 1024
    compressed = os.path.getsize(output_file) / 1024

    print("✅ Compression complete!")
    print(f"Original: {original:.2f} KB → Compressed: {compressed:.2f} KB")

if __name__ == "__main__":
    # Use your actual file path here
    compress_pdf(r"C:\Users\KIIT\Desktop\RTC\freelance_projects\heavy_test.pdf",
             r"C:\Users\KIIT\Desktop\RTC\freelance_projects\heavy_test_compressed.pdf")

