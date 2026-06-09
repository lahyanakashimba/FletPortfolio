from __future__ import annotations

import json
import shutil
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
SITE_ASSETS = SITE / "assets"

LOGO_SOURCE = ROOT / "assets" / "logos" / "unam-logo.jpeg"
ICON_SOURCES = {
    "favicon.png": ROOT / "assets" / "icon.png",
    "icon-192.png": ROOT / "assets" / "icon-192.png",
    "icon-512.png": ROOT / "assets" / "icon-512.png",
}

EVIDENCE_ASSETS = [
    (
        ROOT / "assets" / "screenshots" / "github-commit-history-placeholder.png",
        "commit-history.png",
        "Commit History Asset",
        "A visual record of portfolio and contribution development activity.",
    ),
    (
        ROOT / "assets" / "screenshots" / "github-branch-placeholder.png",
        "development-branch.png",
        "Development Branch Asset",
        "Branch workflow evidence showing organised project development.",
    ),
    (
        ROOT / "assets" / "screenshots" / "github-pr-placeholder.png",
        "pull-request-evidence.png",
        "Pull Request Evidence Asset",
        "Pull request evidence showing review-ready contribution work.",
    ),
    (
        ROOT / "assets" / "screenshots" / "mining-checklist-app-ui-placeholder.png",
        "mining-checklist-interface.png",
        "MiningChecklistApp Interface Asset",
        "Application interface evidence from the semester project.",
    ),
    (
        ROOT / "assets" / "screenshots" / "code-contribution-placeholder.png",
        "code-contribution.png",
        "Code Contribution Asset",
        "Source code evidence connected to the student's project contribution.",
    ),
]


def display_name(path: Path) -> str:
    return path.stem.replace("_", " ").replace("-", " ").strip()


def reset_generated_assets() -> None:
    for subdir in ("logos", "icons", "evidence", "certificates"):
        target = SITE_ASSETS / subdir
        if target.exists():
            shutil.rmtree(target)
        target.mkdir(parents=True, exist_ok=True)


def copy_required_assets() -> None:
    if not LOGO_SOURCE.exists():
        raise FileNotFoundError(f"Missing logo source: {LOGO_SOURCE}")
    shutil.copyfile(LOGO_SOURCE, SITE_ASSETS / "logos" / "unam-logo.jpeg")

    for name, source in ICON_SOURCES.items():
        if source.exists():
            shutil.copyfile(source, SITE_ASSETS / "icons" / name)

    evidence_manifest = []
    for source, public_name, title, caption in EVIDENCE_ASSETS:
        if not source.exists():
            continue
        shutil.copyfile(source, SITE_ASSETS / "evidence" / public_name)
        evidence_manifest.append(
            {
                "title": title,
                "caption": caption,
                "src": f"assets/evidence/{public_name}",
            }
        )

    (SITE / "evidence.json").write_text(
        json.dumps(evidence_manifest, indent=2) + "\n",
        encoding="utf-8",
    )


def generate_certificates_json() -> None:
    cert_source = ROOT / "Certificates"
    if not cert_source.exists():
        cert_source = ROOT / "assets" / "certificates"

    supported = {".pdf", ".png", ".jpg", ".jpeg", ".webp"}
    certificates = []
    if cert_source.exists():
        for source in sorted(cert_source.iterdir(), key=lambda item: item.name.lower()):
            if not source.is_file() or source.suffix.lower() not in supported:
                continue
            destination = SITE_ASSETS / "certificates" / source.name
            shutil.copyfile(source, destination)
            certificates.append(
                {
                    "title": display_name(source),
                    "type": source.suffix.lstrip(".").upper(),
                    "href": f"assets/certificates/{quote(source.name)}",
                }
            )

    (SITE / "certificates.json").write_text(
        json.dumps(certificates, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    SITE.mkdir(exist_ok=True)
    reset_generated_assets()
    copy_required_assets()
    generate_certificates_json()


if __name__ == "__main__":
    main()
