# PHASE 7 — TYPESETTING AUDIT REPORT
## Beacon Educational Consult — JHS Educational Materials Library
**Date:** 2026-10-06
**Agent:** Editorial & Production Agent
**Status:** PHASE 7 COMPLETE

---

## 1. CURRENT PAGE SETUP

### 1.1 DOCX Page Dimensions (Extracted from B7 BECE Mock)

| Parameter | Value (twips) | Value (inches) | Value (mm) | Assessment |
|-----------|:-------------:|:--------------:|:----------:|------------|
| **Page width** | 12,240 | 8.5" | 216 mm | US Letter |
| **Page height** | 15,840 | 11.0" | 279 mm | US Letter |
| **Top margin** | 1,134 | 0.79" | 20 mm | ⚠️ Narrow |
| **Bottom margin** | 1,134 | 0.79" | 20 mm | ⚠️ Narrow |
| **Left margin** | 1,247 | 0.87" | 22 mm | ⚠️ Narrow |
| **Right margin** | 1,247 | 0.87" | 22 mm | ⚠️ Narrow |
| **Header** | 720 | 0.50" | 13 mm | Acceptable |
| **Footer** | 720 | 0.50" | 13 mm | Acceptable |
| **Gutter** | 0 | 0" | 0 mm | ❌ No gutter for binding |
| **Column spacing** | 720 | 0.50" | 13 mm | N/A (single column) |

### 1.2 Page Size Assessment

| Criterion | Current | Recommended | Action |
|-----------|---------|-------------|--------|
| **Page size** | US Letter (8.5" × 11") | A4 (210 × 297 mm) for international; A5 (148 × 210 mm) for student workbook | ⚠️ Decide based on publication format |
| **Top margin** | 20 mm | 18–20 mm | ✅ Acceptable |
| **Bottom margin** | 20 mm | 18–20 mm | ✅ Acceptable |
| **Outside margin** | 22 mm | 18–20 mm | ⚠️ Slightly wide |
| **Inside/gutter** | 0 mm (no gutter) | 20–25 mm for perfect binding | ❌ Add gutter for binding |
| **Text area** | ~172 × 239 mm | Depends on page size | Needs recalculation |

**Recommendation:** For publication, use **A4** for teacher/resource editions and consider **A5** for student workbooks. Add a **20 mm gutter** for perfect binding.

---

## 2. TYPOGRAPHY SYSTEM

### 2.1 Current Font Setup

| Element | Font | Size | Weight | Assessment |
|---------|------|:----:|:------:|------------|
| **Body text** | Times New Roman | 11 pt | Regular | ⚠️ Serif font; readable but not modern |
| **Heading 1** | (inherits) | 14 pt | Bold | ✅ Good size |
| **Heading 2** | (inherits) | 13 pt | Bold | ✅ Good size |
| **Heading 3** | (inherits) | 11 pt | Bold | ⚠️ Same size as body — needs differentiation |
| **MCQ options** | (inherits) | 11 pt | Regular | ✅ Acceptable |
| **Captions** | (inherits) | ~9 pt | Italic | ✅ Acceptable |

### 2.2 Typography Assessment

| Criterion | Rating | Notes |
|-----------|:------:|-------|
| **Readability** | 🟡 Good | Times New Roman is readable but serif; sans-serif may be better for JHS |
| **Mathematical support** | 🟡 Limited | Times New Roman has basic math symbols; no proper equation typesetting |
| **Scientific symbols** | 🟡 Limited | Subscripts/superscripts work but no dedicated science font |
| **Hierarchy clarity** | 🟡 Fair | H3 same size as body; needs differentiation |
| **Consistency** | 🟢 Good | Same font throughout all documents |
| **Print reproduction** | 🟢 Good | Times New Roman prints well at 11 pt |

### 2.3 Recommended Typography System for Publication

