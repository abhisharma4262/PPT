"""
Example: three common Myridius slide patterns built with mkit, then exported and merged into the template.

  cd examples
  python3 example_deck.py                                  # writes example.html
  python3 ../tools/html2pptx.py example.html example_raw.pptx "Example deck"
  python3 ../tools/merge_into_template.py example_raw.pptx example_final.pptx \
          --kicker "Discussion with Client" --title "Myridius|Example proposal" --date "October 2026" --divider "Appendix@3"
  python3 ../tools/lint_text.py example_final.pptx
  python3 ../tools/render_qa.py example_final.pptx

Content here is placeholder wording to show structure; replace all of it.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tools'))
from mkit import *

# ------------------------------------------------------------------ 1. options with a recommendation
def s_options():
    o = [header('Our POV', 'Three ways to run the programme; they differ in certainty',
                'Every option uses AI to do the work; they differ in how the result is governed and proven')]
    cw, gap, y0, h = (1802 - 2 * 24) / 3, 24, 214, 730
    opts = [('A', 'Tool-led', 'Coding agents in each engineer’s hands', False,
             'Each engineer’s own practice', 'Small, well-understood applications', 'Fast to start; hard to prove at scale'),
            ('B', 'Platform-led', 'A managed transformation platform', False,
             'The platform’s supported paths', 'Upgrades along a supported path', 'Custom work for anything off the path'),
            ('C', 'Harness-led', 'Agents inside an engineered harness', True,
             'A method engineered around the AI', 'Business-critical systems with more to follow', 'Set-up first; SME time at the gates')]
    s = []
    for i, (L, name, sub, rec, cert, best, watch) in enumerate(opts):
        x = 59 + i * (cw + gap)
        o.append(f'<div class="card{" dk" if rec else ""}" style="left:{x:.0f}px;top:{y0}px;width:{cw:.0f}px;height:{h}px">'
                 f'<div class="ohd"><span class="olt">{L}</span><span class="onm">{name}</span></div>'
                 + ('<span class="tag" style="right:24px;top:30px">Recommended</span>' if rec else '') +
                 f'<div class="osb">{sub}</div>'
                 f'<div class="blk" style="top:330px"><div class="lbl{" sl" if not rec else ""}">Where certainty comes from</div><div class="big">{cert}</div></div>'
                 f'<div class="blk" style="top:450px"><div class="lbl{" sl" if not rec else ""}">Strongest when</div><div class="txt">{best}</div></div>'
                 f'<div class="blk" style="top:570px"><div class="lbl{" sl" if not rec else ""}">Watch-out</div><div class="txt">{watch}</div></div></div>')
        cx, cy = x + cw / 2, y0 + 210
        if L == 'C':
            for k, a0 in enumerate((180, 270, 0, 90)):
                s.append(f'<path d="{seg_path(cx, cy, 78, 50, a0 + 3, a0 + 87)}" fill="{MINT}"/>')
            s.append(f'<circle cx="{cx}" cy="{cy}" r="40" fill="{PULSE}"/>' + gicon('agent', cx, cy, 38, MOSS, 2))
        elif L == 'B':
            s.append(f'<rect x="{cx-60:.0f}" y="{cy-70}" width="120" height="140" rx="14" fill="{MOSS}"/>' + gicon('cloud', cx, cy, 40, PULSE, 2))
            for dy in (-40, 0, 40):
                s.append(f'<path d="M{cx-150:.0f},{cy+dy} L{cx-68:.0f},{cy+dy}" stroke="{LEAF}" stroke-width="2.4" marker-end="url(#ahl)"/>')
                s.append(f'<path d="M{cx+64:.0f},{cy+dy} L{cx+146:.0f},{cy+dy}" stroke="{LEAF}" stroke-width="2.4" marker-end="url(#ahl)"/>')
        else:
            for k, dx in enumerate((-110, 0, 110)):
                s.append(f'<circle cx="{cx+dx:.0f}" cy="{cy-20}" r="34" fill="{MINT}"/>' + gicon('person', cx + dx, cy - 20, 32, MOSS, 2))
                dash = ['', ' stroke-dasharray="7 5"', ' stroke-dasharray="1.5 6" stroke-linecap="round"'][k]
                s.append(f'<path d="M{cx+dx:.0f},{cy+18} L{cx+dx:.0f},{cy+70}" stroke="{LEAF}" stroke-width="2.4"{dash}/>')
    o.append(svg(''.join(s)))
    return '\n'.join(o)

# ------------------------------------------------------------------ 2. comparison grid (columns x dimensions)
def s_grid():
    o = [header('Comparison', 'A harness-led approach gives the client the most certainty',
                'Each approach seen through the dimensions leadership will ask about')]
    LX, LW, X0, GAP = 59, 300, 379, 22
    cw = (1860 - X0 - 2 * GAP) / 3
    TY, BOT, RY, RH, RG = 196, 948, 470, 80, 8
    rows = [('clock', 'Efficiency &amp; speed', ['Fastest to start; pace depends on each engineer', 'Fast on pre-built paths; custom work elsewhere', 'Set-up first; then parallel lines at a steady pace']),
            ('evals', 'Quality &amp; traceability', ['As good as each engineer’s checks', 'Job logs; proof of business rules left to the client', 'Rules cited to source; evals and parity proof on record']),
            ('loop', 'Repeatability &amp; scale', ['Lives in individual habits', 'Repeatable within the platform', 'Skills and patterns reused on the next application']),
            ('scale', 'Cost of ownership', ['Lowest entry cost; effort repeats per app', 'Platform use plus custom definitions', 'Highest up front; lower for each later app'])]
    for r in range(len(rows)):
        o.append(f'<div class="rowband" style="left:{LX}px;top:{RY + r*(RH+RG)}px;width:{1860-LX}px;height:{RH}px"></div>')
    cols = [('A', 'Tool-led', False), ('B', 'Platform-led', False), ('C', 'Harness-led', True)]
    for k, (L, name, rec) in enumerate(cols):
        x = X0 + k * (cw + GAP)
        o.append(f'<div class="card{" dk" if rec else ""}" style="left:{x:.0f}px;top:{TY}px;width:{cw:.0f}px;height:{BOT-TY}px">'
                 f'<div class="ohd"><span class="olt">{L}</span><span class="onm">{name}</span></div>'
                 f'<div class="osb" style="top:90px">How it works, in two short lines that a CXO can read in five seconds.</div></div>')
        for r, (_, _, vals) in enumerate(rows):
            o.append(f'<div class="cell{" dk" if rec else ""}" style="left:{x+14:.0f}px;top:{RY + r*(RH+RG)}px;width:{cw-28:.0f}px;height:{RH}px">{vals[k]}</div>')
    for r, (ic, lab, _) in enumerate(rows):
        o.append(f'<div class="rlab" style="left:{LX+18}px;top:{RY + r*(RH+RG)}px;width:{LW-24}px;height:{RH}px">{ico(ic, "lt", 44)}<span>{lab}</span></div>')
    return '\n'.join(o)

# ------------------------------------------------------------------ 3. process line with gates and an always-on band
def s_process():
    o = [header('How it works', 'One governed path from legacy to the modern application',
                'Four stages, two human sign-offs, and every step on record')]
    stages = [('context', 'Build the context', 'Code, stories and documents, understood'), ('doc', 'Design the target', 'The blueprint, signed by people'),
              ('dev', 'Convert and scan', 'Slice by slice, with quality gates'), ('parity', 'Prove parity', 'Same inputs, same results')]
    x0, y0, W, H, N = 59, 250, 1801, 300, 4
    w = (W - 3 * 18) / 4
    s = []
    for i, (ic, t, d) in enumerate(stages):
        x = x0 + i * (w + 18)
        fill = MOSS if i % 2 == 0 else LEAF
        pts = [(x, y0), (x + w - 30, y0), (x + w, y0 + H / 2), (x + w - 30, y0 + H), (x, y0 + H)] + ([(x + 30, y0 + H / 2)] if i else [])
        s.append('<path d="M' + ' L'.join(f'{px:.0f},{py:.0f}' for px, py in pts) + f' Z" fill="{fill}"/>')
        o.append(f'<div class="stg" style="left:{x + (48 if i else 30):.0f}px;top:{y0 + 40}px;width:{w - 110:.0f}px">'
                 f'{ico(ic, "pu", 52)}<div class="sn">0{i+1}</div><div class="st">{t}</div><div class="sd">{d}</div></div>')
    for gx, lab in ((x0 + w + 9, 'Human sign-off'), (x0 + 2 * (w + 18) - 9, 'Human sign-off')):
        o.append(f'<span class="tag" style="left:{gx-80:.0f}px;top:{y0-22}px">{lab}</span>')
    o.insert(1, svg(''.join(s)))   # backgrounds go beneath the HTML text
    o.append(f'<div class="band" style="left:59px;top:600px;width:1801px;height:84px"><span class="lbl" style="color:var(--pulse)">Always on</span>'
             f'{icon("shield", 26, PULSE, 2)}<span><b>Guardrails</b> hard limits</span>{icon("evals", 26, PULSE, 2)}<span><b>Evals</b> every output scored</span>'
             f'{icon("person", 26, PULSE, 2)}<span><b>Human gates</b> people sign off</span>{icon("book", 26, PULSE, 2)}<span><b>Audit trail</b> every step recorded</span></div>')
    outs = [('parity', 'Business rules proven at parity'), ('shield', 'Client standards enforced at every gate'), ('book', 'Evidence ready for audit')]
    o.append('<div class="lbl" style="left:59px;top:732px">What it drives</div>')
    for i, (ic, t) in enumerate(outs):
        o.append(f'<div class="out" style="left:{59 + i*610}px;top:780px;width:582px;height:104px">{ico(ic, "lt", 52)}<span>{t}</span></div>')
    return '\n'.join(o)

EXTRA = r'''
.card .ohd{left:28px;top:28px;display:flex;align-items:center;gap:14px}
.olt{width:40px;height:40px;border-radius:10px;background:var(--moss);color:var(--pulse);font:700 20px/40px var(--f);text-align:center;display:inline-block}
.card.dk .olt{background:var(--pulse);color:var(--moss)}
.onm{font:700 32px/1 var(--f);color:var(--leaf)}
.card.dk .onm{color:#fff}
.osb{left:28px;right:28px;top:88px;font:400 20px/1.4 var(--f);color:var(--slate)}
.card.dk .osb{color:var(--mint)}
.blk{left:28px;right:28px;border-top:1.5px solid var(--m10);padding-top:14px}
.card.dk .blk{border-top-color:rgba(210,240,198,.22)}
.card.dk .lbl{color:var(--pulse)}
.blk .big{font:700 26px/1.25 var(--f);color:var(--leaf);margin-top:10px}
.card.dk .blk .big{color:#fff}
.blk .txt{font:400 21px/1.4 var(--f);color:var(--leaf);margin-top:8px}
.card.dk .blk .txt{color:#fff}
.lbl{font-size:17px}
.rowband{border-radius:12px;background:rgba(12,34,38,.05)}
.cell{border-radius:10px;background:var(--m04);display:flex;align-items:center;padding:0 20px;font:400 20px/1.35 var(--f);color:var(--leaf)}
.cell.dk{background:var(--leaf);color:#fff}
.rlab{display:flex;align-items:center;gap:14px;font:700 21px/1.25 var(--f);color:var(--leaf)}
.stg .sn{font:700 18px/1 var(--f);letter-spacing:.14em;color:var(--pulse);margin-top:22px}
.stg .st{font:700 30px/1.15 var(--f);color:#fff;margin-top:8px}
.stg .sd{font:400 20px/1.35 var(--f);color:var(--mint);margin-top:8px}
.band{font-size:21px;gap:14px}
.band span{white-space:nowrap}
.out{display:flex;align-items:center;gap:18px;padding:0 24px;border-radius:16px;border:1.5px solid var(--m16);background:#fff;font:700 23px/1.25 var(--f);color:var(--leaf)}
'''

if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    write_deck(os.path.join(here, 'example.html'), [s_options(), s_grid(), s_process()], EXTRA, 'Example deck')
    print('ok')
