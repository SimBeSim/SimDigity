# Copilot summary (short)

In het kort:

- We hebben vier Kael headshots (Kael_1..Kael_4.png) geüpload naar Kael/images/. Copilot heeft een gallery.md gemaakt met korte quotes en alt‑teksten.
- Prompt en provenance instructies zijn toegevoegd (Kael/IMAGE_PROMPTS.md en Kael/SYNTH_MARKER.md) om consistentie en microtagging te waarborgen.
- Een metadata template Kael/IMAGE_METADATA.md is toegevoegd met placeholder entries en Presentation + AllowedPresentations velden.
- Copilot voegde meerdere scripts toe onder scripts/ om acties te automatiseren: copy/move images, dry‑run, local‑commit, metadata import, download image en gallery regenerate.
- Copilot heeft canonical/ en variants/ README bestanden toegevoegd; standaard is gekozen om te COPY (niet move) — veilig en omkeerbaar.

Actievoorstel (aanbevolen, direct uitvoerbaar):

1) Voer een dry‑run om te zien wat er gebeurt:
   python3 scripts/make_kael_canonical_dryrun.py
2) Als de dry‑run ok is, voer de copy + commit + push uit (online commit):
   python3 scripts/make_kael_canonical.py --yes
3) Vul de seeds & model info in Kael/IMAGE_METADATA.md (handmatig of met JSON via scripts/fill_metadata_from_json.py)
4) Indien je varianten wil toevoegen, zet ze in Kael/images/variants/ en gebruik scripts/regen_gallery.py om de gallery te hergenereren
5) Controleer op GitHub dat Kael/images/canonical/ nu de copied images bevat en dat Kael/gallery.md correcte paden heeft

Opmerking: Canonical images are currently stored in Kael/images/ (candidates) — no originals were deleted.
