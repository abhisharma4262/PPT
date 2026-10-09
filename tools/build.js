// mkit builder: node build.js deck.json out.pptx [deck title] [svgs.json]
const pptxgen = require('pptxgenjs');
const sharp = require('sharp');
const fs = require('fs');
const deck = JSON.parse(fs.readFileSync(process.argv[2] || 'deck.json', 'utf8'));
const OUT = process.argv[3] || 'raw.pptx';
const DECK_TITLE = process.argv[4] || 'Myridius deck';
const SVG_OUT = process.argv[5] || (OUT + '.svgs.json');

const IN = (v) => v / 144;           // px -> inches (1920px = 13.333in)
const PT = (v) => v * 0.5;           // px -> points
const tr = (a) => Math.round((1 - (a == null ? 1 : a)) * 100);
const K = 0.5523;

function fillOpt(f) { return f ? { color: f.hex, transparency: tr(f.a) } : undefined; }
function lineOpt(l, extra) {
  if (!l) return { type: 'none' };
  const o = { color: l.hex, transparency: tr(l.a), width: PT(l.w) };
  if (l.dash) o.dashType = l.dash;
  return Object.assign(o, extra || {});
}
function roundedPoints(w, h, r) { // w,h,r in inches; r=[tl,tr,br,bl]
  const [a, b, c, d] = r;
  return [
    { x: a, y: 0, moveTo: true }, { x: w - b, y: 0 },
    { x: w, y: b, curve: { type: 'cubic', x1: w - b + b * K, y1: 0, x2: w, y2: b - b * K } },
    { x: w, y: h - c },
    { x: w - c, y: h, curve: { type: 'cubic', x1: w, y1: h - c + c * K, x2: w - c + c * K, y2: h } },
    { x: d, y: h },
    { x: 0, y: h - d, curve: { type: 'cubic', x1: d - d * K, y1: h, x2: 0, y2: h - d + d * K } },
    { x: 0, y: a },
    { x: a, y: 0, curve: { type: 'cubic', x1: 0, y1: a - a * K, x2: a - a * K, y2: 0 } },
    { close: true },
  ];
}

