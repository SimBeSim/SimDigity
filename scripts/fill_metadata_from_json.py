#!/usr/bin/env python3
"""
fill_metadata_from_json.py

Takes a JSON file mapping filenames to metadata and merges/appends them into Kael/IMAGE_METADATA.md

Usage:
  python3 scripts/fill_metadata_from_json.py --input metadata.json

metadata.json format example:
{
  "Kael_1.png": {"Seed": "12345", "Date": "2026-09-01", "Operator": "Sim", "Presentation": "female-presenting"},
  "Kael_2.png": {...}
}
"""
import json
from pathlib import Path
import argparse


def load_json(path):
    with open(path,'r',encoding='utf-8') as f:
        return json.load(f)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='path to json metadata file')
    args = parser.parse_args()

    repo_root = Path.cwd()
    meta_file = repo_root / 'Kael' / 'IMAGE_METADATA.md'
    if not meta_file.exists():
        print('ERROR: IMAGE_METADATA.md not found at', meta_file)
        return

    data = load_json(args.input)
    text = meta_file.read_text(encoding='utf-8')

    # Simple merge: append entries for provided filenames under a new section
    append_lines = ['\n\n# Auto-filled entries\n']
    for fname, meta in data.items():
        append_lines.append(f'### {fname}\n')
        for k,v in meta.items():
            append_lines.append(f'- {k}: {v}\n')
        append_lines.append('\n')

    new_text = text + ''.join(append_lines)
    backup = meta_file.with_suffix('.md.bak')
    meta_file.rename(backup)
    meta_file.write_text(new_text, encoding='utf-8')
    print('Merged metadata; backup written to', backup)

if __name__ == '__main__':
    main()
