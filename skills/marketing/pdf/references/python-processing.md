# Python PDF Processing Reference

## 1. pypdf (Basic Operations)

### Merge PDFs

```python
from pypdf import PdfWriter, PdfReader
writer = PdfWriter()
for pdf_file in ["doc1.pdf", "doc2.pdf"]:
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        writer.add_page(page)
with open("merged.pdf", "wb") as output:
    writer.write(output)
```

### Split PDF

```python
reader = PdfReader("input.pdf")
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    writer.add_page(page)
    with open(f"page_{i+1}.pdf", "wb") as output:
        writer.write(output)
```

### Metadata & Rotation

```python
reader = PdfReader("document.pdf")
meta = reader.metadata
# Rotate
page = reader.pages[0].rotate(90)
```

## 2. pdfplumber (Extraction)

### Text with Layout

```python
import pdfplumber
with pdfplumber.open("document.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

### Table Extraction (to Pandas)

```python
with pdfplumber.open("document.pdf") as pdf:
    table = pdf.pages[0].extract_table()
    df = pd.DataFrame(table[1:], columns=table[0])
```

## 3. reportlab (Creation)

### Canvas-based Creation (Low-level)

```python
from reportlab.pdfgen import canvas
c = canvas.Canvas("hello.pdf")
c.drawString(100, 750, "Hello World!")
c.save()
```

### Platypus (Document Templates)

```python
from reportlab.platypus import SimpleDocTemplate, Paragraph
doc = SimpleDocTemplate("report.pdf")
doc.build([Paragraph("Title", style)])
```

## 4. OCR for Scanned PDFs

```python
import pytesseract
from pdf2image import convert_from_path
images = convert_from_path('scanned.pdf')
text = pytesseract.image_to_string(images[0])
```
