from fpdf import FPDF
from PIL import Image
import requests
from io import BytesIO

pdf = FPDF()

# Use free high-res placeholder images (unsplash)
urls = [
    "https://images.unsplash.com/photo-1503264116251-35a269479413",
    "https://images.unsplash.com/photo-1516117172878-fd2c41f4a759",
    "https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d",
    "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e"
]

for idx, url in enumerate(urls, start=1):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    # Convert to RGB (some Unsplash images are RGBA)
    img = img.convert("RGB")
    img.save(f"page_{idx}.jpg")

    pdf.add_page()
    pdf.image(f"page_{idx}.jpg", x=0, y=0, w=210, h=297)

pdf.output("heavy_test.pdf")
print("✅ heavy_test.pdf created (large & image-heavy)")
