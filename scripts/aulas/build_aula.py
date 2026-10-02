"""Monta uma aula (deck paisagem) ou manual (A4) do curso a partir de um corpo HTML.

Uso:
  python3 scripts/aulas/build_aula.py corpo.html "<pasta da aula>/Nome_da_Aula.html" \
      --title "Título da aba" [--manual] [--img NOME=mock.html|tela.jpg ...] [--sheet DIR]

- corpo.html começa em <div class="wrap"> e termina em </html> (ver body_exemplo.html).
- Cada --img NOME=arquivo troca {{IMG_NOME}} no corpo por um data URI JPEG. Um .html é
  tratado como mockup: renderizado no Chrome (tamanho do @page dele) e convertido a 144 DPI.
- Gera o .html autocontido e o .pdf ao lado, imprime as páginas (pdfinfo) e, com --sheet,
  salva DIR/<nome>_sheet.png com todas as páginas para a checagem visual.
"""
import argparse, base64, glob, os, re, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = ["google-chrome", "--headless", "--disable-gpu", "--no-sandbox",
          "--run-all-compositor-stages-before-draw", "--virtual-time-budget=4000",
          "--no-pdf-header-footer"]


def chrome_pdf(src, dst):
    subprocess.run(CHROME + [f"--print-to-pdf={dst}", "file://" + os.path.abspath(src)],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def image_uri(path, tmp):
    if path.endswith(".html"):
        src = open(path).read()
        if "<!--MOCK_BASE-->" in src:  # embute scripts/aulas/mock_base.css
            css = open(os.path.join(HERE, "mock_base.css")).read()
            src = src.replace("<!--MOCK_BASE-->", "<style>\n" + css + "</style>")
        page = os.path.join(os.path.dirname(os.path.abspath(path)), ".render_" + os.path.basename(path))
        open(page, "w").write(src)
        pdf = os.path.join(tmp, "mock.pdf")
        try:
            chrome_pdf(page, pdf)
        finally:
            os.remove(page)
        subprocess.run(["pdftoppm", "-jpeg", "-r", "144", "-singlefile", "-f", "1", "-l", "1",
                        pdf, os.path.join(tmp, "mock")], check=True)
        path = os.path.join(tmp, "mock.jpg")
    with open(path, "rb") as f:
        return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()


def contact_sheet(pdf, out, tmp, cols):
    from PIL import Image
    subprocess.run(["pdftoppm", "-png", "-r", "30", pdf, os.path.join(tmp, "pg")], check=True)
    ims = [Image.open(f) for f in sorted(glob.glob(os.path.join(tmp, "pg-*.png")))]
    w, h = max(i.width for i in ims), max(i.height for i in ims)
    sheet = Image.new("RGB", (cols * (w + 6), -(-len(ims) // cols) * (h + 6)), "#666")
    for k, im in enumerate(ims):
        sheet.paste(im, ((k % cols) * (w + 6), (k // cols) * (h + 6)))
    sheet.save(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("body"); ap.add_argument("out")
    ap.add_argument("--title", required=True)
    ap.add_argument("--manual", action="store_true", help="A4 retrato (head_manual.html)")
    ap.add_argument("--img", action="append", default=[], metavar="NOME=arquivo")
    ap.add_argument("--sheet", metavar="DIR")
    a = ap.parse_args()

    head = open(os.path.join(HERE, "head_manual.html" if a.manual else "head_lesson.html")).read()
    html = head.replace("{{TITLE}}", a.title) + open(a.body).read()
    with tempfile.TemporaryDirectory() as tmp:
        for spec in a.img:
            name, path = spec.split("=", 1)
            html = html.replace("{{IMG_%s}}" % name, image_uri(path, tmp))
        left = sorted(set(re.findall(r"\{\{[A-Z_0-9]+\}\}", html)))
        if left:
            sys.exit("Marcadores sem valor: " + ", ".join(left))
        open(a.out, "w").write(html)
        pdf = os.path.splitext(a.out)[0] + ".pdf"
        chrome_pdf(a.out, pdf)
        pages = re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", pdf], capture_output=True,
                                                            text=True).stdout).group(1)
        sections = html.count('<section class="block') if not a.manual else None
        print(f"{pdf}: {pages} páginas" + (f" ({sections} seções)" if sections else ""))
        if sections and int(pages) != sections:
            print("ATENÇÃO: páginas ≠ seções; alguma seção transbordou para a página seguinte.")
        if a.sheet:
            out = os.path.join(a.sheet, os.path.basename(os.path.splitext(a.out)[0]) + "_sheet.png")
            contact_sheet(pdf, out, tmp, 4 if a.manual else 5)
            print("folha de contato:", out)


if __name__ == "__main__":
    main()
