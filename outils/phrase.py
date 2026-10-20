"""Atlasienne - format "la phrase qu'on envoie à sa copine" : photo d'ambiance plein cadre 1080x1920,
phrase en serif blanc centrée, enchaînement en fondu. Pas de pagination, pas de "glisse"."""
import sys, os, subprocess, tempfile
sys.path.insert(0, "/home/claude/atlasienne")
from atl2 import serif, sans, wrap, fr, logotype, PAPIER, ROSE, symbole
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageStat, ImageOps

RW, RH = 1080, 1920
PH = "/home/claude/atlasienne/eq/l4/"
SIDE = 110          # marges latérales (zone sûre Reels)
TOP_SAFE, BOT_SAFE = 300, 420


def fond(photo, fx=0.5, fy=0.5, voile=0.52, flou=0):
    im = Image.open(PH + photo).convert("RGB")
    iw, ih = im.size
    r = RW / RH
    if iw / ih > r:
        ch = ih; cw = ch * r
    else:
        cw = iw; ch = cw / r
    x0 = min(max(fx * iw - cw / 2, 0), iw - cw)
    y0 = min(max(fy * ih - ch / 2, 0), ih - ch)
    im = im.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((RW, RH), Image.LANCZOS)
    if flou:
        im = im.filter(ImageFilter.GaussianBlur(flou))
    lum = ImageStat.Stat(ImageOps.grayscale(im)).mean[0]
    # voile chaud, plus fort si la photo est claire
    k = min(0.78, voile + max(0, lum - 110) / 400)
    chaud = Image.new("RGB", (RW, RH), (24, 16, 12))
    return Image.blend(im, chaud, k)


def noorph(t):
    """Lie les deux derniers mots et les petits mots à leur suivant (pas de veuve)."""
    t = fr(t)
    for w in (" à ", " de ", " un ", " une ", " le ", " la ", " en ", " et ", " ni "):
        t = t.replace(w, w[:-1] + "\u00a0")
    i = t.rfind(" ")
    if i > 0 and len(t) - i < 16:
        t = t[:i] + "\u00a0" + t[i + 1:]
    return t


def _bloc(d, txt, font, width, lh):
    lines = wrap(d, noorph(txt), font, width)
    return lines, lh * len(lines)


def ecran(path, photo, phrase, sous=None, fx=0.5, fy=0.5, taille=86, voile=0.52, flou=0, cta=None):
    img = fond(photo, fx, fy, voile, flou)
    d = ImageDraw.Draw(img)
    width = RW - 2 * SIDE
    t = taille
    while True:
        fp = serif(t, 560)
        lp, hp = _bloc(d, phrase, fp, width, int(t * 1.16))
        if len(lp) <= 7 or t <= 58:
            break
        t -= 4
    blocs = [(lp, fp, int(t * 1.16), PAPIER, "serif")]
    if sous:
        fs = sans(48, 420)
        ls, hs = _bloc(d, sous, fs, width, 64)
        blocs.append((ls, fs, 64, ROSE, "sans"))
    if cta:
        fc = sans(46, 580)
        lc, hc = _bloc(d, cta, fc, width, 62)
        blocs.append((lc, fc, 62, ROSE, "sans"))
    gap = 54
    total = sum(len(b[0]) * b[2] for b in blocs) + gap * (len(blocs) - 1)
    zone_c = TOP_SAFE + (RH - TOP_SAFE - BOT_SAFE) / 2
    y = int(zone_c - total / 2)
    # ombre douce
    sh = Image.new("L", (RW, RH), 0)
    sd = ImageDraw.Draw(sh)
    yy = y
    for lines, f, lh, col, _ in blocs:
        for ln in lines:
            sd.text((RW / 2, yy + 4), ln, font=f, fill=210, anchor="ma")
            yy += lh
        yy += gap
    sh = sh.filter(ImageFilter.GaussianBlur(12)).point(lambda v: int(v * 0.6))
    img.paste(Image.new("RGB", (RW, RH), (0, 0, 0)), (0, 0), sh)
    d = ImageDraw.Draw(img)
    for i, (lines, f, lh, col, kind) in enumerate(blocs):
        if i > 0 and kind == "sans" and i == len(blocs) - 1 and cta:
            d.line([(RW / 2 - 40, y - gap / 2), (RW / 2 + 40, y - gap / 2)], fill=ROSE, width=3)
        for ln in lines:
            d.text((RW / 2, y), ln, font=f, fill=col, anchor="ma")
            y += lh
        y += gap
    # marque discrète, au-dessus de la zone de légende Instagram
    s = 40
    sym = symbole(s)
    lw = d.textlength("atlasienne", font=serif(34, 620))
    x0 = int(RW / 2 - (s + 12 + lw) / 2)
    yb = RH - BOT_SAFE + 70
    img.paste(sym, (x0, yb - s + 8), sym)
    logotype(d, x0 + s + 12, yb, 34, PAPIER)
    img.save(path, quality=93)
    return path


def duree(txt_total):
    n = len(txt_total.split())
    return round(max(2.0, min(3.6, 0.8 + 0.20 * n)), 2)


def video(frames, durs, out, fade=0.35):
    n = len(frames)
    cmd = ["ffmpeg", "-y", "-loglevel", "error"]
    for f, dd in zip(frames, durs):
        cmd += ["-loop", "1", "-t", f"{dd + fade:.2f}", "-i", f]
    cmd += ["-f", "lavfi", "-t", f"{sum(durs) + fade:.2f}", "-i", "anullsrc=r=44100:cl=stereo"]
    fc, prev, off = [], "0:v", 0.0
    for i in range(1, n):
        off += durs[i - 1]
        fc.append(f"[{prev}][{i}:v]xfade=transition=fade:duration={fade}:offset={off:.2f}[v{i}]")
        prev = f"v{i}"
    fc.append(f"[{prev}]format=yuv420p,fps=30[vout]")
    cmd += ["-filter_complex", ";".join(fc), "-map", "[vout]", "-map", f"{n}:a",
            "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-profile:v", "high",
            "-c:a", "aac", "-b:a", "128k", "-shortest", "-movflags", "+faststart", out]
    subprocess.run(cmd, check=True)
    return out


def reel_phrase(slug, out_dir, ecrans, defaults=None):
    """ecrans : liste de dicts (photo, phrase, sous, cta, fx, fy, taille, duree)."""
    d = os.path.join(out_dir, slug)
    os.makedirs(d, exist_ok=True)
    fs, durs = [], []
    for i, e in enumerate(ecrans, 1):
        e = {**(defaults or {}), **e}
        p = os.path.join(d, f"{i:02d}.jpg")
        ecran(p, e["photo"], e["phrase"], e.get("sous"), e.get("fx", .5), e.get("fy", .5),
              e.get("taille", 86), e.get("voile", .52), e.get("flou", 0), e.get("cta"))
        fs.append(p)
        txt = " ".join(x for x in (e["phrase"], e.get("sous"), e.get("cta")) if x)
        durs.append(e.get("duree", duree(txt)))
    durs[0] = max(durs[0], 2.4)
    out = os.path.join(out_dir, slug + ".mp4")
    video(fs, durs, out)
    return fs, durs, out
