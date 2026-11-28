#!/usr/bin/env python3
"""Genera el tema de iconos "ColinaRetro" (SVG originales, estilo brillante retro).

Solo usa la biblioteca estándar. Escribe en
  config/includes.chroot/usr/share/icons/ColinaRetro/

El tema hereda de Tango y Adwaita: lo que no dibujamos aquí se ve con esos iconos.
Todos los dibujos son originales: no reproducen iconos de ningún sistema operativo.
"""
import math
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
THEME = ROOT / "config/includes.chroot/usr/share/icons/ColinaRetro"
SIZE = 48


# ------------------------------------------------------------ utilidades SVG ----
def lg(i, stops, x1=0, y1=0, x2=0, y2=1):
    s = "".join(
        f'<stop offset="{st[0]}" stop-color="{st[1]}"' + (f' stop-opacity="{st[2]}"' if len(st) > 2 else "") + "/>"
        for st in stops)
    return f'<linearGradient id="{i}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">{s}</linearGradient>'


def rg(i, stops, cx=0.5, cy=0.5, r=0.5, fx=None, fy=None):
    s = "".join(
        f'<stop offset="{st[0]}" stop-color="{st[1]}"' + (f' stop-opacity="{st[2]}"' if len(st) > 2 else "") + "/>"
        for st in stops)
    f = "" if fx is None else f' fx="{fx}" fy="{fy}"'
    return f'<radialGradient id="{i}" cx="{cx}" cy="{cy}" r="{r}"{f}>{s}</radialGradient>'


BLUR = '<filter id="bl" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="1.1"/></filter>'
GLOSS = lg("gl", [(0, "#ffffff", 0.75), (1, "#ffffff", 0.05)])


def svg(body, defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{SIZE}" height="{SIZE}" viewBox="0 0 {SIZE} {SIZE}">'
            f'<defs>{BLUR}{GLOSS}{defs}</defs>{body}</svg>\n')


def shadow(cx=24, cy=43.5, rx=17, ry=2.6, op=0.28):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#0a1a3a" opacity="{op}" filter="url(#bl)"/>'


# ---------------------------------------------------------------- carpetas ----
FOLDER_DEFS = (lg("fb", [(0, "#e2b034"), (1, "#b98219")])
               + lg("ff", [(0, "#fff0b0"), (0.4, "#f8cb4e"), (1, "#e0a223")]))
FOLDER_STROKE = "#8f6310"


def folder_back():
    return (f'<path d="M4 10.5a2 2 0 0 1 2-2h12.5l4 4H42a2 2 0 0 1 2 2V40a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2z" '
            f'fill="url(#fb)" stroke="{FOLDER_STROKE}" stroke-width="1.1"/>')


def folder_closed(emblem=""):
    return svg(
        shadow() + folder_back()
        + '<rect x="8" y="14" width="32" height="12" rx="1.2" fill="#ffffff" stroke="#b9c3d6" stroke-width=".8"/>'
        + f'<path d="M4 20.5a2 2 0 0 1 2-2h36a2 2 0 0 1 2 2V40a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2z" '
          f'fill="url(#ff)" stroke="{FOLDER_STROKE}" stroke-width="1.1"/>'
        + '<path d="M6 21.2h36" stroke="#ffffff" stroke-opacity=".75" stroke-width="1.2"/>'
        + emblem, FOLDER_DEFS)


def folder_open():
    return svg(
        shadow() + folder_back()
        + '<path d="M9 13h29l2 9H8z" fill="#ffffff" stroke="#b9c3d6" stroke-width=".8"/>'
        + '<path d="M12 17h22M12 20h18" stroke="#9fb3d6" stroke-width="1.2"/>'
        + f'<path d="M2.6 40.6 7.4 22.6a2 2 0 0 1 1.9-1.5H46a1.6 1.6 0 0 1 1.5 2.1L42.6 40.6a2 2 0 0 1-1.9 1.4H4.2a1.6 1.6 0 0 1-1.6-1.4z" '
          f'fill="url(#ff)" stroke="{FOLDER_STROKE}" stroke-width="1.1"/>'
        + '<path d="M9 22.2h37" stroke="#ffffff" stroke-opacity=".7" stroke-width="1.2"/>', FOLDER_DEFS)


def em_note():
    return ('<g transform="translate(24 31)"><path d="M-3-6.5 6-8.5V3.2" fill="none" stroke="#2b5fc4" stroke-width="1.8"/>'
            '<path d="M-3-6.5V4" stroke="#2b5fc4" stroke-width="1.8"/><ellipse cx="-5" cy="4.4" rx="3" ry="2.3" fill="#2b5fc4"/>'
            '<ellipse cx="4" cy="3.6" rx="3" ry="2.3" fill="#2b5fc4"/></g>')


def em_down():
    return ('<g transform="translate(24 31)"><path d="M-3.5-8h7v6h4.5L0 6.5-8-2h4.5z" fill="#3aa23a" '
            'stroke="#1f6d1f" stroke-width=".9" stroke-linejoin="round"/></g>')


