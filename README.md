# Lahya Nakashimba Flet Portfolio Showcase

Computer Programming I personal portfolio built with Flet/Python. The app presents a UNAM-themed academic showcase for Lahya Nakashimba, including MiningChecklistApp contributions, reflection, evidence placeholders, MATLAB certificates, learning outcomes, challenges, and GitHub Pages deployment support.

The portfolio is designed as a responsive Flet website with a custom navbar, navy/gold hero card, compact evidence gallery, and certificate icon cards. It should be previewed with Flet, not with a static file server.

## Create Virtual Environment

```bash
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run Locally

```bash
python index.py
```

The Flet desktop/web runtime starts the portfolio app from `index.py`.

Do not use `python -m http.server` from the repository root as the main app preview. This is a Flet app, so run it through Flet.

Browser mode:

```bash
flet run --web index.py
```

## Build for Web

```bash
flet build web --yes --no-rich-output --base-url /FletPortfolio/
```

The expected output folder is `build/web`.

On Windows, if the Flet CLI prints Unicode encoding errors, run:

```bash
$env:PYTHONUTF8='1'
$env:PYTHONIOENCODING='utf-8'
$env:FLET_CLI_NO_RICH_OUTPUT='1'
flet build web --yes --no-rich-output --base-url /FletPortfolio/
```

## Add Certificates

Add PDF or image files to the `Certificates` folder and restart or rebuild the app. The Flet UI scans the folder automatically and uses filenames as display names.

Supported extensions:

- `.pdf`
- `.png`
- `.jpg`
- `.jpeg`
- `.webp`

## Replace Screenshot Placeholders

Replace these valid PNG placeholder files with real evidence using the same filenames:

- `assets/screenshots/github-commit-history-placeholder.png`
- `assets/screenshots/github-branch-placeholder.png`
- `assets/screenshots/github-pr-placeholder.png`
- `assets/screenshots/mining-checklist-app-ui-placeholder.png`
- `assets/screenshots/code-contribution-placeholder.png`

Use accurate screenshots only. Do not fabricate git history, timestamps, or authorship evidence.

## Deploy to GitHub Pages

The workflow `.github/workflows/deploy-pages.yml` installs Python, installs Flutter, builds the Flet app, and uploads `build/web`.

Manual setup after merging to `main`:

1. Open the GitHub repository.
2. Go to Settings.
3. Open Pages.
4. Select GitHub Actions as the source.
5. Run or wait for the `Deploy Flet Portfolio to GitHub Pages` workflow.
6. Open the published site.

Expected URL:

```text
https://lahyanakashimba.github.io/FletPortfolio/
```

## Open Pull Request

```bash
git push -u origin development
```

Then open:

```text
https://github.com/lahyanakashimba/FletPortfolio/pull/new/development
```
