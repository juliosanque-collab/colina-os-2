#!/usr/bin/env python3
"""Genera los recursos gráficos originales de Colina OS.

  - Tema de ventanas xfwm4 "ColinaClassic" (imágenes .xpm + themerc)

Los fondos están en generate_wallpapers.py y los iconos en generate_icons.py.

Uso:  python3 tools/generate_assets.py

Todo el arte se calcula por código; no usa ningún recurso de terceros.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
THEME = ROOT / "config/includes.chroot/usr/share/themes/ColinaClassic/xfwm4"

TITLE_H = 30    # alto de la barra de título
BORDER = 4      # grosor de los bordes
CORNER_W = 8    # ancho de las esquinas
BTN = 22        # tamaño de los botones de ventana
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


# ---------------------------------------------------------------- color ----
def rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def to_hex(c):
    return "#%02x%02x%02x" % tuple(max(0, min(255, round(v))) for v in c)


def gradient(stops, t):
    """stops: [(posición 0..1, '#hex'), ...] ordenadas; t en 0..1."""
    t = max(0.0, min(1.0, t))
    for (p0, c0), (p1, c1) in zip(stops, stops[1:]):
        if t <= p1:
            u = 0.0 if p1 == p0 else (t - p0) / (p1 - p0)
            a, b = rgb(c0), rgb(c1)
            return to_hex(tuple(x + (y - x) * u for x, y in zip(a, b)))
    return stops[-1][1]


# ------------------------------------------------------------------ XPM ----
def write_xpm(path, name, pixels):
    """pixels: lista de filas; cada pixel es '#rrggbb' o None (transparente)."""
    h, w = len(pixels), len(pixels[0])
    index, colors = {}, []
    for row in pixels:
        for p in row:
            if p not in index:
                index[p] = len(colors)
                colors.append(p)
    cpp = 1 if len(colors) <= len(ALPHABET) else 2

    def code(i):
        if cpp == 1:
            return ALPHABET[i]
        return ALPHABET[i // len(ALPHABET)] + ALPHABET[i % len(ALPHABET)]

    ident = name.replace("-", "_")
    lines = ["/* XPM */", f"static char * {ident}_xpm[] = {{",
             f'"{w} {h} {len(colors)} {cpp}",']
    for c in colors:
        lines.append(f'"{code(index[c])} c {"None" if c is None else c}",')
    body = ['"' + "".join(code(index[p]) for p in row) + '"' for row in pixels]
    lines.append(",\n".join(body))
    lines.append("};")
    path.write_text("\n".join(lines) + "\n")


# ----------------------------------------------------------- marco/título ----
ACTIVE = dict(
    title=[(0, "#4b97ff"), (0.10, "#2f7bf2"), (0.45, "#1a5fdc"), (0.85, "#1350c6"), (1, "#0d41a8")],
    border="#1655d0", outline="#0a2f80", shine="#9cc8ff")
INACTIVE = dict(
    title=[(0, "#c3d3ee"), (0.10, "#a2b9e2"), (0.45, "#8aa6d6"), (0.85, "#7c9acd"), (1, "#6f8dc2")],
    border="#8aa6d6", outline="#4a6a9a", shine="#e0e9f8")


def style(active):
    return ACTIVE if active else INACTIVE


def title_color(y, active):
    return gradient(style(active)["title"], y / (TITLE_H - 1))


def title_strip(active, width):
    s = style(active)
    return [[s["outline"] if y == 0 else (s["shine"] if y == 1 else title_color(y, active))] * width
            for y in range(TITLE_H)]


def top_corner(active, right=False):
    s, r = style(active), CORNER_W
    rows = []
    for y in range(TITLE_H):
        row = []
        for x in range(CORNER_W):
            xx = (CORNER_W - 1 - x) if right else x   # distancia al borde exterior
            if y < r:
                d2 = (r - xx - 0.5) ** 2 + (r - y - 0.5) ** 2
                if d2 > r * r:
                    c = None
                elif d2 > (r - 1.2) ** 2:
                    c = s["outline"]
                elif y == 1:
                    c = s["shine"]
                else:
                    c = title_color(y, active)
            else:
                c = s["outline"] if xx == 0 else (s["shine"] if xx == 1 and False else title_color(y, active))
            row.append(c)
        rows.append(row)
    return rows


def side(active, right=False):
    s = style(active)
    row = []
    for x in range(BORDER):
        xx = (BORDER - 1 - x) if right else x
        row.append(s["outline"] if xx == 0 else s["border"])
    return [row[:] for _ in range(4)]


def bottom(active):
    s = style(active)
    return [[s["outline"] if y == BORDER - 1 else s["border"]] * 4
            for y in range(BORDER)]


def bottom_corner(active, right=False):
    s = style(active)
    rows = []
    for y in range(BORDER):
        row = []
        for x in range(CORNER_W):
            xx = (CORNER_W - 1 - x) if right else x
            if y == BORDER - 1 and xx == 0:
                c = None
            elif y == BORDER - 1 or xx == 0:
                c = s["outline"]
            else:
                c = s["border"]
            row.append(c)
        rows.append(row)
    return rows


def make_frame():
    for state, active in (("active", True), ("inactive", False)):
        pieces = {
            "title-1": title_strip(active, 3),
            "title-2": title_strip(active, 1),
            "title-3": title_strip(active, 1),
            "title-4": title_strip(active, 1),
            "title-5": title_strip(active, 3),
            "top-left": top_corner(active, False),
            "top-right": top_corner(active, True),
            "left": side(active, False),
            "right": side(active, True),
            "bottom": bottom(active),
            "bottom-left": bottom_corner(active, False),
            "bottom-right": bottom_corner(active, True),
        }
        for name, px in pieces.items():
            write_xpm(THEME / f"{name}-{state}.xpm", f"{name}-{state}", px)


# ---------------------------------------------------------------- botones ----
BUTTON_FILLS = {
    "blue": {"active": ("#4f8ef0", "#1f5ad0"), "prelight": ("#74a8f8", "#3a74e4"),
             "pressed": ("#1a46a8", "#2352bc"), "inactive": ("#a9bfe6", "#8aa6d8")},
    "red": {"active": ("#ea7050", "#c2391c"), "prelight": ("#f58f72", "#d84e2c"),
            "pressed": ("#a02a12", "#b8341a"), "inactive": ("#a9bfe6", "#8aa6d8")},
}


def button_base(kind, state):
    top, bot = BUTTON_FILLS["red" if kind == "close" else "blue"][state]
    border = "#dbe5f6" if state == "inactive" else "#e9f0fc"
    R = 4
    rows = []
    for y in range(BTN):
        row = []
        for x in range(BTN):
            dx, dy = min(x, BTN - 1 - x), min(y, BTN - 1 - y)
            fill = gradient([(0, top), (1, bot)], y / (BTN - 1))
            if dx < R and dy < R:
                d2 = (R - dx - 0.5) ** 2 + (R - dy - 0.5) ** 2
                if d2 > R * R:
                    c = None
                elif d2 > (R - 1.2) ** 2:
                    c = border
                else:
                    c = fill
            else:
                c = border if (dx == 0 or dy == 0) else fill
            row.append(c)
        rows.append(row)
    return rows


def put(grid, x, y, c):
    if 0 <= x < BTN and 0 <= y < BTN and grid[y][x] is not None:
        grid[y][x] = c


def rect(grid, x0, y0, x1, y1, color, thick_top=2):
    for x in range(x0, x1 + 1):
        for y in range(y0, y0 + thick_top):
            put(grid, x, y, color)
        put(grid, x, y1, color)
    for y in range(y0, y1 + 1):
        put(grid, x0, y, color)
        put(grid, x1, y, color)


def draw_glyph(grid, kind, color, base):
    if kind == "hide":
        for y in range(14, 17):
            for x in range(6, 14):
                put(grid, x, y, color)
    elif kind == "maximize":
        rect(grid, 6, 6, 15, 15, color)
    elif kind == "maximize-toggled":
        rect(grid, 9, 5, 16, 12, color)          # ventana trasera
        for y in range(9, 17):                    # tapa el interior de la delantera
            for x in range(5, 13):
                grid[y][x] = base[y][x]
        rect(grid, 5, 9, 12, 16, color)          # ventana delantera
    elif kind == "close":
        for i in range(10):
            for dx in (0, 1):
                put(grid, 6 + i + dx, 6 + i, color)
                put(grid, 15 - i + dx, 6 + i, color)


def make_buttons():
    for kind in ("close", "hide", "maximize", "maximize-toggled"):
        for state in ("active", "inactive", "prelight", "pressed"):
            base = button_base(kind, state)
            grid = [row[:] for row in base]
            color = "#eef3fb" if state == "inactive" else "#ffffff"
            draw_glyph(grid, kind, color, base)
            write_xpm(THEME / f"{kind}-{state}.xpm", f"{kind}-{state}", grid)


THEMERC = """\
button_layout=|HMC
button_offset=6
button_spacing=2
full_width_title=true
maximized_offset=0
shadow_delta_height=0
shadow_delta_width=0
shadow_delta_x=0
shadow_delta_y=0
shadow_opacity=50
title_horizontal_offset=6
title_shadow_active=true
title_shadow_inactive=true
title_vertical_offset_active=0
title_vertical_offset_inactive=0
active_text_color=#ffffff
inactive_text_color=#eef3fb
active_text_shadow_color=#0b2f7a
inactive_text_shadow_color=#3f5f93
"""


def main():
    THEME.mkdir(parents=True, exist_ok=True)
    make_frame()
    make_buttons()
    (THEME / "themerc").write_text(THEMERC)
    print("Tema xfwm4:", THEME)


if __name__ == "__main__":
    main()
