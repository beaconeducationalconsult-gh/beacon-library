#!/usr/bin/env python3
"""Test the enhance_books module with debug output."""

from fpdf import FPDF
import os

pdf = FPDF(format='A4')
pdf.add_font("Body", "", "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf")
pdf.add_font("Heading", "B", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
pdf.set_auto_page_break(auto=True, margin=25)
pdf.set_margins(20, 20, 20)
pdf.add_page()

pdf.set_font("Heading", "B", 18)
pdf.ln(20)
pdf.cell(0, 10, "Preface", ln=True, align='C')

pdf.ln(10)
pdf.set_font("Body", "", 11)

print(f"After heading - X: {pdf.get_x()}, Y: {pdf.get_y()}")

line1 = "This comprehensive Integrated Science textbook for Basic 7 has been carefully"
pdf.multi_cell(0, 6, line1)
print(f"After line1 - X: {pdf.get_x()}, Y: {pdf.get_y()}")

line2 = "prepared to support Junior High School students in their preparation for the"
try:
    pdf.multi_cell(0, 6, line2)
    print(f"After line2 - X: {pdf.get_x()}, Y: {pdf.get_y()}")
except Exception as e:
    print(f"FAILED on line2: {e}")
    print(f"  X position before: {pdf.get_x()}")
    print(f"  Left margin: {pdf.l_margin}")
    print(f"  Right margin: {pdf.r_margin}")
    print(f"  Effective width: {pdf.w - pdf.l_margin - pdf.r_margin}")
    
    # Try setting x back to left margin
    pdf.set_x(pdf.l_margin)
    print(f"  Reset X to: {pdf.get_x()}")
    try:
        pdf.multi_cell(0, 6, line2)
        print(f"  SUCCESS after reset")
    except Exception as e2:
        print(f"  STILL FAILED: {e2}")
