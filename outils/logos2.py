import sys; sys.path.insert(0, "/home/claude/atlasienne")
exec(open("logos.py").read().split("concepts = {")[0])

def tisse(d, cx, cy, r, col, lw, barbs=True):
    k = 0.80
    pts = [(cx, cy - r), (cx + r * k, cy), (cx, cy + r), (cx - r * k, cy)]
    d.line(pts + [pts[0]], fill=col, width=lw, joint="curve")
    if barbs:  # petites franges perpendiculaires, comme les losanges des tapis de l'Atlas
        for (a, b) in zip(pts, pts[1:] + pts[:1]):
            for t in (0.25, 0.5, 0.75):
                x = a[0] + (b[0] - a[0]) * t; y = a[1] + (b[1] - a[1]) * t
                dx, dy = b[0] - a[0], b[1] - a[1]; L = (dx * dx + dy * dy) ** .5
                nx, ny = -dy / L, dx / L
                q = r * 0.11
                d.line([(x - nx * q, y - ny * q), (x + nx * q, y + ny * q)], fill=col, width=int(lw * 0.75))

def v(barbs, inner_A):
    img, d, n = canvas()
    cx, cy, r = n / 2, n / 2, n * 0.36
    lw = int(n * 0.04)
    tisse(d, cx, cy, r, PAPIER, lw, barbs)
    hh = r * 0.48
    d.line([(cx - hh * 0.82, cy + hh * 0.62), (cx, cy - hh * 0.70), (cx + hh * 0.82, cy + hh * 0.62)],
           fill=ROSE, width=int(lw * 1.3), joint="curve")
    if inner_A:
        d.line([(cx - hh * 0.40, cy + hh * 0.18), (cx + hh * 0.40, cy + hh * 0.18)], fill=ROSE, width=int(lw * 0.9))
    else:
        q = lw * 1.0
        d.ellipse([cx - q, cy + hh * 0.30 - q, cx + q, cy + hh * 0.30 + q], fill=ROSE)
    return done(img)

vs = {"A_franges_point": v(True, False), "B_franges_barre": v(True, True), "C_simple_point": v(False, False)}
for k, im in vs.items(): im.save(OUTL + "losange_" + k + ".png")
b = Image.new("RGB", (1900, 760), "white"); d = ImageDraw.Draw(b)
for i, (k, im) in enumerate(vs.items()):
    x = 50 + i * 620
    d.text((x, 30), k.replace("_", " "), font=sans(38, 600), fill=ENCRE, anchor="lt")
    for sz, (ox, oy) in [(480, (0, 100)), (110, (0, 610)), (40, (150, 645))]:
        a = im.resize((sz, sz), Image.LANCZOS); m = Image.new("L", (sz*4, sz*4), 0); ImageDraw.Draw(m).ellipse([0,0,sz*4,sz*4], fill=255)
        b.paste(a, (x + ox, oy), m.resize((sz, sz), Image.LANCZOS))
b.save(OUTL + "planche_losange.png"); print("ok")
