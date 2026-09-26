"""Generate the original SVG artwork using only the Python standard library."""

from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "assets" / "profile"
SANS = "Arial, Helvetica, sans-serif"
MONO = "'Courier New', monospace"


def text(x, y, value, size=24, color="#fff", weight=400, family=SANS, extra=""):
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="{family}" font-size="{size}" font-weight="{weight}" {extra}>{escape(value)}</text>'


def svg(name, width, height, title, content):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title">\n'
        f'<title id="title">{escape(title)}</title>\n{content}\n</svg>\n'
    )


def header(dark):
    bg, fg, muted, grid = (
        ("#10121e", "#f9f6ee", "#b6bbd1", "#222637") if dark
        else ("#f7f3e9", "#191c2b", "#535a70", "#e9e3d7")
    )
    accent = "#d8f46a" if dark else "#4255ff"
    parts = [f'<rect width="1280" height="500" rx="24" fill="{bg}"/>']
    for x in range(780, 1260, 32):
        for y in range(40, 450, 32):
            parts.append(f'<circle cx="{x}" cy="{y}" r="1.5" fill="{grid}"/>')
    parts.extend([
        '<path d="M852 365C785 304 801 196 902 151C1003 106 1185 147 1203 252C1221 357 1100 422 993 384" fill="none" stroke="#ff795e" stroke-width="3"/>',
        '<rect x="902" y="105" width="250" height="250" rx="48" fill="#4255ff" transform="rotate(-12 1027 230)"/>',
        '<rect x="922" y="125" width="210" height="210" rx="35" fill="none" stroke="#8290ff" stroke-width="1.5" transform="rotate(-12 1027 230)"/>',
        '<path d="M997 183L958 221L997 259M1052 172L1091 210L1052 248M1034 169L1014 263" fill="none" stroke="#f7f3e9" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" transform="rotate(-12 1027 220)"/>',
        '<circle cx="1157" cy="137" r="38" fill="#d8f46a"/>',
        '<path d="M1142 137h30m-15-15v30" stroke="#1b2330" stroke-width="4" stroke-linecap="round"/>',
        '<rect x="817" y="316" width="122" height="84" rx="20" fill="#ff795e" transform="rotate(9 878 358)"/>',
        '<path d="M846 360l11-13 12 26 14-37 13 23 13-9" fill="none" stroke="#1b2330" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>',
        text(51, 62, "YS / BUILDER'S LOG", 19, muted, 700, MONO, 'letter-spacing="2"'),
        text(50, 170, "Yusef Syed.", 102, fg, 700, extra='letter-spacing="-6"'),
        text(55, 242, "Building useful things.", 39, fg, 700, extra='letter-spacing="-1"'),
        text(55, 291, "Testing the edges.", 39, fg, 700, extra='letter-spacing="-1"'),
        f'<path d="M56 319h320" stroke="{accent}" stroke-width="5"/>',
        text(55, 374, "AI evaluation / apps / developer tools", 22, muted, family=MONO),
        f'<path d="M50 421h1180" stroke="{grid}" stroke-width="2"/>',
        text(55, 461, "UNIVERSITY OF TORONTO", 18, muted, 700, MONO, 'letter-spacing="1.5"'),
        text(890, 461, "CURIOUS. BUILDING. ITERATING.", 16, muted, family=MONO),
    ])
    svg(f'header-{"dark" if dark else "light"}.svg', 1280, 500,
        "Yusef Syed — building useful things, testing the edges", "\n".join(parts))


