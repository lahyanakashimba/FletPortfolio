from pathlib import Path
import traceback
from urllib.parse import quote

import flet as ft


ROOT = Path(__file__).resolve().parent
CERTIFICATES_DIR = ROOT / "Certificates"
LOGOS_DIR = ROOT / "assets" / "logos"
VIDEO_DIR = ROOT / "assets" / "videos"
CONTRIBUTION_VIDEO = VIDEO_DIR / "contribution-video.mp4"

NAVY = "#002F6C"
NAVY_DARK = "#001D43"
BLUE = "#0F5EA8"
GOLD = "#BFA046"
GOLD_DARK = "#9A7A20"
WHITE = "#FFFFFF"
CREAM = "#FFFDF5"
PAGE_BG = "#F5F7FB"
SOFT_BLUE = "#EFF6FF"
INK = "#111827"
MUTED = "#4B5563"
LINE = "#E5E7EB"


def log_startup(message: str):
    print(message, flush=True)


def ensure_logo() -> str:
    return "logos/unam-logo.jpeg"


def border_all(width: int | float, color: str) -> ft.Border:
    side = ft.BorderSide(width, color)
    return ft.Border(left=side, top=side, right=side, bottom=side)


def asset_certificate_path(path: Path) -> str:
    return f"certificates/{quote(path.name)}"


def asset_video_path(path: Path) -> str:
    return f"videos/{quote(path.name)}"


def certificate_files() -> list[Path]:
    supported = {".pdf", ".png", ".jpg", ".jpeg", ".webp"}
    if not CERTIFICATES_DIR.exists():
        return []
    return sorted(
        [path for path in CERTIFICATES_DIR.iterdir() if path.is_file() and path.suffix.lower() in supported],
        key=lambda path: path.name.lower(),
    )


def display_name(path: Path) -> str:
    return path.stem.replace("_", " ").replace("-", " ").strip()


def scroll_button(page: ft.Page, label: str, target: str, color: str = NAVY) -> ft.TextButton:
    return ft.TextButton(
        label,
        style=ft.ButtonStyle(
            color=color,
            padding=ft.Padding(8, 6, 8, 6),
        ),
        on_click=lambda _: page.scroll_to(key=target, duration=450),
    )


def section(content: list[ft.Control], key: str | None = None, bgcolor: str = PAGE_BG) -> ft.Container:
    return ft.Container(
        key=key,
        bgcolor=bgcolor,
        padding=ft.Padding(12, 42, 12, 42),
        content=ft.Container(
            content=ft.Column(content, spacing=18, tight=True),
        ),
        alignment=ft.Alignment(0, -1),
    )


def title_block(eyebrow: str, title: str, subtitle: str | None = None) -> ft.Column:
    controls: list[ft.Control] = [
        ft.Text(eyebrow.upper(), size=12, weight=ft.FontWeight.BOLD, color=BLUE),
        ft.Text(title, size=30, weight=ft.FontWeight.BOLD, color=NAVY_DARK),
    ]
    if subtitle:
        controls.append(ft.Text(subtitle, size=16, color=MUTED))
    return ft.Column(controls, spacing=5, tight=True)


def pill(text: str) -> ft.Container:
    return ft.Container(
        content=ft.Text(text, size=13, weight=ft.FontWeight.BOLD, color=NAVY),
        bgcolor="#F8FBFF",
        border=border_all(1, "#D7E3F5"),
        border_radius=24,
        padding=ft.Padding(12, 7, 12, 7),
    )


def bullet_list(items: list[str]) -> ft.Column:
    rows: list[ft.Control] = []
    for item in items:
        rows.append(
            ft.Row(
                [
                    ft.Container(width=8, height=8, bgcolor=GOLD, border_radius=20),
                    ft.Text(item, size=15, color=INK),
                ],
                spacing=10,
                vertical_alignment=ft.CrossAxisAlignment.START,
            )
        )
    return ft.Column(rows, spacing=8, tight=True)


