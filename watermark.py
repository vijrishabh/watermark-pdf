from PyPDF2 import PdfFileMerger, PdfReader, PdfWriter

pdf_file = "input.pdf"
watermark = "watermark.pdf"
merged = "merged.pdf"


with open(pdf_file, "rb") as input_file, open(watermark, "rb") as watermark_file:
    input_pdf = PdfReader(input_file)
    watermark_pdf = PdfReader(watermark_file)
    watermark_page = watermark_pdf.pages[0]

    output = PdfWriter()

    for i in range(len(input_pdf.pages)):
        pdf_page = input_pdf.pages[i]
        pdf_page.merge_page(watermark_page)
        pdf_page.compress_content_streams()
        output.add_page(pdf_page)

    with open(merged, "wb") as merged_file:
        output.write(merged_file)