from reportlab.pdfgen import canvas
my_canvas = canvas.Canvas("hello.pdf")
my_canvas.drawString(100,75,"Welcome to Reportlab!")
my_canvas.showPage()
my_canvas.save()