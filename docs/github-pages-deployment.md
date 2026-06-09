# Static GitHub Pages Deployment

This portfolio keeps the original Python/Flet source in the repository, but GitHub Pages deploys the fast static site in `site/`.

The live site is plain HTML, CSS, JavaScript, images, and PDFs. It does not load Flet, Pyodide, Flutter, or a Python worker in the browser.

## Workflow

The workflow at `.github/workflows/deploy-pages.yml`:

1. Checks out the repository.
2. Runs `python scripts/generate_static_site.py`.
3. Uploads `site/` as the Pages artifact.
4. Deploys the artifact to GitHub Pages.

## Local Static Preview

Regenerate assets:

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

## Flet Source

The Flet version remains available in:

```text
index.py
main.py
requirements.txt
```

Use it only when working on the original Python/Flet source:

```powershell
flet run --web index.py
```

## GitHub Pages Setup

1. Push changes to `main`.
2. Go to repository Settings.
3. Open Pages.
4. Select GitHub Actions as the source.
5. Run the static deployment workflow if it does not start automatically.

Expected URL:

```text
https://lahyanakashimba.github.io/FletPortfolio/
```
