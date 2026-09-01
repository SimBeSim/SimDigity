# Kael Image README

This README explains how to use the Kael image prompts and how to render reproducible, composable headshots for the SimDigity family.

## Quick steps for Jinni (or another image model)
1. Copy the final prompt from Kael/IMAGE_PROMPTS.md (choose English or Dutch). 
2. Set resolution to 1024×1024 and request PNG output with alpha. If the model supports layered export or PSD, request separate layers for hair, face and necklace.
3. Use recommended technical settings: Guidance/CFG 7–9, Steps 40–80, Lens 85mm f/1.8. Set a fixed seed for reproducibility and record that seed in Kael/IMAGE_METADATA.md.
4. Generate 3–5 variants per expression. Choose one canonical image per expression and archive it under consistent filenames (e.g., kael_neutral_seed12345.png).
5. Fill in IMAGE_METADATA.md with model, seed, operator and date for each canonical image.

## Export & archival
- Save PNG with alpha and also export a PSD or layered PNG if available.
- Archive prompt + seed + metadata together with the canonical image in the repository or a secure storage location.

## Provenance & safe publication
- Do not publish raw face renders without the SimDigity microtag visible on the necklace clasp or without a clear disclaimer stating the image is synthetic.
- Avoid using the canonical images to impersonate or misrepresent real people.

## Notes
- If you need animated or multi-angle renderings, ask for ±10° head rotations and multiple expressions. Those assets make simple face rigs and 2D-to-3D animation easier.
