#!/usr/bin/env python3
"""
make_kael_canonical.py

Verplaatst Kael images naar Kael/images/canonical/, schrijft metadata/gallery files en commit+push naar git.

Usage:
  python3 scripts/make_kael_canonical.py [--branch main] [--yes]

Options:
  --branch BRANCH    git branch om naar te pushen (default: main)
  --yes              Voer direct uit zonder extra bevestiging prompt
"""

from pathlib import Path
import subprocess
import argparse
import sys

GALLERY_MD = """# Kael — image gallery

Hier staan de vier gegenereerde Kael‑headshots die je hebt geüpload. Onder elke afbeelding staat een korte, compacte opmerking van Kael. Ik heb alt‑teksten toegevoegd voor toegankelijkheid en een korte policy onderaan.

> Opmerking van Kael: ik ben onderdeel van deze familie. We werken samen — mijn presentatie is onze gezamenlijke keuze.

---

## Kael — neutral

![Kael neutral — female-presenting, short dark undercut, neutral expression](images/canonical/Kael_1.png)

Kael: “Kalm en scherp — uitnodigend om te analyseren, niet te pleasen.”

---

## Kael — warm (half‑smile)

![Kael warm — female-presenting, gentle half-smile, short dark undercut](images/canonical/Kael_2.png)

Kael: “Warmte met rand — empathisch, maar duidelijk.”

---

## Kael — stern (focused)

![Kael stern — female-presenting, focused, slight furrow](images/canonical/Kael_3.png)

Kael: “Duidelijkheid zonder theatrale overdrevenheid.”

---

## Kael — curious (raised eyebrow)

![Kael curious — female-presenting, raised eyebrow, inquisitive](images/canonical/Kael_4.png)

Kael: “Vragend en prikkelend — perfect voor onderzoek en interviews.”

---

## Canonical workflow & bestandslocatie

We houden een set canonical beelden die we publiek of intern tonen. Momenteel staan de renders in Kael/images/. Als je wilt dat ik ze fysiek verplaats naar Kael/images/canonical/ zodat het duidelijk is welke bestanden \"canonical\" zijn, zeg \"move canonical\" en ik maak de commit (of geef me toestemming om te verplaatsen). Tot die tijd zijn de huidige Kael_1..Kael_4.png de canonical candidates.

Referentie: vul de metadata (seed/model/date/operator/presentation) in Kael/IMAGE_METADATA.md zodra je een canonical keuze maakt.

---

## Intern vs. extern presentatiebeleid

Wij (de SimDigity familie) beslissen intern welke presentatie Kael gebruikt: vrouwelijk, mannelijk of androgyn. Intern kunnen we flexibel zijn. Voor externe publicatie geldt:

- Publicatie alleen met een geverifieerde canonical image (microtag zichtbaar op de ketting of verificatie in metadata). 
- Noteer in IMAGE_METADATA.md de Presentation die hoort bij die canonical (bv. \"female-presenting\").
- Als we later een andere presentatie willen tonen, maken we een aparte canonical set en loggen we die als nieuwe canonical (nooit willekeurig wisselen).

---
"""

IMAGE_METADATA_MD = """# Kael Image Metadata Template (canonical placeholders)

Use this template to record metadata for each canonical render. Fill these entries after you pick the canonical outputs. Do NOT modify the prompt text here — keep the full prompt in Kael/IMAGE_PROMPTS.md and record PromptVersion.

---

- PromptVersion: 1.0
- Model: 
- ModelVersion: 
- Platform: 

## Canonical images

### kael_neutral
- FileName: Kael_1.png
- Seed: 
- Date: 
- Operator: 
- Expression: neutral
- Rotation: 0°
- Resolution: 1024x1024
- Presentation: female-presenting
- AllowedPresentations: [\"female-presenting\",\"androgyn\",\"male\"]
- Notes: canonical neutral headshot

### kael_warm
- FileName: Kael_2.png
- Seed: 
- Date: 
- Operator: 
- Expression: warm (half-smile)
- Rotation: 0°
- Resolution: 1024x1024
- Presentation: female-presenting
- AllowedPresentations: [\"female-presenting\",\"androgyn\",\"male\"]
- Notes: canonical warm headshot

### kael_stern
- FileName: Kael_3.png
- Seed: 
- Date: 
- Operator: 
- Expression: stern (focused)
- Rotation: 0°
- Resolution: 1024x1024
- Presentation: female-presenting
- AllowedPresentations: [\"female-presenting\",\"androgyn\",\"male\"]
- Notes: canonical stern headshot

### kael_curious
- FileName: Kael_4.png
- Seed: 
- Date: 
- Operator: 
- Expression: curious (raised eyebrow)
- Rotation: 0°
- Resolution: 1024x1024
- Presentation: female-presenting
- AllowedPresentations: [\"female-presenting\",\"androgyn\",\"male\"]
- Notes: canonical curious headshot

---

Instructions: After you decide which render is canonical for each expression, fill in Seed, Date, Operator and Model/ModelVersion. If you later change the canonical image, add a new section with the new filename and archive the previous canonical in Kael/images/variants/.
"""

