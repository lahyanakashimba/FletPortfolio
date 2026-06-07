# GitHub Pages Deployment

## Automatic Deployment

This repository includes `.github/workflows/deploy-pages.yml`. The workflow runs when changes are pushed to `main` or when it is manually started from the Actions tab.

The workflow:

1. Checks out the repository.
2. Sets up Node.js.
3. Runs `npm install`.
4. Runs `npm run build`.
5. Uploads the `dist` folder as the Pages artifact.
6. Deploys the artifact to GitHub Pages.

## Manual Setup Steps

1. Push the `development` branch.
2. Open and merge a pull request from `development` to `main`.
3. Open the GitHub repository.
4. Go to Settings.
5. Open Pages.
6. Select GitHub Actions as the deployment source.
7. Run the workflow from the Actions tab if it does not start automatically.
8. Open the published GitHub Pages URL shown by the deployment.

## Local Build Check

```bash
npm install
npm run build
```

The generated site is placed in `dist`.