| Element | Recommended Font | Size | Weight | Notes |
|---------|-----------------|:----:|:------:|-------|
| **Book title** | Alegreya or Lato | 24 pt | Bold | Title page only |
| **Heading 1 (Strand/Unit)** | Alegreya or Lato | 16 pt | Bold | Major sections |
| **Heading 2 (Sub-strand)** | Alegreya or Lato | 14 pt | Bold | Section headers |
| **Heading 3 (Topic/Question)** | Alegreya or Lato | 12 pt | Bold | Question group headers |
| **Body text** | Source Serif Pro or Lato | 11 pt | Regular | Question text and instructions |
| **MCQ options** | Source Serif Pro or Lato | 11 pt | Regular | A., B., C., D. options |
| **Captions** | Lato | 9 pt | Italic | Figure captions |
| **Headers/footers** | Lato | 8 pt | Regular | Page numbers, running heads |
| **Mathematical expressions** | Cambria Math or STIX Two Math | 11 pt | Regular | Equations, fractions, indices |
| **Chemical formulae** | Source Serif Pro | 11 pt | Regular | With proper sub/superscripts |

---

## 3. HEADING HIERARCHY

### 3.1 Current Heading Structure

**B7/B8/B9 BECE Mock Papers (Collection B):**
```
# BEACON EDUCATIONAL CONSULT              ← H1: Publisher name
## INTEGRATED SCIENCE (SCIENCE)           ← H2: Subject
### BECE-STYLE MOCK EXAMINATION (PAPER X) ← H3: Paper type
### INSTRUCTIONS                           ← H3: Instructions
## SECTION A: OBJECTIVE TEST (40 marks)   ← H2: Section header
## SECTION B: THEORY (60 marks)           ← H2: Section header
### Question 1  [10 marks]                ← H3: Theory question
## ANSWER KEY                              ← H2: Answer section
### Section A - Objective Test            ← H3: Answer subsection
### Section B - Theory                    ← H3: Answer subsection
## MARKING SCHEME - SECTION B (60 marks)  ← H2: Marking scheme
```

**B7 Strand Mocks (Collection C):**
```
# [SCHOOL NAME]                           ← H1: School placeholder
## INTEGRATED SCIENCE (SCIENCE)           ← H2: Subject
### END-OF-TERM MOCK EXAMINATION          ← H3: Paper type
## SECTION A: OBJECTIVE TEST (40 marks)   ← H2: Section header
## SECTION B: THEORY (60 marks)           ← H2: Section header
```

**B7 Diagram Mode (Collection A):**
```
# [SCHOOL NAME]                           ← H1: School placeholder
INTEGRATED SCIENCE (SCIENCE)              ← Plain text (not heading!)
## PRACTICAL QUESTIONS - DIAGRAM MODE     ← H2: Paper type
### Energy (11.1 - 11.7)                  ← H3: Topic
```

**Mathematics Chapter Mocks (Collection E):**
```
BEACON EDUCATIONAL CONSULT (2026/27)      ← Plain text (not heading!)
MATHEMATICS                               ← Plain text
CHAPTER 1 MOCK EXAMINATION                ← Plain text
Place Value, Rounding...                  ← Plain text (topic)
Strand 1: Number | Sub-Strand 1: ...     ← Plain text (curriculum ref)
Class: JHS 1 (Basic 7)                    ← Plain text
Time Allowed: 2 Hours                     ← Plain text
Total Marks: 100                          ← Plain text
INSTRUCTIONS TO CANDIDATES                ← Plain text
SECTION A: OBJECTIVE TEST [40 MARKS]      ← Plain text
```

### 3.2 Heading Hierarchy Assessment

| Issue | Severity | Location | Recommendation |
|-------|:--------:|----------|----------------|
| **Inconsistent H1 usage** | 🟡 MEDIUM | Collections A, C use [SCHOOL NAME]; B, E use BEACON | Standardize to publisher name |
| **H3 same size as body** | 🟡 MEDIUM | All collections | Increase H3 to 12 pt bold |
| **Maths papers use plain text** | 🔴 HIGH | Collection E | Convert to proper heading hierarchy |
| **Diagram Mode has no H2 for subject** | 🟡 MEDIUM | Collection A | Add H2 for "INTEGRATED SCIENCE" |
| **No heading for academic year** | 🟢 LOW | All collections | Add as metadata, not heading |