def em_pic():
    return ('<g transform="translate(24 31)"><rect x="-8" y="-6.5" width="16" height="13" rx="1.4" fill="#cfe6ff" '
            'stroke="#4a78c4" stroke-width="1"/><path d="M-8 6.5 -2-1l3.5 4 2.5-2.5L8 6.5z" fill="#4ea03a"/>'
            '<circle cx="3.6" cy="-2.4" r="1.7" fill="#ffd84a"/></g>')


def em_film():
    holes = "".join(f'<rect x="{x}" y="-7" width="2" height="2" fill="#fff"/><rect x="{x}" y="5" width="2" height="2" fill="#fff"/>'
                    for x in (-7, -3.5, 0, 3.5, 7 - 0.5))
    return (f'<g transform="translate(24 31)"><rect x="-9" y="-7.5" width="18" height="15" rx="1.4" fill="#3a4258"/>{holes}'
            '<path d="M-2.5-3 4 0-2.5 3z" fill="#fff"/></g>')


def em_doc():
    return ('<g transform="translate(24 31)"><path d="M-6-8h8l4.6 4.6V8H-6z" fill="#fff" stroke="#6f87b8" stroke-width="1"/>'
            '<path d="M-3-1h7M-3 2h7M-3 5h5" stroke="#8aa2d2" stroke-width="1"/></g>')


# ----------------------------------------------------------------- sistema ----
def logo():
    d = (rg("sky", [(0, "#a9dcff"), (1, "#2c7be0")], 0.4, 0.3, 0.85)
         + lg("h1", [(0, "#8fdc5c"), (1, "#2f8f24")]) + lg("h2", [(0, "#5fbf3e"), (1, "#1f7a1c")])
         + rg("sun", [(0, "#fffbe0"), (0.5, "#ffe066"), (1, "#ffb21e")]))
    return svg(
        shadow(24, 44, 15, 2.2)
        + '<circle cx="24" cy="23" r="20" fill="url(#sky)" stroke="#ffffff" stroke-width="2"/>'
        + '<circle cx="24" cy="23" r="20.9" fill="none" stroke="#1b4fa8" stroke-width=".9"/>'
        + '<circle cx="32.5" cy="14.5" r="5.2" fill="url(#sun)"/>'
        + '<clipPath id="cp"><circle cx="24" cy="23" r="19"/></clipPath>'
        + '<g clip-path="url(#cp)"><path d="M3 34C11 22 22 24 29 30s13 2 18-2v18H3z" fill="url(#h1)"/>'
          '<path d="M3 41C10 31 20 33 27 38s12 1 20-3v12H3z" fill="url(#h2)"/></g>'
        + '<path d="M7 17A18 18 0 0 1 41 17C32 13 16 13 7 17z" fill="url(#gl)" opacity=".85"/>', d)


def home():
    d = lg("rf", [(0, "#f08a6a"), (1, "#b8341a")]) + lg("wl", [(0, "#fff6dc"), (1, "#e6d3a2")])
    return svg(
        shadow()
        + '<path d="M9 22h30v18a2 2 0 0 1-2 2H11a2 2 0 0 1-2-2z" fill="url(#wl)" stroke="#a9915a" stroke-width="1"/>'
        + '<path d="M3.5 24 24 6l20.5 18-2.4 2.6L24 10.8 5.9 26.6z" fill="url(#rf)" stroke="#8a2812" stroke-width="1" stroke-linejoin="round"/>'
        + '<rect x="21" y="29" width="8" height="13" rx="1" fill="#8a5a2a" stroke="#5e3b17" stroke-width=".9"/>'
        + '<rect x="12.5" y="26.5" width="6" height="6" rx=".8" fill="#9fd0ff" stroke="#4a78c4" stroke-width=".9"/>'
        + '<rect x="32" y="26.5" width="6" height="6" rx=".8" fill="#9fd0ff" stroke="#4a78c4" stroke-width=".9"/>'
        + '<rect x="33" y="8" width="5" height="9" fill="#c2603f" stroke="#8a2812" stroke-width=".9"/>', d)


def monitor(screen_extra="", flat=False):
    d = (lg("bg", [(0, "#f7f3e6"), (1, "#cdc5ac")]) + lg("sk", [(0, "#7fc4ff"), (1, "#2d7fe0")])
         + lg("gr", [(0, "#79cf55"), (1, "#2c8a26")]))
    return svg(
        shadow()
        + '<rect x="5.5" y="4.5" width="37" height="29" rx="3.2" fill="url(#bg)" stroke="#857e68" stroke-width="1"/>'
        + '<rect x="9.5" y="8.5" width="29" height="20" rx="1.6" fill="url(#sk)" stroke="#3f5578" stroke-width="1"/>'
        + '<path d="M9.5 24.5c5-5.2 11-5.4 16-2.2s9 2.2 13 .2v5.5a1.6 1.6 0 0 1-1.6 1.6H11.1a1.6 1.6 0 0 1-1.6-1.6z" fill="url(#gr)"/>'
        + '<circle cx="32" cy="14" r="2.8" fill="#ffe36a"/>' + screen_extra
        + '<path d="M10 9.5h28.4l-9 9H10z" fill="url(#gl)" opacity=".55"/>'
        + '<path d="M18.5 33.5h11l1.6 4.5h-14.2z" fill="url(#bg)" stroke="#857e68" stroke-width="1"/>'
        + '<rect x="12.5" y="37.5" width="23" height="4.4" rx="1.6" fill="url(#bg)" stroke="#857e68" stroke-width="1"/>'
        + '<circle cx="37.5" cy="31" r="1" fill="#46c23a"/>', d)


