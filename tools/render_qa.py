"""
render_qa: renders a PPTX to images and a contact sheet so every slide can be looked at before delivery.

  python3 render_qa.py deck.pptx [outdir]

Uses LibreOffice. When Segoe UI is not installed, fonts.conf in this folder maps it to Inter
(slightly wider), so a line that fits here fits in PowerPoint. Look at every image: text overflow,
collisions, anything covering the logo or footer, wrapped titles.
"""
import glob, os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))

def main():
    src = os.path.abspath(sys.argv[1])
    out = os.path.abspath(sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(src)[0] + '_qa')
    os.makedirs(out, exist_ok=True)
    env = dict(os.environ)
    fc = os.path.expanduser('~/.config/fontconfig')
    if not os.path.exists(os.path.join(fc, 'fonts.conf')):
        os.makedirs(fc, exist_ok=True)
        shutil.copy(os.path.join(HERE, 'fonts.conf'), os.path.join(fc, 'fonts.conf'))
    prof = tempfile.mkdtemp(prefix='lo_')
    env['SAL_USE_VCLPLUGIN'] = 'svp'
    subprocess.run(['soffice', f'-env:UserInstallation=file://{prof}', '--headless', '--convert-to', 'pdf', '--outdir', out, src],
                   check=True, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=600)
    pdf = os.path.join(out, os.path.splitext(os.path.basename(src))[0] + '.pdf')
    subprocess.run(['pdftoppm', '-jpeg', '-r', '110', pdf, os.path.join(out, 'slide')], check=True)
    from PIL import Image
    fs = sorted(glob.glob(os.path.join(out, 'slide-*.jpg')))
    ims = [Image.open(f) for f in fs]
    w, h = ims[0].size
    tw, th = w // 2, h // 2
    cols = 2
    rows = (len(ims) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * tw + (cols + 1) * 8, rows * th + (rows + 1) * 8), '#8a8a8a')
    for i, im in enumerate(ims):
        sheet.paste(im.resize((tw, th)), (8 + (i % cols) * (tw + 8), 8 + (i // cols) * (th + 8)))
    sheet.save(os.path.join(out, 'contact_sheet.jpg'), quality=88)
    print('rendered', len(fs), 'slides to', out)

if __name__ == '__main__':
    main()
