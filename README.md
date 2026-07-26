# CDR System IR Bento Deck

Private working repository for the CDR System IR / company-introduction Bento deck.

## Latest deck

- `deck/CDR_System_IR_v4_product_videos.bento.html`

Open the `.bento.html` file in a modern browser. The deck is self-contained except for product videos, which are linked to the original homepage/Notion MP4 URLs to keep file size manageable.

## Version history

| Version | File | Notes |
|---|---|---|
| v0 | `deck/CDR_System_IR_v0.bento.html` | First homepage-based Bento draft |
| v1 | `deck/CDR_System_IR_v1_design.bento.html` | Design refined using Adham Dannaway UI principles |
| v2 | `deck/CDR_System_IR_v2_pdf_reflected.bento.html` | Uploaded PDF contents reflected |
| v3 | `deck/CDR_System_IR_v3_consistent_story.bento.html` | v1 narrative restored; v2 history/proof used as support |
| v4 | `deck/CDR_System_IR_v4_product_videos.bento.html` | Product videos inserted as linked Bento media |

## Working rules

- Keep the v1/v3 narrative as the main storyline.
- Use company history, revenue, DIPS/NVIDIA, investment numbers as supporting evidence, not as the main flow.
- Always apply Adham Dannaway UI tips: hierarchy, spacing, contrast, purposeful color, consistency, readable alignment/fonts.
- For large videos, prefer external linked `media` elements. Embed only if explicitly needed for offline presentation.

## Source materials

- Website extraction: `source/home_text.txt`, `source/home_links.txt`, `source/home_imgs.txt`
- PDF extraction: `source/IR_CDR_System_extracted.txt`
- Original PDFs: `source/*.pdf`
- Detailed handoff: `docs/IR_WORK_HANDOFF.md`

## Verification

Latest verified deck:

```text
CDR_System_IR_v4_product_videos.bento.html
slides: 11
size: 1,627,718 bytes
sha256: 3d0daeaf5ec2950f686210f278f62492e695c21a99d0b80e42c3a8ba42ce4416
local HTTP: HTTP/1.0 200 OK
video HEAD checks: 4/4 returned 200 video/mp4
```