def harddisk():
    d = lg("hd", [(0, "#eef1f5"), (1, "#a4acb9")]) + lg("hf", [(0, "#8d96a6"), (1, "#5a6272")])
    return svg(
        shadow()
        + '<path d="M7 18 12 8h24l5 10z" fill="url(#hd)" stroke="#6b7384" stroke-width="1" stroke-linejoin="round"/>'
        + '<rect x="6" y="18" width="36" height="17" rx="2.4" fill="url(#hf)" stroke="#434b5a" stroke-width="1"/>'
        + '<path d="M7 19h34" stroke="#fff" stroke-opacity=".5"/>'
        + '<circle cx="35.5" cy="26.5" r="2.2" fill="#52e04a" stroke="#1f7a1c" stroke-width=".8"/>'
        + '<path d="M11 24.5h14M11 28.5h14" stroke="#2f3644" stroke-width="1.4" stroke-linecap="round"/>'
        + '<path d="M13 12h22" stroke="#fff" stroke-opacity=".7" stroke-width="1.2"/>', d)


def optical():
    d = (rg("cd", [(0, "#ffffff"), (0.35, "#e9eef7"), (1, "#aab6cc")], 0.45, 0.4, 0.75)
         + lg("w1", [(0, "#ff9ad5", 0.65), (1, "#ff9ad5", 0)], 0, 0, 1, 1)
         + lg("w2", [(0, "#7fe9ff", 0.7), (1, "#7fe9ff", 0)], 1, 1, 0, 0))
    return svg(
        shadow(24, 43, 15, 2.4)
        + '<circle cx="24" cy="23" r="19" fill="url(#cd)" stroke="#6f7c96" stroke-width="1.1"/>'
        + '<path d="M24 23 6.5 15.5A19 19 0 0 1 24 4z" fill="url(#w1)"/>'
        + '<path d="M24 23 41.5 30.5A19 19 0 0 1 24 42z" fill="url(#w2)"/>'
        + '<circle cx="24" cy="23" r="7.5" fill="none" stroke="#ffffff" stroke-opacity=".8" stroke-width="3"/>'
        + '<circle cx="24" cy="23" r="3.3" fill="#7f8aa3" stroke="#59627a" stroke-width=".8"/>'
        + '<circle cx="24" cy="23" r="1.6" fill="#e8eef8"/>', d)


def usbstick():
    d = lg("us", [(0, "#8fb8ff"), (1, "#2c62d0")]) + lg("mt", [(0, "#f2f4f8"), (1, "#a6afc0")])
    return svg(
        shadow()
        + '<rect x="15" y="4" width="18" height="13" rx="1.6" fill="url(#mt)" stroke="#6b7384" stroke-width="1"/>'
        + '<rect x="19" y="7" width="3.2" height="4.6" fill="#4a5262"/><rect x="25.8" y="7" width="3.2" height="4.6" fill="#4a5262"/>'
        + '<path d="M12 18a2.5 2.5 0 0 1 2.5-2.5h19A2.5 2.5 0 0 1 36 18v22a3 3 0 0 1-3 3H15a3 3 0 0 1-3-3z" fill="url(#us)" stroke="#173f93" stroke-width="1"/>'
        + '<path d="M14 19.5h20" stroke="#fff" stroke-opacity=".6" stroke-width="1.2"/>'
        + '<circle cx="24" cy="35" r="2" fill="#57e44a" stroke="#1f7a1c" stroke-width=".7"/>'
        + '<path d="M16 25h16" stroke="#fff" stroke-opacity=".45" stroke-width="1.2"/>', d)


def trash(full=False):
    d = lg("bn", [(0, "#e8eef8"), (1, "#8f9db8")], 0, 0, 1, 0) + lg("lid", [(0, "#f6f8fc"), (1, "#b4bfd4")])
    paper = ""
    if full:
        paper = ('<path d="M14 14l5-7 6 3 5-6 5 6 4-1-3 9z" fill="#fff" stroke="#9fb0cf" stroke-width=".9" stroke-linejoin="round"/>'
                 '<path d="M18 12l3 3M26 10l2 4" stroke="#b6c3dc" stroke-width=".9"/>')
    ribs = "".join(f'<path d="M{x} 19 {x + (24 - x) * 0.07:.1f} 40" stroke="#6f7f9d" stroke-opacity=".55" stroke-width="1.1"/>'
                   for x in (14, 19, 24, 29, 34))
    return svg(
        shadow(24, 44, 14, 2.2)
        + paper
        + '<path d="M10 17h28l-3 24a2.6 2.6 0 0 1-2.6 2.2H15.6A2.6 2.6 0 0 1 13 41z" fill="url(#bn)" stroke="#59698a" stroke-width="1" stroke-linejoin="round"/>'
        + ribs
        + '<rect x="7.5" y="12.5" width="33" height="5" rx="2.2" fill="url(#lid)" stroke="#59698a" stroke-width="1"/>'
        + '<path d="M18 12.5v-1.6a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v1.6" fill="none" stroke="#59698a" stroke-width="1.6"/>'
        + '<path d="M12 14.2h24" stroke="#fff" stroke-opacity=".8" stroke-width="1.1"/>', d)


