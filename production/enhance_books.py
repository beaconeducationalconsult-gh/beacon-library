#!/usr/bin/env python3
"""
Enhanced Front/Back Matter Generator
Adds glossaries, formula sheets, and enhanced front matter to all books
"""

import json
import os
from fpdf import FPDF
from PyPDF2 import PdfReader, PdfWriter

class EnhancedMatterGenerator:
    """Generate enhanced front and back matter for Beacon books."""
    
    def __init__(self, subject, level):
        self.subject = subject
        self.level = level
        self.font_dir = "/usr/share/fonts/truetype/dejavu"
        
    def _create_base_pdf(self):
        """Create a base PDF with proper fonts."""
        pdf = FPDF(format='A4')
        pdf.add_font("Body", "", os.path.join(self.font_dir, "DejaVuSerif.ttf"))
        pdf.add_font("Body", "B", os.path.join(self.font_dir, "DejaVuSerif-Bold.ttf"))
        pdf.add_font("Heading", "", os.path.join(self.font_dir, "DejaVuSans.ttf"))
        pdf.add_font("Heading", "B", os.path.join(self.font_dir, "DejaVuSans-Bold.ttf"))
        pdf.set_auto_page_break(auto=True, margin=25)
        pdf.set_margins(20, 20, 20)  # left, top, right margins
        return pdf
    
    def generate_title_page(self):
        """Generate professional title page."""
        pdf = self._create_base_pdf()
        pdf.add_page()
        
        # Title
        pdf.set_font("Heading", "B", 28)
        pdf.ln(40)
        
        if self.subject == "Integrated Science":
            pdf.cell(0, 15, "Integrated Science", ln=True, align='C')
        else:
            pdf.cell(0, 15, "Mathematics", ln=True, align='C')
        
        pdf.set_font("Heading", "", 20)
        pdf.ln(5)
        pdf.cell(0, 12, f"Basic {self.level}", ln=True, align='C')
        
        pdf.ln(10)
        pdf.set_font("Body", "", 14)
        pdf.cell(0, 10, "Complete BECE Preparation", ln=True, align='C')
        pdf.cell(0, 10, "Examination Papers & Marking Schemes", ln=True, align='C')
        
        pdf.ln(30)
        pdf.set_font("Heading", "B", 16)
        pdf.cell(0, 10, "Beacon Educational Consult", ln=True, align='C')
        
        pdf.ln(5)
        pdf.set_font("Body", "", 12)
        pdf.cell(0, 8, "2026 Edition", ln=True, align='C')
        
        return pdf
    
    def generate_copyright_page(self):
        """Generate copyright page."""
        pdf = self._create_base_pdf()
        pdf.add_page()
        
        pdf.set_font("Body", "", 10)
        pdf.ln(50)
        
        copyright_text = [
            f"© 2026 Beacon Educational Consult",
            "All rights reserved.",
            "",
            "No part of this publication may be reproduced, stored in a retrieval system,",
            "or transmitted in any form or by any means, electronic, mechanical, photocopying,",
            "recording, or otherwise, without prior written permission from the publisher.",
            "",
            "Published by Beacon Educational Consult",
            "Accra, Ghana",
            "",
            "First Edition: 2026",
            "",
            "ISBN: [To be assigned]",
            "",
            "Printed in Ghana",
            "",
            "This book has been prepared in accordance with the",
            "Ghana Education Service Standards-Based Curriculum (2019)",
            "and the National Council for Curriculum and Assessment (NaCCA) guidelines.",
            "",
            "The publisher has made every effort to ensure the accuracy of the information",
            "contained in this book. However, the publisher cannot accept responsibility for",
            "any errors or omissions or for any consequences arising from the use of this book.",
            "",
            "For permissions and inquiries:",
            "Beacon Educational Consult",
            "Email: info@beaconeducational.com",
            "Website: www.beaconeducational.com"
        ]
        
        for line in copyright_text:
            if line.strip() == "":
                pdf.ln(4)
            else:
                pdf.cell(0, 6, line, new_x="LMARGIN", new_y="NEXT", align='C')
        
        return pdf
    
    def generate_preface_page(self):
        """Generate preface page."""
        pdf = self._create_base_pdf()
        pdf.add_page()
        
        pdf.set_font("Heading", "B", 18)
        pdf.ln(20)
        pdf.cell(0, 10, "Preface", ln=True, align='C')
        
        pdf.ln(10)
        pdf.set_font("Body", "", 11)
        
        preface_text = [
            f"This comprehensive {self.subject} textbook for Basic {self.level} has been carefully",
            "prepared to support Junior High School students in their preparation for the",
            "Basic Education Certificate Examination (BECE).",
            "",
            "The book contains:",
            "• Multiple choice questions with complete answer keys",
            "• Theory questions with detailed marking schemes",
            "• Curriculum-aligned content following the 2019 Standards-Based Curriculum",
            "• Practice papers from BECE Mock examinations",
        ]
        
        if self.subject == "Integrated Science" and self.level == "7":
            preface_text.append("• Diagram Mode practice papers with scientific illustrations")
        
        preface_text.extend([
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
        ])
        
        for line in preface_text:
            if line.strip() == "":
                pdf.ln(4)
            else:
                pdf.set_x(pdf.l_margin)
                pdf.multi_cell(0, 6, line)
        
        return pdf
    
    def generate_glossary(self, glossary_data):
        """Generate glossary section."""
        pdf = self._create_base_pdf()
        pdf.add_page()
        
        # Title
        pdf.set_font("Heading", "B", 18)
        pdf.ln(20)
        pdf.cell(0, 10, glossary_data['title'], ln=True, align='C')
        
        pdf.ln(10)
        pdf.set_font("Body", "", 10)
        pdf.set_x(pdf.l_margin)
        pdf.multi_cell(0, 5, "This glossary contains key terms and definitions that appear throughout this book. "
                       "Use it as a quick reference while studying and preparing for examinations.")
        
        # Terms
        for term_data in glossary_data['terms']:
            # Check if we need a new page
            if pdf.get_y() > 250:
                pdf.add_page()
                pdf.set_font("Body", "", 10)
            
            pdf.ln(3)
            pdf.set_font("Body", "B", 11)
            pdf.cell(0, 6, term_data['term'], ln=True)
            
            pdf.set_font("Body", "", 10)
            pdf.set_x(pdf.l_margin)
            pdf.multi_cell(0, 5, term_data['definition'])
        
        return pdf
    
    def generate_formula_sheet(self, formula_data):
        """Generate formula sheet section."""
        pdf = self._create_base_pdf()
        pdf.add_page()
        
        # Title
        pdf.set_font("Heading", "B", 18)
        pdf.ln(20)
        pdf.cell(0, 10, formula_data['title'], ln=True, align='C')
        
        pdf.ln(10)
        
        # Sections
        for section in formula_data['sections']:
            # Check if we need a new page
            if pdf.get_y() > 240:
                pdf.add_page()
            
            pdf.ln(5)
            pdf.set_font("Heading", "B", 12)
            pdf.cell(0, 8, section['name'], ln=True)
            
            pdf.ln(2)
            pdf.set_font("Body", "", 10)
            
            for formula in section['formulas']:
                # Check if we need a new page
                if pdf.get_y() > 270:
                    pdf.add_page()
                    pdf.set_font("Body", "", 10)
                
                pdf.set_x(pdf.l_margin)
                pdf.set_font("Body", "B", 10)
                pdf.cell(70, 5, formula['name'])
                
                pdf.set_font("Body", "", 10)
                pdf.multi_cell(0, 5, formula['formula'])
                pdf.ln(1)
        
        return pdf
    
    def generate_curriculum_reference(self):
        """Generate curriculum reference page."""
        pdf = self._create_base_pdf()
        pdf.add_page()
        
        pdf.set_font("Heading", "B", 18)
        pdf.ln(20)
        pdf.cell(0, 10, "Curriculum Reference", ln=True, align='C')
        
        pdf.ln(10)
        pdf.set_font("Body", "", 11)
        
        curriculum_text = [
            "This book aligns with the following curriculum standards:",
            "",
            "• Ghana Education Service (GES)",
            "  Standards-Based Curriculum for Junior High Schools (2019)",
            "",
            "• National Council for Curriculum and Assessment (NaCCA)",
            "  Curriculum Framework for Basic Education",
            "",
            "• West African Examinations Council (WAEC)",
            "  BECE Syllabus for Integrated Science / Mathematics",
            "",
            "The content has been reviewed to ensure alignment with:",
            "• Strand and sub-strand organization",
            "• Learning indicators and objectives",
            "• Cognitive levels (Knowledge, Understanding, Application, Analysis)",
            "• Core competencies (Critical Thinking, Problem Solving, Communication)",
            "",
            "Teachers and students should use this book in conjunction with the",
            "official curriculum documents available from the Ghana Education Service.",
            "",
            "For more information:",
            "Ghana Education Service: www.ges.gov.gh",
            "NaCCA: www.nacca.gov.gh",
            "WAEC: www.waec.org"
        ]
        
        for line in curriculum_text:
            if line.strip() == "":
                pdf.ln(4)
            else:
                pdf.set_x(pdf.l_margin)
                pdf.multi_cell(0, 6, line)
        
        return pdf
    
    def generate_about_publisher(self):
        """Generate about the publisher page."""
        pdf = self._create_base_pdf()
        pdf.add_page()
        
        pdf.set_font("Heading", "B", 18)
        pdf.ln(20)
        pdf.cell(0, 10, "About Beacon Educational Consult", ln=True, align='C')
        
        pdf.ln(10)
        pdf.set_font("Body", "", 11)
        
        about_text = [
            "Beacon Educational Consult is a Ghanaian educational publishing company",
            "dedicated to producing high-quality learning materials for Junior High School",
            "students across Ghana.",
            "",
            "Our mission is to support students in achieving academic excellence through",
            "comprehensive, curriculum-aligned resources that prepare them for the Basic",
            "Education Certificate Examination (BECE) and beyond.",
            "",
            "We believe that every student deserves access to excellent educational materials,",
            "and we are committed to making quality textbooks affordable and accessible to",
            "schools and families throughout Ghana.",
            "",
            "Our books are:",
            "• Written by experienced Ghanaian educators",
            "• Aligned with the national curriculum",
            "• Reviewed for accuracy and quality",
            "• Designed to support both classroom learning and independent study",
            "",
            "For more information about our publications and educational resources:",
            "",
            "Website: www.beaconeducational.com",
            "Email: info@beaconeducational.com",
            "Phone: [Contact information]",
            "",
            "Follow us on social media:",
            "Facebook: @BeaconEducational",
            "Instagram: @BeaconEducational",
            "Twitter: @BeaconEdu"
        ]
        
        for line in about_text:
            if line.strip() == "":
                pdf.ln(4)
            else:
                pdf.set_x(pdf.l_margin)
                pdf.multi_cell(0, 6, line)
        
        return pdf
    
    def generate_notes_pages(self, count=2):
        """Generate blank notes pages."""
        pdf = self._create_base_pdf()
        
        for i in range(count):
            pdf.add_page()
            pdf.set_font("Heading", "B", 14)
            pdf.cell(0, 10, "Notes", ln=True, align='C')
            pdf.ln(5)
            
            # Draw lines for writing
            pdf.set_line_width(0.2)
            y = 30
            while y < 270:
                pdf.line(20, y, 190, y)
                y += 8
        
        return pdf
    
    def generate_all_front_matter(self):
        """Generate all front matter pages."""
        pdfs = []
        pdfs.append(self.generate_title_page())
        pdfs.append(self.generate_copyright_page())
        pdfs.append(self.generate_preface_page())
        return pdfs
    
    def generate_all_back_matter(self, glossary_data=None, formula_data=None):
        """Generate all back matter pages."""
        pdfs = []
        
        if glossary_data:
            pdfs.append(self.generate_glossary(glossary_data))
        
        if formula_data:
            pdfs.append(self.generate_formula_sheet(formula_data))
        
        pdfs.append(self.generate_curriculum_reference())
        pdfs.append(self.generate_about_publisher())
        pdfs.append(self.generate_notes_pages(2))
        
        return pdfs

