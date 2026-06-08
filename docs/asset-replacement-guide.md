# Asset Replacement Guide

This guide is for maintainers updating portfolio evidence files.

## Evidence Images

Replace files in `assets/screenshots/` and keep the same filenames to avoid code changes:

- `github-commit-history-placeholder.png`
- `github-branch-placeholder.png`
- `github-pr-placeholder.png`
- `mining-checklist-app-ui-placeholder.png`
- `code-contribution-placeholder.png`

Use accurate screenshots that match the portfolio claim. Do not fabricate Git history, timestamps, or authorship evidence.

## Certificates

Certificate PDFs are served from `assets/certificates/` for web and GitHub Pages builds.

When adding or updating certificates:

- Add the certificate to `Certificates/` so the app can scan the display list.
- Add the same certificate to `assets/certificates/` so the web build can serve the file.
- Keep filenames clear because filenames become certificate card labels.

## Verify Changes

After updating assets, run:

```powershell
.\.venv\Scripts\Activate.ps1
python -m py_compile index.py
flet run --web index.py
```

For GitHub Pages, rebuild with:

```powershell
flet build web --yes --no-rich-output --base-url /FletPortfolio/ --web-renderer canvaskit --no-wasm --no-cdn
```
