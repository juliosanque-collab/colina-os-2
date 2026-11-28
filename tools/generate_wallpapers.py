#!/usr/bin/env python3
"""Genera los fondos de colinas de Colina OS con un render 3D procedural.

No usa fotos ni imágenes de terceros: el terreno (colinas, campos de cultivo, setos y
bosques), el cielo con nubes, la niebla y las sombras se calculan por código.

Requiere:  python3-numpy  python3-scipy  python3-pil

Uso:
    python3 tools/generate_wallpapers.py                 # los 5 fondos en 1920x1080
    python3 tools/generate_wallpapers.py manana          # solo uno
    python3 tools/generate_wallpapers.py manana --size 640x360 --out /tmp/prueba.jpg
"""
import argparse
import copy
import math
import multiprocessing as mp
import sys
import time
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage
from scipy.spatial import cKDTree

ROOT = Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "config/includes.chroot/usr/share/backgrounds/colina"

N = 2048            # celdas por lado del mapa de terreno
CELL = 6.0          # metros por celda
WORLD = N * CELL    # el terreno se repite cada WORLD metros


# --------------------------------------------------------------- utilidades ----
def lin(hexcolor):
    h = hexcolor.lstrip("#")
    v = np.array([int(h[i:i + 2], 16) for i in (0, 2, 4)], np.float32) / 255.0
    return v ** 2.2


def smoothstep(a, b, x):
    t = np.clip((x - a) / (b - a), 0.0, 1.0)
    return t * t * (3.0 - 2.0 * t)


class Grid:
    """Rejilla periódica con muestreo bilineal (1 o 3 canales)."""

    def __init__(self, a):
        a = np.ascontiguousarray(a, np.float32)
        self.n = a.shape[0]
        self.m = self.n - 1
        self.ch = 1 if a.ndim == 2 else a.shape[2]
        self.flat = a.reshape(self.n * self.n, self.ch)

    def __call__(self, u, v):
        n, m = self.n, self.m
        u0 = np.floor(u)
        v0 = np.floor(v)
        fu = (u - u0).astype(np.float32)
        fv = (v - v0).astype(np.float32)
        i0 = u0.astype(np.int32) & m
        j0 = v0.astype(np.int32) & m
        i1 = (i0 + 1) & m
        j1 = (j0 + 1) & m
        r0 = j0 * n
        r1 = j1 * n
        f = self.flat
        a00, a10, a01, a11 = f[r0 + i0], f[r0 + i1], f[r1 + i0], f[r1 + i1]
        if self.ch == 1:
            a00, a10, a01, a11 = a00[:, 0], a10[:, 0], a01[:, 0], a11[:, 0]
        else:
            fu, fv = fu[:, None], fv[:, None]
        return (a00 + (a10 - a00) * fu) * (1 - fv) + (a01 + (a11 - a01) * fu) * fv

    def nearest(self, u, v):
        i = np.floor(u).astype(np.int32) & self.m
        j = np.floor(v).astype(np.int32) & self.m
        r = self.flat[j * self.n + i]
        return r[:, 0] if self.ch == 1 else r


def spectral(rng, n, beta, wl_min=None, wl_max=None):
    """Ruido periódico con espectro de potencia k^-beta (longitudes de onda en celdas)."""
    w = rng.standard_normal((n, n)).astype(np.float32)
    F = np.fft.rfft2(w)
    ky = np.fft.fftfreq(n)[:, None]
    kx = np.fft.rfftfreq(n)[None, :]
    k = np.hypot(kx, ky)
    k[0, 0] = 1.0
    amp = k ** (-beta / 2.0)
    if wl_min:
        amp = amp * np.exp(-(k * wl_min) ** 2)
    if wl_max:
        amp = amp * (1.0 - np.exp(-(k * wl_max) ** 2))
    amp[0, 0] = 0.0
    out = np.fft.irfft2(F * amp, s=(n, n)).astype(np.float32)
    out -= out.mean()
    out /= out.std()
    return out


