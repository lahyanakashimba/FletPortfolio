# Lahya Nakashimba Portfolio Showcase

Computer Programming I personal portfolio website for Lahya Nakashimba. The site is a UNAM-themed academic showcase with a semester project contribution section, reflection, evidence placeholders, MATLAB certificates, learning outcomes, and GitHub Pages deployment support.

## Run Locally

This is a static website with a small Node build script.

```bash
npm install
npm run build
```

Serve the project root or the generated `dist` folder to preview locally:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`.

## Add New Certificates

1. Add PDF or image certificate files to the `Certificates` folder.
2. Run:

```bash
npm run build
```

The build regenerates `assets/certificates-manifest.json`, and the Certificates section updates automatically.

## Replace Screenshot Placeholders

Replace the placeholder PNG files in `assets/screenshots` with real evidence using the same filenames:

- `github-commit-history-placeholder.png`
- `github-branch-placeholder.png`
- `github-pr-placeholder.png`
- `mining-checklist-app-ui-placeholder.png`
- `code-contribution-placeholder.png`

Use accurate screenshots only. Do not fabricate git history, contribution timestamps, or authorship evidence.

## Deploy to GitHub Pages

The repository includes `.github/workflows/deploy-pages.yml`. After the branch is merged to `main`, GitHub Actions can build the static site and deploy the `dist` folder to GitHub Pages.

Manual setup:

1. Push the branch.
2. Merge the pull request into `main`.
3. Go to the GitHub repository settings.
4. Open Pages.
5. Select GitHub Actions as the source.
6. Run the deployment workflow if it does not start automatically.
7. Open the published Pages URL.

## Open a Pull Request

From the `development` branch:

```bash
git push -u origin development
```

Then open a pull request from `development` to `main` on GitHub, or use GitHub CLI if authenticated:

```bash
gh pr create --base main --head development --title "Upgrade portfolio showcase" --body "Adds the Computer Programming I portfolio showcase."
```