def globe():
    d = rg("gb", [(0, "#bfe6ff"), (0.55, "#3f94ea"), (1, "#1b52b8")], 0.38, 0.32, 0.8)
    return svg(
        shadow(24, 44, 14, 2.2)
        + '<circle cx="24" cy="23" r="19" fill="url(#gb)" stroke="#143f94" stroke-width="1"/>'
        + '<clipPath id="gc"><circle cx="24" cy="23" r="19"/></clipPath>'
        + '<g clip-path="url(#gc)" fill="#5cbf3f" stroke="#2c7a22" stroke-width=".8">'
          '<path d="M8 14c4-4 9-4 11-1s-1 6-4 6-2 5-5 6-5-7-2-11z"/>'
          '<path d="M24 28c4-3 9-1 10 3s-2 9-6 10-6-6-4-13z"/>'
          '<path d="M27 8c4-3 11-1 14 4-4 2-8 1-9 4s-5-1-6-4z"/></g>'
        + '<path d="M7 16A18 18 0 0 1 41 16C32 11 16 11 7 16z" fill="url(#gl)" opacity=".8"/>', d)


def server():
    d = lg("sv", [(0, "#f3f5f9"), (1, "#a6afc0")])
    body = ""
    for k, y in enumerate((6, 18, 30)):
        body += (f'<rect x="8" y="{y}" width="32" height="10" rx="2" fill="url(#sv)" stroke="#5b6478" stroke-width="1"/>'
                 f'<circle cx="14" cy="{y + 5}" r="1.5" fill="#52e04a"/><path d="M20 {y + 5}h14" stroke="#4a5262" stroke-width="1.6" stroke-linecap="round"/>')
    return svg(shadow(24, 44, 15, 2.2) + body, d)


def filemanager():
    d = (lg("wt", [(0, "#5b9cf5"), (1, "#1d58cc")]) + lg("wb", [(0, "#ffffff"), (1, "#e7ecf5")]) + FOLDER_DEFS)
    return svg(
        shadow()
        + '<rect x="4.5" y="6.5" width="39" height="35" rx="3" fill="url(#wb)" stroke="#1646b0" stroke-width="1"/>'
        + '<path d="M4.5 9.5a3 3 0 0 1 3-3h33a3 3 0 0 1 3 3V15h-39z" fill="url(#wt)" stroke="#1646b0" stroke-width="1"/>'
        + '<circle cx="9.5" cy="10.8" r="1.4" fill="#ffffff" opacity=".9"/><circle cx="14" cy="10.8" r="1.4" fill="#ffffff" opacity=".6"/>'
        + '<path d="M10 22a1.4 1.4 0 0 1 1.4-1.4h6l2.2 2.4h9.8A1.4 1.4 0 0 1 31 24.4V35a1.4 1.4 0 0 1-1.4 1.4H11.4A1.4 1.4 0 0 1 10 35z" '
          'fill="url(#ff)" stroke="#8f6310" stroke-width=".9"/>'
        + '<path d="M33 22h6M33 26h6M33 30h6" stroke="#9fb3d6" stroke-width="1.4" stroke-linecap="round"/>', d)


def terminal():
    d = lg("wt", [(0, "#5b9cf5"), (1, "#1d58cc")]) + lg("tb", [(0, "#2d3446"), (1, "#0f1320")])
    return svg(
        shadow()
        + '<rect x="4.5" y="6.5" width="39" height="35" rx="3" fill="url(#tb)" stroke="#1646b0" stroke-width="1"/>'
        + '<path d="M4.5 9.5a3 3 0 0 1 3-3h33a3 3 0 0 1 3 3V15h-39z" fill="url(#wt)" stroke="#1646b0" stroke-width="1"/>'
        + '<circle cx="9.5" cy="10.8" r="1.4" fill="#ffffff" opacity=".9"/><circle cx="14" cy="10.8" r="1.4" fill="#ffffff" opacity=".6"/>'
        + '<path d="M10 21l7 5-7 5" fill="none" stroke="#5cf05a" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>'
        + '<path d="M21 32h9" stroke="#5cf05a" stroke-width="2.4" stroke-linecap="round"/>', d)


def texteditor():
    d = lg("pp", [(0, "#ffffff"), (1, "#e9eef7")]) + lg("pc", [(0, "#ffe27a"), (1, "#f0a826")])
    rings = "".join(f'<rect x="{x}" y="3" width="2.4" height="7" rx="1.2" fill="#5a6478"/>' for x in (12, 18, 24, 30))
    return svg(
        shadow()
        + '<rect x="7.5" y="6.5" width="30" height="36" rx="2.4" fill="url(#pp)" stroke="#6f7c96" stroke-width="1"/>'
        + rings
        + '<path d="M12 17h22M12 22h22M12 27h22M12 32h14" stroke="#8fb0e6" stroke-width="1.4" stroke-linecap="round"/>'
        + '<path d="M12 12.5h6" stroke="#e06a5a" stroke-width="1.6" stroke-linecap="round"/>'
        + '<g transform="rotate(38 36 33)"><rect x="33.6" y="17" width="5.6" height="22" rx="1" fill="url(#pc)" stroke="#9a6a10" stroke-width=".9"/>'
          '<path d="M33.6 39h5.6l-2.8 6z" fill="#f4d9a8" stroke="#9a6a10" stroke-width=".9"/><path d="M36.4 43v2" stroke="#444" stroke-width="1.4"/>'
          '<rect x="33.6" y="17" width="5.6" height="3.4" fill="#f08a8a" stroke="#9a6a10" stroke-width=".9"/></g>', d)