# ------------------------------------------------------------------ escenas ----
# Colores en sRGB (hex). Ángulos en grados. Alturas y distancias en metros.
SCENES = {
    # Mañana despejada: luz lateral, cúmulos ligeros y campiña en capas
    "manana": dict(
        file="colina-manana.jpg", seed=21,
        cam=dict(auto=True, h=42, fov=45, sky_frac=0.40),
        terrain=dict(amp=30, beta=3.4, wl_min=28, wl_max=300, amp2=85, warp=6, hedge_h=5.0, wood_h=11),
        fields=dict(n=1900, wood=0.10, pasture=0.45, hedge=0.8, palette=[
            "#6c9a3a", "#789f40", "#5d8a30", "#8fa645", "#a3a350", "#b8a55c", "#7a9a42", "#86683f"]),
        sun=dict(az_rel=-68, el=20, col="#fff0d2", i=3.6),
        sky=dict(zen="#2a67c9", hor="#a9cdee", amb="#6f9bd6", amb_i=1.05, bounce="#5a6a35"),
        clouds=dict(alt=2000, scale=95, lo=0.30, hi=0.62, bias=0.12, lit="#ffffff", dark="#8ea3c3", cirrus=0.30),
        fog=dict(ext=0.00015, y0=0, hf=700, col="#b3d0ee", sun_col="#ffeccb", sun_pow=6, sun_amt=0.5),
        exposure=1.0, sat=0.97, flowers=None),

    # Primavera: sol alto, grandes cúmulos, colza amarilla y flores silvestres
    "primavera": dict(
        file="colina-primavera.jpg", seed=7,
        cam=dict(auto=True, h=38, fov=45, sky_frac=0.36),
        terrain=dict(amp=34, beta=3.3, wl_min=26, wl_max=280, amp2=75, warp=6, hedge_h=5.0, wood_h=10),
        fields=dict(n=1700, wood=0.09, pasture=0.55, hedge=0.85, palette=[
            "#62a032", "#6fae38", "#58952c", "#7fb53c", "#6aa836", "#8ab640", "#5f9a30", "#d9c93a", "#a9b34a"]),
        tree_cols=["#2f5a20", "#47782a", "#6a9a34"],
        sun=dict(az_rel=-45, el=46, col="#fff6e0", i=3.4),
        sky=dict(zen="#1f62cc", hor="#9fcaf0", amb="#6a9bdc", amb_i=1.1, bounce="#5a7a35"),
        clouds=dict(alt=1800, scale=85, lo=0.22, hi=0.52, bias=0.18, lit="#ffffff", dark="#8fa6c8", cirrus=0.12),
        fog=dict(ext=0.00011, y0=0, hf=700, col="#b0d2f0", sun_col="#fff2d8", sun_pow=6, sun_amt=0.35),
        exposure=0.93, sat=1.0,
        flowers=dict(thr=2.15, dist=300, cols=["#ffffff", "#ffe34a", "#d6a8ee", "#ffffff"])),

    # Atardecer: luz dorada rasante, sombras largas, cielo cálido
    "atardecer": dict(
        file="colina-atardecer.jpg", seed=4,
        cam=dict(auto=True, h=40, fov=45, sky_frac=0.42),
        terrain=dict(amp=32, beta=3.4, wl_min=28, wl_max=300, amp2=90, warp=6, hedge_h=5.0, wood_h=11),
        fields=dict(n=1900, wood=0.11, pasture=0.5, hedge=0.8, palette=[
            "#8a9a3a", "#9aa240", "#7c8e34", "#b3a548", "#c2a64e", "#a8803f", "#889a3c", "#8f6a3a"]),
        tree_cols=["#34481c", "#4a5e22", "#6a6a28"],
        sun=dict(az_rel=-24, el=7, col="#ffb868", i=4.6, glow=1.3),
        sky=dict(zen="#25458c", hor="#f3b27c", amb="#5a6ca8", amb_i=0.95, bounce="#6a5a30"),
        clouds=dict(alt=2200, scale=90, lo=0.30, hi=0.64, bias=0.14, lit="#ffd2a0", dark="#6a5c88", cirrus=0.45),
        fog=dict(ext=0.00019, y0=0, hf=800, col="#e8a878", sun_col="#ffc07a", sun_pow=5, sun_amt=0.75),
        exposure=0.95, sat=1.02, flowers=None),

    # Amanecer con niebla: valles llenos de bruma y crestas en capas
    "niebla": dict(
        file="colina-niebla.jpg", seed=4,
        cam=dict(auto=True, h=60, fov=45, sky_frac=0.38),
        terrain=dict(amp=36, beta=3.3, wl_min=26, wl_max=300, amp2=110, warp=6, hedge_h=5.0, wood_h=12),
        fields=dict(n=1700, wood=0.16, pasture=0.5, hedge=0.8, palette=[
            "#5f8a40", "#6a9444", "#547f38", "#7d9a48", "#8f9a52", "#a09a58", "#6d9040", "#7a6a46"]),
        tree_cols=["#2a4424", "#3a5a2c", "#4c6a34"],
        sun=dict(az_rel=-30, el=9, col="#ffe0b8", i=3.0, glow=1.2),
        sky=dict(zen="#6f93c4", hor="#e8d9d2", amb="#8aa4c8", amb_i=1.0, bounce="#5a6a40"),
        clouds=dict(alt=2600, scale=100, lo=0.40, hi=0.80, bias=0.0, lit="#fff0e6", dark="#a8b2c8", cirrus=0.25),
        fog=dict(ext=0.0009, y0=-10, hf=170, col="#dcd6dc", sun_col="#ffddb4", sun_pow=4, sun_amt=0.6),
        exposure=1.0, sat=0.92, flowers=None),

    # Otoño: arbolado dorado y rojizo, cielo con nubes movidas
    "otono": dict(
        file="colina-otono.jpg", seed=4,
        cam=dict(auto=True, h=42, fov=45, sky_frac=0.40),
        terrain=dict(amp=32, beta=3.4, wl_min=28, wl_max=300, amp2=90, warp=6, hedge_h=5.5, wood_h=12),
        fields=dict(n=1800, wood=0.16, pasture=0.45, hedge=0.85, palette=[
            "#7f9a3a", "#8f9c40", "#6f8a36", "#a89a46", "#9a7e3c", "#7f6038", "#86963f", "#9c8a3e"]),
        tree_cols=["#8a3a18", "#b8681c", "#d49a2a", "#5a6a26"],
        sun=dict(az_rel=-60, el=26, col="#ffe9c4", i=3.7),
        sky=dict(zen="#3e6cb8", hor="#bccfe0", amb="#6a92cc", amb_i=1.0, bounce="#6a5a30"),
        clouds=dict(alt=1900, scale=95, lo=0.24, hi=0.52, bias=0.2, lit="#ffffff", dark="#7a8aa6", cirrus=0.2),
        fog=dict(ext=0.00015, y0=0, hf=700, col="#c4d3e2", sun_col="#ffe6c0", sun_pow=6, sun_amt=0.45),
        exposure=0.93, sat=1.05, flowers=None),
}