def card(name, bg, fg, secondary, tag, title_lines, description, stack, motif):
    parts = [f'<rect x="1" y="1" width="718" height="318" rx="24" fill="{bg}" stroke="{fg}" stroke-opacity=".12" stroke-width="2"/>',
             text(32, 42, tag, 17, fg, 700, MONO, 'letter-spacing="2"'),
             '<path d="M658 39h27v27m-28 1 27-27" fill="none" stroke="' + fg + '" stroke-width="3"/>']
    for i, line in enumerate(title_lines):
        parts.append(text(32, 108 + i * 49, line, 46, fg, 700, extra='letter-spacing="-1.6"'))
    parts.extend([
        text(32, 221, description, 25, fg),
        f'<path d="M32 252h656" stroke="{fg}" stroke-opacity=".20"/>',
        text(32, 287, stack, 19, secondary, 700, MONO),
    ])
    if motif == "lab":
        parts.append(f'<g fill="none" stroke="{fg}" stroke-width="3"><rect x="590" y="84" width="35" height="35" rx="6"/><rect x="640" y="134" width="35" height="35" rx="6"/><path d="M608 119v34h32M625 102h32v32"/></g>')
    elif motif == "watch":
        parts.append(f'<g fill="none" stroke="{fg}" stroke-width="3"><path d="M617 75v17m36-17v17m-36 66v17m36-17v17"/><rect x="601" y="92" width="67" height="66" rx="19"/><path d="M613 125h8l6-15 10 29 8-18 7 4h5" stroke-linejoin="round"/></g>')
    elif motif == "shirt":
        parts.append(f'<path d="M612 94l-24 21 17 18 12-10v47h44v-47l12 10 17-18-25-21-13 8h-27z" fill="none" stroke="{fg}" stroke-width="3" stroke-linejoin="round"/>')
    elif motif == "proof":
        parts.append(f'<g fill="none" stroke="{fg}" stroke-width="3"><rect x="596" y="90" width="89" height="72" rx="10"/><path d="M610 110l13 12-13 12m23 0h14m10 10 8 8 14-17" stroke-linejoin="round" stroke-linecap="round"/></g>')
    svg(name + ".svg", 720, 336, " — ".join([" ".join(title_lines), description, stack]), "\n".join(parts))


def mobile_header(dark):
    bg, fg, muted = ("#10121e", "#f9f6ee", "#b6bbd1") if dark else ("#f7f3e9", "#191c2b", "#535a70")
    parts = [
        f'<rect width="720" height="370" rx="24" fill="{bg}"/>',
        text(32, 47, "YS / BUILDER'S LOG", 19, muted, 700, MONO),
        text(29, 136, "Yusef Syed.", 72, fg, 700, extra='letter-spacing="-4"'),
        text(32, 207, "Building useful things.", 32, fg, 700, extra='letter-spacing="-1"'),
        text(32, 253, "Testing the edges.", 32, fg, 700, extra='letter-spacing="-1"'),
        '<path d="M33 282h245" stroke="#4255ff" stroke-width="4"/>',
        text(32, 329, "AI EVALUATION / APPS / DEV TOOLS", 20, muted, 700, MONO),
        '<circle cx="571" cy="195" r="97" fill="none" stroke="#ff795e" stroke-width="2"/>',
        '<rect x="501" y="116" width="143" height="143" rx="30" fill="#4255ff" transform="rotate(-12 572 187)"/>',
        '<path d="M548 165l-22 22 22 22m46-44 22 22-22 22m-15-58-15 72" fill="none" stroke="#f7f3e9" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>',
        '<circle cx="644" cy="129" r="25" fill="#d8f46a"/>',
        '<path d="M634 129h20m-10-10v20" stroke="#202a27" stroke-width="3"/>',
    ]
    svg(f'header-mobile-{"dark" if dark else "light"}.svg', 720, 370,
        "Yusef Syed — building useful things, testing the edges", "\n".join(parts))


if __name__ == "__main__":
    header(False)
    header(True)
    mobile_header(False)
    mobile_header(True)
    card("eval-lab", "#4255ff", "#fffaf0", "#e0e4ff", "01 / EVALUATION", ["Agent Eval", "Mutation Lab"], "What did the agent actually do?", "PYTHON / INSPECT / SQLITE", "lab")
    card("providence", "#ff795e", "#211d2a", "#3c2831", "02 / HACK THE NORTH", ["Providence"], "Your wrist. Your voice. Your Mac.", "MY WATCH CLIENT / SWIFTUI", "watch")
    card("tiraz", "#d8f46a", "#202a27", "#344134", "03 / MACHINE LEARNING", ["Tiraz", "Garment Completion"], "Prediction meets uncertainty.", "PYTORCH / ANNOTATION-ONLY STUDY", "shirt")
    card("agent-proof", "#222639", "#f9f6ee", "#c1c8e1", "04 / DEVELOPER TOOLS", ["Agent Proof"], "Run the checks. Keep the evidence.", "TYPESCRIPT / NODE.JS / CLI", "proof")