def installer():
    d = lg("bx", [(0, "#e8c48a"), (1, "#b98a4a")]) + lg("ar", [(0, "#7fe06a"), (1, "#2f9a2c")])
    return svg(
        shadow()
        + '<path d="M6 17 24 11l18 6v20l-18 6-18-6z" fill="url(#bx)" stroke="#7a5424" stroke-width="1" stroke-linejoin="round"/>'
        + '<path d="M6 17l18 6 18-6M24 23v20" fill="none" stroke="#7a5424" stroke-width="1"/>'
        + '<path d="M15 14l18 6" stroke="#fff" stroke-opacity=".35"/>'
        + '<path d="M19 3h10v9h6L24 23 13 12h6z" fill="url(#ar)" stroke="#1f6d1f" stroke-width="1" stroke-linejoin="round"/>', d)


def wineglass():
    d = lg("gw", [(0, "#ffffff", 0.9), (1, "#cfe3ff", 0.45)]) + lg("wn", [(0, "#c0344a"), (1, "#6a0f2a")])
    return svg(
        shadow(24, 44.5, 11, 1.8)
        + '<path d="M13 5h22c1 11-1 20-11 21.5C14 25 12 16 13 5z" fill="url(#gw)" stroke="#6f87b8" stroke-width="1"/>'
        + '<path d="M13.4 14h21.2c-.6 7.6-4 11.2-10.6 12C17.4 25.2 13.8 21.6 13.4 14z" fill="url(#wn)"/>'
        + '<path d="M14 14c4 1.6 16 1.6 20 0" stroke="#e8708a" stroke-width="1" fill="none"/>'
        + '<path d="M24 26.5v13" stroke="#6f87b8" stroke-width="2.2"/>'
        + '<ellipse cx="24" cy="41" rx="9" ry="2.6" fill="url(#gw)" stroke="#6f87b8" stroke-width="1"/>'
        + '<path d="M16 8c-.5 4 0 8 2 11" stroke="#fff" stroke-width="1.8" stroke-linecap="round" opacity=".85" fill="none"/>', d)


# ------------------------------------------------------- categorías (mosaicos) ----
def tile(top, bot, glyph, cut):
    d = lg("tl", [(0, top), (1, bot)])
    return svg(
        shadow(24, 44, 16, 2.2, 0.25)
        + '<rect x="4" y="4" width="40" height="40" rx="9.5" fill="url(#tl)" stroke="#0c2a66" stroke-opacity=".55" stroke-width="1"/>'
        + '<rect x="5" y="5" width="38" height="38" rx="8.6" fill="none" stroke="#fff" stroke-opacity=".55" stroke-width="1"/>'
        + f'<g transform="translate(0 1)" fill="#000" stroke="#000" opacity=".22">{glyph(cut)}</g>'
        + f'<g fill="#fff" stroke="#fff">{glyph(cut)}</g>'
        + '<path d="M5 20C5 11 11 5 20 5h8c9 0 15 6 15 15C32 16 16 16 5 20z" fill="url(#gl)" opacity=".7" stroke="none"/>', d)


def gear_path(cx, cy, ro, ri, teeth):
    pts = []
    n = teeth * 4
    for i in range(n):
        a = 2 * math.pi * i / n
        r = ro if (i % 4) in (0, 1) else ri
        pts.append(f"{cx + r * math.cos(a):.2f} {cy + r * math.sin(a):.2f}")
    return "M" + "L".join(pts) + "z"


def g_toolbox(c):
    return (f'<rect x="10" y="19" width="28" height="18" rx="2.5" stroke="none"/><path d="M18 19v-3.5a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2V19" '
            f'fill="none" stroke-width="2.6"/><path d="M10 27.5h28" stroke="{c}" stroke-width="1.6" fill="none"/>'
            f'<rect x="21.5" y="25" width="5" height="5" rx="1" fill="{c}" stroke="none"/>')


def g_code(c):
    return ('<path d="M19 15 10 24l9 9M29 15l9 9-9 9" fill="none" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>'
            '<path d="M26 12 22 36" fill="none" stroke-width="2.8" stroke-linecap="round"/>')


def g_book(c):
    return (f'<path d="M24 17c-4-3-9-3.6-14-3v21c5-.6 10 0 14 3 4-3 9-3.6 14-3V14c-5-.6-10 0-14 3z" stroke="none"/>'
            f'<path d="M24 17v21" stroke="{c}" stroke-width="1.6" fill="none"/>')


def g_gamepad(c):
    return (f'<path d="M14 18h20a7 7 0 0 1 7 7.2l-.4 4.6a4.6 4.6 0 0 1-8 2.6L30 29.4H18l-2.6 3a4.6 4.6 0 0 1-8-2.6L7 25.2A7 7 0 0 1 14 18z" stroke="none"/>'
            f'<path d="M14.5 21.5v6M11.5 24.5h6" stroke="{c}" stroke-width="2.2" fill="none"/>'
            f'<circle cx="32" cy="22.8" r="1.9" fill="{c}" stroke="none"/><circle cx="35.6" cy="26.2" r="1.9" fill="{c}" stroke="none"/>')


