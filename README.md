# Lahya Nakashimba - Computer Programming I Portfolio Showcase

## Overview

This is a Flet-based web portfolio for the Computer Programming I semester project showcase.

It presents Lahya Nakashimba's MiningChecklistApp contribution, evidence assets, certificates, learning outcomes, challenges, and contribution video section.

## Live Site

Expected URL:

```text
https://lahyanakashimba.github.io/FletPortfolio/
```

## Tech Stack

- Python
- Flet
- GitHub Pages
- GitHub Actions
- Flutter build runtime for Flet web export

## Local Setup

PowerShell:

```powershell
cd D:\Documents\Jobs\Morning\Programming\FletPortfolio
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run Locally

Browser mode:

```powershell
flet run --web index.py
```

Desktop mode:

```powershell
python index.py
```

## Build for Web

GitHub Pages cannot run Python directly. The Flet app is built into static files under `build/web`, and GitHub Pages serves those generated files.

```powershell
flet build web --yes --no-rich-output --base-url /FletPortfolio/ --web-renderer canvaskit --no-wasm --no-cdn
```

## Deployment

- Deployment happens from `main`.
- GitHub Actions builds the Flet web output.
- GitHub Pages serves `build/web`.
- Pages Source must be set to GitHub Actions.

The deployment workflow is `.github/workflows/deploy-pages.yml`.

## Evidence Assets

- Evidence assets live in `assets/screenshots`.
- Replace PNG files using the same filenames to update visual evidence.
- Public UI uses polished labels such as Commit History Asset and Pull Request Evidence Asset.

See `docs/asset-replacement-guide.md` for maintainer instructions.

## Certificates

- Certificates are managed from `Certificates/` and `assets/certificates/`.
- The app displays certificate files as compact cards.
- Keep certificate filenames clear because the app uses filenames as display labels.

## Project Structure

```text
index.py
requirements.txt
assets/
Certificates/
docs/
.github/workflows/deploy-pages.yml
```

## Maintenance Notes

- Do not use `python -m http.server` from the repository root to run the app.
- Use Flet run/build commands.
- Keep GitHub Pages source as GitHub Actions.
