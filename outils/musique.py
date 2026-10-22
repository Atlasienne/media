"""Atlasienne - musique d'ambiance originale (générée, libre de droits, sponsorisable).
Pad doux + arpège pincé + pulsation légère. Sortie WAV 44,1 kHz stéréo."""
import numpy as np, wave, sys

SR = 44100


def note(n):  # n : numéro MIDI
    return 440.0 * 2 ** ((n - 69) / 12)


def pluck(freq, dur, decay=0.996):
    n = int(SR * dur)
    p = max(2, int(SR / freq))
    buf = np.random.uniform(-1, 1, p)
    out = np.zeros(n)
    for i in range(n):
        out[i] = buf[i % p]
        buf[i % p] = decay * 0.5 * (buf[i % p] + buf[(i + 1) % p])
    return out


def pad(freqs, dur):
    t = np.arange(int(SR * dur)) / SR
    s = sum(np.sin(2 * np.pi * f * t) * 0.6 + np.sin(2 * np.pi * f * 2.003 * t) * 0.15 for f in freqs)
    env = np.minimum(1, t / 0.6) * np.minimum(1, (dur - t) / 0.6)
    return s * env / len(freqs)


def kick(dur=0.25):
    t = np.arange(int(SR * dur)) / SR
    f = 55 + 70 * np.exp(-t * 30)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 14)


def shaker(dur=0.06):
    t = np.arange(int(SR * dur)) / SR
    return np.random.uniform(-1, 1, len(t)) * np.exp(-t * 70)


def morceau(path, bpm=92, racine=57, longueur=32.0, seed=1):
    np.random.seed(seed)
    beat = 60 / bpm
    # progression vi IV I V (couleur chaleureuse)
    prog = [(0, [0, 3, 7]), (-4, [0, 4, 7]), (3, [0, 4, 7]), (-2, [0, 4, 7])]
    total = int(SR * longueur)
    L = np.zeros(total); R = np.zeros(total)
    bar = 4 * beat
    t0, k = 0.0, 0
    while t0 < longueur:
        deg, tri = prog[k % 4]
        base = racine + deg
        fr = [note(base + i - 12) for i in tri]
        p = pad(fr, bar + 0.4)
        i0 = int(t0 * SR); i1 = min(total, i0 + len(p))
        L[i0:i1] += p[:i1 - i0] * 0.22; R[i0:i1] += p[:i1 - i0] * 0.22
        # arpège en croches
        arp = [base + tri[0], base + tri[1], base + tri[2], base + 12, base + tri[2], base + tri[1], base + tri[0], base + tri[1]]
        for j, n in enumerate(arp):
            ts = t0 + j * beat / 2
            if ts >= longueur:
                break
            s = pluck(note(n), beat * 1.5) * 0.16
            a = int(ts * SR); b = min(total, a + len(s))
            pan = 0.35 + 0.3 * (j % 2)
            L[a:b] += s[:b - a] * (1 - pan); R[a:b] += s[:b - a] * pan
        for j in range(4):
            ts = t0 + j * beat
            if ts >= longueur:
                break
            kk = kick() * (0.35 if j % 2 == 0 else 0.22)
            a = int(ts * SR); b = min(total, a + len(kk))
            L[a:b] += kk[:b - a]; R[a:b] += kk[:b - a]
            for h in (0.5,):
                sh = shaker() * 0.05
                a2 = int((ts + h * beat) * SR); b2 = min(total, a2 + len(sh))
                if a2 < total:
                    L[a2:b2] += sh[:b2 - a2] * 0.8; R[a2:b2] += sh[:b2 - a2]
        t0 += bar; k += 1
    st = np.stack([L, R], 1)
    st = np.tanh(st * 1.4) / np.tanh(1.4)
    st = st / np.max(np.abs(st)) * 0.7
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((st * 32767).astype(np.int16).tobytes())
    return path


if __name__ == "__main__":
    import os
    d = "/home/claude/atlasienne/musique/"
    os.makedirs(d, exist_ok=True)
    morceau(d + "ambiance_a.wav", bpm=92, racine=57, seed=1)
    morceau(d + "ambiance_b.wav", bpm=100, racine=60, seed=7)
    morceau(d + "ambiance_c.wav", bpm=86, racine=55, seed=3)
    print("ok")
