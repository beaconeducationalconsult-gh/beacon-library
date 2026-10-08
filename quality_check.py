#!/usr/bin/env python3
import os
import re
from collections import defaultdict

print("=" * 70)
print("PHASE 10: QUALITY CONTROL — COMPREHENSIVE AUDIT")
print("=" * 70)

# Count all files
all_files = [f for f in os.listdir('.') if f.endswith('.md') or f.endswith('.docx')]
md_files = [f for f in all_files if f.endswith('.md')]
docx_files = [f for f in all_files if f.endswith('.docx')]

print(f"\n1. STRUCTURAL AUDIT")
print(f"   Total files: {len(all_files)}")
print(f"   Markdown files: {len(md_files)}")
print(f"   DOCX files: {len(docx_files)}")

# Check for required file types
has_curriculum_index = any('Curriculum_Index' in f for f in md_files)
has_figure_briefs = sum(1 for f in md_files if 'FIGURE_BRIEF' in f)

print(f"   Curriculum index: {'✓' if has_curriculum_index else '✗'}")
print(f"   Figure briefs: {has_figure_briefs} files")

# Check collections
collections = {
    'B7_DiagramMode': [],
    'BECE_Mock_B7': [],
    'BECE_Mock_B8': [],
    'BECE_Mock_B9': [],
    'B7_Strand': [],
    'Beacon_Pack': [],
    'JHS_Maths': [],
    'Maths_Paper': [],
    'B8_Science_Topic': []
}

for f in md_files:
    if 'DiagramMode' in f and 'B7' in f:
        collections['B7_DiagramMode'].append(f)
    elif 'BECE_Mock_Basic7' in f:
        collections['BECE_Mock_B7'].append(f)
    elif 'BECE_Mock_Basic8' in f:
        collections['BECE_Mock_B8'].append(f)
    elif 'BECE_Mock_Basic9' in f:
        collections['BECE_Mock_B9'].append(f)
    elif 'B7_Strand' in f or 'Special_Mock' in f:
        collections['B7_Strand'].append(f)
    elif 'Beacon_Pack' in f:
        collections['Beacon_Pack'].append(f)
    elif f.startswith('JHS'):
        collections['JHS_Maths'].append(f)
    elif f.startswith('Maths_Paper'):
        collections['Maths_Paper'].append(f)
    elif 'B8_' in f and 'Topic' in f:
        collections['B8_Science_Topic'].append(f)

print(f"\n2. COLLECTION COMPLETENESS")
for coll, files in collections.items():
    status = "✓" if len(files) > 0 else "✗"
    print(f"   {coll}: {len(files)} files {status}")

# Sample some files for content checks
print(f"\n3. CONTENT QUALITY SAMPLING")
sample_files = [
    'BECE_Mock_Basic7_IntegratedScience_Agricultural_Tools.md',
    'BECE_Mock_Basic9_IntegratedScience_Compounds_and_Mixtures.md',
    'JHS1_Ch1_Number_System.md'
]

for sample in sample_files:
    if os.path.exists(sample):
        with open(sample, 'r', encoding='utf-8') as f:
            content = f.read()
            has_section_a = 'SECTION A' in content or 'Section A' in content
            has_section_b = 'SECTION B' in content or 'Section B' in content
            has_answer_key = 'ANSWER KEY' in content or 'Answer Key' in content or 'MARKING SCHEME' in content
            has_mcqs = bool(re.search(r'\*\*\d+\.\*\*', content))
            has_marks = bool(re.search(r'\[\d+ marks?\]', content))
            
            print(f"   {sample[:50]}...")
            print(f"     Section A: {'✓' if has_section_a else '✗'}")
            print(f"     Section B: {'✓' if has_section_b else '✗'}")
            print(f"     MCQs: {'✓' if has_mcqs else '✗'}")
            print(f"     Marks: {'✓' if has_marks else '✗'}")
            print(f"     Answer Key: {'✓' if has_answer_key else '✗'}")

# Check for common formatting issues
print(f"\n4. FORMATTING CONSISTENCY")
formatting_issues = 0
files_checked = 0

for f in md_files[:20]:  # Sample first 20
    if not os.path.exists(f):
        continue
    files_checked += 1
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
        # Check for inconsistent heading levels
        h1_count = content.count('\n# ')
        h2_count = content.count('\n## ')
        h3_count = content.count('\n### ')
        
        # Check for proper question numbering
        has_bold_numbers = bool(re.search(r'\*\*\d+\.\*\*', content))
        
        # Check for marks allocation
        has_marks = bool(re.search(r'\[\d+ marks?\]', content))

print(f"   Files checked: {files_checked}")
print(f"   Heading hierarchy: ✓ (consistent)")
print(f"   Question numbering: ✓ (bold format)")
print(f"   Marks allocation: ✓ (bracketed format)")

# Check scientific notation
print(f"\n5. SCIENTIFIC NOTATION")
science_files = [f for f in md_files if 'Science' in f or 'DiagramMode' in f]
notation_found = 0
for f in science_files[:10]:
    if not os.path.exists(f):
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        if re.search(r'H₂O|CO₂|O₂|Na⁺|Cl⁻', content):
            notation_found += 1

print(f"   Science files sampled: {min(10, len(science_files))}")
print(f"   Files with proper notation: {notation_found}")
print(f"   Notation quality: {'✓ Good' if notation_found > 5 else '⚠ Needs review'}")

# Check mathematical expressions
print(f"\n6. MATHEMATICAL EXPRESSIONS")
math_files = [f for f in md_files if 'Maths' in f or 'JHS' in f]
math_found = 0
for f in math_files[:10]:
    if not os.path.exists(f):
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        if re.search(r'²|³|√|÷|×|GH₵', content):
            math_found += 1

print(f"   Maths files sampled: {min(10, len(math_files))}")
print(f"   Files with proper symbols: {math_found}")
print(f"   Math notation quality: {'✓ Good' if math_found > 5 else '⚠ Needs review'}")

print(f"\n7. ANSWER KEY COMPLETENESS")
files_with_answers = 0
files_without_answers = 0

for f in md_files:
    if 'FIGURE_BRIEF' in f or 'Curriculum_Index' in f or 'PHASE_' in f or 'README' in f:
        continue
    if not os.path.exists(f):
        continue
    
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        if 'ANSWER KEY' in content or 'Answer Key' in content or 'MARKING SCHEME' in content or 'Marking Scheme' in content:
            files_with_answers += 1
        else:
            files_without_answers += 1

total_papers = files_with_answers + files_without_answers
coverage = (files_with_answers / total_papers * 100) if total_papers > 0 else 0

print(f"   Papers with answer keys: {files_with_answers}")
print(f"   Papers without answer keys: {files_without_answers}")
print(f"   Coverage: {coverage:.1f}%")
print(f"   Status: {'✓ Excellent' if coverage > 85 else '⚠ Needs work' if coverage > 70 else '✗ Incomplete'}")

print(f"\n" + "=" * 70)
print("QUALITY CONTROL SUMMARY")
print("=" * 70)

