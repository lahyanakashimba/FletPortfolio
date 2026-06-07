# Flet GitHub Pages Deployment

This portfolio is a Flet/Python app. GitHub Pages must deploy the Flet web build output, not the repository root and not a Node/static build.

## Workflow

The workflow at `.github/workflows/deploy-pages.yml`:

1. Checks out the repository.
2. Sets up Python 3.12.
3. Installs dependencies from `requirements.txt`.
4. Runs `flet build web --yes --no-rich-output --base-url /FletPortfolio/`.
5. Uploads `build/web`.
6. Deploys the artifact to GitHub Pages.

## Local Build

```bash
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
flet build web --yes --no-rich-output --base-url /FletPortfolio/
```

Expected output:

```text
build/web
```

## Windows Notes

If the local Flet CLI fails with a Unicode console error, set:

```powershell
$env:PYTHONUTF8='1'
$env:PYTHONIOENCODING='utf-8'
$env:FLET_CLI_NO_RICH_OUTPUT='1'
```

If Flutter SDK installation takes a long time locally, let GitHub Actions run the build after the branch is merged.

## GitHub Pages Setup

1. Push `development`.
2. Open and merge the PR into `main`.
3. Go to repository Settings.
4. Open Pages.
5. Select GitHub Actions as the source.
6. Run the deployment workflow if it does not start automatically.

Expected URL:

```text
https://lahyanakashimba.github.io/FletPortfolio/
```
