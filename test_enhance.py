#!/usr/bin/env python3
"""Test the enhance_books module with debug output."""

import sys
sys.path.insert(0, '/home/user/beacon-library')

from production.enhance_books import EnhancedMatterGenerator

# Test with Integrated Science B7
generator = EnhancedMatterGenerator("Integrated Science", "7")

print("Testing generate_preface_page...")
try:
    pdf = generator.generate_preface_page()
    print("✓ generate_preface_page succeeded")
except Exception as e:
    print(f"✗ generate_preface_page failed: {e}")
    import traceback
    traceback.print_exc()
