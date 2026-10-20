"""Transforme un carrousel (liste de JPEG 1080x1350) en Reel 1080x1920 avec fondus."""
import sys, os, subprocess, tempfile
from PIL import Image, ImageFilter, ImageEnhance

W, H = 1080, 1920


def frame(src, dst):
    im = Image.open(src).convert("RGB")
    bg = im.resize((W, int(im.height * W / im.width * 1.42))).crop((0, 0, W, H)) if False else im.resize((int(im.width * H / im.height), H))
    x = (bg.width - W) // 2
    bg = bg.crop((x, 0, x + W, H)).filter(ImageFilter.GaussianBlur(40))
    bg = ImageEnhance.Brightness(bg).enhance(0.45)
    bg.paste(im, (0, (H - im.height) // 2))
    bg.save(dst, quality=95)


def reel(slides, out, first=2.4, each=2.6, last=3.2, fade=0.4):
    tmp = tempfile.mkdtemp()
    frames = []
    for i, s in enumerate(slides):
        f = os.path.join(tmp, f"{i:02d}.jpg")
        frame(s, f)
        frames.append(f)
    n = len(frames)
    durs = [first] + [each] * (n - 2) + [last]
    cmd = ["ffmpeg", "-y", "-loglevel", "error"]
    for f, d in zip(frames, durs):
        cmd += ["-loop", "1", "-t", f"{d + fade:.2f}", "-i", f]
    cmd += ["-f", "lavfi", "-t", f"{sum(durs) + fade:.2f}", "-i", "anullsrc=r=44100:cl=stereo"]
    fc, prev, off = [], "0:v", 0.0
    for i in range(1, n):
        off += durs[i - 1]
        lab = f"v{i}"
        fc.append(f"[{prev}][{i}:v]xfade=transition=fade:duration={fade}:offset={off:.2f}[{lab}]")
        prev = lab
    fc.append(f"[{prev}]format=yuv420p,fps=30[vout]")
    cmd += ["-filter_complex", ";".join(fc), "-map", "[vout]", "-map", f"{n}:a",
            "-c:v", "libx264", "-preset", "medium", "-crf", "21", "-profile:v", "high",
            "-c:a", "aac", "-b:a", "128k", "-shortest", "-movflags", "+faststart", out]
    subprocess.run(cmd, check=True)
    return out


if __name__ == "__main__":
    d, out = sys.argv[1], sys.argv[2]
    sl = sorted(os.path.join(d, f) for f in os.listdir(d) if f.endswith(".jpg"))
    reel(sl, out)
    print(out)
