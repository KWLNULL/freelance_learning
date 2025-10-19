from fpdf import FPDF

pdf = FPDF()
for i in range(1, 3):
    pdf.add_page()
    pdf.set_font("Arial", size=18)
    pdf.cell(200, 100, txt=f"This is sample PDF {i}", ln=True, align="C")
    pdf.output(f"{chr(96+i)}.pdf")  # creates a.pdf, b.pdf

print("✅ Created sample a.pdf and b.pdf")