# ------------------------------------------------------------------ terreno ----
class Land:
    """Mapas del mundo: altura, normales, albedo y propiedades de cada campo."""

    def __init__(self, sc):
        rng = np.random.default_rng(sc["seed"])
        t, f = sc["terrain"], sc["fields"]
        self.sc = sc
        gz, gx = np.mgrid[0:N, 0:N].astype(np.float32)

        # relieve base + deformación para que las colinas no sean isótropas
        base = spectral(rng, N, t["beta"], wl_min=t["wl_min"], wl_max=t["wl_max"])
        wx = spectral(rng, N, 3.0, wl_min=80, wl_max=500) * t["warp"]
        wz = spectral(rng, N, 3.0, wl_min=80, wl_max=500) * t["warp"]
        base = ndimage.map_coordinates(base, [gz + wz, gx + wx], order=1, mode="grid-wrap")
        large = spectral(rng, N, 3.0, wl_min=200, wl_max=1200)
        H = base * t["amp"] + large * t.get("amp2", 0)

        # campos (Voronoi periódico)
        M = f["n"]
        pts = rng.random((M, 2)) * N
        allp = np.concatenate([pts + [dx * N, dz * N] for dx in (-1, 0, 1) for dz in (-1, 0, 1)])
        tree = cKDTree(allp)
        q = np.stack([(gx + 0.5).ravel(), (gz + 0.5).ravel()], 1)
        d, ix = tree.query(q, k=2, workers=-1)
        label = (ix[:, 0] % M).astype(np.int32).reshape(N, N)
        other = (ix[:, 1] % M).astype(np.int32).reshape(N, N)
        gap = ((d[:, 1] - d[:, 0]) * CELL).reshape(N, N).astype(np.float32)  # ~2x distancia al borde

        pal = np.stack([lin(c) for c in f["palette"]])
        pick = rng.integers(0, len(pal), M)
        cell_col = pal[pick] * (0.88 + 0.24 * rng.random((M, 1)).astype(np.float32))
        wn = spectral(rng, N, 2.6, wl_min=40, wl_max=700)
        site = wn[np.clip(pts[:, 1].astype(int), 0, N - 1), np.clip(pts[:, 0].astype(int), 0, N - 1)]
        is_wood = site > np.quantile(site, 1.0 - f["wood"])
        is_past = (~is_wood) & (rng.random(M) < f["pasture"])
        ang = rng.random(M) * math.pi
        spacing = np.where(is_past, 9 + 9 * rng.random(M), 2.6 + 2.5 * rng.random(M))
        stripe_amp = np.where(is_past, 0.05, 0.07) * (0.6 + 0.8 * rng.random(M))
        stripe_amp[is_wood] = 0
        phase = rng.random(M) * 6.28

        # setos entre campos (no todos los bordes tienen)
        lo_id = np.minimum(label, other).astype(np.int64)
        hi_id = np.maximum(label, other).astype(np.int64)
        hsh = ((lo_id * 73856093) ^ (hi_id * 19349663)) % 1000 / 1000.0
        hedge_on = (hsh < f["hedge"]).astype(np.float32)
        hedge = (1.0 - smoothstep(1.5, 6.0, gap * 0.5)) * hedge_on

        # bosques: dosel irregular
        wood_f = ndimage.gaussian_filter(is_wood[label].astype(np.float32), 1.2)
        trees_n = spectral(rng, N, 0.8, wl_min=2.2)
        canopy = np.clip(0.5 + 0.3 * trees_n, 0.0, 1.0)
        tall = smoothstep(1.2, 2.2, trees_n) * np.clip(hedge * 1.5, 0, 1)
        tall = ndimage.gaussian_filter(tall, 1.3)
        H = H + hedge * t["hedge_h"] * (0.55 + 0.25 * np.clip(trees_n, -1, 2)) + tall * t["hedge_h"] * 3.2
        H = H + wood_f * t["wood_h"] * (0.35 + 0.65 * canopy)
        H = H.astype(np.float32)
        self.H = H
        self.hmax = float(H.max())

        # normales y oclusión ambiental
        dHdz, dHdx = np.gradient(H, CELL)
        nrm = np.sqrt(dHdx ** 2 + 1.0 + dHdz ** 2)
        nx, nz = (-dHdx / nrm).astype(np.float32), (-dHdz / nrm).astype(np.float32)
        slope = np.sqrt(dHdx ** 2 + dHdz ** 2)
        blur = ndimage.gaussian_filter(H, 9, mode="wrap")
        ao = np.clip(1.0 + (H - blur) * 0.010, 0.55, 1.12).astype(np.float32)

        # albedo precalculado
        mott = spectral(rng, N, 2.0, wl_min=4, wl_max=70)
        alb = cell_col[label] * (1.0 + 0.24 * mott[..., None])
        rock = lin("#7a6f5a")
        alb = alb * (1 - 0.0) + 0.0
        rockmix = smoothstep(0.45, 0.9, slope)[..., None] * 0.55
        alb = alb * (1 - rockmix) + rock * rockmix
        veg = np.clip(np.maximum(hedge, wood_f), 0, 1)[..., None]
        tcols = np.stack([lin(c) for c in sc.get("tree_cols", ["#2f4f1c", "#3f6a24", "#56802c"])])
        tn2 = spectral(rng, N, 1.6, wl_min=3)
        pos = np.clip(0.5 + 0.32 * tn2, 0, 0.999) * (len(tcols) - 1)
        k0 = np.floor(pos).astype(int)
        fr = (pos - k0)[..., None]
        tree_col = tcols[k0] * (1 - fr) + tcols[np.minimum(k0 + 1, len(tcols) - 1)] * fr
        tree_col = tree_col * (0.65 + 0.7 * np.clip(trees_n[..., None] * 0.5 + 0.5, 0, 1))
        alb = alb * (1 - veg) + tree_col * veg

        self.G_H = Grid(H)
        self.G_nx, self.G_nz = Grid(nx), Grid(nz)
        self.G_ao = Grid(ao)
        self.G_alb = Grid(alb.astype(np.float32))
        self.G_label = Grid(label.astype(np.float32))
        self.G_veg = Grid(veg[..., 0])
        self.label = label
        self.stripe = dict(ang=ang.astype(np.float32), spacing=spacing.astype(np.float32),
                           amp=stripe_amp.astype(np.float32), phase=phase.astype(np.float32))
        # texturas finas (periódicas)
        self.G_micro = Grid(spectral(rng, 1024, 1.2, wl_min=2))
        self.G_meso = Grid(spectral(rng, 1024, 1.8, wl_min=3, wl_max=250))
        self.G_flow = Grid(spectral(rng, 1024, 0.0, wl_min=1.2))
        # nubes
        self.G_cloud = Grid(spectral(rng, 1024, 2.9, wl_min=5, wl_max=260))
        self.G_cirrus = Grid(spectral(rng, 1024, 2.0, wl_min=2.0, wl_max=200))



