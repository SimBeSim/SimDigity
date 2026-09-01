#!/usr/bin/env python3
"""
make_kael_canonical_dryrun.py

Dry-run version of make_kael_canonical.py: prints the actions that would be taken but does not modify files or run git.

Usage:
  python3 scripts/make_kael_canonical_dryrun.py
  python3 scripts/make_kael_canonical_dryrun.py --branch main
"""
from pathlib import Path
import argparse

DEFAULT_FILES = ["Kael_1.png","Kael_2.png","Kael_3.png","Kael_4.png"]

GALLERY_SUMMARY = "Will write Kael/gallery.md with canonical image references pointing to Kael/images/canonical/"
META_SUMMARY = "Will write Kael/IMAGE_METADATA.md with canonical placeholders for the four images"
VARIANTS_SUMMARY = "Will create Kael/images/variants/README.md for non-canonical renders"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--branch", default="main")
    args = parser.parse_args()

    repo_root = Path.cwd()
    kael_images = repo_root / "Kael" / "images"
    canonical_dir = kael_images / "canonical"

    print("DRY RUN: make_kael_canonical_dryrun")
    print("Repo root:", repo_root)
    print("Target branch:", args.branch)

    print("\nPlanned actions:")
    print("- Ensure directory:", canonical_dir)
    for f in DEFAULT_FILES:
        src = kael_images / f
        dst = canonical_dir / f
        print(f"- Copy (if exists): {src} -> {dst}")

    print(f"- {GALLERY_SUMMARY}")
    print(f"- {META_SUMMARY}")
    print(f"- {VARIANTS_SUMMARY}")
    print("- Stage files with git add, commit message: 'Mark Kael canonical images + metadata placeholders', and push to the branch")

    print("\nNo files will be changed in this dry run.")

if __name__ == '__main__':
    main()
