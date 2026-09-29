"""Build the profile's local SVGs. Python standard library only."""
from html import escape
from pathlib import Path
import textwrap

OUT = Path(__file__).resolve().parents[1] / 'assets' / 'profile'
CYAN, PANEL, WHITE, MUTED = '#5cdeff', '#142431', '#edf6fc', '#aec4d4'
SANS, MONO = 'Arial, Helvetica, sans-serif', "Menlo, Consolas, monospace"


def text(x, y, content, size=24, color=WHITE, weight=400, family=SANS, extra=''):
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-family="{family}" font-weight="{weight}" {extra}>{escape(content)}</text>'


def write(name, width, height, title, body):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / (name + '.svg')).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title>\n{body}\n</svg>\n')


def university_emblem(color, animated):
    """Original oak-and-book student crest, drawn as small monospaced strokes."""
    # Keep paths grouped by drawing phase: silhouette, oak, then book and initials.
    paths = [
        ('outline', 'M10 31H74V56C74 76 60 89 42 99C24 89 10 76 10 56Z'),
        ('detail', 'M15 36H69V56C69 72 58 83 42 93C26 83 15 72 15 56Z'),
        ('oak', 'M42 28V9M42 21L32 13M42 17L52 9M42 26L54 19M42 27L28 20'),
        ('oak', 'M42 10C33 7 36 1 42 0C48 1 51 7 42 10Z'),
        ('oak', 'M32 14C24 16 20 10 23 6C29 4 35 7 32 14Z'),
        ('oak', 'M51 11C49 3 55 0 60 3C62 9 57 14 51 11Z'),
        ('oak', 'M29 21C20 25 15 21 16 16C21 12 28 14 29 21Z'),
        ('oak', 'M54 20C55 12 62 11 66 15C66 21 60 25 54 20Z'),
        ('detail', 'M34 28H50M21 43H63'),
        ('book', 'M42 55C35 50 28 50 22 52V70C29 68 36 69 42 73C48 69 55 68 62 70V52C56 50 49 50 42 55ZM42 55V73'),
        ('book', 'M27 57C31 56 35 57 38 59M27 62C31 61 35 62 38 64M46 59C49 57 53 56 57 57M46 64C49 62 53 61 57 62'),
        ('initials', 'M32 79V83C32 88 39 88 39 83V79M46 79H55M50.5 79V87'),
    ]
    body = []
    for phase, path in paths:
        cls = f' class="ink {phase}" pathLength="1"' if animated else ''
        opacity = ' opacity="0.45"' if phase == 'detail' else ''
        body.append(f'<path{cls}{opacity} d="{path}"/>')
    return (f'<g transform="translate(164 12) scale(.82)" fill="none" '
            f'stroke="{color}" stroke-width="1.6" stroke-linecap="round" '
            f'stroke-linejoin="round">' + ''.join(body) + '</g>')


def intro(theme):
    color = CYAN if theme == 'dark' else '#006c87'
    lines = ['Student at the University of Toronto', 'Building apps and developer tools', 'Interested in AI evaluation']
    name = text(258, 63, 'Yusef Syed', 29, color, family=MONO)
    css = ['.still{display:none}',
           '.ink{stroke-dasharray:1;stroke-dashoffset:1;animation:draw 18s steps(24,end) infinite both}',
           '.oak{animation-name:grow}.book{animation-name:book}.initials{animation-name:initials}',
           '.detail{animation-name:detail}',
           '@keyframes draw{0%{stroke-dashoffset:1}12%,94%{stroke-dashoffset:0}100%{stroke-dashoffset:1}}',
           '@keyframes detail{0%,3%{stroke-dashoffset:1}15%,94%{stroke-dashoffset:0}100%{stroke-dashoffset:1}}',
           '@keyframes grow{0%,4%{stroke-dashoffset:1}16%,94%{stroke-dashoffset:0}100%{stroke-dashoffset:1}}',
           '@keyframes book{0%,7%{stroke-dashoffset:1}18%,94%{stroke-dashoffset:0}100%{stroke-dashoffset:1}}',
           '@keyframes initials{0%,12%{stroke-dashoffset:1}19%,94%{stroke-dashoffset:0}100%{stroke-dashoffset:1}}']
    body = [name, '<g class="moving">' + university_emblem(color, True) + '</g>']
    for i, line in enumerate(lines):
        width = len(line) * 14.4 + 3
        start = round((600 - width) / 2, 1)
        css.append(f'@keyframes type{i}{{0%{{width:0}}16%,26%{{width:{width}px}}33.32%,100%{{width:0}}}}')
        css.append(f'#reveal{i}{{width:0;animation:type{i} 18s steps({len(line)},end) {i*6}s infinite both}}')
        body.append(f'<clipPath id="clip{i}"><rect id="reveal{i}" x="{start}" y="119" width="0" height="34"/></clipPath>')
        body.append(f'<g class="moving" clip-path="url(#clip{i})">{text(start, 145, line, 24, color, family=MONO)}</g>')
    css.append('@media(prefers-reduced-motion:reduce){.moving{display:none}.still{display:block}}')
    still = university_emblem(color, False) + text(300, 145, lines[0], 24, color, family=MONO, extra='text-anchor="middle"')
    body.append(f'<g class="still">{still}</g>')
    body.insert(0, '<style>' + ''.join(css) + '</style>')
    write('intro-' + theme, 600, 172,
          'Yusef Syed — University of Toronto student, with an animated oak-and-book student crest', '\n'.join(body))
    write('intro-static-' + theme, 600, 172,
          'Yusef Syed — Student at the University of Toronto, with an oak-and-book student crest', name + still)