# ------------------------------------------------------------------ cámara ----
def choose_camera(land, sc):
    """Busca una loma desde la que se vean varias capas de colinas hacia el horizonte."""
    cam = dict(sc["cam"])
    if not cam.get("auto"):
        return cam
    rng = np.random.default_rng(sc["seed"] + 1)
    sm = ndimage.gaussian_filter(land.H, 40, mode="wrap")
    thr = np.quantile(sm, 0.70)
    jj, ii = np.nonzero(sm > thr)
    pick = rng.choice(len(ii), 260, replace=False)
    ts = np.geomspace(110, 9000, 110)
    best, best_s = None, -1e9
    for k in pick:
        cx, cz = (ii[k] + 0.5) * CELL, (jj[k] + 0.5) * CELL
        oy = float(land.G_H(np.array([cx / CELL]), np.array([cz / CELL]))[0]) + cam["h"]
        for yaw in range(0, 360, 8):
            yr = math.radians(yaw)
            hh = land.G_H((cx + math.sin(yr) * ts) / CELL, (cz + math.cos(yr) * ts) / CELL)
            ang = np.degrees(np.arctan2(hh - oy, ts))
            run = np.maximum.accumulate(ang)
            prev = np.concatenate([[-90.0], run[:-1]])
            peaks = (ang[1:-1] > ang[:-2]) & (ang[1:-1] >= ang[2:]) & (ang[1:-1] > prev[1:-1] + 0.12)
            ridges = int(peaks.sum())
            near = ang[:6].mean()
            sky = run[-1]
            vg = float(land.G_veg((cx + math.sin(yr) * ts[:28]) / CELL, (cz + math.cos(yr) * ts[:28]) / CELL).mean())
            score = (min(ridges, 6) * 1.0 - abs(near + 9.0) * 0.18 - max(0.0, sky - 3.0) * 1.2
                     - max(0.0, -1.0 - sky) * 0.6 - vg * 9.0 + rng.random() * 0.4)
            if score > best_s:
                best_s, best = score, (cx, cz, yaw, sky)
    cx, cz, yaw, sky = best
    th = math.tan(math.radians(cam["fov"]) / 2)
    v = 1.0 - 2.0 * cam.get("sky_frac", 0.40)
    cam.update(x=cx, z=cz, yaw=yaw + cam.get("yaw_off", 0),
               pitch=sky - math.degrees(math.atan(v * th)))
    return cam

