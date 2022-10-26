from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "", 50)
pdf.image("shirtificate.png", 0, 50)
pdf.cell(0, 30, "CS50 Shirtificate", align ="C" )
pdf.set_y(80)
pdf.set_font("helvetica", "", 30)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 80,f"{input('Name: ')} took CS50", align= "C")
pdf.output("shirtificate.pdf")