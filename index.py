from pathlib import Path
from urllib.parse import quote

import flet as ft


ROOT = Path(__file__).resolve().parent
CERTIFICATES_DIR = ROOT / "Certificates"
LOGOS_DIR = ROOT / "assets" / "logos"
SCREENSHOTS_DIR = ROOT / "assets" / "screenshots"

NAVY = "#002f6c"
NAVY_DARK = "#001d43"
BLUE = "#0f5ea8"
GOLD = "#f2c230"
GOLD_SOFT = "#fff4c7"
WHITE = "#ffffff"
SURFACE = "#f4f7fb"
INK = "#172033"
MUTED = "#5b6474"
LINE = "#dce3ef"


def ensure_logo_placeholder() -> str:
    LOGOS_DIR.mkdir(parents=True, exist_ok=True)
    existing = sorted(LOGOS_DIR.glob("unam-logo.*"))
    if existing:
        return f"assets/logos/{existing[0].name}"

    placeholder = LOGOS_DIR / "unam-logo-placeholder.svg"
    if not placeholder.exists():
        placeholder.write_text(
            """<svg xmlns="http://www.w3.org/2000/svg" width="320" height="320" viewBox="0 0 320 320">
  <rect width="320" height="320" rx="160" fill="#002f6c"/>
  <circle cx="160" cy="160" r="118" fill="none" stroke="#f2c230" stroke-width="12"/>
  <text x="160" y="148" text-anchor="middle" font-family="Arial, sans-serif" font-size="58" font-weight="700" fill="#ffffff">UNAM</text>
  <text x="160" y="198" text-anchor="middle" font-family="Arial, sans-serif" font-size="24" fill="#f2c230">Logo Placeholder</text>
</svg>
""",
            encoding="utf-8",
        )
    return "assets/logos/unam-logo-placeholder.svg"


def encoded_asset_path(path: Path) -> str:
    return "/".join(quote(part) for part in path.relative_to(ROOT).parts)


def certificate_files() -> list[Path]:
    supported = {".pdf", ".png", ".jpg", ".jpeg", ".webp"}
    if not CERTIFICATES_DIR.exists():
        return []
    return sorted(
        (path for path in CERTIFICATES_DIR.iterdir() if path.is_file() and path.suffix.lower() in supported),
        key=lambda path: path.name.lower(),
    )


def display_name(path: Path) -> str:
    return path.stem.replace("_", " ").replace("-", " ").strip()


def border_all(width: int | float, color: str) -> ft.Border:
    side = ft.BorderSide(width, color)
    return ft.Border(left=side, top=side, right=side, bottom=side)


def card(content: list[ft.Control], col=None, bgcolor=WHITE) -> ft.Container:
    return ft.Container(
        content=ft.Column(content, spacing=10),
        bgcolor=bgcolor,
        border=border_all(1, LINE),
        border_radius=8,
        padding=18,
        shadow=ft.BoxShadow(blur_radius=18, color="#1f3a5f18", offset=ft.Offset(0, 8)),
        col=col or {"xs": 12, "md": 6, "lg": 4},
    )


def section_title(eyebrow: str, title: str, body: str | None = None) -> ft.Column:
    controls: list[ft.Control] = [
        ft.Text(eyebrow.upper(), size=12, weight=ft.FontWeight.BOLD, color=BLUE),
        ft.Text(title, size=34, weight=ft.FontWeight.BOLD, color=NAVY_DARK),
    ]
    if body:
        controls.append(ft.Text(body, size=16, color=MUTED))
    return ft.Column(controls, spacing=6)


def bullet_items(items: list[str]) -> ft.Column:
    return ft.Column(
        [
            ft.Row(
                [
                    ft.Container(width=8, height=8, bgcolor=GOLD, border_radius=20),
                    ft.Text(item, size=15, color=INK, expand=True),
                ],
                spacing=10,
                vertical_alignment=ft.CrossAxisAlignment.START,
            )
            for item in items
        ],
        spacing=8,
    )


def tag_list(tags: list[str]) -> ft.Row:
    return ft.Row(
        [
            ft.Container(
                content=ft.Text(tag, size=13, weight=ft.FontWeight.BOLD, color=NAVY),
                bgcolor="#eef5ff",
                border=border_all(1, "#cdddf2"),
                border_radius=30,
                padding=ft.Padding(12, 7, 12, 7),
            )
            for tag in tags
        ],
        wrap=True,
        spacing=8,
        run_spacing=8,
    )


