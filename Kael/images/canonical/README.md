# Canonical images folder

This directory is reserved for canonical Kael images. At the moment, the canonical candidate files are present in `Kael/images/` (Kael_1.png .. Kael_4.png). When you're ready to mark them as canonical, you can either:

- Move the files into this directory (so they live at `Kael/images/canonical/Kael_1.png`, etc.), or
- Keep them in `Kael/images/` and update `Kael/IMAGE_METADATA.md` to point to the chosen filenames.

Notes:
- I have intentionally NOT moved or duplicated any image files to avoid accidental data loss and to keep the operation reversible.
- If you want me to perform the move/copy now, reply with `move canonical` (I will copy by default, not delete originals). If you prefer I create a single commit that copies the files into this folder now, reply `copy canonical` and I'll do that.
