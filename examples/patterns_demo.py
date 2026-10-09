"""
patterns_demo: three slides that exercise the brochure patterns and the newer export features
(links, strikethrough, rotated groups, entrance animation, band_items, metric_list, header without eyebrow).

  python3 examples/patterns_demo.py demo.html
  python3 tools/html2pptx.py demo.html raw.pptx "Patterns demo"
  python3 tools/merge_into_template.py raw.pptx merged.pptx --kicker "Kit test" --title "Patterns|demo" --date "October 2026"
  python3 tools/group_anim.py merged.pptx demo.pptx
  python3 tools/render_qa.py demo.pptx qa
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tools'))
from mkit import *
from patterns import PATTERN_CSS, scatter_hub_card, out_card, ui_window, flow_ribbons

PANEL = '<div class="card soft" style="left:59px;top:196px;width:1801px;height:620px;background:var(--beige)"></div>'


def s_scatter():
    o = [header('Example pattern', 'One trusted answer for every agent, human or AI', accent='every agent, human or AI'), PANEL]
    chips = [(100, 230, 'SOP: card servicing, v4', 'doc', -2, False),
             (220, 296, 'Wiki page, last edited 2023', 'doc', 2.5, True),
             (120, 362, 'Product guide, release 12', 'book', 1.5, False),
             (150, 428, 'SOP copy on a shared drive', 'doc', -2, True),
             (100, 494, 'Client configuration: Bank A', 'gear', -1.5, False),
             (190, 560, 'Regulatory guidance', 'shield', 2, False),
             (110, 626, 'Resolved case notes', 'check', -1, False)]
    card = out_card(1180, 222, 520, 560, 'book', 'One trusted answer', 'For every agent, human or AI', 'Approved', [
        ('Question', [('chat', 'What changed in Bank A fee settings?', None)]),
        ('Answer', [('check', 'Fee settings moved to the Pricing tab', None), ('check', 'Tiered fees: changes need dual approval', None)]),
        ('Cited sources', [('doc', 'Product guide, release 12, section 4', 'link'), ('gear', 'Client configuration: Bank A', 'link')]),
    ], foot='Illustrative example')
    o.append(scatter_hub_card(chips, (820, 450), 'layers', 'Knowledge foundation', 'Ingested, approved, versioned, cited', card,
                              (712, [('minus', 'Outdated and duplicate copies retired')])))
    o.append(sources_line(59, 900, [('Gartner predictions', 'https://www.gartner.com/en/newsroom'), ('Fiserv Investor Day', 'https://investors.fiserv.com')]))
    return '\n'.join(o)


def s_window():
    o = [header(None, 'Agents get help during the contact and spend less time after it', accent='help during the contact')]
    panes = ''
    for i, (lab, ic, t) in enumerate((('Before', 'context', 'Arrives with context'), ('During', 'compass', 'Guided in the moment'), ('After', 'doc', 'Wrap-up drafted'))):
        x = 100 + i * 580
        panes += (f'<div class="card" style="left:{x}px;top:290px;width:540px;height:260px;border-color:var(--m10)">'
                  f'<div class="flow" style="left:22px;top:20px;right:20px"><div style="display:flex;align-items:center;gap:12px">{ico(ic, "lt", 44)}'
                  f'<span class="lbl" style="font-size:18px">{lab}</span></div><div class="h3" style="font-size:24px;margin-top:12px">{t}</div></div></div>')
    o.append(ui_window(70, 220, 1780, 360, 'Agent desktop', panes))
    o.append(f'<div class="flow" style="left:70px;top:640px;width:700px">{metric_list([("down", "Handle time"), ("down", "After-contact work"), ("up", "Quality coverage"), ("up", "Compliance adherence")])}</div>')
    o.append(band_items(59, 800, 1801, 100, 'handshake', 'How we work',
                        [('users', 'Alongside your teams and platform partners'), ('target', 'Outcomes agreed up front'), ('book', 'Knowledge transferred as we go')]))
    return '\n'.join(o)


def s_flow():
    o = [header(None, 'Most requests can be resolved before they reach an engineer', accent='resolved before they reach an engineer'), PANEL]
    tiers = [('Resolved by AI', 'Answer or fix sent; ticket closed', 150, PULSE, .62),
             ('L1 support', 'How-to, configuration, known errors', 110, TEAL, .5),
             ('L2 investigation', 'Data fixes and workarounds', 80, SLATE, .45),
             ('Product engineering', 'Code-level fixes, with evidence attached', 40, MOSS, .35)]
    s, body = flow_ribbons(120, 420, 1120, 320, 380, tiers)
    o.append(svg(''.join(s)))
    o.append('\n'.join(body))
    o.append('<div class="flow" style="left:1164px;top:226px"><div style="font:700 21px/1.2 var(--f);color:var(--leaf)">Where they land</div>'
             '<div style="font:400 18px/1.3 var(--f);color:var(--slate)">Illustrative flow</div></div>')
    return '\n'.join(o)


if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else 'patterns_demo.html'
    write_deck(out, [s_scatter(), s_window(), s_flow()], PATTERN_CSS, 'Patterns demo')
    print('written', out)
