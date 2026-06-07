# Evidence Gallery and Certificates

## Evidence Gallery

The Flet portfolio displays valid PNG placeholders from `assets/screenshots`. Replace the files with real screenshots while keeping the same names so the app continues to load them without code changes.

Required placeholders:

- `github-commit-history-placeholder.png`
- `github-branch-placeholder.png`
- `github-pr-placeholder.png`
- `mining-checklist-app-ui-placeholder.png`
- `code-contribution-placeholder.png`

## Certificates

The Flet app scans `Certificates/` at startup. PDF and image files are displayed as cards using each filename as the display name.

Supported certificate formats:

- PDF
- PNG
- JPG/JPEG
- WEBP

Restart or rebuild the Flet app after adding certificates.