def merge_pdfs(pdf_objects, output_path):
    """Merge multiple PDF objects into a single file."""
    writer = PdfWriter()
    
    for pdf_obj in pdf_objects:
        if isinstance(pdf_obj, PdfReader):
            # Already a PdfReader, add pages directly
            for page in pdf_obj.pages:
                writer.add_page(page)
        else:
            # It's an fpdf object, save to temporary file first
            temp_path = f"/tmp/temp_{id(pdf_obj)}.pdf"
            pdf_obj.output(temp_path)
            
            # Read and add to writer
            reader = PdfReader(temp_path)
            for page in reader.pages:
                writer.add_page(page)
            
            # Clean up
            os.remove(temp_path)
    
    # Write final output
    with open(output_path, 'wb') as f:
        writer.write(f)

def enhance_book(subject, level, existing_pdf_path, output_path):
    """Enhance a book with front and back matter."""
    print(f"Enhancing {subject} B{level}...")
    
    # Create generator
    generator = EnhancedMatterGenerator(subject, level)
    
    # Load glossary data
    glossary_path = f"production/front_back_matter/{'science' if 'Science' in subject else 'maths'}_glossaries.json"
    glossary_data = None
    if os.path.exists(glossary_path):
        with open(glossary_path, 'r') as f:
            all_glossaries = json.load(f)
            glossary_data = all_glossaries.get(f"B{level}")
    
    # Load formula data (for maths only)
    formula_data = None
    if "Mathematics" in subject:
        formula_path = "production/front_back_matter/maths_formulas.json"
        if os.path.exists(formula_path):
            with open(formula_path, 'r') as f:
                all_formulas = json.load(f)
                formula_data = all_formulas.get(f"B{level}")
    
    # Generate front and back matter
    print(f"  Generating front matter...")
    front_matter = generator.generate_all_front_matter()
    
    print(f"  Generating back matter...")
    back_matter = generator.generate_all_back_matter(glossary_data, formula_data)
    
    # Load existing book
    print(f"  Loading existing book...")
    existing_reader = PdfReader(existing_pdf_path)
    existing_pages = [existing_reader]
    
    # Merge all PDFs
    print(f"  Merging all sections...")
    all_pdfs = front_matter + existing_pages + back_matter
    merge_pdfs(all_pdfs, output_path)
    
    print(f"  ✓ Enhanced book saved to {output_path}")
    
    # Report page count
    final_reader = PdfReader(output_path)
    print(f"  Total pages: {len(final_reader.pages)}")

