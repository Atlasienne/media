"""Atlasienne - format Reel v5 : animé, court, accroche lisible dès la première image.
- zoom lent continu sur la photo (effet Ken Burns)
- écran 1 : texte entier visible dès l'image 0 (accroche)
- écrans suivants : les mots apparaissent vite, un par un, avec une petite montée
- coupe franche entre écrans (plus nerveux que le fondu)
- musique d'ambiance originale intégrée, fondu de sortie
"""
import sys, os, subprocess
sys.path.insert(0, "/home/claude/atlasienne")
from atl2 import serif, sans, wrap, logotype, PAPIER, ROSE, symbole
from phrase import fond, noorph, RW, RH, SIDE, TOP_SAFE, BOT_SAFE
from PIL import Image, ImageDraw, ImageFilter

FPS = 30
MUS = "/home/claude/atlasienne/musique/"


def mise_en_page(phrase, sous, cta, taille):
    d = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    width = RW - 2 * SIDE
    t = taille
    while True:
        fp = serif(t, 580)
        lp = wrap(d, noorph(phrase), fp, width)
        if len(lp) <= 6 or t <= 60:
            break
        t -= 4
    blocs = [(lp, fp, int(t * 1.15), PAPIER)]
    if sous:
        fs = sans(50, 440)
        blocs.append((wrap(d, noorph(sous), fs, width), fs, 66, ROSE))
    if cta:
        fc = sans(48, 600)
        blocs.append((wrap(d, noorph(cta), fc, width), fc, 64, ROSE))
    gap = 56
    total = sum(len(b[0]) * b[2] for b in blocs) + gap * (len(blocs) - 1)
    y = int(TOP_SAFE + (RH - TOP_SAFE - BOT_SAFE) / 2 - total / 2)
    mots = []  # (x_centre_ligne, y, texte_ligne, font, couleur, index_mot, sous-chaîne)
    lignes = []
    for lines, f, lh, col in blocs:
        for ln in lines:
            lignes.append((ln, f, y, col))
            y += lh
        y += gap
    return lignes


def calque_texte(lignes, n_mots, montee=0.0):
    """Calque RGBA avec les n_mots premiers mots visibles. montee : décalage vertical du dernier mot (px)."""
    lay = Image.new("RGBA", (RW, RH), (0, 0, 0, 0))
    sh = Image.new("L", (RW, RH), 0)
    d = ImageDraw.Draw(lay); sd = ImageDraw.Draw(sh)
    compte = 0
    for ln, f, y, col in lignes:
        words = ln.split(" ")
        full_w = d.textlength(ln, font=f)
        x = RW / 2 - full_w / 2
        for i, w in enumerate(words):
            if compte >= n_mots:
                break
            seg = w + (" " if i < len(words) - 1 else "")
            dy = montee if compte == n_mots - 1 else 0
            d.text((x, y + dy), w, font=f, fill=col, anchor="la")
            sd.text((x, y + dy + 4), w, font=f, fill=220, anchor="la")
            x += d.textlength(seg, font=f)
            compte += 1
    sh = sh.filter(ImageFilter.GaussianBlur(12)).point(lambda v: int(v * 0.65))
    out = Image.new("RGBA", (RW, RH), (0, 0, 0, 0))
    out.paste(Image.new("RGBA", (RW, RH), (0, 0, 0, 255)), (0, 0), sh)
    out.alpha_composite(lay)
    return out


def nb_mots(lignes):
    return sum(len(l[0].split(" ")) for l in lignes)


