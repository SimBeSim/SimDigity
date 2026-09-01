# Scripts — usage summary

This folder contains helper scripts to manage Kael images and metadata. Short summary:

- make_kael_canonical.py : copy/move images, write templates, commit & push (already present)
- make_kael_canonical_dryrun.py : prints actions without changing files
- make_kael_no_push.py : performs changes and commits locally only (no push)
- fill_metadata_from_json.py : merges JSON metadata into Kael/IMAGE_METADATA.md
- add_image_from_url.py : download image into variants or canonical and optionally commit
- regen_gallery.py : regenerate Kael/gallery.md from files in Kael/images/canonical/

Examples:
  python3 scripts/make_kael_canonical_dryrun.py
  python3 scripts/make_kael_no_push.py --yes
  python3 scripts/fill_metadata_from_json.py --input mymeta.json
  python3 scripts/add_image_from_url.py --url https://example.com/img.png --commit
  python3 scripts/regen_gallery.py

Notes:
- These scripts assume you run them from the repository root (where .git/ lives).
- They use the system git client for commits/push. Ensure your machine has credentials configured for pushes.
