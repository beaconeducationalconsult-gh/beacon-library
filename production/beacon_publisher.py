#!/usr/bin/env python3
"""
Beacon Educational Library — Typesetting Engine
Implements the Phase 9 Design System using fpdf2

Fonts:
  - DejaVu Sans (Bold) for headings
  - DejaVu Serif for body text (Regular, Bold)

Page: A4, 20mm top/bottom/outside margins, 25mm gutter
"""

import re
import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos


class BeaconPublisher(FPDF):
    """Professional textbook typesetter for the Beacon Educational Library."""

    # Design System Constants (mm)
    PAGE_W = 210
    PAGE_H = 297
    MARGIN_TOP = 20
    MARGIN_BOTTOM = 20
    MARGIN_OUTSIDE = 20
    MARGIN_GUTTER = 25
    CONTENT_W = PAGE_W - MARGIN_OUTSIDE - MARGIN_GUTTER  # 165mm
    HEADER_Y = 10  # Running header position
    FOOTER_Y = PAGE_H - 10  # Footer position

    # Font paths
    FONT_DIR = "/usr/share/fonts/truetype/dejavu"

    def __init__(self, book_title="", subject="", level="", publisher="Beacon Educational Consult"):
        super().__init__(format='A4')
        self.book_title = book_title
        self.subject = subject
        self.level = level
        self.publisher_name = publisher
        self._is_right_page = True  # Track recto/verso
        self._in_front_matter = True
        self._front_page_num = 0
        self._main_page_num = 0
        self._current_paper_title = ""
        self._current_section = ""
        self._setup_fonts()

    def _setup_fonts(self):
        """Register all available fonts."""
        self.add_font("Body", "", os.path.join(self.FONT_DIR, "DejaVuSerif.ttf"))
        self.add_font("Body", "B", os.path.join(self.FONT_DIR, "DejaVuSerif-Bold.ttf"))
        self.add_font("Heading", "", os.path.join(self.FONT_DIR, "DejaVuSans.ttf"))
        self.add_font("Heading", "B", os.path.join(self.FONT_DIR, "DejaVuSans-Bold.ttf"))
        self.add_font("Mono", "", os.path.join(self.FONT_DIR, "DejaVuSansMono.ttf"))
        self.add_font("Mono", "B", os.path.join(self.FONT_DIR, "DejaVuSansMono-Bold.ttf"))
        self.set_auto_page_break(auto=True, margin=self.MARGIN_BOTTOM + 5)

    def _get_margins(self):
        """Return (left_margin, right_margin) based on page side."""
        if self._is_right_page:
            return self.MARGIN_GUTTER, self.MARGIN_OUTSIDE
        else:
            return self.MARGIN_OUTSIDE, self.MARGIN_GUTTER

    def add_page(self, *args, **kwargs):
        """Override to track page sides and apply correct margins."""
        super().add_page(*args, **kwargs)
        left, right = self._get_margins()
        self.set_margins(self.MARGIN_TOP, left, right)
        self.set_left_margin(left)
        self.set_right_margin(right)
        self._is_right_page = not self._is_right_page

    def _roman(self, num):
        """Convert integer to Roman numeral."""
        vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syms = ['m', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'ix', 'v', 'iv', 'i']
        result = ''
        for i, v in enumerate(vals):
            while num >= v:
                result += syms[i]
                num -= v
        return result

    def _current_page_display(self):
        """Return display page number string."""
        if self._in_front_matter:
            return self._roman(self._front_page_num) if self._front_page_num > 0 else ""
        return str(self._main_page_num) if self._main_page_num > 0 else ""

    def header(self):
        """Running header — skipped on title/chapter pages."""
        if self._in_front_matter:
            return
        if self.page == 1:
            return
        # Don't show on chapter opener pages (we handle this manually)
        left, right = self._get_margins()
        self.set_y(self.HEADER_Y)
        self.set_font("Heading", "", 7.5)
        self.set_text_color(100, 100, 100)
        content_w = self.PAGE_W - left - right

        if self._is_right_page:
            self.set_x(left)
            self.cell(content_w / 2, 4, self.book_title, align="L")
            self.cell(content_w / 2, 4, self._current_paper_title or self._current_section, align="R")
        else:
            self.set_x(left)
            self.cell(content_w / 2, 4, self._current_section or self.subject, align="L")
            self.cell(content_w / 2, 4, self.book_title, align="R")

        # Header rule
        self.set_draw_color(180, 180, 180)
        self.set_line_width(0.15)
        self.line(left, self.HEADER_Y + 5, left + content_w, self.HEADER_Y + 5)
        self.set_text_color(0, 0, 0)

    def footer(self):
        """Page numbers in footer."""
        if self.page == 1 and self._in_front_matter:
            return  # No footer on first front matter page
        left, right = self._get_margins()
        content_w = self.PAGE_W - left - right
        self.set_y(self.PAGE_H - 12)
        self.set_font("Body", "", 9)
        self.set_text_color(80, 80, 80)
        page_str = self._current_page_display()
        if page_str:
            if self._is_right_page:
                self.set_x(left)
                self.cell(content_w, 6, page_str, align="R")
            else:
                self.set_x(left)
                self.cell(content_w, 6, page_str, align="L")
        self.set_text_color(0, 0, 0)

    # ──────────────────────────────────────────────
    # FRONT MATTER
    # ──────────────────────────────────────────────

    def title_page(self):
        """Generate the title page."""
        self._in_front_matter = True
        self._front_page_num = 0
        self.add_page()
        self._is_right_page = True  # Reset

        # Centre content vertically
        self.set_y(60)

        # Series title
        self.set_font("Heading", "B", 11)
        self.set_text_color(100, 100, 100)
        self.cell(0, 6, "BEACON EDUCATIONAL SERIES", align="C",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(4)

        # Decorative rule
        self.set_draw_color(0, 0, 0)
        self.set_line_width(0.5)
        cx = self.PAGE_W / 2
        self.line(cx - 30, self.get_y(), cx + 30, self.get_y())
        self.ln(12)

        # Book title
        self.set_font("Heading", "B", 28)
        self.set_text_color(0, 0, 0)
        title_lines = self.book_title.split('\n')
        for line in title_lines:
            self.cell(0, 14, line, align="C",
                      new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(6)

        # Subtitle
        self.set_font("Body", "", 14)
        self.set_text_color(60, 60, 60)
        self.cell(0, 8, "A Comprehensive Question Bank", align="C",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.cell(0, 8, "with Marking Schemes", align="C",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(12)

        # Description
        self.set_font("Body", "", 11)
        self.set_text_color(80, 80, 80)
        self.cell(0, 7, "Curriculum-Aligned Practice Papers", align="C",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.cell(0, 7, f"for {self.level} Students and Teachers", align="C",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(20)

        # Decorative rule
        self.set_line_width(0.3)
        self.line(cx - 20, self.get_y(), cx + 20, self.get_y())
        self.ln(12)

        # Publisher
        self.set_font("Heading", "", 10)
        self.set_text_color(0, 0, 0)
        self.cell(0, 6, self.publisher_name, align="C",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_font("Body", "", 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 6, "2026 Edition", align="C",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    def copyright_page(self, isbn=""):
        """Generate the copyright page."""
        self.add_page()
        self._front_page_num += 1
        self.set_y(60)

        self.set_font("Body", "", 9)
        self.set_text_color(60, 60, 60)
        lines = [
            f"{self.book_title}",
            "First Edition, 2026",
            "",
            f"Copyright © 2026 {self.publisher_name}",
            "",
            "All rights reserved. No part of this publication may be reproduced,",
            "stored in a retrieval system, or transmitted in any form or by any",
            "means, electronic, mechanical, photocopying, recording, or otherwise,",
            "without prior written permission from the publisher.",
            "",
            "This book is designed to support the Ghana Education Service (GES)",
            "curriculum for Junior High School. It is intended as a supplementary",
            "resource for teachers and students.",
            "",
            "The questions in this book are original practice materials created",
            "for educational purposes. They are not official BECE or GES",
            "examination questions.",
            "",
            f"Published by: {self.publisher_name}",
            "",
            f"ISBN: {isbn}" if isbn else "ISBN: [To be assigned]",
            "",
            "Printed in Ghana",
        ]
        for line in lines:
            self.cell(0, 5.5, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    def preface_page(self):
        """Generate the preface page."""
        self.add_page()
        self._front_page_num += 1

        self.set_font("Heading", "B", 18)
        self.cell(0, 12, "PREFACE", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(6)

        self.set_font("Body", "", 11)
        paras = [
            f"This book has been developed to support Junior High School {self.level} students and teachers in their study of {self.subject}, as prescribed by the Ghana Education Service (GES) and the National Council for Curriculum and Assessment (NaCCA).",
            "The book contains a comprehensive collection of practice questions organised according to the curriculum's strand and sub-strand structure. Each paper includes both multiple-choice questions (Section A) and structured theory questions (Section B), reflecting the format of BECE examinations.",
        ]
        for p in paras:
            self.multi_cell(0, 6, p)
            self.ln(3)

        self.set_font("Body", "B", 11)
        self.cell(0, 7, "Key Features", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)

        features = [
            "Curriculum-Aligned Content — All questions mapped to specific content standards.",
            "Comprehensive Coverage — Topic-based papers covering all major strands.",
            "Detailed Marking Schemes — Complete answer keys with method marks and marking guidance.",
            "Professional Diagrams — Clear, scientifically accurate illustrations.",
            "Cognitive Demand — Questions spanning all levels of Bloom's taxonomy.",
        ]
        self.set_font("Body", "", 10.5)
        for f in features:
            left_m = self._get_margins()[0]
            self.set_x(left_m + 5)
            self.cell(3, 6, "•")
            self.multi_cell(self.CONTENT_W - 8, 6, f)
            self.ln(1.5)

    def toc_page(self, entries):
        """Generate table of contents.
        entries: list of (title, page_num, indent_level) tuples
        """
        self.add_page()
        self._front_page_num += 1

        self.set_font("Heading", "B", 18)
        self.cell(0, 12, "CONTENTS", align="C",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(8)

        left_m = self._get_margins()[0]

        for title, page, level in entries:
            indent = level * 7
            if level == 0:
                self.set_font("Heading", "B", 11)
            else:
                self.set_font("Body", "", 10.5)

            self.set_x(left_m + indent)
            available_w = self.CONTENT_W - indent

            # Calculate title width and page width
            self.set_font("Heading" if level == 0 else "Body", "B" if level == 0 else "", 11 if level == 0 else 10.5)
            title_w = self.get_string_width(title)
            page_str = str(page)
            page_w = self.get_string_width(page_str)

            # Print title
            self.cell(title_w + 1, 6.5, title)

            # Dotted leader
            dots_start = self.get_x()
            dots_end = left_m + available_w - page_w - 2
            if dots_end > dots_start:
                self.set_draw_color(180, 180, 180)
                self.set_line_width(0.1)
                # Draw dotted line
                y_mid = self.get_y() + 5
                x = dots_start + 1
                while x < dots_end:
                    self.line(x, y_mid, x + 0.5, y_mid)
                    x += 2

            # Page number
            self.set_x(left_m + available_w - page_w)
            self.cell(page_w, 6.5, page_str, align="R",
                      new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # ──────────────────────────────────────────────
    # MAIN CONTENT — PAPER LAYOUT
    # ──────────────────────────────────────────────

    def start_main_content(self):
        """Switch from front matter to main content pagination."""
        self._in_front_matter = False
        self._main_page_num = 0

    def chapter_opener(self, chapter_num, chapter_title, description=""):
        """Generate a chapter/strand opener page."""
        self._main_page_num += 1
        self.add_page()
        self._current_section = chapter_title

        # Large chapter number
        self.set_y(50)
        self.set_font("Heading", "B", 42)
        self.set_text_color(30, 30, 30)
        self.cell(0, 20, f"STRAND {chapter_num}",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(3)

        # Chapter title
        self.set_font("Heading", "B", 24)
        self.set_text_color(0, 0, 0)
        self.cell(0, 12, chapter_title,
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(4)

        # Rule
        self.set_draw_color(0, 0, 0)
        self.set_line_width(0.8)
        left_m = self._get_margins()[0]
        self.line(left_m, self.get_y(), left_m + self.CONTENT_W, self.get_y())
        self.ln(8)

        # Description
        if description:
            self.set_font("Body", "", 12)
            self.set_text_color(80, 80, 80)
            self.multi_cell(self.CONTENT_W * 0.75, 7, description)

    def paper_header(self, title, time_allowed="", total_marks="", paper_num=""):
        """Generate paper header at start of a question paper."""
        self._main_page_num += 1
        self.add_page()
        self._current_paper_title = title

        # Paper title
        self.set_font("Heading", "B", 16)
        self.cell(0, 10, title, align="C",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)

        # Metadata
        if time_allowed or total_marks:
            self.set_font("Body", "", 10)
            self.set_text_color(80, 80, 80)
            meta_parts = []
            if time_allowed:
                meta_parts.append(f"Time Allowed: {time_allowed}")
            if total_marks:
                meta_parts.append(f"Total Marks: {total_marks}")
            self.cell(0, 6, "  |  ".join(meta_parts), align="C",
                      new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.set_text_color(0, 0, 0)
            self.ln(4)

        # Rule
        self.set_draw_color(180, 180, 180)
        self.set_line_width(0.3)
        left_m = self._get_margins()[0]
        self.line(left_m, self.get_y(), left_m + self.CONTENT_W, self.get_y())
        self.ln(6)

    def section_header(self, title, instruction=""):
        """Generate section header (SECTION A, SECTION B)."""
        self.ln(4)
        self.set_font("Heading", "B", 13)
        self.cell(0, 8, title.upper(), align="C",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        if instruction:
            self.set_font("Body", "", 10)
            self.set_text_color(80, 80, 80)
            self.multi_cell(0, 5.5, instruction, align="C")
            self.set_text_color(0, 0, 0)
        self.ln(4)

    def instructions_block(self, instructions):
        """Generate instructions box."""
        left_m = self._get_margins()[0]
        self.set_font("Heading", "B", 10)
        self.cell(0, 6, "INSTRUCTIONS", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)

        self.set_font("Body", "", 10)
        for i, inst in enumerate(instructions, 1):
            self.set_x(left_m + 3)
            self.cell(6, 5.5, f"{i}.")
            self.multi_cell(self.CONTENT_W - 9, 5.5, inst)
            self.ln(1)
        self.ln(4)

    def question_mcq(self, number, text, options):
        """Render an MCQ question.
        options: list of (letter, text) tuples e.g. [('A', 'option text'), ...]
        """
        left_m = self._get_margins()[0]
        q_indent = 10  # mm for question number
        opt_indent = 16  # mm for options

        # Check if we need a new page (question + 4 options ≈ 30mm)
        if self.get_y() > self.PAGE_H - self.MARGIN_BOTTOM - 35:
            self.add_page()
            self._main_page_num += 1

        # Question number + text
        self.set_x(left_m)
        self.set_font("Heading", "B", 11)
        num_str = f"{number}."
        self.cell(q_indent, 6, num_str)
        self.set_font("Body", "", 11)
        # Use multi_cell for wrapping
        self.multi_cell(self.CONTENT_W - q_indent, 6, text)
        self.ln(1)

        # Options
        for letter, opt_text in options:
            self.set_x(left_m + opt_indent)
            self.set_font("Body", "", 10.5)
            self.cell(8, 5.5, f"{letter}.")
            self.multi_cell(self.CONTENT_W - opt_indent - 8, 5.5, opt_text)

        self.ln(3)

    def question_theory(self, number, parts):
        """Render a theory question with sub-parts.
        parts: list of (label, text, marks) tuples
        """
        left_m = self._get_margins()[0]

        # Check space
        if self.get_y() > self.PAGE_H - self.MARGIN_BOTTOM - 30:
            self.add_page()
            self._main_page_num += 1

        # Question header
        self.set_font("Heading", "B", 13)
        self.cell(0, 8, f"Question {number}",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)

        for label, text, marks in parts:
            if self.get_y() > self.PAGE_H - self.MARGIN_BOTTOM - 15:
                self.add_page()
                self._main_page_num += 1

            self.set_x(left_m + 5)
            self.set_font("Heading", "B", 11)
            self.cell(8, 6, f"({label})")
            self.set_font("Body", "", 11)

            # Question text
            if marks:
                full_text = f"{text}  [{marks}]"
            else:
                full_text = text
            self.multi_cell(self.CONTENT_W - 13, 6, full_text)
            self.ln(3)

    # ──────────────────────────────────────────────
    # ANSWER KEY LAYOUT
    # ──────────────────────────────────────────────

    def answer_key_header(self, paper_title):
        """Header for answer key section."""
        self._main_page_num += 1
        self.add_page()
        self._current_paper_title = f"Answer Key: {paper_title}"

        self.set_font("Heading", "B", 16)
        self.cell(0, 10, paper_title, align="C",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)

        self.set_font("Heading", "B", 12)
        self.cell(0, 8, "ANSWER KEY", align="C",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(4)

    def answer_key_section_a(self, answers, total_marks=40):
        """Render Section A answer key as a compact table.
        answers: list of (question_num, answer_letter, topic, cognitive_level)
        """
        left_m = self._get_margins()[0]
        self.set_font("Heading", "B", 11)
        self.cell(0, 7, "SECTION A: OBJECTIVE TEST",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_font("Body", "", 10)
        self.cell(0, 5, f"Total Marks: {total_marks}",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(3)

        # Table header
        col_widths = [12, 14, 80, 50]  # Q, Ans, Topic, Cognitive
        headers = ["Q", "Ans", "Curriculum Area", "Cognitive Level"]

        self.set_font("Heading", "B", 8)
        self.set_fill_color(240, 240, 240)
        x_start = left_m
        for i, (header, w) in enumerate(zip(headers, col_widths)):
            self.set_x(x_start + sum(col_widths[:i]))
            self.cell(w, 6, header, border=1, fill=True, align="C")
        self.ln()

        # Table rows
        self.set_font("Body", "", 8.5)
        for q_num, ans, topic, cog in answers:
            if self.get_y() > self.PAGE_H - self.MARGIN_BOTTOM - 10:
                self.add_page()
                self._main_page_num += 1
                # Repeat header
                self.set_font("Heading", "B", 8)
                self.set_fill_color(240, 240, 240)
                for i, (header, w) in enumerate(zip(headers, col_widths)):
                    self.set_x(x_start + sum(col_widths[:i]))
                    self.cell(w, 6, header, border=1, fill=True, align="C")
                self.ln()
                self.set_font("Body", "", 8.5)

            row_h = 5.5
            self.set_x(x_start)
            self.cell(col_widths[0], row_h, str(q_num), border=1, align="C")
            self.set_font("Heading", "B", 8.5)
            self.cell(col_widths[1], row_h, ans, border=1, align="C")
            self.set_font("Body", "", 8.5)
            # Truncate topic if too long
            topic_display = topic[:42] + "..." if len(topic) > 45 else topic
            self.cell(col_widths[2], row_h, topic_display, border=1)
            self.cell(col_widths[3], row_h, cog, border=1)
            self.ln()

        self.ln(4)

        # Answer distribution
        from collections import Counter
        dist = Counter(a for _, a, _, _ in answers)
        self.set_font("Body", "B", 9)
        self.cell(0, 5, "Answer Distribution:", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_font("Body", "", 9)
        total = sum(dist.values())
        dist_str = "  |  ".join(
            f"{k}: {v} ({v*100//total}%)" for k, v in sorted(dist.items())
        )
        self.cell(0, 5, dist_str, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)

        # Cognitive distribution
        cog_dist = Counter(c for _, _, _, c in answers)
        self.set_font("Body", "B", 9)
        self.cell(0, 5, "Cognitive Level Distribution:", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_font("Body", "", 9)
        cog_str = "  |  ".join(
            f"{k}: {v} ({v*100//total}%)" for k, v in sorted(cog_dist.items())
        )
        self.cell(0, 5, cog_str, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    def answer_key_section_b(self, paper_title, marking_schemes):
        """Render Section B marking scheme.
        marking_schemes: list of (question_num, total_marks, parts)
          parts: list of (label, text, answer_text, marks_note)
        """
        self._main_page_num += 1
        self.add_page()
        self._current_paper_title = f"Marking Scheme: {paper_title}"

        self.set_font("Heading", "B", 14)
        self.cell(0, 9, f"{paper_title}",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)
        self.set_font("Heading", "B", 12)
        self.cell(0, 8, "SECTION B: THEORY — MARKING SCHEME",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(4)

        left_m = self._get_margins()[0]

        for q_num, total_marks, parts in marking_schemes:
            if self.get_y() > self.PAGE_H - self.MARGIN_BOTTOM - 30:
                self.add_page()
                self._main_page_num += 1

            # Question header
            self.set_font("Heading", "B", 12)
            self.cell(0, 8, f"Question {q_num}  [Total: {total_marks} marks]",
                      new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.ln(2)

            for label, question_text, answer_text, marks_note in parts:
                if self.get_y() > self.PAGE_H - self.MARGIN_BOTTOM - 25:
                    self.add_page()
                    self._main_page_num += 1

                # Sub-question
                self.set_x(left_m + 3)
                self.set_font("Body", "B", 10.5)
                self.cell(8, 6, f"({label})")
                self.set_font("Body", "", 10.5)
                self.multi_cell(self.CONTENT_W - 11, 6,
                                f"{question_text}  [{marks_note}]")
                self.ln(1)

                # Answer (indented with left accent bar)
                self.set_x(left_m + 11)
                bar_x = self.get_x() - 2
                bar_y_start = self.get_y()
                self.set_font("Body", "", 10)
                self.set_text_color(40, 40, 40)
                self.multi_cell(self.CONTENT_W - 16, 5.5, answer_text)
                bar_y_end = self.get_y()
                self.set_text_color(0, 0, 0)

                # Draw accent bar
                self.set_draw_color(0, 0, 0)
                self.set_line_width(0.6)
                self.line(bar_x, bar_y_start, bar_x, bar_y_end)
                self.ln(4)

            self.ln(4)

    # ──────────────────────────────────────────────
    # UTILITY
    # ──────────────────────────────────────────────

    def blank_page(self):
        """Add a blank page (for even-page endings)."""
        self.add_page()
        if self._in_front_matter:
            self._front_page_num += 1
        else:
            self._main_page_num += 1

    def save(self, path):
        """Save the PDF."""
        os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
        self.output(path)
        size = os.path.getsize(path)
        print(f"✓ Saved: {path} ({size:,} bytes, {self.page} pages)")


# ──────────────────────────────────────────────
# MARKDOWN PARSER
# ──────────────────────────────────────────────

    def question_mcq_two_column(self, questions):
        """Render MCQs in two-column layout for space efficiency."""
        left_m = self._get_margins()[0]
        col_width = (self.CONTENT_W - 8) / 2  # 8mm gap between columns
        col_x = [left_m, left_m + col_width + 8]
        
        q_indent = 8  # mm for question number
        opt_indent = 14  # mm for options
        
        # Track vertical positions for both columns
        col_y = [self.get_y(), self.get_y()]
        
        for i, q in enumerate(questions):
            col = i % 2
            x_pos = col_x[col]
            
            # Check if we need a new page
            if col_y[col] > self.PAGE_H - self.MARGIN_BOTTOM - 28:
                if col == 0:
                    # First column full, check second column
                    if col_y[1] > self.PAGE_H - self.MARGIN_BOTTOM - 28:
                        # Both columns full, new page
                        self.add_page()
                        self._main_page_num += 1
                        col_y = [self.get_y(), self.get_y()]
                else:
                    # Second column full, move to next row
                    self.set_y(max(col_y[0], col_y[1]) + 6)
                    if self.get_y() > self.PAGE_H - self.MARGIN_BOTTOM - 28:
                        self.add_page()
                        self._main_page_num += 1
                    col_y = [self.get_y(), self.get_y()]
            
            # Set position
            self.set_y(col_y[col])
            self.set_x(x_pos)
            
            # Question number + text
            self.set_font("Heading", "B", 10)
            num_str = f"{q['number']}."
            self.cell(q_indent, 5, num_str)
            self.set_font("Body", "", 10)
            
            text_width = col_width - q_indent
            y_start = self.get_y()
            self.multi_cell(text_width, 5, q['text'], new_x=XPos.LEFT, new_y=YPos.NEXT)
            
            # Options
            for letter, opt_text in q['options']:
                self.set_x(x_pos + opt_indent)
                self.set_font("Body", "", 9.5)
                self.cell(6, 4.5, f"{letter}.")
                opt_width = col_width - opt_indent - 6
                self.multi_cell(opt_width, 4.5, opt_text, new_x=XPos.LEFT, new_y=YPos.NEXT)
            
            col_y[col] = self.get_y() + 4
        
        # Move to bottom of both columns
        self.set_y(max(col_y[0], col_y[1]))


def parse_paper(md_text):
    """Parse a Markdown question paper into structured data.

    Returns dict with:
      title, time, marks, instructions,
      section_a: list of {number, text, options},
      section_b: list of {number, parts: [{label, text, marks}]}
      answer_key: {section_a: [...], section_b: [...]}
    """
    result = {
        'title': '',
        'time': '',
        'marks': '',
        'instructions': [],
        'section_a': [],
        'section_b': [],
        'answer_key_section_a': [],
        'answer_key_section_b': [],
        'has_answer_key': False,
    }

    lines = md_text.split('\n')
    current_section = None
    current_question = None
    i = 0

    # Extract title from first few lines
    for line in lines[:10]:
        stripped = line.strip()
        if stripped.startswith('# ') and not result['title']:
            result['title'] = stripped[2:].strip()
            break
        elif stripped.startswith('## ') and not result['title']:
            result['title'] = stripped[3:].strip()
            break

    # Extract metadata from first 20 lines
    for line in lines[:20]:
        if '**Time' in line:
            m = re.search(r'\*\*Time:?\*\*\s*(.+?)(?:\s{2,}|$)', line)
            if m:
                result['time'] = m.group(1).strip()
        if '**Total Marks' in line or '**Marks:**' in line:
            m = re.search(r'Marks:?\*\*\s*(\d+)', line)
            if m:
                result['marks'] = m.group(1)

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Detect sections
        if re.match(r'##?\s*SECTION\s*A', stripped, re.I):
            current_section = 'A'
            # Get instruction from next non-empty line
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and lines[j].strip().startswith('*'):
                result['section_a_instruction'] = lines[j].strip().strip('*_')
            i += 1
            continue

        if re.match(r'##?\s*SECTION\s*B', stripped, re.I):
            current_section = 'B'
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and lines[j].strip().startswith('*'):
                result['section_b_instruction'] = lines[j].strip().strip('*_')
            i += 1
            continue

        if re.match(r'##?\s*ANSWER\s*KEY', stripped, re.I):
            current_section = 'ANSWER_KEY'
            result['has_answer_key'] = True
            i += 1
            continue

        if re.match(r'##?\s*MARKING\s*SCHEME', stripped, re.I):
            current_section = 'MARKING_SCHEME'
            i += 1
            continue

        # Parse MCQ questions (Section A)
        if current_section == 'A':
            # Match **1.** format
            m = re.match(r'\*\*(\d+)\.\*\*\s*(.+)', stripped)
            if m:
                q_num = int(m.group(1))
                q_text = m.group(2).strip()
                current_question = {
                    'number': q_num,
                    'text': q_text,
                    'options': []
                }
                result['section_a'].append(current_question)
                i += 1
                continue

            # Parse options (A. B. C. D.)
            if current_question is not None:
                m = re.match(r'^([A-D])\.\s*(.+)', stripped)
                if m:
                    current_question['options'].append(
                        (m.group(1), m.group(2).strip())
                    )

        # Parse theory questions (Section B or Diagram Mode)
        if current_section in ['B', None]:  # None for Diagram Mode papers
            # Match numbered questions like "1. Question text **[4 marks]**"
            m = re.match(r'^(\d+)\.\s+(.+?)(?:\s*\*\*\[(\d+)\s*marks?\]\*\*)?\s*$', stripped)
            if m and not stripped.startswith('```'):  # Skip code blocks
                q_num = int(m.group(1))
                q_text = m.group(2).strip()
                marks = m.group(3) or ""
                
                # For Diagram Mode, treat as theory questions
                if current_section is None or current_section == 'B':
                    q_entry = {
                        'number': q_num,
                        'parts': [{
                            'label': 'a',
                            'text': q_text,
                            'marks': marks
                        }]
                    }
                    result['section_b'].append(q_entry)
                    current_question = q_entry
                    i += 1
                    continue

            # Match "Question 1" format
            m = re.match(r'\*?\*?Question\s+(\d+)\*?\*?', stripped)
            if m:
                current_question = {
                    'number': int(m.group(1)),
                    'parts': []
                }
                result['section_b'].append(current_question)
                i += 1
                continue

            # Sub-question: (a), (b), etc.
            if current_question is not None and 'parts' in current_question:
                m = re.match(r'\(([a-z])\)\s*(.+?)(?:\s*\[(\d+)\s*marks?\])?\s*$', stripped)
                if m:
                    label = m.group(1)
                    text = m.group(2).strip()
                    marks = m.group(3) or ""
                    current_question['parts'].append({
                        'label': label,
                        'text': text,
                        'marks': marks
                    })

        i += 1

    return result


def get_b7_science_papers(base_dir):
    """Get all B7 Science paper files in reading order."""
    papers = []

    # Collection A: Diagram Mode papers
    diagram_papers = sorted([
        f for f in os.listdir(base_dir)
        if f.startswith('B7_DiagramMode_') and f.endswith('.md')
    ])
    for f in diagram_papers:
        topic = f.replace('B7_DiagramMode_', '').replace('.md', '')
        topic = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', topic)
        papers.append({
            'file': f,
            'title': topic,
            'collection': 'A',
            'strand': 'Diagram Practice'
        })

    # Collection B: BECE Mock B7
    bece_papers = sorted([
        f for f in os.listdir(base_dir)
        if f.startswith('BECE_Mock_Basic7_') and f.endswith('.md')
    ])
    for f in bece_papers:
        topic = f.replace('BECE_Mock_Basic7_IntegratedScience_', '').replace('.md', '')
        topic = topic.replace('_', ' ')
        papers.append({
            'file': f,
            'title': topic,
            'collection': 'B',
            'strand': 'BECE Mock'
        })

    return papers


if __name__ == "__main__":
    print("Beacon Publisher — Typesetting Engine")
    print("Ready to generate books.")