def marque_calque():
    lay = Image.new("RGBA", (RW, RH), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    s = 40
    sym = symbole(s)
    lw = d.textlength("atlasienne", font=serif(34, 620))
    x0 = int(RW / 2 - (s + 12 + lw) / 2)
    yb = RH - BOT_SAFE + 70
    lay.paste(sym, (x0, yb - s + 8), sym.convert("RGBA") if sym.mode != "RGBA" else sym)
    logotype(d, x0 + s + 12, yb, 34, PAPIER)
    return lay


def duree_ecran(e, premier):
    txt = " ".join(x for x in (e["phrase"], e.get("sous"), e.get("cta")) if x)
    n = len(txt.split())
    d = 0.9 + 0.24 * n + (0.8 if e.get("cta") else 0)
    return round(max(1.8, min(4.2, d)) + (0.3 if premier else 0), 2)


def reel_anime(slug, out_dir, ecrans, musique="ambiance_a_m.wav", zoom=0.07):
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, slug + ".mp4")
    apercu_dir = os.path.join(out_dir, slug)
    os.makedirs(apercu_dir, exist_ok=True)
    marque = marque_calque()
    plans = []
    for i, e in enumerate(ecrans):
        big = fond(e["photo"], e.get("fx", .5), e.get("fy", .5), e.get("voile", .55), e.get("flou", 0))
        big = big.resize((int(RW * (1 + zoom)), int(RH * (1 + zoom))), Image.LANCZOS)
        lignes = mise_en_page(e["phrase"], e.get("sous"), e.get("cta"), e.get("taille", 92))
        plans.append(dict(big=big, lignes=lignes, n=nb_mots(lignes), dur=e.get("duree", duree_ecran(e, i == 0))))
    total = sum(p["dur"] for p in plans)
    nframes = int(round(total * FPS))
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{RW}x{RH}", "-r", str(FPS), "-i", "-",
           "-i", MUS + musique, "-filter_complex",
           f"[1:a]atrim=0:{total:.2f},afade=t=in:st=0:d=0.3,afade=t=out:st={max(0, total - 1.2):.2f}:d=1.2,volume=0.9[a]",
           "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p",
           "-profile:v", "high", "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", out]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    cache = {}
    t_debut = 0.0
    f = 0
    for pi, p in enumerate(plans):
        n_f = int(round((t_debut + p["dur"]) * FPS)) - f
        reveal = 0 if pi == 0 else min(0.55 + 0.05 * p["n"], p["dur"] * 0.45)
        for k in range(n_f):
            t_glob = (f + k) / FPS
            z = 1 + zoom * (t_glob / total)
            bw, bh = p["big"].size
            cw, ch = int(bw / z * (1 / (1 + zoom)) * (1 + zoom)), 0
            # recadrage centré qui se resserre
            sc = (1 + zoom) / z
            cw, ch = int(RW * sc), int(RH * sc)
            x0, y0 = (bw - cw) // 2, (bh - ch) // 2
            fr_img = p["big"].crop((x0, y0, x0 + cw, y0 + ch)).resize((RW, RH), Image.BILINEAR).convert("RGBA")
            t_loc = k / FPS
            if reveal == 0 or t_loc >= reveal:
                key = (pi, p["n"], 0)
                if key not in cache:
                    cache[key] = calque_texte(p["lignes"], p["n"])
                lay = cache[key]
            else:
                prog = t_loc / reveal * p["n"]
                nm = max(1, int(prog) + 1)
                frac = prog - int(prog)
                mont = int(18 * (1 - min(1, frac * 2)))
                key = (pi, nm, mont)
                if key not in cache:
                    cache[key] = calque_texte(p["lignes"], nm, mont)
                lay = cache[key]
            fr_img.alpha_composite(lay)
            fr_img.alpha_composite(marque)
            if k == n_f - 1:
                fr_img.convert("RGB").save(os.path.join(apercu_dir, f"{pi + 1:02d}.jpg"), quality=88)
            proc.stdin.write(fr_img.convert("RGB").tobytes())
        f += n_f
        t_debut += p["dur"]
        cache = {k: v for k, v in cache.items() if k[0] == pi + 1}
    proc.stdin.close()
    proc.wait()
    return out, round(total, 1), [os.path.join(apercu_dir, f"{i + 1:02d}.jpg") for i in range(len(plans))]