def simple_card(title: str, body: str, icon=ft.Icons.DESCRIPTION, col=None) -> ft.Container:
    return ft.Container(
        col=col or {"xs": 12, "sm": 12, "md": 6, "lg": 4},
        bgcolor=WHITE,
        border=border_all(1, LINE),
        border_radius=8,
        padding=18,
        shadow=ft.BoxShadow(blur_radius=18, color="#1F3A5F10", offset=ft.Offset(0, 8)),
        content=ft.Column(
            [
                ft.Icon(icon, color=GOLD, size=28),
                ft.Text(title, size=19, weight=ft.FontWeight.BOLD, color=NAVY),
                ft.Text(body, size=14, color=MUTED),
            ],
            spacing=9,
            tight=True,
        ),
    )


def card_row(cards: list[ft.Control]) -> ft.Row:
    return ft.ResponsiveRow(cards, spacing=16, run_spacing=16)


def evidence_card(filename: str, title: str, caption: str) -> ft.Container:
    return ft.Container(
        col={"xs": 12, "sm": 12, "md": 6, "lg": 4},
        bgcolor=WHITE,
        border=border_all(1, LINE),
        border_radius=8,
        padding=14,
        shadow=ft.BoxShadow(blur_radius=16, color="#1F3A5F0F", offset=ft.Offset(0, 7)),
        content=ft.Column(
            [
                ft.Image(
                    src=f"screenshots/{filename}",
                    height=180,
                    fit=ft.BoxFit.COVER,
                    border_radius=8,
                    semantics_label=title,
                    error_content=ft.Container(
                        height=150,
                        bgcolor=SOFT_BLUE,
                        border_radius=8,
                        alignment=ft.Alignment(0, 0),
                        content=ft.Text("Evidence image unavailable", color=NAVY, weight=ft.FontWeight.BOLD),
                    ),
                ),
                ft.Text(title, size=18, weight=ft.FontWeight.BOLD, color=NAVY),
                ft.Text(caption, size=13, color=MUTED),
            ],
            spacing=10,
            tight=True,
        ),
    )


def certificate_card(path: Path, page: ft.Page) -> ft.Container:
    kind = "PDF certificate" if path.suffix.lower() == ".pdf" else "Image certificate"
    href = asset_certificate_path(path)

    def open_file(_):
        page.launch_url(href)

    return ft.Container(
        col={"xs": 12, "sm": 12, "md": 6, "lg": 4},
        bgcolor=WHITE,
        border=border_all(1, LINE),
        border_radius=8,
        padding=16,
        shadow=ft.BoxShadow(blur_radius=14, color="#1F3A5F0D", offset=ft.Offset(0, 6)),
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(
                            width=44,
                            height=44,
                            bgcolor=SOFT_BLUE,
                            border_radius=8,
                            alignment=ft.Alignment(0, 0),
                            content=ft.Icon(ft.Icons.WORKSPACE_PREMIUM, color=GOLD_DARK, size=28),
                        ),
                        ft.Column(
                            [
                                ft.Text(display_name(path), size=16, weight=ft.FontWeight.BOLD, color=NAVY),
                                ft.Text(kind, size=13, color=MUTED),
                            ],
                            spacing=2,
                            tight=True,
                        ),
                    ],
                    spacing=12,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                ),
                ft.Row(
                    [
                        ft.Button("Open", icon=ft.Icons.OPEN_IN_NEW, bgcolor=NAVY, color=WHITE, on_click=open_file),
                        ft.Button("View file", icon=ft.Icons.FOLDER_OPEN, bgcolor=CREAM, color=NAVY, on_click=open_file),
                    ],
                    wrap=True,
                    spacing=8,
                ),
            ],
            spacing=14,
            tight=True,
        ),
    )


