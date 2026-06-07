# Manual Flet Layout Check

Screenshot automation was not available in this environment, so use this manual check before final submission.

## Run The App

```powershell
.\.venv\Scripts\Activate.ps1
python index.py
```

Optional browser mode:

```powershell
flet run --web index.py
```

## Confirm

- Header appears at the top.
- Hero card appears immediately below the header.
- No large blank grey area appears after the header.
- Sections appear in this order: Hero, About, MiningChecklistApp, Reflection, Evidence, Certificates, Learning Outcomes, Challenges, Footer.
- Screenshot placeholders are visible and not stretched to full-screen height.
- Certificates render as compact cards/icons, not embedded full PDF previews.
- Scrolling works on desktop and narrow/mobile width.

Save the final proof screenshot as `docs/qa/flet-layout-fixed.png` when you capture it.
