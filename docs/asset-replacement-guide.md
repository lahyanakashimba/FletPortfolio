# Asset Replacement Guide

This guide is for maintainers updating portfolio evidence files for the static GitHub Pages site.

## Evidence Images

Replace files in `assets/screenshots/` and keep the same source filenames:

- `github-commit-history-placeholder.png`
- `github-branch-placeholder.png`
- `github-pr-placeholder.png`
- `mining-checklist-app-ui-placeholder.png`
- `code-contribution-placeholder.png`

The static site generator copies these files into `site/assets/evidence/` using clean public filenames.

Use accurate screenshots that match the portfolio claim. Do not fabricate Git history, timestamps, or authorship evidence.

## Certificates

When adding or updating certificates:

- Add the certificate to `Certificates/`.
- Keep filenames clear because filenames become certificate card labels.
- Run the static site generator so files are copied to `site/assets/certificates/` and `site/certificates.json` is updated.

## Logo And Favicon

The public static site uses:

```text
assets/logos/unam-logo.jpeg
assets/icon.png
assets/icon-192.png
assets/icon-512.png
```

After updating these assets, regenerate the static site.

## Verify Changes

Regenerate static files:

```powershell
python scripts/generate_static_site.py
```

Serve the static site:

```powershell
python -m http.server 8000 --directory site
```

Open:

```text
http://localhost:8000
```
