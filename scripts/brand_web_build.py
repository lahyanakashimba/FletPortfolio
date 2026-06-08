from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILD_WEB = ROOT / "build" / "web"
ICON_SOURCE = ROOT / "assets" / "icon.png"
ICON_192_SOURCE = ROOT / "assets" / "icon-192.png"
ICON_512_SOURCE = ROOT / "assets" / "icon-512.png"
LOGO_SOURCE = ROOT / "assets" / "logos" / "unam-logo.jpeg"


def copy_brand_assets() -> None:
    if not ICON_SOURCE.exists():
        raise FileNotFoundError(f"Missing icon source: {ICON_SOURCE}")
    if not ICON_192_SOURCE.exists():
        raise FileNotFoundError(f"Missing 192px icon source: {ICON_192_SOURCE}")
    if not ICON_512_SOURCE.exists():
        raise FileNotFoundError(f"Missing 512px icon source: {ICON_512_SOURCE}")
    if not LOGO_SOURCE.exists():
        raise FileNotFoundError(f"Missing logo source: {LOGO_SOURCE}")

    shutil.copyfile(ICON_SOURCE, BUILD_WEB / "favicon.png")
    shutil.copyfile(ICON_SOURCE, BUILD_WEB / "brand-icon.png")

    logos_dir = BUILD_WEB / "logos"
    logos_dir.mkdir(exist_ok=True)
    shutil.copyfile(LOGO_SOURCE, logos_dir / "unam-logo.jpeg")

    icons_dir = BUILD_WEB / "icons"
    icons_dir.mkdir(exist_ok=True)
    for name in ("Icon-192.png", "Icon-maskable-192.png", "apple-touch-icon-192.png"):
        shutil.copyfile(ICON_192_SOURCE, icons_dir / name)
    for name in ("Icon-512.png", "Icon-maskable-512.png"):
        shutil.copyfile(ICON_512_SOURCE, icons_dir / name)


def update_manifest() -> None:
    manifest_path = BUILD_WEB / "manifest.json"
    if not manifest_path.exists():
        return

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["name"] = "Lahya Nakashimba Portfolio Showcase"
    manifest["short_name"] = "Lahya Portfolio"
    manifest["background_color"] = "#FFFDF5"
    manifest["theme_color"] = "#002F6C"
    manifest["icons"] = [
        {"src": "icons/Icon-192.png", "sizes": "192x192", "type": "image/png"},
        {"src": "icons/Icon-512.png", "sizes": "512x512", "type": "image/png"},
        {
            "src": "icons/Icon-maskable-192.png",
            "sizes": "192x192",
            "type": "image/png",
            "purpose": "maskable",
        },
        {
            "src": "icons/Icon-maskable-512.png",
            "sizes": "512x512",
            "type": "image/png",
            "purpose": "maskable",
        },
    ]
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def branded_loader_markup() -> str:
    return """<style id="portfolio-loading-style">
    html, body {
      background: #FFFDF5;
    }

    #portfolio-loading {
      position: fixed;
      inset: 0;
      z-index: 2147483647;
      display: flex;
      align-items: center;
      justify-content: center;
      background:
        radial-gradient(circle at top left, rgba(191, 160, 70, 0.14), transparent 34rem),
        linear-gradient(135deg, #FFFDF5 0%, #F5F7FB 100%);
      color: #001D43;
      font-family: Arial, Helvetica, sans-serif;
      transition: opacity 220ms ease, visibility 220ms ease;
    }

    #portfolio-loading.portfolio-loading-hidden {
      opacity: 0;
      visibility: hidden;
    }

    .portfolio-loading-card {
      width: min(88vw, 420px);
      padding: 30px 26px;
      text-align: center;
      border: 1px solid rgba(191, 160, 70, 0.28);
      border-radius: 12px;
      background: rgba(255, 253, 245, 0.92);
      box-shadow: 0 18px 46px rgba(0, 29, 67, 0.14);
    }

    .portfolio-loading-logo {
      width: 82px;
      height: 82px;
      object-fit: contain;
      margin: 0 auto 18px;
      display: block;
      border-radius: 18px;
      background: #FFFDF5;
    }

    .portfolio-loading-name {
      margin: 0 0 8px;
      font-size: 24px;
      line-height: 1.2;
      font-weight: 700;
      color: #002F6C;
    }

    .portfolio-loading-text {
      margin: 0 0 20px;
      font-size: 15px;
      line-height: 1.4;
      color: #4B5563;
    }

    .portfolio-loading-spinner {
      width: 30px;
      height: 30px;
      margin: 0 auto;
      border: 3px solid rgba(0, 47, 108, 0.18);
      border-top-color: #BFA046;
      border-radius: 50%;
      animation: portfolio-loading-spin 0.85s linear infinite;
    }

    @keyframes portfolio-loading-spin {
      to {
        transform: rotate(360deg);
      }
    }
  </style>
  <div id="portfolio-loading" role="status" aria-live="polite">
    <div class="portfolio-loading-card">
      <img class="portfolio-loading-logo" src="brand-icon.png" alt="UNAM logo">
      <h1 class="portfolio-loading-name">Lahya Nakashimba</h1>
      <p class="portfolio-loading-text">Loading Portfolio Showcase&hellip;</p>
      <div class="portfolio-loading-spinner" aria-hidden="true"></div>
    </div>
  </div>
  <script>
    (function () {
      var shownAt = Date.now();
      var minDisplayMs = 1400;

      function hidePortfolioLoader() {
        var loader = document.getElementById("portfolio-loading");
        if (!loader) {
          return;
        }
        loader.classList.add("portfolio-loading-hidden");
        window.setTimeout(function () {
          loader.remove();
          var style = document.getElementById("portfolio-loading-style");
          if (style) {
            style.remove();
          }
        }, 260);
      }

      window.addEventListener("flutter-first-frame", function () {
        var remaining = Math.max(0, minDisplayMs - (Date.now() - shownAt));
        window.setTimeout(function () {
          window.requestAnimationFrame(function () {
            window.requestAnimationFrame(hidePortfolioLoader);
          });
        }, remaining);
      });
    })();
  </script>"""


