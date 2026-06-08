# Flet GitHub Pages Deployment

This portfolio is a Flet/Python app. GitHub Pages must deploy the Flet web build output, not the repository root and not a Node/static build.

Use GitHub Actions as the Pages source. Do not use "Deploy from a branch" with `main / root`, because raw Python files are not a deployable GitHub Pages website.

## Workflow

The workflow at `.github/workflows/deploy-pages.yml`:

1. Checks out the repository.
2. Sets up Python 3.12.
3. Installs Flutter through `subosito/flutter-action`.
4. Installs dependencies from `requirements.txt`.
5. Runs `flet build web --yes --no-rich-output --module-name index --base-url /FletPortfolio/ --web-renderer canvaskit --no-wasm --no-cdn`.
6. Verifies that `build/web` exists.
7. Uploads `build/web`.
8. Deploys the artifact to GitHub Pages.

The workflow installs Flutter explicitly because local Flet web builds require Flutter SDK support.

## Local Build

```bash
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
flet build web --yes --no-rich-output --module-name index --base-url /FletPortfolio/ --web-renderer canvaskit --no-wasm --no-cdn
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

## Local App Preview

Do not use `python -m http.server` from the repository root as the main app. Use:

```powershell
.\.venv\Scripts\Activate.ps1
python index.py
```

Or run browser mode:

```powershell
flet run --web index.py
```

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