def g_palette(c):
    return (f'<path d="M24 10C14 10 8 17 8 24.5S14.5 38 23 38c3.4 0 4.6-2.2 3.4-4.6s-.4-4.4 3-4.4h4.4c4.2 0 7.2-3 7.2-7.4C41 15 33.6 10 24 10z" stroke="none"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="2.5" fill="{col}" stroke="none"/>'
                      for x, y, col in ((15, 22, "#e0453a"), (20.5, 16.5, "#f0b429"), (28, 16.5, "#3aa23a"), (34, 21.5, c))))


def g_globe(c):
    return ('<circle cx="24" cy="24" r="13" fill="none" stroke-width="2.6"/><ellipse cx="24" cy="24" rx="5.6" ry="13" fill="none" stroke-width="2.2"/>'
            '<path d="M11 24h26M13.4 17.4h21.2M13.4 30.6h21.2" fill="none" stroke-width="2"/>')


def g_play(c):
    return '<circle cx="24" cy="24" r="14" fill="none" stroke-width="2.8"/><path d="M20 16.8 32.4 24 20 31.2z" stroke="none"/>'


def g_office(c):
    return (f'<path d="M14 10h14l8 8v18a2.5 2.5 0 0 1-2.5 2.5h-19.5A2.5 2.5 0 0 1 12 36V12.5A2.5 2.5 0 0 1 14.5 10z" stroke="none"/>'
            f'<path d="M28 10v8h8" fill="{c}" fill-opacity=".35" stroke="{c}" stroke-width="1.2"/>'
            f'<path d="M17 24h14M17 28.5h14M17 33h9" stroke="{c}" stroke-width="2" fill="none"/>')


def g_other(c):
    return "".join(f'<circle cx="{x}" cy="{y}" r="2.7" stroke="none"/>' for x in (14, 24, 34) for y in (14, 24, 34))


def g_flask(c):
    return (f'<path d="M20 10h8v10l8.6 15.4a3.2 3.2 0 0 1-2.8 4.8H14.2a3.2 3.2 0 0 1-2.8-4.8L20 20z" stroke="none"/>'
            f'<path d="M16.5 29h15l3 5.4a1.6 1.6 0 0 1-1.4 2.4H14.9a1.6 1.6 0 0 1-1.4-2.4z" fill="{c}" fill-opacity=".55" stroke="none"/>'
            f'<circle cx="23" cy="32" r="1.4" fill="#fff" stroke="none"/><path d="M18 10h12" stroke-width="2.6" fill="none" stroke-linecap="round"/>')


def g_gear(c):
    return (f'<path d="{gear_path(24, 24, 15.5, 11.2, 8)}" stroke="none"/><circle cx="24" cy="24" r="5.2" fill="{c}" stroke="none"/>')


def g_wrench(c):
    return ('<path d="M33.5 11.5a8.4 8.4 0 0 0-10.4 10.6L11.4 33.8a3.6 3.6 0 0 0 5.1 5.1L28.2 27.2a8.4 8.4 0 0 0 10.6-10.4l-5.4 5.4-4.4-1.2-1.2-4.4z" '
            f'stroke="none"/><circle cx="14" cy="36.5" r="1.5" fill="{c}" stroke="none"/>')


def g_sliders(c):
    out = ""
    for y, x in ((15, 18), (24, 30), (33, 22)):
        out += (f'<path d="M10 {y}h28" stroke-width="2.4" stroke-linecap="round" fill="none"/>'
                f'<circle cx="{x}" cy="{y}" r="4" stroke="{c}" stroke-width="1.6"/>')
    return out


# --------------------------------------------------------------- documentos ----
PAGE_DEFS = lg("pg", [(0, "#ffffff"), (1, "#e3e8f0")])


def page(emblem="", header=None):
    hdr = ""
    if header:
        hdr = f'<path d="M10 10a2 2 0 0 1 2-2h17v10H10z" fill="{header}" opacity=".0"/>'
    return svg(
        shadow()
        + '<path d="M9.5 6a2 2 0 0 1 2-2H29l10 10v28a2 2 0 0 1-2 2H11.5a2 2 0 0 1-2-2z" fill="url(#pg)" stroke="#7f8ba3" stroke-width="1" stroke-linejoin="round"/>'
        + '<path d="M29 4v8a2 2 0 0 0 2 2h8z" fill="#cfd8e8" stroke="#7f8ba3" stroke-width="1" stroke-linejoin="round"/>'
        + hdr + emblem, PAGE_DEFS)


def mt_text():
    return page('<path d="M14 21h20M14 26h20M14 31h20M14 36h12" stroke="#8fa8d8" stroke-width="1.5" stroke-linecap="round"/>')


def mt_image():
    return page('<rect x="14" y="20" width="22" height="17" rx="1.5" fill="#bfe0ff" stroke="#4a78c4" stroke-width="1"/>'
                '<path d="M14 37 22 27l5 6 3-3 6 7z" fill="#4ea03a"/><circle cx="31" cy="24.5" r="2.2" fill="#ffd84a"/>')


