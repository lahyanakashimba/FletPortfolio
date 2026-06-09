# Lahya Nakashimba - Computer Programming I Portfolio Showcase

## Overview

This repository contains Lahya Nakashimba's Computer Programming I portfolio showcase for the MiningChecklistApp semester project.

The live GitHub Pages site is a fast static website generated from the portfolio content and public assets in this repository. The original Python/Flet version is preserved in `index.py` and `main.py` for reference and local Flet development.

## Live Site

```text
https://lahyanakashimba.github.io/FletPortfolio/
```

## Deployment Model

GitHub Pages serves the `site/` folder.

The deployed site is plain static HTML, CSS, JavaScript, images, and PDFs. It does not run Python in the browser, does not start a Pyodide worker, and does not load the Flet runtime.

## Static Site

Main files:

```text
site/index.html
site/styles.css
site/script.js
site/certificates.json
site/evidence.json
site/assets/
```

The static site includes:

- Navbar and hero section
- Student profile
- MiningChecklistApp project overview
- Individual contribution reflection
- Evidence assets
- Certificate cards
- Learning outcomes
- Challenges and solutions
- Individual contribution video section
- Contact/footer

## Generate Static Assets

Run this after changing certificates, screenshots, logos, or icons:

```powershell
python scripts/generate_static_site.py
```

The generator copies public assets into `site/assets/`, renames evidence images to clean public filenames, and updates:

```text
site/certificates.json
site/evidence.json
```

## Test Locally

Serve the static site folder:

```powershell
python -m http.server 8000 --directory site
```

Open:

```text
http://localhost:8000
```

The local static site should load without Flet, Pyodide, a Python worker, or a loading screen.

## Flet Source

The original Python/Flet implementation remains available:

```text
index.py
main.py
requirements.txt
assets/
Certificates/
```

Run the Flet version locally only when you need to inspect or continue the Python/Flet source:

```powershell
flet run --web index.py
```

## Deployment

Deployment happens from `main` through GitHub Actions.

Workflow:

```text
.github/workflows/deploy-pages.yml
```

The workflow runs `scripts/generate_static_site.py`, uploads `site/` as the Pages artifact, and deploys through GitHub Pages Actions.

## Maintenance Notes

- Keep `index.py` and `main.py` as the preserved Flet source.
- Keep public static content in `site/`.
- Add or update certificates in `Certificates/`, then regenerate the static site.
- Replace evidence images in `assets/screenshots/`, then regenerate the static site.
- Keep GitHub Pages source set to GitHub Actions.
