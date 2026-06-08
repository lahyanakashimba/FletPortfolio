# Manual Website Layout Check

Screenshot automation was not available in this environment. Use this browser-first QA check before final submission.

## Run Browser Mode

```powershell
.\.venv\Scripts\Activate.ps1
flet run --web index.py
```

## Check The Top Of The Page

- The white website navbar is visible first.
- The UNAM logo and "Lahya Nakashimba" appear on the left.
- Navigation links wrap naturally if the window is narrow.
- The navy/gold hero card appears immediately below the navbar.
- There is no giant grey blank panel between the navbar and hero.

## Check Sections

- Hero, About, MiningChecklistApp, Individual Contribution, Evidence, Certificates, Learning Outcomes, Challenges, and Footer appear in order.
- Screenshot placeholders are compact cards around 190px tall.
- Certificate PDFs render as compact icon cards, not embedded preview panels.
- The page background is light blue/off-white, with white cards and navy/gold accents.
- Desktop and browser mode both scroll naturally.

Save a proof screenshot as `docs/qa/website-layout-fixed.png` after manual capture.