def mt_audio():
    return page('<g transform="translate(25 29)"><path d="M-4-7 7-9.5V4.5" fill="none" stroke="#2b5fc4" stroke-width="2"/><path d="M-4-7V6" stroke="#2b5fc4" stroke-width="2"/>'
                '<ellipse cx="-6.4" cy="6.4" rx="3.6" ry="2.8" fill="#2b5fc4"/><ellipse cx="4.6" cy="4.8" rx="3.6" ry="2.8" fill="#2b5fc4"/></g>')


def mt_video():
    return page('<rect x="13" y="21" width="24" height="16" rx="1.6" fill="#3a4258"/>'
                + "".join(f'<rect x="{x}" y="22.2" width="1.8" height="1.8" fill="#fff"/><rect x="{x}" y="34" width="1.8" height="1.8" fill="#fff"/>' for x in (15, 19.5, 24, 28.5, 33))
                + '<path d="M22 26.5 29.5 29 22 31.6z" fill="#fff"/>')


def mt_package():
    d = lg("bx", [(0, "#e8c48a"), (1, "#b98a4a")])
    return svg(
        shadow()
        + '<path d="M6 16 24 10l18 6v21l-18 6-18-6z" fill="url(#bx)" stroke="#7a5424" stroke-width="1" stroke-linejoin="round"/>'
        + '<path d="M6 16l18 6 18-6M24 22v21" fill="none" stroke="#7a5424" stroke-width="1"/>'
        + '<path d="M15 13l18 6v6l-4-1.4v-5.6L11 11.6z" fill="#f4e2bd" opacity=".9" stroke="#7a5424" stroke-width=".8"/>', d)


def mt_exe():
    d = lg("wt", [(0, "#5b9cf5"), (1, "#1d58cc")]) + lg("wb", [(0, "#ffffff"), (1, "#e7ecf5")])
    return svg(
        shadow()
        + '<rect x="5.5" y="8.5" width="37" height="30" rx="3" fill="url(#wb)" stroke="#1646b0" stroke-width="1"/>'
        + '<path d="M5.5 11.5a3 3 0 0 1 3-3h31a3 3 0 0 1 3 3V17h-37z" fill="url(#wt)" stroke="#1646b0" stroke-width="1"/>'
        + '<circle cx="10.5" cy="12.8" r="1.4" fill="#fff" opacity=".9"/><circle cx="15" cy="12.8" r="1.4" fill="#fff" opacity=".6"/>'
        + f'<path d="{gear_path(24, 28.5, 7.6, 5.4, 8)}" fill="#6f87b8"/><circle cx="24" cy="28.5" r="2.4" fill="#fff"/>', d)


def mt_pdf():
    return page('<path d="M9.5 8a2 2 0 0 1 2-2H12v14H9.5z" fill="none"/>'
                '<rect x="14" y="19" width="20" height="8" rx="1.6" fill="#d8402f"/>'
                '<path d="M17 23h6M26 23h5" stroke="#fff" stroke-width="1.6" stroke-linecap="round"/>'
                '<path d="M14 32h20M14 36.5h14" stroke="#b0bbd2" stroke-width="1.5" stroke-linecap="round"/>')


def mt_doc():
    return page('<rect x="14" y="19" width="20" height="5" rx="1" fill="#3f78d8"/>'
                '<path d="M14 29h20M14 33.5h20M14 38h12" stroke="#8fa8d8" stroke-width="1.5" stroke-linecap="round"/>')


def mt_sheet():
    cells = "".join(f'<path d="M14 {y}h22" stroke="#4aa24a" stroke-width="1"/>' for y in (24.5, 29, 33.5))
    cells += "".join(f'<path d="M{x} 20v18" stroke="#4aa24a" stroke-width="1"/>' for x in (21, 28.5))
    return page('<rect x="14" y="20" width="22" height="18" fill="#eaf8e6" stroke="#4aa24a" stroke-width="1"/>' + cells
                + '<rect x="14" y="20" width="22" height="4.5" fill="#6cc85a" stroke="#4aa24a" stroke-width="1"/>')


def mt_slides():
    return page('<rect x="13.5" y="20" width="23" height="16" rx="1.4" fill="#fff4e6" stroke="#e08a2a" stroke-width="1"/>'
                '<path d="M17 33v-5M22 33v-9M27 33v-7M32 33v-11" stroke="#f0952f" stroke-width="3" stroke-linecap="butt"/>')