def patch_index() -> None:
    index_path = BUILD_WEB / "index.html"
    html = index_path.read_text(encoding="utf-8")

    html = html.replace(
        '<link rel="icon" type="image/png" href="favicon.png">',
        '<link rel="icon" type="image/png" href="favicon.png?v=unam">',
    )
    html = html.replace(
        '<link rel="apple-touch-icon" href="icons/apple-touch-icon-192.png">',
        '<link rel="apple-touch-icon" href="icons/Icon-192.png?v=unam">',
    )
    html = html.replace(
        'canvasKitBaseUrl: "/canvaskit/"',
        'canvasKitBaseUrl: "/FletPortfolio/canvaskit/"',
    )
    html = html.replace(
        'pyodideUrl: "/pyodide/pyodide.js"',
        'pyodideUrl: "/FletPortfolio/pyodide/pyodide.js"',
    )

    marker = "<body>"
    loader = branded_loader_markup()
    if loader not in html:
        html = html.replace(marker, f"{marker}\n  {loader}", 1)

    index_path.write_text(html, encoding="utf-8")


def patch_flutter_bootstrap() -> None:
    bootstrap_path = BUILD_WEB / "flutter_bootstrap.js"
    if not bootstrap_path.exists():
        return

    js = bootstrap_path.read_text(encoding="utf-8")
    marker = "    flutterConfig.renderer = flet.webRenderer;\n"
    patch = marker + '    flutterConfig.canvasKitVariant = "full";\n'
    if marker in js and patch not in js:
        js = js.replace(marker, patch, 1)
    bootstrap_path.write_text(js, encoding="utf-8")


def normalize_pyodide_lock_hashes() -> None:
    lock_path = BUILD_WEB / "pyodide" / "pyodide-lock.json"
    if not lock_path.exists():
        return

    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    changed = False
    for package in lock.get("packages", {}).values():
        file_name = package.get("file_name")
        if not file_name:
            continue
        package_path = lock_path.parent / file_name
        if not package_path.exists():
            continue
        actual_hash = hashlib.sha256(package_path.read_bytes()).hexdigest()
        if package.get("sha256") != actual_hash:
            package["sha256"] = actual_hash
            changed = True

    if changed:
        lock_path.write_text(json.dumps(lock, separators=(",", ":")) + "\n", encoding="utf-8")


def main() -> None:
    if not BUILD_WEB.exists():
        raise FileNotFoundError(f"Missing Flet build output: {BUILD_WEB}")
    copy_brand_assets()
    update_manifest()
    patch_index()
    patch_flutter_bootstrap()
    normalize_pyodide_lock_hashes()


if __name__ == "__main__":
    main()