def main():
    """Enhance all 6 books."""
    print("=" * 70)
    print("PHASE 16: ENHANCED FRONT/BACK MATTER GENERATION")
    print("=" * 70)
    print()
    
    books = [
        ("Integrated Science", "7", "production/books/Integrated_Science_Basic7_Complete.pdf"),
        ("Integrated Science", "8", "production/books/Integrated_Science_Basic8_TwoColumn.pdf"),
        ("Integrated Science", "9", "production/books/Integrated_Science_Basic9_TwoColumn.pdf"),
        ("Mathematics", "7", "production/books/Mathematics_Basic7_WithAnswers.pdf"),
        ("Mathematics", "8", "production/books/Mathematics_Basic8_WithAnswers.pdf"),
        ("Mathematics", "9", "production/books/Mathematics_Basic9_WithAnswers.pdf"),
    ]
    
    for subject, level, existing_path in books:
        if not os.path.exists(existing_path):
            print(f"⚠ Skipping {subject} B{level}: source file not found")
            continue
        
        output_name = existing_path.replace(".pdf", "_Enhanced.pdf")
        enhance_book(subject, level, existing_path, output_name)
        print()
    
    print("=" * 70)
    print("✅ Phase 16 Complete — All books enhanced with front/back matter")
    print("=" * 70)

if __name__ == "__main__":
    main()