def camera_basis(cam):
    yaw, pitch = math.radians(cam["yaw"]), math.radians(cam["pitch"])
    f = np.array([math.sin(yaw) * math.cos(pitch), math.sin(pitch), math.cos(yaw) * math.cos(pitch)])
    r = np.array([math.cos(yaw), 0.0, -math.sin(yaw)])
    u = np.cross(f, r)
    return f, r, u


def sun_vec(az, el):
    az, el = math.radians(az), math.radians(el)
    return np.array([math.sin(az) * math.cos(el), math.sin(el), math.cos(az) * math.cos(el)], np.float32)


# -------------------------------------------------------------------- cielo ----
def sky_color(d, o, sc, L):
    s = sc["sky"]
    zen, hor = lin(s["zen"]), lin(s["hor"])
    e = d[:, 1]
    g = np.clip(e, 0, 1) ** 0.42
    col = hor + (zen - hor) * g[:, None]
    sun = lin(sc["sun"]["col"])
    cs = np.clip(d @ L, 0, 1)
    glow = (0.10 * cs ** 4 + 0.30 * cs ** 32 + 0.55 * cs ** 160 + 0.9 * cs ** 900)
    horizon_w = np.exp(-np.clip(e, 0, 1) * 6.0)
    col = col + sun * (glow * (0.35 + 0.65 * horizon_w) * sc["sun"].get("glow", 1.0))[:, None]
    disc = smoothstep(0.999955, 0.999985, cs)
    col = col + sun * (disc * 40.0)[:, None]
    fw = np.exp(-np.clip(e, 0, 1) * 38.0)[:, None]
    col = col * (1 - fw) + fog_color(sc, d, L) * fw
    return col, cs


