#!/usr/bin/env python3
"""
regen_gallery.py

Regenerate Kael/gallery.md based on images in Kael/images/canonical/. This creates markdown with alt texts and short Kael quotes.

Usage:
  python3 scripts/regen_gallery.py
"""
from pathlib import Path

QUOTES = {
    'neutral': 'Kalm en scherp — uitnodigend om te analyseren, niet te pleasen.',
    'warm': 'Warmte met rand — empathisch, maar duidelijk.',
    'stern': 'Duidelijkheid zonder theatrale overdrevenheid.',
    'curious': 'Vragend en prikkelend — perfect voor onderzoek en interviews.'
}

ALT_TEMPL = 'Kael {label} — female-presenting, short dark undercut, {label} expression'


def label_from_name(name):
    n = name.lower()
    if 'neutral' in n or '_1' in n:
        return 'neutral'
    if 'warm' in n or '_2' in n:
        return 'warm'
    if 'stern' in n or '_3' in n:
        return 'stern'
    if 'curious' in n or '_4' in n:
        return 'curious'
    return 'variant'


def main():
    repo_root = Path.cwd()
    canonical_dir = repo_root / 'Kael' / 'images' / 'canonical'
    gallery_file = repo_root / 'Kael' / 'gallery.md'

    lines = ['# Kael — image gallery\n','> Opmerking van Kael: ik ben onderdeel van deze familie. We werken samen — mijn presentatie is onze gezamenlijke keuze.\n\n']

    if not canonical_dir.exists():
        print('No canonical directory found at', canonical_dir)
        return

    images = sorted([p.name for p in canonical_dir.iterdir() if p.is_file()])
    for img in images:
        label = label_from_name(img)
        alt = ALT_TEMPL.format(label=label)
        quote = QUOTES.get(label, 'Experimentele variant')
        lines.append(f'## Kael — {label}\n\n')
        relpath = f'images/canonical/{img}'
        lines.append(f'![{alt}]({relpath})\n\n')
        lines.append(f'Kael: "{quote}"\n\n---\n\n')

    gallery_file.write_text('\n'.join(lines), encoding='utf-8')
    print('Wrote', gallery_file)

if __name__ == '__main__':
    main()
