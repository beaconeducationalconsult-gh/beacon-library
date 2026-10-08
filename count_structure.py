#!/usr/bin/env python3
import os
import re
from collections import defaultdict

# Count papers by collection
collections = {
    'Collection A (B7 Diagram Mode)': [],
    'Collection B (BECE Mock)': [],
    'Collection C (B7 Strand Mocks)': [],
    'Collection D (Beacon Packs)': [],
    'Collection E (Maths Chapters)': [],
    'Collection F (Maths Papers)': [],
    'Collection G (B8 Topic Science)': []
}

for f in sorted(os.listdir('.')):
    if not (f.endswith('.md') or f.endswith('.docx')):
        continue
    if f.endswith('.docx'):
        continue  # Only count .md files
        
    if 'DiagramMode' in f:
        collections['Collection A (B7 Diagram Mode)'].append(f)
    elif 'BECE_Mock' in f:
        collections['Collection B (BECE Mock)'].append(f)
    elif 'B7_Strand' in f or 'Special_Mock' in f:
        collections['Collection C (B7 Strand Mocks)'].append(f)
    elif 'Beacon_Pack' in f:
        collections['Collection D (Beacon Packs)'].append(f)
    elif re.match(r'JHS\d+_Ch\d+', f):
        collections['Collection E (Maths Chapters)'].append(f)
    elif re.match(r'Maths_Paper_\d+', f):
        collections['Collection F (Maths Papers)'].append(f)
    elif 'B8_' in f and 'Science' in f and 'Topic' in f:
        collections['Collection G (B8 Topic Science)'].append(f)

print("=" * 70)
print("PUBLISHING STRUCTURE ANALYSIS")
print("=" * 70)

for coll, files in collections.items():
    print(f"\n{coll}: {len(files)} papers")
    
# Determine subject split
science_count = 0
maths_count = 0

for coll, files in collections.items():
    for f in files:
        if 'Maths' in f or 'JHS' in f:
            maths_count += 1
        else:
            science_count += 1

print(f"\n{'=' * 70}")
print(f"SUBJECT SPLIT:")
print(f"  Integrated Science: {science_count} papers")
print(f"  Mathematics: {maths_count} papers")
print(f"  Total: {science_count + maths_count} papers")

# Determine level split
b7_count = 0
b8_count = 0
b9_count = 0

for coll, files in collections.items():
    for f in files:
        if 'B7' in f or 'JHS1' in f:
            b7_count += 1
        elif 'B8' in f or 'JHS2' in f:
            b8_count += 1
        elif 'B9' in f or 'JHS3' in f:
            b9_count += 1

print(f"\n{'=' * 70}")
print(f"LEVEL SPLIT:")
print(f"  Basic 7 (JHS 1): {b7_count} papers")
print(f"  Basic 8 (JHS 2): {b8_count} papers")
print(f"  Basic 9 (JHS 3): {b9_count} papers")

