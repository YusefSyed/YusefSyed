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


def intro(theme):
    color = CYAN if theme == 'dark' else '#006c87'
    lines = ['Student at the University of Toronto', 'Building apps and developer tools', 'Interested in AI evaluation']
    body = [text(300, 34, 'Yusef Syed', 29, color, family=MONO, extra='text-anchor="middle"')]
    css = ['.still{display:none}']
    for i, line in enumerate(lines):
        width = len(line) * 14.4 + 3
        start = (600 - width) / 2
        css.append(f'@keyframes type{i}{{0%{{width:0}}16%,26%{{width:{width}px}}33.32%,100%{{width:0}}}}')
        css.append(f'#reveal{i}{{width:0;animation:type{i} 18s steps({len(line)},end) {i*6}s infinite both}}')
        body.append(f'<clipPath id="clip{i}"><rect id="reveal{i}" x="{start}" y="65" width="0" height="34"/></clipPath>')
        body.append(f'<g class="moving" clip-path="url(#clip{i})">{text(start, 91, line, 24, color, family=MONO)}</g>')
    css.append('@media(prefers-reduced-motion:reduce){.moving{display:none}.still{display:block}}')
    body.append(f'<g class="still">{text(300, 91, lines[0], 24, color, family=MONO, extra="text-anchor=\"middle\"")}</g>')
    body.insert(0, '<style>' + ''.join(css) + '</style>')
    write('intro-' + theme, 600, 116, 'Yusef Syed — University of Toronto student, apps, developer tools, and AI evaluation', '\n'.join(body))
    write('intro-static-' + theme, 600, 116, 'Yusef Syed — Student at the University of Toronto',
          text(300, 34, 'Yusef Syed', 29, color, family=MONO, extra='text-anchor="middle"') +
          text(300, 91, lines[0], 24, color, family=MONO, extra='text-anchor="middle"'))


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
        for name, label in [('portfolio','PORTFOLIO'),('linkedin','LINKEDIN'),('email','EMAIL'),('resume','RESUME'),('github','GITHUB')]:
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