### 3.3 Recommended Heading Hierarchy for Publication

```
H1: Book Title / Paper Title (16 pt bold)
  H2: Section Header — "SECTION A", "SECTION B", "ANSWER KEY" (14 pt bold)
    H3: Question Group — "Question 1 [10 marks]" (12 pt bold)
      H4: Sub-question — "(a)", "(b)", "(c)" (11 pt bold)
Body: Question text and options (11 pt regular)
Caption: Figure captions (9 pt italic)
```

---

## 4. QUESTION FORMATTING

### 4.1 Section A (MCQ) Formatting

**Current format (Collection B — BECE Mock):**
```
**1.** The smallest unit of a living organism that can carry out all the activities of life is

A. the system
B. the cell
C. the organ
D. the tissue
```

**Current format (Collection C — Strand Mock):**
```
**1. The basic unit of structure and function of all living things is the**

A. tissue
B. cell
C. organ
D. system
```

**Assessment:**

| Criterion | Collection B | Collection C | Recommended |
|-----------|:------------:|:------------:|:-----------:|
| **Question number** | Bold with period | Bold with period and bold text | Bold number, regular text |
| **Question stem** | Regular weight | Bold weight | Regular weight (less visual noise) |
| **Options** | Plain A./B./C./D. | Plain A./B./C./D. | Indented with hanging indent |
| **Spacing** | Blank line between Q and options | Blank line between Q and options | 6 pt space after stem |
| **Inter-question spacing** | Blank line | Blank line | 12 pt space between questions |

### 4.2 Section B (Theory) Formatting

**Current format:**
```
### Question 1  [10 marks]

Fig. 1 shows a cell taken from the cheek lining of a mammal.

**(a)** Name the parts labelled **A**, **B**, **C**, **D** and **E**.  **[5 marks]**

**(b)** State ONE function of EACH of the parts **A**, **C** and **D**.  **[3 marks]**
```

**Assessment:**

| Criterion | Current | Recommended | Assessment |
|-----------|---------|-------------|:----------:|
| **Question header** | ### Question 1 [10 marks] | H3 with marks in brackets | ✅ Good |
| **Sub-question marker** | **(a)** bold | Bold letter in parentheses | ✅ Good |
| **Marks indicator** | **[5 marks]** bold | Bold in square brackets at end | ✅ Good |
| **Figure reference** | "Fig. 1 shows..." | Italic caption below figure | ✅ Good |
| **Answer space** | Not shown (separate booklet) | Provide answer lines if workbook | Depends on format |

### 4.3 Mark Allocation Formatting

**Current format:**
- Question totals: `[10 marks]`, `[12 marks]`, `[8 marks]`
- Sub-question marks: `[5 marks]`, `[3 marks]`, `[2 marks]`, `[1 mark]`

**Assessment:** ✅ Excellent — consistent use of square brackets, bold formatting, and singular/plural "mark/marks".

---

## 5. TABLE FORMATTING

### 5.1 Current Table Style

**Markdown pipe tables:**
```markdown
| Part of the cell | Function |
|---|---|
| Cytoplasm | ......... |
| Nucleus | ......... |
| Mitochondrion | ......... |
```

**Answer key tables:**
```markdown
| Question | Answer | Curriculum Area (Topic) | Cognitive Level |
| --- | --- | --- | --- |
| 1 | B | 2.1 Cells as the Units of Living Things | Remember |
```

### 5.2 Table Assessment

