# CDR System IR Bento Deck

Public CDR System IR site and version history for the company-introduction Bento deck.

## Current published IR

- Korean IR v5: [CDR_System_IR_v5.bento.html](https://i073073.github.io/cdr-ir/CDR_System_IR_v5.bento.html)
- Stable homepage IR link: [i073073.github.io/cdr-ir/](https://i073073.github.io/cdr-ir/) — redirects to the current Korean v5 file, preserving query/hash navigation.
- English IR: [CDR_System_IR_english.html](https://i073073.github.io/cdr-ir/CDR_System_IR_english.html) — unchanged.
- Latest-file alias: `deck/latest.html` contains the same public Korean v5 deck.

The Korean IR has 13 slides after the user-requested deletion of the duplicated first cover. The former second page is now the cover; all remaining slide text, notes, layout, images, chart, linked product videos and embedded animation are unchanged. Its internal v4.8 title is retained as supplied. The public copy uses the existing read-only publishing mode, omits collaboration credentials, and has a separate document identity to avoid restoring an older browser copy.

## Earlier editable deck

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
| v5 Korean | `CDR_System_IR_v5.bento.html` | 13-slide Korean IR after removing the duplicated first cover, published read-only without collaboration credentials |

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

Earlier v4 verification baseline:

```text
CDR_System_IR_v4_product_videos.bento.html
slides: 11
size: 1,627,718 bytes
sha256: 3d0daeaf5ec2950f686210f278f62492e695c21a99d0b80e42c3a8ba42ce4416
local HTTP: HTTP/1.0 200 OK
video HEAD checks: 4/4 returned 200 video/mp4
```
