# PDF Command-Line Tools Reference

## 1. qpdf (Structural Operations)

- **Merge**: `qpdf --empty --pages f1.pdf f2.pdf -- merged.pdf`
- **Split**: `qpdf input.pdf --pages . 1-5 -- pages1-5.pdf`
- **Rotate**: `qpdf input.pdf output.pdf --rotate=+90:1`
- **Decrypt**: `qpdf --password=pw --decrypt encrypted.pdf decrypted.pdf`

## 2. poppler-utils (Extraction)

- **pdftotext**: `pdftotext -layout input.pdf output.txt`
- **pdfimages**: `pdfimages -j input.pdf output_prefix`
- **pdffonts**: List fonts used in a PDF.

## 3. pdftk (Versatile Operations)

- **Merge**: `pdftk f1.pdf f2.pdf cat output merged.pdf`
- **Rotate**: `pdftk input.pdf rotate 1east output rotated.pdf`
- **Burst**: `pdftk input.pdf burst` (splits into individual pages)

## 4. ghostscript (Optimization)

- **Compress**:
  ```bash
  gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf
  ```