def nav_button(label: str, target: str, page: ft.Page) -> ft.TextButton:
    return ft.TextButton(
        label,
        style=ft.ButtonStyle(color=NAVY),
        on_click=lambda _: page.scroll_to(key=target, duration=500),
    )


def evidence_image(filename: str, title: str, caption: str) -> ft.Container:
    return card(
        [
            ft.Image(
                src=f"assets/screenshots/{filename}",
                height=170,
                fit=ft.BoxFit.COVER,
                border_radius=8,
                semantics_label=title,
                error_content=ft.Container(
                    content=ft.Text("Screenshot placeholder missing", color="#8a1f11"),
                    bgcolor="#fff0ed",
                    padding=18,
                    border_radius=8,
                ),
            ),
            ft.Text(title, size=18, weight=ft.FontWeight.BOLD, color=NAVY),
            ft.Text(caption, size=14, color=MUTED),
        ]
    )


def certificate_card(path: Path, page: ft.Page) -> ft.Container:
    href = encoded_asset_path(path)
    kind = "PDF certificate" if path.suffix.lower() == ".pdf" else "Image certificate"

    def open_certificate(_):
        page.launch_url(href)

    return card(
        [
            ft.Icon(ft.Icons.WORKSPACE_PREMIUM, color=GOLD, size=30),
            ft.Text(display_name(path), size=18, weight=ft.FontWeight.BOLD, color=NAVY),
            ft.Text(kind, size=14, color=MUTED),
            ft.Row(
                [
                    ft.Button("View/Open", icon=ft.Icons.OPEN_IN_NEW, bgcolor=NAVY, color=WHITE, on_click=open_certificate),
                    ft.Button("Download/Open", icon=ft.Icons.DOWNLOAD, bgcolor=GOLD, color=NAVY_DARK, on_click=open_certificate),
                ],
                wrap=True,
                spacing=8,
            ),
        ]
    )


def build_header(page: ft.Page, logo_src: str) -> ft.Container:
    return ft.Container(
        content=ft.Row(
            [
                ft.Row(
                    [
                        ft.Image(src=logo_src, width=42, height=42, fit=ft.BoxFit.CONTAIN, semantics_label="UNAM logo"),
                        ft.Text("Lahya Nakashimba", size=18, weight=ft.FontWeight.BOLD, color=NAVY),
                    ],
                    spacing=10,
                ),
                ft.Row(
                    [
                        nav_button("About", "about", page),
                        nav_button("Project", "project", page),
                        nav_button("Reflection", "reflection", page),
                        nav_button("Evidence", "evidence", page),
                        nav_button("Certificates", "certificates", page),
                    ],
                    wrap=True,
                    alignment=ft.MainAxisAlignment.END,
                    expand=True,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            wrap=True,
        ),
        bgcolor="#fffffff2",
        border=ft.Border(bottom=ft.BorderSide(1, LINE)),
        padding=ft.Padding(24, 12, 24, 12),
    )


def build_hero(page: ft.Page, logo_src: str) -> ft.Container:
    return ft.Container(
        key="home",
        content=ft.Container(
            content=ft.ResponsiveRow(
                [
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("UNIVERSITY OF NAMIBIA | COMPUTER PROGRAMMING I", size=13, color=GOLD, weight=ft.FontWeight.BOLD),
                                ft.Text("Lahya Nakashimba", size=46, weight=ft.FontWeight.BOLD, color=WHITE),
                                ft.Text("Computer Programming I Portfolio Showcase", size=23, weight=ft.FontWeight.BOLD, color=GOLD),
                                ft.Text(
                                    "A Flet-based academic portfolio documenting my MiningChecklistApp contribution, reflection, evidence, certificates, and learning outcomes.",
                                    size=17,
                                    color="#eef5ff",
                                ),
                                ft.Row(
                                    [
                                        ft.Button("View Contributions", icon=ft.Icons.WORK, bgcolor=GOLD, color=NAVY_DARK, on_click=lambda _: page.scroll_to(key="project", duration=500)),
                                        ft.Button("View Certificates", icon=ft.Icons.WORKSPACE_PREMIUM, bgcolor=WHITE, color=NAVY, on_click=lambda _: page.scroll_to(key="certificates", duration=500)),
                                        ft.Button("View Video", icon=ft.Icons.PLAY_CIRCLE, bgcolor="#ffffff22", color=WHITE, on_click=lambda _: page.scroll_to(key="video", duration=500)),
                                    ],
                                    wrap=True,
                                    spacing=10,
                                ),
                            ],
                            spacing=14,
                            tight=True,
                        ),
                        col={"xs": 12, "md": 7},
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Image(src=logo_src, height=96, fit=ft.BoxFit.CONTAIN, semantics_label="UNAM logo"),
                                ft.Container(content=ft.Text("Project: MiningChecklistApp", color=INK, weight=ft.FontWeight.BOLD), bgcolor=WHITE, padding=14, border_radius=8),
                                ft.Container(content=ft.Text("Theme: UNAM navy, gold, and white", color=INK, weight=ft.FontWeight.BOLD), bgcolor=WHITE, padding=14, border_radius=8),
                                ft.Container(content=ft.Text("Evidence: real placeholders ready for replacement", color=INK, weight=ft.FontWeight.BOLD), bgcolor=WHITE, padding=14, border_radius=8),
                            ],
                            spacing=12,
                            tight=True,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        bgcolor="#ffffff22",
                        border=border_all(1, "#ffffff55"),
                        border_radius=8,
                        padding=20,
                        col={"xs": 12, "md": 5},
                    ),
                ],
                spacing=22,
                run_spacing=22,
                vertical_alignment=ft.CrossAxisAlignment.START,
                            ),
            gradient=ft.LinearGradient(begin=ft.Alignment(-1, -1), end=ft.Alignment(1, 1), colors=[NAVY_DARK, NAVY, BLUE]),
            border_radius=8,
            padding=ft.Padding(24, 28, 24, 28),
            shadow=ft.BoxShadow(blur_radius=24, color="#1f3a5f24", offset=ft.Offset(0, 10)),
        ),
        bgcolor=SURFACE,
        padding=ft.Padding(16, 16, 16, 8),
    )


