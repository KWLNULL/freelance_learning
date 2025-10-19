import os
from PyPDF2 import PdfMerger

pdfs = ['a.pdf', 'b.pdf']
merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged_basic.pdf")
merger.close()

print("✅ merged_basic.pdf created successfully!")
