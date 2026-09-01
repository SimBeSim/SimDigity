# SimDigity Synthetic Marker (Microtag)

Purpose: a small provenance marker to reduce misuse and enable verification that an image is synthetic and part of the SimDigity project.

## Recommendation
- Include a tiny discrete engraved SimDigity symbol (or a short microtext like "SD") on the clasp/backside of the Kael name necklace. This should be visible at 1:1 scale or detectable in metadata layers.
- Make the microtag subtle in final artistic output but present in the layered output and in the canonical image.

## Why this matters
- Visual provenance reduces the risk that a generated headshot will be passed off as a photograph of a real person.
- It enables third parties and your team to verify origin: if a published image lacks the microtag, it may not be the canonical/approved render.

## Implementation notes
- Add the microtag instruction to the prompt (already included in Kael/IMAGE_PROMPTS.md). 
- When rendering, request a separate "necklace isolated" layer or a high-res crop of the clasp to confirm the marker.
- Log the canonical seed and the filename in IMAGE_METADATA.md so that later verification is possible.