| Criterion | Current | Recommended | Assessment |
|-----------|---------|-------------|:----------:|
| **Header row** | Bold in markdown | Bold with light grey background | ⚠️ Needs styling |
| **Borders** | Markdown default | Light rules (0.5 pt) | ⚠️ Needs styling |
| **Column widths** | Auto | Proportional to content | ⚠️ Needs adjustment |
| **Alignment** | Left-aligned | Left for text, centre for numbers | ⚠️ Needs adjustment |
| **Answer space** | "........." dots | Ruled lines or blank cells | ⚠️ Needs redesign |
| **Font size** | Body size (11 pt) | 10 pt for tables | ⚠️ Slightly large |

### 5.3 Table Types Found

| Type | Count | Purpose | Assessment |
|------|:-----:|---------|:----------:|
| **Student completion tables** | ~50 | Students fill in blanks | ⚠️ Dots need replacing with lines |
| **Answer key tables** | ~62 | Show correct answers | ✅ Good structure |
| **Curriculum coverage tables** | ~10 | Map papers to standards | ✅ Good structure |
| **Comparison tables** | ~20 | Plant vs animal, etc. | ⚠️ Need consistent formatting |
| **Data tables** | ~15 | Experimental data | ✅ Acceptable |

---

## 6. PAGE COMPOSITION

### 6.1 Current Page Elements

| Element | Present? | Location | Assessment |
|---------|:--------:|----------|:----------:|
| **Page numbers** | ❌ No | Not in any file | ❌ Must add for publication |
| **Running headers** | ❌ No | Not in any file | ❌ Must add for publication |
| **Running footers** | ❌ No | Not in any file | ❌ Must add for publication |
| **Page breaks** | ⚠️ Partial | `\newpage` in Beacon Pack only | ⚠️ Needs systematic breaks |
| **Orphan control** | ❌ No | Not implemented | ❌ Must add |
| **Widow control** | ❌ No | Not implemented | ❌ Must add |
| **Keep-with-next** | ❌ No | Not implemented | ❌ Must add for question+options |

### 6.2 Page Break Requirements

| Break Point | Current | Recommended |
|-------------|---------|-------------|
| **Before Section A** | Natural flow | Force new page |
| **Before Section B** | Natural flow | Force new page |
| **Before Answer Key** | Natural flow | Force new page |
| **Before Marking Scheme** | Natural flow | Force new page |
| **Before each theory question** | Natural flow | Optional (keep with sub-questions) |
| **Between papers (Pack)** | `\newpage` | Force new page |
| **Before TOC** | N/A | Force new page |

### 6.3 Running Head System

**Recommended for publication:**

| Page Type | Header (left) | Header (right) | Footer |
|-----------|---------------|----------------|--------|
| **Question paper** | "BEACON Integrated Science B7" | "Paper X: [Topic]" | Page number |
| **Answer key** | "BEACON Integrated Science B7 — Answer Key" | "Paper X: [Topic]" | Page number |
| **Marking scheme** | "BEACON Integrated Science B7 — Marking Scheme" | "Paper X: [Topic]" | Page number |
| **Front matter** | (none) | (none) | Roman numeral |

---

## 7. MATHEMATICAL TYPESETTING

### 7.1 Current Maths Formatting

**From Collection E (Maths Chapter Mocks):**
- Numbers: Plain text with commas (e.g., "4,275,308,619")
- Decimals: Plain text (e.g., "6.74", "0.997")
- Currency: GH₵ symbol used correctly
- Operations: Written in words or plain symbols (+, −, ×, ÷)
- Fractions: Written as "1/2" or in words
- Indices: Written as "10²" or "x²" (superscript available)
- Equations: Written inline (e.g., "PE = mgh")

### 7.2 Mathematical Typesetting Assessment