def card(name, title, description, language, status, dot='#3572a5'):
    body = [f'<rect x="1" y="1" width="550" height="256" rx="12" fill="{PANEL}" stroke="#294151" stroke-width="2"/><path d="M28 28v24m-5-19 5-5 5 5m-5 14 5 5-5 5" fill="none" stroke="{CYAN}" stroke-width="2"/>', text(47, 48, title, 26, CYAN, 700)]
    lines = textwrap.wrap(description, width=38, break_long_words=False, break_on_hyphens=False)
    assert len(lines) <= 3, (name, lines)
    for i, line in enumerate(lines):
        body.append(text(30, 94 + 31*i, line, 24))
    status_color = '#f4d76d' if status == 'OPEN PR' else '#a9d6b1' if status == 'MERGED PR' else MUTED
    body += [f'<circle cx="37" cy="221" r="9" fill="{dot}"/>', text(57, 228, language, 22), text(520, 228, status, 19, status_color, 700, extra='text-anchor="end"')]
    write(name, 552, 270, f'{title} — {description} {language}. {status}.', '\n'.join(body))


ICONS = {
    'portfolio': '<circle cx="24" cy="22" r="14"/><ellipse cx="24" cy="22" rx="6" ry="14"/><path d="M10 22h28M13 15h22M13 29h22"/>',
    'email': '<rect x="8" y="11" width="32" height="23" rx="3"/><path d="m9 13 15 12 15-12"/>',
    'resume': '<path d="M14 7h15l8 8v23H14zM29 7v9h8M20 23h11M20 29h11"/>',
    'github': '<path d="m17 13-9 9 9 9m14-18 9 9-9 9M27 8l-6 28"/>',
    'linkedin': '<rect x="8" y="6" width="32" height="32" rx="3" fill="currentColor" stroke="none"/><circle cx="16" cy="15" r="2" fill="#142431" stroke="none"/><path d="M16 21v11m8-11v11m0-7c0-7 9-7 9 0v7" stroke="#142431" stroke-width="3.5"/>',
}


def icon(name, label, theme):
    color = CYAN if theme == 'dark' else '#006c87'
    body = f'<g color="{color}" stroke="{color}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" fill="none" transform="translate(12 0)">{ICONS[name]}</g>'
    body += text(36, 56, label, 10, color, 700, MONO, 'text-anchor="middle"')
    write(f'link-{name}-{theme}', 72, 64, label, body)


def button(name, label, color=CYAN):
    width = len(label)*15 + 70
    write(name, width, 58, label, f'<rect width="{width}" height="52" rx="3" fill="{PANEL}"/>' + text(24, 34, '↗', 26, color) + text(58, 33, label, 19, WHITE, 700, MONO, 'letter-spacing="1"'))


if __name__ == '__main__':
    for theme in ['dark', 'light']:
        intro(theme)
        for name, label in [('portfolio','PORTFOLIO'),('linkedin','LINKEDIN'),('email','EMAIL'),('resume','RESUME')]:
            icon(name,label,theme)
    card('eval-lab', 'agent-eval-mutation-lab', 'Tests what agents actually do when tools fail or results are missing.', 'Python', 'PROJECT')
    card('tiraz', 'tiraz-garment-completion', 'A garment-completion experiment with calibration and missing-context tests.', 'Python', 'ML STUDY')
    card('agent-proof', 'agent-proof', 'Runs reviewer-selected checks and saves redacted verification reports.', 'TypeScript', 'CLI', '#3178c6')
    card('callreclaim-webmcp', 'callreclaim-webmcp', 'An agent prepares a missed-call plan. The owner decides. Synthetic demo.', 'TypeScript', 'DEMO', '#3178c6')
    card('shiftproof', 'shiftproof', 'Volunteer scheduling with constraint checks and coordinator approval.', 'Python', 'PROTOTYPE')
    card('providence', 'Providence', 'My Apple Watch client for our voice-controlled Mac assistant at Hack the North.', 'Swift', 'TEAM PROJECT', '#f05138')
    card('oss-lightning', 'microsoft / agent-lightning', 'Fixed a race that could start new rollouts during shutdown.', 'Python', 'MERGED PR')
    card('oss-scout', 'meridianlabs / inspect_scout', 'Fixed per-item model-usage accounting for custom loaders.', 'Python', 'MERGED PR')
    card('oss-kornia', 'kornia / kornia', 'Handled empty accelerator tensors in color transforms.', 'Python', 'MERGED PR')
    card('oss-pyrit', 'microsoft / PyRIT', 'Added Dart, Perl, and Raku package-hallucination techniques.', 'Python', 'MERGED PR')
    card('oss-wandb', 'wandb / rai-toolkit', 'Preserved default categories in LLM judge scorers.', 'Python', 'MERGED PR')
    card('oss-pytorch', 'pytorch / pytorch', 'Proposed CPU/CUDA shape gradients for incomplete gamma functions.', 'C++ / CUDA', 'OPEN PR', '#f34b7d')
    button('all-repos','ALL MY REPOSITORIES')
    button('contributions','CONTRIBUTION DETAILS')
