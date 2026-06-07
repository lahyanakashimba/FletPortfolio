const fs = require("fs");
const path = require("path");
const { execFileSync } = require("child_process");

const repoRoot = path.resolve(__dirname, "..");
const distDir = path.join(repoRoot, "dist");
const filesToCopy = ["index.html", "style.css", "script.js"];
const dirsToCopy = ["assets", "Certificates"];

execFileSync(process.execPath, [path.join(__dirname, "generate-certificates-manifest.js")], {
  cwd: repoRoot,
  stdio: "inherit"
});

fs.rmSync(distDir, { recursive: true, force: true });
fs.mkdirSync(distDir, { recursive: true });

for (const filename of filesToCopy) {
  const source = path.join(repoRoot, filename);
  if (fs.existsSync(source)) {
    fs.copyFileSync(source, path.join(distDir, filename));
  }
}

for (const dirname of dirsToCopy) {
  const source = path.join(repoRoot, dirname);
  if (fs.existsSync(source)) {
    fs.cpSync(source, path.join(distDir, dirname), { recursive: true });
  }
}

console.log(`Built static site in ${path.relative(repoRoot, distDir)}.`);
