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

preface_text = [
    "This comprehensive Integrated Science textbook for Basic 7 has been carefully",
    "prepared to support Junior High School students in their preparation for the",
    "Basic Education Certificate Examination (BECE).",
    "",
    "The book contains:",
    "• Multiple choice questions with complete answer keys",
    "• Theory questions with detailed marking schemes",
    "• Curriculum-aligned content following the 2019 Standards-Based Curriculum",
    "• Practice papers from BECE Mock examinations",
    "• Diagram Mode practice papers with scientific illustrations",
    "",
    "Each question has been verified for accuracy and aligned with the appropriate",
    "curriculum objectives. The marking schemes provide detailed explanations to",
    "help students understand the reasoning behind each answer.",
    "",
    "We hope this book will be a valuable resource in your academic journey.",
    "",
    "— Beacon Educational Consult",
    "Accra, Ghana",
    "2026"
]

for i, line in enumerate(preface_text):
    print(f"Line {i}: {repr(line[:50])}...")
    print(f"  Y position: {pdf.get_y()}")
    if line.strip() == "":
        pdf.ln(4)
        print(f"  -> Empty line, ln(4)")
    else:
        try:
            pdf.multi_cell(0, 6, line)
            print(f"  -> SUCCESS")
        except Exception as e:
            print(f"  -> FAILED: {e}")
            break

print("\nTest complete")