| Criterion | Current | Recommended | Assessment |
|-----------|---------|-------------|:----------:|
| **Fractions** | "1/2" or words | Stacked fractions (½) | ⚠️ Needs proper typesetting |
| **Indices** | Superscript available | Proper superscript | ✅ Acceptable |
| **Square roots** | "√" symbol | Proper radical sign | ⚠️ Needs math font |
| **Equations** | Inline text | Display equations with proper alignment | ⚠️ Needs equation environment |
| **Units** | "m/s²" inline | Proper superscript (m/s²) | ⚠️ Needs consistent formatting |
| **Currency** | GH₵ | GH₵ with proper cedi symbol | ✅ Good |
| **Large numbers** | Commas as separators | Thin spaces or commas | ✅ Acceptable |
| **Decimals** | Point as separator | Point (Ghanaian convention) | ✅ Good |
| **Greek letters** | Not found | π, θ, etc. as needed | ⚠️ Add math font |
| **Geometric notation** | Not found | ∠, △, ∥, ⊥ as needed | ⚠️ Add math font |

### 7.3 Scientific Notation Assessment

| Criterion | Current | Recommended | Assessment |
|-----------|---------|-------------|:----------:|
| **Chemical formulae** | CO₂, H₂O (subscripts) | Proper subscripts | ✅ Good (when present) |
| **Chemical symbols** | Na, Fe, Cu, Mg | Italic for variables, roman for elements | ⚠️ Check consistency |
| **Units** | J, m/s, kg, m/s² | Roman (upright) for units | ⚠️ Check consistency |
| **Variables** | m, g, h, v | Italic for variables | ⚠️ Check consistency |
| **Equations** | PE = mgh | Proper equation formatting | ⚠️ Needs improvement |

---

## 8. CONSISTENCY ACROSS COLLECTIONS

### 8.1 Header/Title Consistency

| Collection | H1 Text | H2 Text | H3 Text | Assessment |
|-----------|---------|---------|---------|:----------:|
| **B — BECE Mock** | BEACON EDUCATIONAL CONSULT | INTEGRATED SCIENCE (SCIENCE) | BECE-STYLE MOCK EXAMINATION | ✅ Consistent |
| **C — Strand Mock** | [SCHOOL NAME] | INTEGRATED SCIENCE (SCIENCE) | END-OF-TERM MOCK EXAMINATION | ⚠️ Different H1 |
| **A — Diagram Mode** | [SCHOOL NAME] | (plain text) | PRACTICAL QUESTIONS - DIAGRAM MODE | ⚠️ Different format |
| **D — Beacon Pack** | BEACON EDUCATIONAL CONSULT | BASIC 7 (JHS 1) INTEGRATED SCIENCE | BECE-STYLE MOCK EXAMINATION PACK | ✅ Consistent |
| **E — Maths** | (plain text) | (plain text) | (plain text) | ❌ No heading hierarchy |

### 8.2 Metadata Consistency

| Field | Collection B | Collection C | Collection A | Collection D | Collection E |
|-------|:------------:|:------------:|:------------:|:------------:|:------------:|
| **Class/Level** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Time allowed** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Total marks** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Academic year** | 2026/2027 | 2025/2026 | 2025/2026 | 2026/2027 | 2026/27 |
| **Subject** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Instructions** | ✅ | ✅ | ✅ | ✅ | ✅ |

**Issue:** Academic year is inconsistent (2025/2026 vs 2026/2027 vs 2026/27). Standardize to **2026/2027** for publication.

### 8.3 Instruction Text Consistency

| Collection | Instruction Style | Assessment |
|-----------|-------------------|:----------:|
| **B — BECE Mock** | Numbered list, 7 items, formal | ✅ Good |
| **C — Strand Mock** | Numbered list, 8 items, formal | ✅ Good |
| **A — Diagram Mode** | Numbered list, 5 items, simpler | ⚠️ Different style |
| **D — Beacon Pack** | Numbered list, 7 items, formal | ✅ Good |
| **E — Maths** | Numbered list, 6 items, formal | ✅ Good |

---

## 9. SPECIAL FORMATTING ELEMENTS

### 9.1 Emphasis and Bold Usage