def add_clouds(col, d, o, sc, land, L):
    c = sc["clouds"]
    if not c:
        return col
    e = d[:, 1]
    ok = e > 0.012
    if not ok.any():
        return col
    idx = np.nonzero(ok)[0]
    de = d[idx]
    tc = (c["alt"] - o[1]) / de[:, 1]
    px = o[0] + de[:, 0] * tc
    pz = o[2] + de[:, 2] * tc
    cs = c["scale"]
    u, v = px / cs, pz / cs
    n1 = land.G_cloud(u, v)
    su = (L[0] / max(L[1], 0.15)) * 1.6
    sv = (L[2] / max(L[1], 0.15)) * 1.6
    n2 = land.G_cloud(u + su, v + sv)
    dens = n1 * 0.5 + c["bias"]
    cov = smoothstep(c["lo"], c["hi"], dens)
    shade = np.clip(0.58 + (n1 - n2) * 1.5, 0, 1) * (1.0 - 0.45 * smoothstep(0.3, 1.5, dens))
    lit, dark = lin(c["lit"]), lin(c["dark"])
    sun = lin(sc["sun"]["col"])
    ccol = dark + (lit * (0.55 + 0.45 * sun / max(sun.max(), 1e-3)) - dark) * shade[:, None]
    ccol = ccol * (1.0 + 0.0)
    # velos de cirros
    ci = c.get("cirrus", 0)
    if ci:
        cc = land.G_cirrus(u * 0.25 + 40, v * 1.4)
        cir = smoothstep(0.2, 1.6, cc) * ci
        cov = 1 - (1 - cov) * (1 - cir * (1 - cov * 0.6))
        ccol = ccol * (1 - cir[:, None] * 0.3) + lit * (cir[:, None] * 0.3)
    fade = smoothstep(0.012, 0.16, de[:, 1])
    hazew = (1.0 - fade) * 0.85
    hor = lin(sc["sky"]["hor"])
    ccol = ccol * (1 - hazew[:, None]) + hor * hazew[:, None]
    a = (cov * (0.35 + 0.65 * fade))[:, None]
    out = col.copy()
    out[idx] = col[idx] * (1 - a) + ccol * a * 1.0
    return out


# ----------------------------------------------------------------- marcha ----
def march(land, o, d, tmax):
    n = d.shape[0]
    G = land.G_H
    hmax = land.hmax + 2
    res = np.full(n, np.nan, np.float32)
    idx = np.arange(n)
    dx, dy, dz = d[:, 0].copy(), d[:, 1].copy(), d[:, 2].copy()
    t = np.full(n, 2.0, np.float32)
    lo = np.zeros(n, np.float32)
    inv = np.float32(1.0 / CELL)
    for _ in range(900):
        if idx.size == 0:
            break
        x = o[0] + dx * t
        z = o[2] + dz * t
        y = o[1] + dy * t
        h = G(x * inv, z * inv)
        c = y - h
        hitm = c < 0
        if hitm.any():
            a, b = lo[hitm].copy(), t[hitm].copy()
            hx, hy, hz = dx[hitm], dy[hitm], dz[hitm]
            for _k in range(7):
                m = 0.5 * (a + b)
                below = (o[1] + hy * m) < G((o[0] + hx * m) * inv, (o[2] + hz * m) * inv)
                b = np.where(below, m, b)
                a = np.where(below, a, m)
            res[idx[hitm]] = 0.5 * (a + b)
        esc = (t > tmax) | ((y > hmax) & (dy > 0))
        keep = ~(hitm | esc)
        dt = np.maximum(0.45 * c, 0.012 * t + 1.0)
        nt = t + dt
        idx, dx, dy, dz = idx[keep], dx[keep], dy[keep], dz[keep]
        lo, t = t[keep], nt[keep]
    return res


def shadow(land, p, L, soft=6.0):
    G = land.G_H
    inv = np.float32(1.0 / CELL)
    vis = np.ones(p.shape[0], np.float32)
    s = 3.0
    for _ in range(30):
        q = p + L[None, :] * s
        h = G(q[:, 0] * inv, q[:, 2] * inv)
        vis = np.minimum(vis, np.clip(soft * (q[:, 1] - h) / s, 0, 1))
        s *= 1.27
    return vis


def fog_tau(sc, oy, dy, t):
    f = sc["fog"]
    hf = f["hf"]
    k = dy.astype(np.float64) / hf
    t = t.astype(np.float64)
    base = f["ext"] * math.exp(-np.clip((oy - f["y0"]) / hf, -30, 30))
    small = np.abs(k) < 1e-6
    kk = np.where(small, 1.0, k)
    integ = np.where(small, t, (1.0 - np.exp(np.clip(-kk * t, -60, 60))) / kk)
    return (base * integ).astype(np.float32)