# --------------------------------------------------------------------- tema ----
def build():
    if THEME.exists():
        shutil.rmtree(THEME)
    dirs = {
        "places": ("Places", {}),
        "devices": ("Devices", {}),
        "apps": ("Applications", {}),
        "categories": ("Categories", {}),
        "mimetypes": ("MimeTypes", {}),
    }

    def add(ctx, names, content):
        for n in ([names] if isinstance(names, str) else names):
            dirs[ctx][1][n] = content

    fc = folder_closed()
    add("places", ["folder", "inode-directory", "folder-default"], fc)
    add("places", ["folder-open", "folder-drag-accept"], folder_open())
    add("places", "folder-documents", folder_closed(em_doc()))
    add("places", "folder-download", folder_closed(em_down()))
    add("places", "folder-music", folder_closed(em_note()))
    add("places", "folder-pictures", folder_closed(em_pic()))
    add("places", "folder-videos", folder_closed(em_film()))
    add("places", ["folder-publicshare", "folder-templates", "folder-remote"], fc)
    add("places", ["start-here", "colina-logo", "distributor-logo", "start-here-xfce"], logo())
    add("places", ["user-home", "go-home"], home())
    add("places", ["user-desktop", "show-desktop"], monitor())
    add("places", "user-trash", trash(False))
    add("places", "user-trash-full", trash(True))
    add("places", ["network-workgroup", "network-server", "network"], globe())
    add("places", "folder-network", globe())

    add("devices", ["computer", "computer-symbolic-fallback"], monitor())
    add("devices", ["drive-harddisk", "drive-harddisk-system", "drive-multidisk"], harddisk())
    add("devices", ["drive-optical", "media-optical", "media-optical-cd-audio", "media-optical-dvd"], optical())
    add("devices", ["drive-removable-media", "drive-removable-media-usb", "media-removable", "media-flash"], usbstick())

    fm, term, ed = filemanager(), terminal(), texteditor()
    add("apps", ["system-file-manager", "org.xfce.thunar", "thunar", "Thunar", "org.xfce.filemanager"], fm)
    add("apps", ["utilities-terminal", "org.xfce.terminal", "xfce-terminal", "terminal"], term)
    add("apps", ["accessories-text-editor", "org.xfce.mousepad", "mousepad", "text-editor"], ed)
    add("apps", ["system-software-install", "colina-install"], installer())
    add("apps", ["wine", "wine-winecfg", "wine-notepad"], wineglass())
    add("apps", ["org.xfce.settings.manager", "preferences-system", "preferences-desktop-theme"],
        tile("#8fa7c8", "#46618f", g_sliders, "#46618f"))

    cats = {
        "applications-accessories": ("#f6a24a", "#d0661a", g_toolbox),
        "applications-development": ("#6c8fe8", "#2a4fb8", g_code),
        "applications-education": ("#46c3b3", "#168a7c", g_book),
        "applications-games": ("#a07ae8", "#6338b8", g_gamepad),
        "applications-graphics": ("#f27aa8", "#c2386c", g_palette),
        "applications-internet": ("#5fb2f5", "#1f66d0", g_globe),
        "applications-multimedia": ("#f58a6a", "#c2391c", g_play),
        "applications-office": ("#7ccf63", "#3a9a2c", g_office),
        "applications-other": ("#a9b4c6", "#6a7790", g_other),
        "applications-science": ("#56cfe8", "#1d8aaa", g_flask),
        "applications-system": ("#9aa9c4", "#566890", g_gear),
        "applications-utilities": ("#9cc86a", "#5a8a2a", g_wrench),
        "applications-engineering": ("#9cc86a", "#5a8a2a", g_wrench),
        "preferences-desktop": ("#8fa7c8", "#46618f", g_sliders),
        "preferences-other": ("#8fa7c8", "#46618f", g_sliders),
    }
    for name, (top, bot, glyph) in cats.items():
        add("categories", name, tile(top, bot, glyph, bot))

    add("mimetypes", ["text-x-generic", "text-plain", "text-x-script"], mt_text())
    add("mimetypes", ["image-x-generic"], mt_image())
    add("mimetypes", ["audio-x-generic"], mt_audio())
    add("mimetypes", ["video-x-generic"], mt_video())
    add("mimetypes", ["package-x-generic", "application-x-archive", "application-zip", "application-x-compressed-tar",
                      "application-x-tar", "application-x-7z-compressed", "application-x-rar"], mt_package())
    add("mimetypes", ["application-x-executable", "application-x-ms-dos-executable", "application-x-msdownload",
                      "application-x-msi", "application-x-ms-installer"], mt_exe())
    add("mimetypes", "application-pdf", mt_pdf())
    add("mimetypes", ["x-office-document", "application-msword", "application-vnd.oasis.opendocument.text"], mt_doc())
    add("mimetypes", ["x-office-spreadsheet", "application-vnd.oasis.opendocument.spreadsheet"], mt_sheet())
    add("mimetypes", ["x-office-presentation", "application-vnd.oasis.opendocument.presentation"], mt_slides())
    add("mimetypes", ["application-octet-stream", "unknown", "text-x-preview"], mt_text())

    count = 0
    for sub, (_ctx, files) in dirs.items():
        out = THEME / "scalable" / sub
        out.mkdir(parents=True, exist_ok=True)
        for name, content in files.items():
            (out / f"{name}.svg").write_text(content)
            count += 1

    index = ["[Icon Theme]", "Name=Colina Retro", "Comment=Iconos retro originales de Colina OS",
             "Inherits=Tango,Adwaita,hicolor", "Example=folder",
             "Directories=" + ",".join(f"scalable/{k}" for k in dirs), ""]
    for sub, (ctx, _f) in dirs.items():
        index += [f"[scalable/{sub}]", "Size=48", "MinSize=8", "MaxSize=512", "Type=Scalable", f"Context={ctx}", ""]
    (THEME / "index.theme").write_text("\n".join(index))
    print(f"Tema de iconos: {THEME}  ({count} archivos SVG)")


if __name__ == "__main__":
    build()