(async () => {
  const pres = new pptxgen();
  pres.layout = 'LAYOUT_WIDE';
  pres.title = DECK_TITLE;
  pres.company = 'Evoq · Myridius';
  pres.theme = { headFontFace: 'Segoe UI', bodyFontFace: 'Segoe UI' };
  let iconN = 0;
  const svgs = {};
  for (let si = 0; si < deck.length; si++) {
    const slide = pres.addSlide();
    slide.background = { color: 'FFFFFF' };
    let n = 0;
    for (const it of deck[si]) {
      n++;
      if (it.t === 'shape') {
        const w = IN(it.w), h = IN(it.h);
        if (w <= 0 || h <= 0) continue;
        const base = { x: IN(it.x), y: IN(it.y), w, h, fill: fillOpt(it.fill), line: lineOpt(it.line) };
        if (it.name) base.objectName = it.name;
        if (it.gn) base.objectName = (base.objectName ? base.objectName + '~' : 'Shape~') + it.gn;
        if (it.shadow) base.shadow = { type: 'outer', color: it.shadow.color, opacity: Math.min(1, it.shadow.a * 1.6), blur: PT(it.shadow.blur), offset: PT(Math.max(0, it.shadow.oy)), angle: 90 };
        if (!base.fill) base.fill = { type: 'none' };
        const r = it.radii || [0, 0, 0, 0];
        if (it.kind === 'ellipse') slide.addShape(pres.shapes.OVAL, base);
        else if (r.every(v => v < 0.3)) slide.addShape(pres.shapes.RECTANGLE, base);
        else if (r.every(v => Math.abs(v - r[0]) < 0.3)) slide.addShape(pres.shapes.ROUNDED_RECTANGLE, Object.assign(base, { rectRadius: IN(r[0]) }));
        else slide.addShape(pres.shapes.CUSTOM_GEOMETRY, Object.assign(base, { points: roundedPoints(w, h, r.map(IN)) }));
      } else if (it.t === 'circle') {
        const o = { x: IN(it.cx - it.r), y: IN(it.cy - it.r), w: IN(2 * it.r), h: IN(2 * it.r),
          fill: it.fill ? fillOpt(it.fill) : { type: 'none' }, line: lineOpt(it.stroke) };
        if (it.gn) o.objectName = 'Oval~' + it.gn;
        slide.addShape(pres.shapes.OVAL, o);
      } else if (it.t === 'rrect') {
        const o = { x: IN(it.x), y: IN(it.y), w: IN(it.w), h: IN(it.h), fill: it.fill ? fillOpt(it.fill) : { type: 'none' }, line: lineOpt(it.stroke) };
        if (it.gn) o.objectName = 'Rect~' + it.gn;
        if (it.rx > 0) slide.addShape(pres.shapes.ROUNDED_RECTANGLE, Object.assign(o, { rectRadius: IN(it.rx) }));
        else slide.addShape(pres.shapes.RECTANGLE, o);
      } else if (it.t === 'path') {
        const P = [];
        it.segs.forEach(s => { if (s.p) P.push(s.p); if (s.c1) P.push(s.c1); if (s.c2) P.push(s.c2); });
        let x0 = Math.min(...P.map(p => p[0])), y0 = Math.min(...P.map(p => p[1]));
        let x1 = Math.max(...P.map(p => p[0])), y1 = Math.max(...P.map(p => p[1]));
        if (x1 - x0 < 1) { x0 -= 0.5; x1 += 0.5; }
        if (y1 - y0 < 1) { y0 -= 0.5; y1 += 0.5; }
        const rp = (p) => ({ x: IN(p[0] - x0), y: IN(p[1] - y0) });
        const pts = [];
        it.segs.forEach((s, i) => {
          if (s.c === 'M') pts.push(Object.assign(rp(s.p), { moveTo: true }));
          else if (s.c === 'L') pts.push(rp(s.p));
          else if (s.c === 'Q') { const a = rp(s.c1); pts.push(Object.assign(rp(s.p), { curve: { type: 'quadratic', x1: a.x, y1: a.y } })); }
          else if (s.c === 'C') { const a = rp(s.c1), b = rp(s.c2); pts.push(Object.assign(rp(s.p), { curve: { type: 'cubic', x1: a.x, y1: a.y, x2: b.x, y2: b.y } })); }
          else if (s.c === 'Z') pts.push({ close: true });
        });
        const o = { x: IN(x0), y: IN(y0), w: IN(x1 - x0), h: IN(y1 - y0), points: pts,
          fill: it.fill ? fillOpt(it.fill) : { type: 'none' },
          line: lineOpt(it.stroke, it.arrow ? { endArrowType: 'triangle' } : null) };
        if (it.gn) o.objectName = 'Path~' + it.gn;
        slide.addShape(pres.shapes.CUSTOM_GEOMETRY, o);
      } else if (it.t === 'photo') {
        slide.addImage({ path: it.src, x: IN(it.x), y: IN(it.y), w: IN(it.w), h: IN(it.h), objectName: `shot-r${(it.radius||0).toFixed(1)}-${(it.w).toFixed(1)}-${(it.h).toFixed(1)}`, altText: 'AEO screenshot' });
      } else if (it.t === 'img') {
        iconN++;
        const base = `svgicon-${iconN}`;
        const name = base + (it.gn ? '~' + it.gn : '');
        const svg = it.svg.includes('xmlns=') ? it.svg : it.svg.replace('<svg', '<svg xmlns="http://www.w3.org/2000/svg"');
        const png = await sharp(Buffer.from(svg), { density: 72 * 8 }).png().toBuffer();
        svgs[base] = svg;
        slide.addImage({ data: 'image/png;base64,' + png.toString('base64'), x: IN(it.x), y: IN(it.y), w: IN(it.w), h: IN(it.h), objectName: name, altText: 'icon' });
      } else if (it.t === 'char') {
        const s = it.size * 1.7;
        slide.addText(it.ch, { objectName: it.gn ? 'Char~' + it.gn : undefined, x: IN(it.cx - s / 2), y: IN(it.cy - s / 2), w: IN(s), h: IN(s), rotate: it.rot,
          fontFace: it.face, bold: it.bold, fontSize: PT(it.size), color: it.color, transparency: tr(it.alpha),
          align: 'center', valign: 'middle', margin: 0, wrap: false, isTextBox: true, fit: 'none' });
      } else if (it.t === 'text') {
        const runs = [];
        for (const r of it.runs) {
          if (r.br) { if (runs.length) runs[runs.length - 1].options.breakLine = true; continue; }
          const o = { fontFace: r.face, bold: r.bold, italic: r.italic, fontSize: PT(r.size), color: r.color };
          if (r.alpha < 0.999) o.transparency = tr(r.alpha);
          if (r.spacing) o.charSpacing = PT(r.spacing);
          if (r.hl) o.highlight = 'A8EFC0';
          if (r.strike) o.strike = 'sngStrike';
          if (r.link) { o.hyperlink = { url: r.link }; o.underline = { style: 'sng', color: r.color }; }
          else if (r.underline) o.underline = { style: 'sng' };
          runs.push({ text: r.text, options: o });
        }
        if (!runs.length) continue;
        const single = it.lines <= 1;
        let x = it.x, w = it.w, y, h;
        const opts = { margin: 0, isTextBox: true, fit: 'none', align: it.align };
        if (single) {
          const extra = w * 0.14 + 8;
          if (it.align === 'center') { x -= extra / 2; } else if (it.align === 'right') { x -= extra; }
          w += extra; h = it.lh; y = it.y + it.h / 2 - h / 2;
          opts.valign = 'middle'; opts.wrap = false;
        } else {
          const extra = w * 0.04 + 4;
          if (it.align === 'center') x -= extra / 2; else if (it.align === 'right') x -= extra;
          w += extra; y = it.y; h = it.h + it.lh * 0.2;
          opts.valign = 'top'; opts.lineSpacing = PT(it.lh);
        }
        if (it.name) opts.objectName = it.name;
        if (it.gn) opts.objectName = (opts.objectName ? opts.objectName + '~' : 'Text~') + it.gn;
        slide.addText(runs, Object.assign(opts, { x: IN(x), y: IN(y), w: IN(w), h: IN(h) }));
      }
    }
  }
  await pres.writeFile({ fileName: OUT });
  fs.writeFileSync(SVG_OUT, JSON.stringify(svgs));
  console.log('written', iconN, 'icons');
})();