def build_about() -> ft.Container:
    return ft.Container(
        key="about",
        content=ft.ResponsiveRow(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            section_title("About Me", "Student Profile"),
                            ft.Text(
                                "I am Lahya Nakashimba, a Computer Programming I student building practical programming skills through project work, documentation, testing, and presentation preparation.",
                                size=16,
                                color=INK,
                            ),
                            ft.Text(
                                "This portfolio identifies my own work honestly and leaves clear spaces where final GitHub screenshots, code evidence, design notes, and video evidence can be added.",
                                size=16,
                                color=INK,
                            ),
                        ],
                        spacing=12,
                    ),
                    col={"xs": 12, "md": 8},
                ),
                card(
                    [
                        ft.Text("Academic Context", size=20, weight=ft.FontWeight.BOLD, color=NAVY),
                        bullet_items(["Course: Computer Programming I", "Institution: University of Namibia", "Portfolio year: 2026", "Focus: honest contribution evidence"]),
                    ],
                    col={"xs": 12, "md": 4},
                ),
            ],
            spacing=18,
            run_spacing=18,
        ),
        padding=ft.Padding(24, 32, 24, 32),
    )


def build_project() -> ft.Container:
    project_cards = [
        ("Project Overview", "MiningChecklistApp is a mobile safety checklist project for mining environments, designed to support workers and supervisors with organized pre-shift checks."),
        ("Problem Solved", "Paper-based checks can be difficult to track and review. A digital checklist improves consistency, record keeping, and accountability."),
        ("My Contribution", "My contribution area focuses on requirement understanding, interface planning, testing support, documentation, and preparing accurate evidence of my work."),
        ("Lessons Learned", "The project improved my understanding of app structure, GitHub workflows, debugging, documentation, and presentation preparation."),
    ]
    return ft.Container(
        key="project",
        bgcolor=SURFACE,
        padding=ft.Padding(24, 32, 24, 32),
        content=ft.Column(
            [
                section_title(
                    "Semester Project",
                    "MiningChecklistApp",
                    "A clear contribution area for my Computer Programming I semester project.",
                ),
                ft.ResponsiveRow(
                    [
                        card(
                            [
                                ft.Text(title, size=20, weight=ft.FontWeight.BOLD, color=NAVY),
                                ft.Text(body, size=15, color=MUTED),
                            ]
                        )
                        for title, body in project_cards
                    ],
                    spacing=14,
                    run_spacing=14,
                ),
                ft.ResponsiveRow(
                    [
                        card(
                            [
                                ft.Text("Key Features", size=20, weight=ft.FontWeight.BOLD, color=NAVY),
                                bullet_items(["Worker checklist submission flow", "Supervisor review area", "Firebase-backed storage concept", "Mobile-friendly interface"]),
                            ],
                            col={"xs": 12, "md": 6},
                        ),
                        card(
                            [
                                ft.Text("Technologies Used", size=20, weight=ft.FontWeight.BOLD, color=NAVY),
                                tag_list(["React Native", "Expo", "Firebase", "JavaScript", "GitHub", "Documentation"]),
                            ],
                            col={"xs": 12, "md": 6},
                        ),
                    ],
                    spacing=14,
                    run_spacing=14,
                ),
            ],
            spacing=20,
        ),
    )


