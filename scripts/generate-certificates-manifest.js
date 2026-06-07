const fs = require("fs");
const path = require("path");

const repoRoot = path.resolve(__dirname, "..");
const certificatesDir = path.join(repoRoot, "Certificates");
const assetsDir = path.join(repoRoot, "assets");
const manifestPath = path.join(assetsDir, "certificates-manifest.json");
const supportedExtensions = new Set([".pdf", ".png", ".jpg", ".jpeg", ".webp"]);

function toWebPath(...parts) {
  return parts.map((part) => encodeURIComponent(part).replace(/%2F/g, "/")).join("/");
}

function displayName(filename) {
  return path.basename(filename, path.extname(filename)).replace(/[-_]+/g, " ").trim();
}

function fileType(extension) {
  if (extension === ".pdf") {
    return "PDF certificate";
  }
  return "Image certificate";
}

const files = fs.existsSync(certificatesDir)
  ? fs.readdirSync(certificatesDir, { withFileTypes: true })
      .filter((entry) => entry.isFile())
      .map((entry) => entry.name)
      .filter((filename) => supportedExtensions.has(path.extname(filename).toLowerCase()))
      .sort((a, b) => a.localeCompare(b))
  : [];

const manifest = files.map((filename) => {
  const extension = path.extname(filename).toLowerCase();
  return {
    filename,
    displayName: displayName(filename),
    type: fileType(extension),
    path: toWebPath("Certificates", filename)
  };
});

fs.mkdirSync(assetsDir, { recursive: true });
fs.writeFileSync(manifestPath, `${JSON.stringify(manifest, null, 2)}\n`);
console.log(`Generated ${path.relative(repoRoot, manifestPath)} with ${manifest.length} certificate(s).`);
