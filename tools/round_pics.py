# mkit: gives exported screenshots their rounded corners (roundRect geometry).
import zipfile, re, sys
src, dst = sys.argv[1], sys.argv[2]
zin = zipfile.ZipFile(src); files = {n: zin.read(n) for n in zin.namelist()}
cnt = 0
for n in list(files):
    if not re.match(r'ppt/slides/slide\d+\.xml$', n): continue
    x = files[n].decode()
    def rep(m):
        global cnt
        body = m.group(0)
        r, w, h = float(m.group(1)), float(m.group(2)), float(m.group(3))
        body = re.sub(r'name="shot-r[^"]*"', 'name="Screenshot"', body, count=1)
        if r > 0.5:
            adj = int(round(r / min(w, h) * 100000))
            body = body.replace('<a:prstGeom prst="rect"><a:avLst/></a:prstGeom>', f'<a:prstGeom prst="roundRect"><a:avLst><a:gd name="adj" fmla="val {adj}"/></a:avLst></a:prstGeom>', 1)
            cnt += 1
        return body
    x = re.sub(r'<p:pic>\s*<p:nvPicPr><p:cNvPr id="\d+" name="shot-r([\d.]+)-([\d.]+)-([\d.]+)".*?</p:pic>', rep, x, flags=re.S)
    files[n] = x.encode()
order = ['[Content_Types].xml'] + [k for k in files if k != '[Content_Types].xml']
with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as z:
    for k in order: z.writestr(k, files[k])
print('rounded', cnt)