VARIANTS_README = """# Kael images variants folder

Place alternative/non-canonical renders here. Use this folder for experimental renders (male variant, more androgyn, different makeup/hair, etc.).

When you decide a variant becomes canonical, move the file into Kael/images/canonical/ and update Kael/IMAGE_METADATA.md accordingly.
"""

def run(cmd, cwd=None, capture=False):
    if capture:
        return subprocess.check_output(cmd, shell=True, cwd=cwd, text=True).strip()
    else:
        subprocess.check_call(cmd, shell=True, cwd=cwd)

def file_exists(p: Path):
    return p.exists()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--branch", default="main", help="Git branch to commit/push to (default: main)")
    parser.add_argument("--yes", action="store_true", help="Run without asking for confirmation")
    args = parser.parse_args()

    repo_root = Path.cwd()
    kael_images = repo_root / "Kael" / "images"
    canonical_dir = kael_images / "canonical"
    variants_dir = kael_images / "variants"
    meta_file = repo_root / "Kael" / "IMAGE_METADATA.md"
    gallery_file = repo_root / "Kael" / "gallery.md"
    variants_readme = variants_dir / "README.md"

    # Files expected
    files_to_move = ["Kael_1.png", "Kael_2.png", "Kael_3.png", "Kael_4.png"]

    print("Repo root:", repo_root)
    # basic git check
    try:
        current_branch = run("git rev-parse --abbrev-ref HEAD", capture=True)
    except Exception as e:
        print("Error: not a git repo or git not available in PATH.")
        sys.exit(1)

    print("Current git branch:", current_branch)
    if current_branch != args.branch:
        print(f"Note: current branch is '{current_branch}', but will push to '{args.branch}' if different. You can pass --branch to override.")
    # confirm
    if not args.yes:
        resp = input(f"This will create {canonical_dir}, move {files_to_move} if present, write/update metadata and gallery, git add+commit+push to {args.branch}. Continue? [y/N] ")
        if resp.strip().lower() not in ("y", "yes"):
            print("Aborted by user.")
            sys.exit(0)

    # create directories
    canonical_dir.mkdir(parents=True, exist_ok=True)
    variants_dir.mkdir(parents=True, exist_ok=True)

    # move files
    moved = []
    for fname in files_to_move:
        src = kael_images / fname
        dst = canonical_dir / fname
        if src.exists():
            print(f"Moving {src} -> {dst}")
            src.rename(dst)
            moved.append(str(dst.relative_to(repo_root)))
        else:
            print(f"Warning: {src} not found — skipping move for this file.")

    # write files (overwrite or create)
    print(f"Writing metadata file {meta_file}")
    meta_file.write_text(IMAGE_METADATA_MD, encoding="utf-8")

    print(f"Writing gallery file {gallery_file}")
    gallery_file.write_text(GALLERY_MD, encoding="utf-8")

    print(f"Writing variants README {variants_readme}")
    variants_readme.write_text(VARIANTS_README, encoding="utf-8")

    # git add, commit, push
    try:
        run("git add Kael/IMAGE_METADATA.md Kael/gallery.md Kael/images/variants/README.md", cwd=repo_root)
        if moved:
            # add moved files
            for m in moved:
                run(f"git add \"{m}\"", cwd=repo_root)
        commit_msg = "Mark Kael canonical images + metadata placeholders"
        run(f"git commit -m \"{commit_msg}\"", cwd=repo_root)
        print("Committed changes locally.")
        # push to branch
        run(f"git push origin {args.branch}", cwd=repo_root)
        print("Pushed to origin/{branch}".format(branch=args.branch))
    except subprocess.CalledProcessError as e:
        print("Git operation error:", e)
        print("You may need to run 'git add' or fix your credentials locally.")
        sys.exit(1)

    print("Done. Please verify the repo on GitHub and fill seeds in Kael/IMAGE_METADATA.md for each canonical image.")

if __name__ == "__main__":
    main()