def shade_hits(land, sc, o, d, t, L):
    n = d.shape[0]
    p = o[None, :] + d * t[:, None]
    inv = np.float32(1.0 / CELL)
    u, v = p[:, 0] * inv, p[:, 2] * inv
    nx, nz = land.G_nx(u, v), land.G_nz(u, v)
    ny = np.sqrt(np.clip(1.0 - nx * nx - nz * nz, 0.01, 1.0))
    # microrrelieve en la normal para dar textura a la hierba
    mm = land.G_micro(p[:, 0] / 0.05, p[:, 2] / 0.05)
    fade = np.clip(1.0 - t / 500.0, 0, 1)
    nx = nx + 0.10 * (land.G_micro(p[:, 0] / 0.7, p[:, 2] / 0.7)) * fade
    nz = nz + 0.10 * (land.G_micro(p[:, 0] / 0.7 + 100, p[:, 2] / 0.7)) * fade
    nl = np.sqrt(nx * nx + ny * ny + nz * nz)
    nx, ny, nz = nx / nl, ny / nl, nz / nl

    alb = land.G_alb(u, v)
    ao = land.G_ao(u, v)
    veg = land.G_veg(u, v)
    lab = land.G_label.nearest(u, v).astype(np.int32)
    st = land.stripe
    a = st["ang"][lab]
    sp = st["spacing"][lab]
    s = np.sin(2 * math.pi * (p[:, 0] * np.cos(a) + p[:, 2] * np.sin(a)) / sp + st["phase"][lab])
    sfade = np.clip(1.0 - t / 450.0, 0, 1)
    tex = 1.0 + st["amp"][lab] * s * sfade
    meso = land.G_meso(p[:, 0] / 1.2, p[:, 2] / 1.2)
    tex = tex * (1.0 + (0.10 + 0.12 * veg) * meso * fade + 0.17 * mm * np.clip(1 - t / 300.0, 0, 1))
    alb = alb * tex[:, None]

    fl = sc.get("flowers")
    if fl:
        ff = land.G_flow(p[:, 0] / 0.12, p[:, 2] / 0.12)
        fm = smoothstep(fl["thr"], fl["thr"] + 0.5, ff) * np.clip(1 - t / fl["dist"], 0, 1) * (1 - veg)
        pick = (np.floor(land.G_flow.nearest(p[:, 0] / 0.12 + 7, p[:, 2] / 0.12 + 3) * 3) % len(fl["cols"])).astype(int)
        fcol = np.stack([lin(c) for c in fl["cols"]])[pick]
        alb = alb * (1 - fm[:, None]) + fcol * fm[:, None]

    ndl = np.clip(nx * L[0] + ny * L[1] + nz * L[2], 0, 1)
    vis = np.ones(n, np.float32)
    m = ndl > 0.0
    if m.any():
        pm = p[m] + np.stack([nx[m], ny[m], nz[m]], 1) * 0.6
        vis[m] = shadow(land, pm, L)
    sun = lin(sc["sun"]["col"]) * sc["sun"]["i"]
    sk = sc["sky"]
    amb_sky = lin(sk["amb"]) * sk["amb_i"]
    bounce = lin(sk["bounce"]) * 0.5 * sk["amb_i"]
    w = (0.5 + 0.5 * ny)[:, None]
    ambient = (amb_sky * w + bounce * (1 - w)) * ao[:, None]
    back = (1.0 - ndl)[:, None] ** 3 * 0.10   # transmisión de la hierba
    direct = sun[None, :] * ((ndl * vis)[:, None] * (0.92 + 0.08 * back / 0.10))
    col = alb * (direct + ambient)
    return col, p


def fog_color(sc, d, L):
    f = sc["fog"]
    c = lin(f["col"])
    sun = lin(f["sun_col"])
    cs = np.clip(d @ L, 0, 1) ** f["sun_pow"]
    return c[None, :] * (1 - f["sun_amt"] * cs[:, None]) + sun[None, :] * (f["sun_amt"] * cs[:, None])


def render_band(args):
    land, sc, W, Hh, r0, r1, cam = args
    f, r, u = camera_basis(cam)
    th = math.tan(math.radians(cam["fov"]) / 2)
    aspect = W / Hh
    xs = ((np.arange(W) + 0.5) / W * 2 - 1) * th * aspect
    ys = (1 - (np.arange(r0, r1) + 0.5) / Hh * 2) * th
    d = (f[None, None, :] + xs[None, :, None] * r[None, None, :] + ys[:, None, None] * u[None, None, :])
    d = d.reshape(-1, 3)
    d /= np.linalg.norm(d, axis=1, keepdims=True)
    d = d.astype(np.float32)
    L = sun_vec(sc["sun"]["az"], sc["sun"]["el"])
    ground = float(land.G_H(np.array([cam["x"] / CELL]), np.array([cam["z"] / CELL]))[0])
    o = np.array([cam["x"], ground + cam["h"], cam["z"]], np.float32)
    tmax = sc.get("tmax", 13000.0)

    t = march(land, o, d, tmax)
    hit = ~np.isnan(t)
    out = np.zeros((d.shape[0], 3), np.float32)
    depth = np.full(d.shape[0], np.inf, np.float32)

    # cielo (también el fondo donde no hay terreno)
    skyc, _ = sky_color(d, o, sc, L)
    skyc = add_clouds(skyc, d, o, sc, land, L)
    out[:] = skyc
    # rayos sin impacto que bajan: horizonte lejano -> color de niebla
    far = (~hit) & (d[:, 1] < 0.02)
    if far.any():
        out[far] = fog_color(sc, d[far], L) * 1.0

    if hit.any():
        hi = np.nonzero(hit)[0]
        th_ = t[hi]
        col, p = shade_hits(land, sc, o, d[hi], th_, L)
        tau = fog_tau(sc, o[1], d[hi, 1], th_)
        tr = np.exp(-tau)[:, None]
        fc = fog_color(sc, d[hi], L)
        out[hi] = col * tr + fc * (1 - tr)
        depth[hi] = th_
    return r0, out.reshape(r1 - r0, W, 3), depth.reshape(r1 - r0, W)