def contribution_video_card(page: ft.Page) -> ft.Container:
    if CONTRIBUTION_VIDEO.exists():
        href = asset_video_path(CONTRIBUTION_VIDEO)

        def open_video(_):
            page.launch_url(href)

        return ft.Container(
            col={"xs": 12, "sm": 12, "md": 4},
            bgcolor=WHITE,
            border=border_all(1, LINE),
            border_radius=8,
            padding=20,
            content=ft.Column(
                [
                    ft.Icon(ft.Icons.PLAY_CIRCLE, size=44, color=GOLD),
                    ft.Text("Individual Contribution Video", size=18, weight=ft.FontWeight.BOLD, color=NAVY, text_align=ft.TextAlign.CENTER),
                    ft.Text(
                        "Play the recorded contribution video from the app assets.",
                        size=14,
                        color=MUTED,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Button("Open Video", icon=ft.Icons.PLAY_CIRCLE_OUTLINE, bgcolor=NAVY, color=WHITE, on_click=open_video),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        padding=ft.Padding(0, 10, 0, 0),
                    ),
                ],
                spacing=14,
                tight=True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    return ft.Container(
        col={"xs": 12, "sm": 12, "md": 4},
        bgcolor=WHITE,
        border=border_all(1, LINE),
        border_radius=8,
        padding=20,
        content=ft.Column(
            [
                ft.Icon(ft.Icons.WARNING_AMBER, size=44, color=GOLD),
                ft.Text("Contribution Video Missing", size=18, weight=ft.FontWeight.BOLD, color=NAVY, text_align=ft.TextAlign.CENTER),
                ft.Text(
                    "Add assets/videos/contribution-video.mp4 and restart the app to enable playback.",
                    size=14,
                    color=MUTED,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            spacing=14,
            tight=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )


def navbar(page: ft.Page, logo_src: str) -> ft.Container:
    return ft.Container(
        key="top",
        bgcolor=WHITE,
        border=ft.Border(bottom=ft.BorderSide(1, LINE)),
        padding=ft.Padding(16, 13, 16, 13),
        content=ft.ResponsiveRow(
            [
                ft.Container(
                    col={"xs": 12, "sm": 12, "md": 4},
                    content=ft.Row(
                        [
                            ft.Image(src=logo_src, width=42, height=42, fit=ft.BoxFit.CONTAIN, semantics_label="UNAM logo"),
                            ft.Text("Lahya Nakashimba", size=18, weight=ft.FontWeight.BOLD, color=NAVY_DARK),
                        ],
                        spacing=10,
                    ),
                ),
                ft.Container(
                    col={"xs": 12, "sm": 12, "md": 8},
                    content=ft.Row(
                        [
                            scroll_button(page, "Home", "top"),
                            scroll_button(page, "Project", "project"),
                            scroll_button(page, "Contributions", "contribution"),
                            scroll_button(page, "Certificates", "certificates"),
                            scroll_button(page, "Evidence", "evidence"),
                            scroll_button(page, "Contact", "contact"),
                        ],
                        wrap=True,
                        spacing=2,
                        run_spacing=2,
                        alignment=ft.MainAxisAlignment.START,
                    ),
                ),
            ],
            spacing=12,
            run_spacing=6,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )


def hero(page: ft.Page, logo_src: str) -> ft.Container:
    visual = ft.Container(
        col={"xs": 12, "sm": 12, "md": 5},
        bgcolor=WHITE,
        border=border_all(1, "#E6EDF7"),
        border_radius=8,
        padding=18,
        content=ft.Column(
            [
                ft.Image(src=logo_src, height=88, fit=ft.BoxFit.CONTAIN, semantics_label="UNAM logo"),
                ft.Container(content=ft.Text("MiningChecklistApp Contribution Portfolio", color=NAVY, weight=ft.FontWeight.BOLD), bgcolor=SOFT_BLUE, padding=12, border_radius=8),
                ft.Container(content=ft.Text("Reflection, evidence, certificates, and learning outcomes", color=INK), bgcolor=CREAM, padding=12, border_radius=8),
                ft.Container(content=ft.Text("Prepared for Computer Programming I", color=INK), bgcolor="#F9FAFB", padding=12, border_radius=8),
            ],
            spacing=10,
            tight=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    return section(
        [
            ft.Container(
                bgcolor=CREAM,
                border_radius=8,
                border=border_all(1, "#E8DDBF"),
                padding=ft.Padding(18, 32, 18, 32),
                shadow=ft.BoxShadow(blur_radius=24, color="#1F3A5F18", offset=ft.Offset(0, 10)),
                content=ft.ResponsiveRow(
                    [
                        ft.Container(
                            col={"xs": 12, "sm": 12, "md": 7},
                            content=ft.Column(
                                [
                                    ft.Text("UNIVERSITY OF NAMIBIA | COMPUTER PROGRAMMING I", size=13, color=GOLD_DARK, weight=ft.FontWeight.BOLD),
                                    ft.Text("Lahya Nakashimba", size=38, weight=ft.FontWeight.BOLD, color=NAVY_DARK),
                                    ft.Text("Computer Programming I Portfolio Showcase", size=23, weight=ft.FontWeight.BOLD, color=NAVY),
                                    ft.Text("MiningChecklistApp Contribution Portfolio", size=18, weight=ft.FontWeight.BOLD, color=GOLD_DARK),
                                    ft.Text(
                                        "A professional Flet portfolio presenting my semester project contribution, reflection, learning evidence, challenges, certificates, and contribution records.",
                                        size=16,
                                        color=MUTED,
                                    ),
                                    ft.Row(
                                        [
                                            ft.Button("View Contribution", icon=ft.Icons.WORK, bgcolor=NAVY, color=WHITE, on_click=lambda _: page.scroll_to(key="contribution", duration=450)),
                                            ft.Button("View Certificates", icon=ft.Icons.WORKSPACE_PREMIUM, bgcolor=WHITE, color=NAVY, on_click=lambda _: page.scroll_to(key="certificates", duration=450)),
                                            ft.Button("View Evidence", icon=ft.Icons.IMAGE, bgcolor="#F3EBD1", color=NAVY_DARK, on_click=lambda _: page.scroll_to(key="evidence", duration=450)),
                                        ],
                                        wrap=True,
                                        spacing=10,
                                    ),
                                ],
                                spacing=12,
                                tight=True,
                            ),
                        ),
                        visual,
                    ],
                    spacing=28,
                    run_spacing=18,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                ),
            )
        ],
        key="home",
        bgcolor=PAGE_BG,
    )


def about_section() -> ft.Container:
    return section(
        [
            title_block("About Me", "Student Profile", "A clear academic portfolio for Computer Programming I."),
            ft.ResponsiveRow(
                [
                    ft.Container(
                        col={"xs": 12, "sm": 12, "md": 7},
                        content=ft.Column(
                            [
                                ft.Text(
                                    "I am Lahya Nakashimba, a Computer Programming I student building practical programming skills through project work, testing, documentation, and presentation preparation.",
                                    size=16,
                                    color=INK,
                                ),
                                ft.Text(
                                    "This portfolio identifies my work honestly and presents organised areas for GitHub screenshots, code evidence, design notes, and final video evidence.",
                                    size=16,
                                    color=INK,
                                ),
                            ],
                            spacing=10,
                            tight=True,
                        ),
                    ),
                    simple_card(
                        "Academic Context",
                        "Course: Computer Programming I\nInstitution: University of Namibia\nPortfolio year: 2026",
                        ft.Icons.SCHOOL,
                        col={"xs": 12, "sm": 12, "md": 5},
                    ),
                ],
                spacing=18,
                run_spacing=18,
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
        ],
        key="about",
        bgcolor=WHITE,
    )


def project_section() -> ft.Container:
    cards = [
        simple_card("Project Overview", "MiningChecklistApp supports mining safety checks through a mobile checklist workflow.", ft.Icons.APPS),
        simple_card("Problem Solved", "Digital checklists improve consistency, record keeping, and supervisor visibility.", ft.Icons.TASK_ALT),
        simple_card("Key Features", "Worker checklist submission, supervisor review, Firebase storage concept, and mobile-first interface.", ft.Icons.FEATURED_PLAY_LIST),
        simple_card("Technologies Used", "React Native, Expo, Firebase, JavaScript, GitHub, and documentation.", ft.Icons.CODE),
    ]
    return section(
        [
            title_block("Semester Project", "MiningChecklistApp", "My semester project contribution area."),
            card_row(cards),
        ],
        key="project",
        bgcolor=PAGE_BG,
    )


def contribution_section(page: ft.Page) -> ft.Container:
    return section(
        [
            title_block("Individual Contribution", "Contribution Reflection", "Written in an honest student style without overclaiming."),
            ft.ResponsiveRow(
                [
                    ft.Container(
                        col={"xs": 12, "sm": 12, "md": 8},
                        bgcolor=WHITE,
                        border=border_all(1, LINE),
                        border_radius=8,
                        padding=20,
                        shadow=ft.BoxShadow(blur_radius=16, color="#1F3A5F12", offset=ft.Offset(0, 7)),
                        content=ft.Column(
                            [
                                ft.Text(
                                    "During the semester, I learned that programming includes understanding requirements, planning screens, testing carefully, documenting progress, and explaining technical decisions clearly.",
                                    size=16,
                                    color=INK,
                                ),
                                ft.Text(
                                    "For MiningChecklistApp, my contribution evidence focuses on understanding the checklist workflow, supporting documentation, preparing testing notes, and organising accurate project records.",
                                    size=16,
                                    color=INK,
                                ),
                                ft.Text("Code Snippet Space", size=19, weight=ft.FontWeight.BOLD, color=NAVY),
                                ft.Container(
                                    bgcolor="#101827",
                                    border_radius=8,
                                    padding=14,
                                    content=ft.Text("Contribution code sample area prepared for the final project submission.", color="#E6EDF7", selectable=True),
                                ),
                            ],
                            spacing=12,
                            tight=True,
                        ),
                    ),
                    contribution_video_card(page),
                ],
                spacing=18,
                run_spacing=18,
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
            card_row(
                [
                    simple_card("Design / Mockup Evidence", "Screen planning, workflow sketches, and interface decisions for the project.", ft.Icons.DRAW),
                    simple_card("Documentation Evidence", "Testing notes, README updates, and presentation preparation evidence.", ft.Icons.ARTICLE),
                    simple_card("Lessons Learned", "Requirements, Git workflow, debugging, documentation, and presentation preparation.", ft.Icons.LIGHTBULB),
                ]
            ),
        ],
        key="contribution",
        bgcolor=WHITE,
    )


def evidence_section() -> ft.Container:
    # MAINTAINER NOTE:
    # To update evidence images, replace the PNG files in assets/screenshots/
    # using the same filenames. The public UI labels below are intentionally
    # polished and should not contain "replace with..." instructions.
    return section(
        [
            title_block("Evidence Gallery", "Contribution Evidence", "Evidence assets are presented as compact portfolio cards."),
            card_row(
                [
                    evidence_card("github-commit-history-placeholder.png", "Commit History Asset", "A visual record of portfolio and contribution development activity."),
                    evidence_card("github-branch-placeholder.png", "Development Branch Asset", "Branch workflow evidence showing organised project development."),
                    evidence_card("github-pr-placeholder.png", "Pull Request Evidence Asset", "Pull request evidence showing review-ready contribution work."),
                    evidence_card("mining-checklist-app-ui-placeholder.png", "MiningChecklistApp Interface Asset", "Application interface evidence from the semester project."),
                    evidence_card("code-contribution-placeholder.png", "Code Contribution Asset", "Source code evidence connected to the student's project contribution."),
                ]
            ),
        ],
        key="evidence",
        bgcolor=PAGE_BG,
    )


def certificates_section(page: ft.Page) -> ft.Container:
    certs = certificate_files()
    cards = [certificate_card(path, page) for path in certs]
    if not cards:
        cards = [simple_card("No certificates found", "Add PDF or image files to the Certificates folder and restart the app.", ft.Icons.WORKSPACE_PREMIUM)]
    return section(
        [
            title_block("Certificates", "MATLAB Learning Evidence", "PDF files are shown as compact cards, not embedded grey preview panels."),
            card_row(cards),
        ],
        key="certificates",
        bgcolor=WHITE,
    )


def learning_section() -> ft.Container:
    outcomes = [
        "Programming fundamentals",
        "Problem solving",
        "Git/GitHub workflow",
        "UI design",
        "Debugging",
        "Documentation",
        "Team collaboration",
        "Presentation preparation",
    ]
    challenges = [
        simple_card("Understanding Requirements", "I broke broad assignment requirements into portfolio sections and evidence tasks.", ft.Icons.LIST_ALT),
        simple_card("Debugging Errors", "I checked imports, paths, and runtime behavior after each meaningful change.", ft.Icons.BUG_REPORT),
        simple_card("UI Responsiveness", "I used wrapped rows, compact cards, and controlled image heights.", ft.Icons.DEVICES),
        simple_card("Git Workflow", "I used normal development branches and commits without fake timestamps.", ft.Icons.ACCOUNT_TREE),
        simple_card("Time Management", "I organized tasks into sections that can be completed and checked.", ft.Icons.SCHEDULE),
        simple_card("Testing/Demo Preparation", "I prepared manual QA notes and evidence assets for final review.", ft.Icons.CHECK_CIRCLE),
    ]
    return section(
        [
            title_block("Learning Outcomes", "Skills Developed"),
            ft.Row([pill(item) for item in outcomes], wrap=True, spacing=9, run_spacing=9),
            title_block("Challenges", "Challenges and Solutions"),
            card_row(challenges),
        ],
        key="learning",
        bgcolor=PAGE_BG,
    )


def footer() -> ft.Container:
    return ft.Container(
        key="contact",
        bgcolor=NAVY_DARK,
        padding=ft.Padding(20, 34, 20, 34),
        alignment=ft.Alignment(0, -1),
        content=ft.Row(
            [
                ft.Column(
                    [
                        ft.Text("Contact", size=26, weight=ft.FontWeight.BOLD, color=GOLD),
                        ft.Text("Email: lahyanakashimba038@gmail.com", color=WHITE, selectable=True),
                        ft.Text("GitHub: github.com/lahyanakashimba/FletPortfolio", color=WHITE, selectable=True),
                    ],
                    spacing=7,
                    tight=True,
                ),
                ft.Text("Computer Programming I Portfolio Showcase 2026", color="#EAF2FF"),
            ],
            wrap=True,
            spacing=24,
            run_spacing=16,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )


def main(page: ft.Page):
    log_startup("[START] main called")
    try:
        page.title = "Lahya Nakashimba | Computer Programming I Portfolio Showcase"
        page.theme_mode = ft.ThemeMode.LIGHT
        page.bgcolor = PAGE_BG
        page.scroll = ft.ScrollMode.AUTO
        page.padding = 0
        page.spacing = 0
        page.window.width = 1180
        page.window.height = 860

        log_startup("[STEP] loading assets")
        logo_src = ensure_logo()

        log_startup("[STEP] scanning certificates")
        cert_section = certificates_section(page)

        log_startup("[STEP] building page sections")
        controls = [
            navbar(page, logo_src),
            hero(page, logo_src),
            about_section(),
            project_section(),
            contribution_section(page),
            evidence_section(),
            cert_section,
            learning_section(),
            footer(),
        ]

        log_startup("[STEP] adding controls to page")
        page.controls.clear()
        page.add(
            ft.Column(
                controls,
                spacing=0,
                tight=True,
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            )
        )
        page.update()
        log_startup("[DONE] page rendered")
    except Exception as exc:
        log_startup(f"[FATAL] Portfolio failed to render: {exc!r}")
        error_details = traceback.format_exc()
        print(error_details, flush=True)
        page.controls.clear()
        page.add(
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Portfolio failed to load", size=28, weight=ft.FontWeight.BOLD, color=NAVY_DARK),
                        ft.Text(str(exc), selectable=True, color=INK),
                        ft.Text(error_details, selectable=True, color=MUTED, size=12),
                    ],
                    spacing=12,
                ),
                padding=30,
                bgcolor=WHITE,
            )
        )
        page.update()


if __name__ == "__main__":
    ft.run(main, assets_dir="assets", web_renderer=ft.WebRenderer.CANVAS_KIT, no_cdn=True)
