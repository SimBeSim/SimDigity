#!/usr/bin/env python3
"""
add_image_from_url.py

Download an image from a URL into Kael/images/variants/ or Kael/images/canonical/ and optionally commit+push.

Usage:
  python3 scripts/add_image_from_url.py --url <image_url> [--canonical] [--commit]
"""
import argparse
from pathlib import Path
import requests
import sys
import subprocess


def run(cmd):
    subprocess.check_call(cmd, shell=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', required=True)
    parser.add_argument('--canonical', action='store_true', help='Place image in canonical folder')
    parser.add_argument('--filename', help='Optional filename (defaults to basename of URL)')
    parser.add_argument('--commit', action='store_true', help='Commit and push the added image (requires git creds)')
    args = parser.parse_args()

    repo_root = Path.cwd()
    dest_dir = repo_root / 'Kael' / 'images' / ('canonical' if args.canonical else 'variants')
    dest_dir.mkdir(parents=True, exist_ok=True)

    fname = args.filename or args.url.split('/')[-1]
    dest = dest_dir / fname

    print('Downloading', args.url, '->', dest)
    r = requests.get(args.url, timeout=30)
    if r.status_code != 200:
        print('Download failed:', r.status_code)
        sys.exit(1)
    dest.write_bytes(r.content)
    print('Saved', dest)

    if args.commit:
        try:
            run(f'git add "{dest}"')
            run('git commit -m "Add image via add_image_from_url.py"')
            run('git push origin main')
            print('Committed and pushed')
        except subprocess.CalledProcessError as e:
            print('Git error:', e)
            print('Image saved locally but commit/push failed')

if __name__ == '__main__':
    main()