_LAND = None


def _worker(args):
    r0, r1, W, Hh, sc, cam = args
    return render_band((_LAND, sc, W, Hh, r0, r1, cam))


def render_scene(name, W, Hh, ssaa=1.0, workers=2, seed=None, quiet=False):
    global _LAND
    sc = copy.deepcopy(SCENES[name])
    if seed is not None:
        sc["seed"] = seed
    t0 = time.time()
    _LAND = Land(sc)
    sc["cam"] = choose_camera(_LAND, sc)
    if "az_rel" in sc["sun"]:
        sc["sun"]["az"] = sc["cam"]["yaw"] + sc["sun"]["az_rel"]
    if not quiet:
        c = sc["cam"]
        print(f"  terreno listo ({time.time() - t0:.0f}s); cámara x={c['x']:.0f} z={c['z']:.0f} "
              f"yaw={c['yaw']} pitch={c['pitch']:.1f}", flush=True)
    RW, RH = int(W * ssaa), int(Hh * ssaa)
    bands = [(r, min(r + 24, RH), RW, RH, sc, sc["cam"]) for r in range(0, RH, 24)]
    img = np.zeros((RH, RW, 3), np.float32)
    ctx = mp.get_context("fork")
    with ctx.Pool(workers) as pool:
        for k, (r0, band, _depth) in enumerate(pool.imap_unordered(_worker, bands)):
            img[r0:r0 + band.shape[0]] = band
            if not quiet and k % 10 == 0:
                print(f"  {k + 1}/{len(bands)} bandas", flush=True)
    if ssaa != 1.0:
        img = np.stack([np.asarray(Image.fromarray(img[..., c]).resize((W, Hh), Image.LANCZOS))
                        for c in range(3)], -1)
    return tonemap(img, sc, W, Hh)


def tonemap(img, sc, W, Hh):
    x = np.maximum(img, 0) * sc.get("exposure", 1.0)
    # ACES (Narkowicz)
    x = np.clip((x * (2.51 * x + 0.03)) / (x * (2.43 * x + 0.59) + 0.14), 0, 1)
    lum = (x * np.array([0.2126, 0.7152, 0.0722], np.float32)).sum(-1, keepdims=True)
    x = np.clip(lum + (x - lum) * sc.get("sat", 1.0), 0, 1)
    x = np.where(x <= 0.0031308, x * 12.92, 1.055 * np.power(x, 1 / 2.4) - 0.055)
    yy, xx = np.mgrid[0:Hh, 0:W].astype(np.float32)
    r2 = ((xx / W - 0.5) ** 2 * 1.1 + (yy / Hh - 0.5) ** 2 * 1.4)
    x = x * (1.0 - 0.28 * r2[..., None])
    rng = np.random.default_rng(1)
    x = x + (rng.random((Hh, W, 1), dtype=np.float32) - 0.5) / 255.0 * 1.5
    return (np.clip(x, 0, 1) * 255 + 0.5).astype(np.uint8)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("names", nargs="*", help="escenas (por defecto todas)")
    ap.add_argument("--size", default="1920x1080")
    ap.add_argument("--ssaa", type=float, default=1.5)
    ap.add_argument("--out", help="archivo de salida (solo con una escena)")
    ap.add_argument("--seed", type=int)
    ap.add_argument("--workers", type=int, default=2)
    a = ap.parse_args()
    W, Hh = (int(v) for v in a.size.split("x"))
    names = a.names or list(SCENES)
    OUTDIR.mkdir(parents=True, exist_ok=True)
    for nm in names:
        print(f"[{nm}] {W}x{Hh} ssaa={a.ssaa}", flush=True)
        t0 = time.time()
        rgb = render_scene(nm, W, Hh, a.ssaa, a.workers, a.seed)
        out = Path(a.out) if a.out else OUTDIR / SCENES[nm]["file"]
        Image.fromarray(rgb).save(out, quality=90, optimize=True, subsampling=0)
        print(f"  -> {out} ({time.time() - t0:.0f}s)", flush=True)


if __name__ == "__main__":
    main()
