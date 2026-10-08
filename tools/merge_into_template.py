"""
merge_into_template: puts slides exported by html2pptx.py into the Myridius 2026 template, so every
slide gets the real logo, copyright line, page number, cover and end slide.

  python3 merge_into_template.py content.pptx final.pptx \
      --template ../template/Myridius_Template_2026.pptx \
      --kicker "Discussion with Disney" --title "Myridius|DCL GRATS Migration" --date "October 2026" \
      [--divider "Appendix@9"] [--no-cover] [--no-end]

The template holds four sample slides in this order: cover, content, divider, end.
--title uses "|" for a line break. --divider "Text@N" inserts a divider before content slide N
(1-based, repeatable).
"""
import argparse, copy, io, os, re
from pptx import Presentation
from pptx.opc.package import Part
from pptx.opc.constants import RELATIONSHIP_TYPE as RT
from lxml import etree

HERE = os.path.dirname(os.path.abspath(__file__))
NS = {'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
      'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
      'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
R_ATTRS = ['{%s}embed' % NS['r'], '{%s}link' % NS['r'], '{%s}id' % NS['r']]

def clone_slide(prs, src):
    """Append a copy of an existing slide (same layout, shapes and relationships)."""
    new = prs.slides.add_slide(src.slide_layout)
    for sh in list(new.shapes):
        sh._element.getparent().remove(sh._element)
    rid_map = {}
    for rel in src.part.rels.values():
        if rel.reltype in (RT.SLIDE_LAYOUT, RT.NOTES_SLIDE):
            continue
        if rel.is_external:
            rid_map[rel.rId] = new.part.relate_to(rel.target_ref, rel.reltype, is_external=True)
        else:
            rid_map[rel.rId] = new.part.relate_to(rel.target_part, rel.reltype)
    tree = new.shapes._spTree
    for el in src.shapes._spTree.iterchildren():
        if el.tag.endswith('}nvGrpSpPr') or el.tag.endswith('}grpSpPr'):
            continue
        e = copy.deepcopy(el)
        for node in e.iter():
            for att in R_ATTRS:
                v = node.get(att)
                if v in rid_map:
                    node.set(att, rid_map[v])
        tree.append(e)
    bg = src._element.find('.//p:cSld/p:bg', NS)
    if bg is not None:
        new._element.find('.//p:cSld', NS).insert(0, copy.deepcopy(bg))
    return new

def import_shapes(dst_slide, src_slide, dst_pkg):
    """Deep-copy every shape of src_slide (another presentation) into dst_slide, carrying images and SVGs."""
    rid_map = {}
    tree = dst_slide.shapes._spTree
    for el in src_slide.shapes._spTree.iterchildren():
        if el.tag.endswith('}nvGrpSpPr') or el.tag.endswith('}grpSpPr'):
            continue
        e = copy.deepcopy(el)
        for node in e.iter():
            for att in R_ATTRS:
                v = node.get(att)
                if not v:
                    continue
                if v not in rid_map:
                    rel = src_slide.part.rels[v]
                    if rel.is_external:
                        rid_map[v] = dst_slide.part.relate_to(rel.target_ref, rel.reltype, is_external=True)
                    else:
                        sp = rel.target_part
                        ext = os.path.splitext(str(sp.partname))[1] or '.bin'
                        partname = dst_pkg.next_partname('/ppt/media/mkit%d' + ext)
                        np_ = Part(partname, sp.content_type, dst_pkg, sp.blob)
                        rid_map[v] = dst_slide.part.relate_to(np_, rel.reltype)
                node.set(att, rid_map[v])
        tree.append(e)

def renumber_ids(slide):
    n = 2
    for node in slide.shapes._spTree.iter():
        if node.tag.endswith('}cNvPr'):
            node.set('id', str(n)); n += 1

def set_text(shape, text):
    """Replace text keeping the first run's formatting. '|' = line break inside a paragraph."""
    tf = shape.text_frame
    p0 = tf.paragraphs[0]
    runs = p0.runs
    for para in tf.paragraphs[1:]:
        para._p.getparent().remove(para._p)
    for br in p0._p.findall('a:br', NS):
        p0._p.remove(br)
    first = runs[0]
    for r in runs[1:]:
        r._r.getparent().remove(r._r)
    parts = text.split('|')
    first.text = parts[0]
    anchor = first._r
    for part in parts[1:]:
        br = etree.SubElement(p0._p, '{%s}br' % NS['a'])
        rpr = first._r.find('a:rPr', NS)
        if rpr is not None:
            br.append(copy.deepcopy(rpr))
        anchor.addnext(br)
        nr = copy.deepcopy(first._r); nr.find('a:t', NS).text = part
        br.addnext(nr); anchor = nr

def drop_slide(prs, slide):
    lst = prs.slides._sldIdLst
    for sid in list(lst):
        rid = sid.get('{%s}id' % NS['r'])
        if prs.part.related_part(rid) is slide.part:
            prs.part.drop_rel(rid); lst.remove(sid); return

def move_to(prs, slide, index):
    lst = prs.slides._sldIdLst
    for sid in list(lst):
        if prs.part.related_part(sid.get('{%s}id' % NS['r'])) is slide.part:
            lst.remove(sid); lst.insert(index, sid); return

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('content'); ap.add_argument('out')
    ap.add_argument('--template', default=os.path.join(HERE, '..', 'template', 'Myridius_Template_2026.pptx'))
    ap.add_argument('--kicker', default=''); ap.add_argument('--title', default=''); ap.add_argument('--date', default='')
    ap.add_argument('--divider', action='append', default=[])
    ap.add_argument('--no-cover', action='store_true'); ap.add_argument('--no-end', action='store_true')
    a = ap.parse_args()

    prs = Presentation(a.template)
    cover, sample, divider, end = list(prs.slides)[:4]
    src = Presentation(a.content)
    pkg = prs.part.package

    # cover
    if not a.no_cover:
        for sh in cover.shapes:
            if not sh.has_text_frame:
                continue
            t = sh.text_frame.text.strip()
            if sh.is_placeholder and sh.placeholder_format.idx == 0 and a.title:
                set_text(sh, a.title)
            elif sh.is_placeholder and a.date:
                set_text(sh, a.date)
            elif not sh.is_placeholder and a.kicker:
                set_text(sh, a.kicker)

    dividers = {}
    for d in a.divider:
        txt, _, pos = d.rpartition('@')
        dividers.setdefault(int(pos), []).append(txt)

    sequence = []
    for i, s in enumerate(src.slides, 1):
        for txt in dividers.get(i, []):
            dv = clone_slide(prs, divider)
            for sh in dv.shapes:
                if sh.has_text_frame and sh.text_frame.text.strip():
                    set_text(sh, txt)
            sequence.append(dv)
        ns = clone_slide(prs, sample)
        # keep only the footer placeholder (copyright + page number) from the sample
        for sh in list(ns.shapes):
            if not sh.is_placeholder:
                sh._element.getparent().remove(sh._element)
        import_shapes(ns, s, pkg)
        renumber_ids(ns)
        sequence.append(ns)

    order = ([] if a.no_cover else [cover]) + sequence + ([] if a.no_end else [end])
    for s in (sample, divider):
        drop_slide(prs, s)
    if a.no_cover:
        drop_slide(prs, cover)
    if a.no_end:
        drop_slide(prs, end)
    for idx, s in enumerate(order):
        move_to(prs, s, idx)
    prs.save(a.out)
    print('written', a.out, 'slides:', len(order))

if __name__ == '__main__':
    main()
