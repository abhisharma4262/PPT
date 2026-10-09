# mkit: adds native SVG (svgBlip) to every exported icon, keeping the PNG fallback.
# python3 postproc.py raw.pptx out.pptx [svgs.json]
import zipfile, re, json, sys, os
src, dst = sys.argv[1], sys.argv[2]
svgs = json.load(open(sys.argv[3] if len(sys.argv) > 3 else src + '.svgs.json'))
zin = zipfile.ZipFile(src)
files = {n: zin.read(n) for n in zin.namelist()}
ct = files['[Content_Types].xml'].decode()
if 'Extension="svg"' not in ct:
    ct = ct.replace('<Default Extension="xml"', '<Default Extension="svg" ContentType="image/svg+xml"/><Default Extension="xml"', 1)
files['[Content_Types].xml'] = ct.encode()
for name in list(files):
    m = re.match(r'ppt/slides/(slide\d+)\.xml$', name)
    if not m: continue
    xml = files[name].decode()
    relsn = f'ppt/slides/_rels/{m.group(1)}.xml.rels'
    rels = files[relsn].decode()
    ids = [int(x) for x in re.findall(r'Id="rId(\d+)"', rels)]
    nxt = max(ids) + 1 if ids else 1
    def rep(mo):
        global nxt
        icon = mo.group(1); body = mo.group(0)
        rid = f'rId{nxt}'; nxt += 1
        files[f'ppt/media/{icon}.svg'] = svgs[icon].encode()
        nonlocal_rels.append(f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="../media/{icon}.svg"/>')
        return re.sub(r'<a:blip r:embed="(rId\d+)"></a:blip>',
            lambda b: f'<a:blip r:embed="{b.group(1)}"><a:extLst><a:ext uri="{{96DAC541-7B7A-43D3-8B79-37D633B846F1}}"><asvg:svgBlip xmlns:asvg="http://schemas.microsoft.com/office/drawing/2016/SVG/main" r:embed="{rid}"/></a:ext></a:extLst></a:blip>', body, count=1)
    nonlocal_rels = []
    xml = re.sub(r'<p:pic>\s*<p:nvPicPr><p:cNvPr id="\d+" name="(svgicon-\d+)[^"]*".*?</p:pic>', rep, xml, flags=re.S)
    rels = rels.replace('</Relationships>', ''.join(nonlocal_rels) + '</Relationships>')
    files[name] = xml.encode(); files[relsn] = rels.encode()
order = ['[Content_Types].xml'] + [n for n in files if n != '[Content_Types].xml']
with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as z:
    for n in order: z.writestr(n, files[n])
print('ok', dst)