| Element | Current Usage | Assessment |
|---------|---------------|:----------:|
| **Question numbers** | Bold (**1.**, **2.**) | ✅ Good |
| **Sub-question letters** | Bold (**(a)**, **(b)**) | ✅ Good |
| **Marks** | Bold (**[5 marks]**) | ✅ Good |
| **Key terms in questions** | Bold (**A**, **B**, **C** for labels) | ✅ Good |
| **Option letters** | Regular (A., B., C., D.) | ✅ Good |
| **Instructions** | Italic (*Answer ALL questions...*) | ✅ Good |
| **Figure captions** | Italic (*Fig. 1: ...*) | ✅ Good |
| **Marking notes** | Italic (*Marking note: ...*) | ✅ Good |

### 9.2 Special Characters and Symbols

| Symbol | Usage | Assessment |
|--------|-------|:----------:|
| **GH₵** | Ghanaian cedi | ✅ Correct |
| **°** | Degrees (angles, temperature) | ✅ Available |
| **²** | Squared (area, indices) | ✅ Available |
| **³** | Cubed (volume) | ✅ Available |
| **π** | Pi | ⚠️ Not found in sampled content |
| **√** | Square root | ⚠️ Not found in sampled content |
| **≤, ≥** | Inequalities | ⚠️ Not found in sampled content |
| **→** | Arrows (processes) | ✅ Used in text |
| **₂** | Subscript (CO₂, H₂O) | ✅ Available |

### 9.3 LaTeX-Style Elements

The Beacon Pack (Collection D) uses LaTeX-style page break commands:
```
\newpage
```

This suggests the documents may have been prepared with LaTeX or a LaTeX-aware tool in mind. For publication, these should be converted to proper page break instructions in the layout software.

---

## 10. TYPESETTING QUALITY SCORE

| Category | Score (0–100) | Rating |
|----------|:-------------:|:------:|
| Page Setup | 65 | 🟡 Fair (US Letter, no gutter) |
| Typography | 70 | 🟡 Good (readable but needs refinement) |
| Heading Hierarchy | 75 | 🟡 Good (consistent within collections) |
| Question Formatting | 85 | 🟢 Excellent (clear and consistent) |
| Table Formatting | 60 | 🟡 Fair (needs styling for print) |
| Page Composition | 40 | 🔴 Poor (no page numbers, headers, footers) |
| Mathematical Typesetting | 65 | 🟡 Fair (basic but not professional) |
| Scientific Notation | 75 | 🟡 Good (when present) |
| Cross-Collection Consistency | 60 | 🟡 Fair (different styles across collections) |
| Special Elements | 80 | 🟢 Good (emphasis, symbols well used) |
| **OVERALL** | **67** | **🟡 Needs typesetting work for publication** |

---

## 11. PUBLICATION TYPESETTING SPECIFICATION

### 11.1 Recommended Page Setup

| Parameter | Teacher/Resource Edition | Student Workbook |
|-----------|:-----------------------:|:----------------:|
| **Page size** | A4 (210 × 297 mm) | A5 (148 × 210 mm) |
| **Top margin** | 20 mm | 15 mm |
| **Bottom margin** | 20 mm | 15 mm |
| **Outside margin** | 20 mm | 15 mm |
| **Inside margin (gutter)** | 25 mm | 20 mm |
| **Text area** | 165 × 257 mm | 113 × 180 mm |
| **Header** | 10 mm from top | 8 mm from top |
| **Footer** | 10 mm from bottom | 8 mm from bottom |

### 11.2 Recommended Font System