def build_reflection() -> ft.Container:
    return ft.Container(
        key="reflection",
        padding=ft.Padding(24, 32, 24, 32),
        content=ft.Column(
            [
                section_title("Individual Contribution Reflection", "My Semester Reflection"),
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text(
                                        "During the semester, I learned that programming is not only writing code. It also includes understanding requirements, planning screens, testing carefully, documenting progress, and explaining decisions clearly.",
                                        size=16,
                                        color=INK,
                                    ),
                                    ft.Text(
                                        "For MiningChecklistApp, I focused on learning the project structure, supporting the checklist workflow, preparing documentation, and organizing honest evidence that can be replaced with real screenshots from GitHub and the app.",
                                        size=16,
                                        color=INK,
                                    ),
                                    ft.Text("Code Snippet Space", size=20, weight=ft.FontWeight.BOLD, color=NAVY),
                                    ft.Container(
                                        content=ft.Text("// Add a short code snippet here that shows your own contribution.", color="#e6edf7", selectable=True),
                                        bgcolor="#101827",
                                        border_radius=8,
                                        padding=16,
                                    ),
                                ],
                                spacing=14,
                            ),
                            col={"xs": 12, "md": 8},
                        ),
                        ft.Container(
                            key="video",
                            content=ft.Column(
                                [
                                    ft.Icon(ft.Icons.PLAY_CIRCLE, size=54, color=GOLD),
                                    ft.Text("Individual Contribution Video", size=20, weight=ft.FontWeight.BOLD, color=WHITE, text_align=ft.TextAlign.CENTER),
                                    ft.Text("Contribution video link will be added here.", size=16, color="#eef5ff", text_align=ft.TextAlign.CENTER),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            height=260,
                            bgcolor=NAVY,
                            border_radius=8,
                            padding=24,
                            col={"xs": 12, "md": 4},
                        ),
                    ],
                    spacing=18,
                    run_spacing=18,
                ),
                ft.ResponsiveRow(
                    [
                        card(
                            [
                                ft.Text("Design / Mockup Evidence", size=18, weight=ft.FontWeight.BOLD, color=NAVY),
                                ft.Text("Add design notes, screen planning, workflow sketches, or interface decisions here.", color=MUTED),
                            ],
                            col={"xs": 12, "md": 6},
                        ),
                        card(
                            [
                                ft.Text("Documentation Evidence", size=18, weight=ft.FontWeight.BOLD, color=NAVY),
                                ft.Text("Add links or screenshots showing documentation, testing notes, or presentation preparation.", color=MUTED),
                            ],
                            col={"xs": 12, "md": 6},
                        ),
                    ],
                    spacing=14,
                    run_spacing=14,
                ),
            ],
            spacing=20,
        ),
    )


def build_evidence() -> ft.Container:
    return ft.Container(
        key="evidence",
        bgcolor=SURFACE,
        padding=ft.Padding(24, 32, 24, 32),
        content=ft.Column(
            [
                section_title(
                    "Contribution Evidence",
                    "Evidence Gallery",
                    "These are valid PNG placeholders. Replace them with accurate screenshots when final project evidence is ready.",
                ),
                ft.ResponsiveRow(
                    [
                        evidence_image("github-commit-history-placeholder.png", "GitHub Commit History", "Replace with real commit history showing actual contribution activity."),
                        evidence_image("github-branch-placeholder.png", "Development Branch", "Replace with a real branch screenshot."),
                        evidence_image("github-pr-placeholder.png", "Pull Request Evidence", "Replace with the real pull request screenshot."),
                        evidence_image("mining-checklist-app-ui-placeholder.png", "MiningChecklistApp UI", "Replace with a screenshot from the running app."),
                        evidence_image("code-contribution-placeholder.png", "Code Contribution", "Replace with code evidence that clearly identifies your work."),
                    ],
                    spacing=14,
                    run_spacing=14,
                ),
            ],
            spacing=20,
        ),
    )


