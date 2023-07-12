from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from PyPDF2 import PdfFileReader, PdfFileWriter

def makeWatermark():
    text = input("Enter the watermark text here:")
    pdf = canvas.Canvas("watermark.pdf", pagesize=A4)
    pdf.translate(inch, inch)
    pdf.setFillColor(colors.grey, alpha=0.6)
    pdf.setFont("Helvetica", 125)
    pdf.rotate(45)
    pdf.drawCentredString(400, 30, text)
    pdf.save()

makeWatermark()