| Element | Font | Size | Weight | Colour |
|---------|------|:----:|:------:|:------:|
| **Book title** | Alegreya | 24 pt | Bold | Black |
| **H1 (Paper title)** | Alegreya | 16 pt | Bold | Black |
| **H2 (Section header)** | Alegreya | 14 pt | Bold | Dark navy #1b3a5c |
| **H3 (Question group)** | Alegreya | 12 pt | Bold | Black |
| **Body text** | Source Serif Pro | 11 pt | Regular | Black |
| **MCQ options** | Source Serif Pro | 11 pt | Regular | Black |
| **Captions** | Lato | 9 pt | Italic | Dark grey #444 |
| **Headers/footers** | Lato | 8 pt | Regular | Dark grey #444 |
| **Maths** | Cambria Math | 11 pt | Regular | Black |
| **Code/diagrams** | Consolas | 9 pt | Regular | Black |

### 11.3 Question Layout Specification

**Section A (MCQ):**
```
1.  Question stem text in regular weight, 11 pt.        [6 pt space]
    A.  First option text                               [3 pt space]
    B.  Second option text                              [3 pt space]
    C.  Third option text                               [3 pt space]
    D.  Fourth option text                              [12 pt space]

2.  Next question stem text...
```

**Section B (Theory):**
```
Question 1  [10 marks]                                  [12 pt space]

Context paragraph or figure reference.                   [6 pt space]

(a)  Sub-question text.  [5 marks]                      [6 pt space]
(b)  Sub-question text.  [3 marks]                      [6 pt space]
(c)  Sub-question text.  [2 marks]                      [18 pt space]

Question 2  [12 marks]                                  [12 pt space]
...
```

### 11.4 Table Specification

| Element | Specification |
|---------|---------------|
| **Header row** | Bold text, light grey background (#f0f0f0), 0.5 pt rule below |
| **Body rows** | Regular text, alternating white/light grey (optional) |
| **Borders** | 0.5 pt light grey rules between rows; 1 pt rule above header and below last row |
| **Column widths** | Proportional to content; left-aligned for text, centre for numbers |
| **Font size** | 10 pt for table content |
| **Padding** | 4 pt cell padding |
| **Answer space** | Ruled lines (0.5 pt, 8 mm spacing) instead of dots |

---

## 12. RECOMMENDATIONS

### 12.1 Immediate Actions

1. **Decide on page size** — A4 for teacher editions, A5 for student workbooks
2. **Add gutter margin** — 25 mm for perfect binding
3. **Establish font system** — Alegreya + Source Serif Pro + Cambria Math
4. **Create page template** — With running headers, footers, and page numbers
5. **Standardize heading hierarchy** — Across all collections

### 12.2 Production Workflow

1. **Set up master template** — In InDesign, LaTeX, or equivalent
2. **Import content** — From markdown or DOCX source files
3. **Apply styles** — Using the typography system above
4. **Add page elements** — Headers, footers, page numbers
5. **Insert diagrams** — From FIGURE BRIEF production
6. **Proof** — Check pagination, orphans, widows, and breaks
7. **Export** — Print-ready PDF

### 12.3 Automation Opportunities

| Task | Tool | Effort Saved |
|------|------|:------------:|
| **Markdown to layout** | Pandoc + LaTeX template | High |
| **DOCX to layout** | InDesign import + style mapping | Medium |
| **Page numbering** | Automatic in layout software | High |
| **Running headers** | Automatic from section titles | High |
| **Table of contents** | Automatic from heading hierarchy | High |
| **Answer key compilation** | Script to extract and compile | Medium |

---

*End of Phase 7 Typesetting Audit Report*

**PUBLICATION STATUS: NOT READY — PHASE 7 COMPLETE, TYPESETTING SPECIFICATION ESTABLISHED**

**Key findings:**
- ✅ **Question formatting is excellent** (85/100) — clear, consistent, well-structured
- ✅ **Emphasis and symbols are well used** (80/100)
- 🟡 **Page setup needs adjustment** (65/100) — US Letter → A4, add gutter
- 🟡 **Typography needs refinement** (70/100) — better font system for publication
- 🔴 **Page composition is poor** (40/100) — no page numbers, headers, or footers
- 🟡 **Cross-collection consistency needs work** (60/100) — different styles across collections
- **Overall typesetting quality: 67/100** — good foundation, needs professional finishing