def build_certificates(page: ft.Page) -> ft.Container:
    certificates = certificate_files()
    content: ft.Control
    if certificates:
        content = ft.ResponsiveRow([certificate_card(path, page) for path in certificates], spacing=14, run_spacing=14)
    else:
        content = card([ft.Text("No certificates found yet.", size=18, weight=ft.FontWeight.BOLD, color=NAVY), ft.Text("Add PDF or image files to the Certificates folder and restart the app.", color=MUTED)], col=12)

    return ft.Container(
        key="certificates",
        padding=ft.Padding(24, 32, 24, 32),
        content=ft.Column(
            [
                section_title("Certificates", "MATLAB Learning Evidence", "Certificate cards are scanned automatically from the Certificates folder when the Flet app starts."),
                content,
            ],
            spacing=20,
        ),
    )


def build_learning_and_challenges() -> ft.Container:
    challenges = [
        ("Understanding requirements", "I broke assignment requirements into sections, evidence items, and presentation tasks."),
        ("Debugging errors", "I practiced reading errors carefully, checking imports and paths, and testing after each change."),
        ("UI responsiveness", "I used responsive rows, wrapping controls, readable spacing, and cards for desktop and mobile layouts."),
        ("Git workflow", "I used normal branches and commits without fabricating history or timestamps."),
        ("Time management", "I organized the work into focused sections that can be completed and checked."),
        ("Testing/demo preparation", "I prepared screenshot and demo checklists so the final presentation can be verified."),
    ]
    return ft.Container(
        key="learning",
        bgcolor=SURFACE,
        padding=ft.Padding(24, 32, 24, 32),
        content=ft.Column(
            [
                section_title("Skills and Learning Outcomes", "What I Learned"),
                tag_list(["Programming fundamentals", "Problem solving", "Git/GitHub workflow", "UI design", "Debugging", "Documentation", "Team collaboration", "Presentation preparation"]),
                section_title("Challenges and Solutions", "How I Addressed Project Challenges"),
                ft.ResponsiveRow(
                    [
                        card(
                            [
                                ft.Text(title, size=18, weight=ft.FontWeight.BOLD, color=NAVY),
                                ft.Text(body, size=14, color=MUTED),
                            ],
                            col={"xs": 12, "md": 6},
                        )
                        for title, body in challenges
                    ],
                    spacing=14,
                    run_spacing=14,
                ),
            ],
            spacing=22,
        ),
    )


def build_footer() -> ft.Container:
    return ft.Container(
        key="contact",
        bgcolor=NAVY_DARK,
        padding=ft.Padding(24, 36, 24, 36),
        content=ft.ResponsiveRow(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Contact", size=26, weight=ft.FontWeight.BOLD, color=GOLD),
                            ft.Text("Email: lahyanakashimba038@gmail.com", color=WHITE, selectable=True),
                            ft.Text("GitHub: github.com/lahyanakashimba/FletPortfolio", color=WHITE, selectable=True),
                        ],
                        spacing=8,
                    ),
                    col={"xs": 12, "md": 7},
                ),
                ft.Container(
                    content=ft.Text("Computer Programming I Portfolio Showcase 2026", color="#eef5ff", text_align=ft.TextAlign.RIGHT),
                    col={"xs": 12, "md": 5},
                ),
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=12,
            run_spacing=12,
        ),
    )


def main(page: ft.Page):
    page.title = "Lahya Nakashimba | Computer Programming I Portfolio Showcase"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = WHITE
    page.scroll = ft.ScrollMode.AUTO
    page.window.width = 1120
    page.window.height = 860
    page.padding = 0

    logo_src = ensure_logo_placeholder()

    page.add(
        ft.Container(
            content=ft.Column(
                [
                    build_header(page, logo_src),
                    build_hero(page, logo_src),
                    build_about(),
                    build_project(),
                    build_reflection(),
                    build_evidence(),
                    build_certificates(page),
                    build_learning_and_challenges(),
                    build_footer(),
                ],
                spacing=0,
                tight=True,
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            ),
            bgcolor=WHITE,
            alignment=ft.Alignment(0, -1),
        )
    )


if __name__ == "__main__":
    ft.run(main, assets_dir=".")
