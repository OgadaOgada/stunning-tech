# hello_reportlab.py
from reportlab.pdfgen import canvas

filename = "myReportlab.pdf"
documentTitle = "This is My Document Title"
title = "Collince Technologies"
subtitle = "We run the ICTR"
textlines = [
    """Video provides a powerful way to help you prove your point. When you click Online Video, you can paste in the embed code for the video you want to add. You can also type a keyword to search online for the video that best fits your document.
To make your document look professionally produced, Word provides header, footer, cover page, and text box designs that complement each other. For example, you can add a matching cover page, header, and sidebar. Click Insert and then choose the elements you want from the different galleries.
Themes and styles also help keep your document coordinated. When you click Design and choose a new Theme, the pictures, charts, and SmartArt graphics change to match your new theme. When you apply styles, your headings change to match the new theme.
Save time in Word with new buttons that show up where you need them. To change the way a picture fits in your document, click it and a button for layout options appears next to it. When you work on a table, click where you want to add a row or a column, and then click the plus sign.
"""
]
def drawRuler(pdf):
    pdf.drawString(100,810,'x100')
    pdf.drawString(200,810,'x200')
    pdf.drawString(300,810,'x300')
    pdf.drawString(400,810,'x400')
    pdf.drawString(500,810,'x500')

    pdf.drawString(10,100,'y100')
    pdf.drawString(10,200,'y200')
    pdf.drawString(10,300,'y300')
    pdf.drawString(10,400,'y400')
    pdf.drawString(10,500,'y500')
    pdf.drawString(10,600,'y600')
    pdf.drawString(10,700,'y700')
    pdf.drawString(10,810,'y800')


pdf = canvas.Canvas(filename)
pdf.setTitle(documentTitle)

# show all fonts
for font in pdf.getAvailableFonts():
    print(font)

# register new font
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(
    TTFont('abc',)
)

pdf.drawString(250,800, title)

drawRuler(pdf)




pdf.save()

