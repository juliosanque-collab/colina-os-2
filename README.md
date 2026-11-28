
# Colina OS

Distribución Linux basada en **Debian 13 (trixie)** con un escritorio **XFCE de aspecto clásico**
(barra de tareas azul, botón Inicio verde, ventanas con barra de título azul) y **compatibilidad
con programas de Windows** me[Desktop Entry]
Type=Application
Name=Fondo de escritorio de Colina OS
Exec=/usr/local/bin/colina-set-wallpaper
OnlyShowIn=XFCE;
NoDisplay=true
X-GNOME-Autostart-enabled=true

[greeter]
background=/usr/share/backgrounds/colina/colina-atardecer.jpg
theme-name=Greybird
icon-theme-name=ColinaRetro
font-name=DejaVu Sans 10
indicators=~host;~spacer;~clock;~spacer;~session;~a11y;~power
clock-format=%A %d de %B, %H:%M
position=50%,center 60%,center

[Default Applications]
application/x-ms-dos-executable=wine.desktop
application/x-msdownload=wine.desktop
application/x-msi=wine.desktop
text/html=firefox-esr.desktop
x-scheme-handler/http=firefox-esr.desktop
x-scheme-handler/https=firefox-esr.desktop

<?xml version="1.0" encoding="UTF-8"?>

<channel name="xfce4-panel" version="1.0">
  <property name="configver" type="int" value="2"/>
  <property name="panels" type="array">
    <value type="int" value="1"/>
    <property name="panel-1" type="empty">
      <property name="position" type="string" value="p=10;x=0;y=0"/>
      <property name="length" type="uint" value="100"/>
      <property name="position-locked" type="bool" value="true"/>
      <property name="size" type="uint" value="30"/>
      <property name="icon-size" type="uint" value="0"/>
      <property name="nrows" type="uint" value="1"/>
      <property name="mode" type="uint" value="0"/>
      <property name="background-style" type="uint" value="0"/>
      <property name="plugin-ids" type="array">
        <value type="int" value="1"/>
        <value type="int" value="2"/>
        <value type="int" value="3"/>
        <value type="int" value="4"/>
        <value type="int" value="5"/>
        <value type="int" value="6"/>
        <value type="int" value="7"/>
      </property>
    </property>
  </property>
  <property name="plugins" type="empty">
    <property name="plugin-1" type="string" value="whiskermenu"/>
    <property name="plugin-2" type="string" value="showdesktop"/>
    <property name="plugin-3" type="string" value="tasklist">
      <property name="grouping" type="uint" value="0"/>
      <property name="show-labels" type="bool" value="true"/>
      <property name="flat-buttons" type="bool" value="false"/>
      <property name="show-handle" type="bool" value="false"/>
    </property>
    <property name="plugin-4" type="string" value="pulseaudio">
      <property name="enable-keyboard-shortcuts" type="bool" value="true"/>
    </property>
    <property name="plugin-5" type="string" value="power-manager-plugin"/>
    <property name="plugin-6" type="string" value="systray">
      <property name="square-icons" type="bool" value="true"/>
    </property>
    <property name="plugin-7" type="string" value="clock">
      <property name="mode" type="uint" value="2"/>
      <property name="digital-layout" type="uint" value="3"/>
      <property name="digital-time-format" type="string" value="%I:%M %p"/>
      <property name="tooltip-format" type="string" value="%A, %d de %B de %Y"/>
    </property>
  </property>
</channel>

<?xml version="1.0" encoding="UTF-8"?>

<channel name="xfwm4" version="1.0">
  <property name="general" type="empty">
    <property name="theme" type="string" value="ColinaClassic"/>
    <property name="button_layout" type="string" value="|HMC"/>
    <property name="title_alignment" type="string" value="left"/>
    <property name="title_font" type="string" value="DejaVu Sans Bold 9"/>
    <property name="double_click_action" type="string" value="maximize"/>
    <property name="use_compositing" type="bool" value="false"/>
    <property name="workspace_count" type="int" value="1"/>
  </property>
</channel>

<?xml version="1.0" encoding="UTF-8"?>

<channel name="xsettings" version="1.0">
  <property name="Net" type="empty">
    <property name="ThemeName" type="string" value="Greybird"/>
    <property name="IconThemeName" type="string" value="ColinaRetro"/>
  </property>
  <property name="Gtk" type="empty">
    <property name="FontName" type="string" value="DejaVu Sans 9"/>
    <property name="MonospaceFontName" type="string" value="DejaVu Sans Mono 10"/>
  </property>
  <property name="Xft" type="empty">
    <property name="Antialias" type="int" value="1"/>
    <property name="HintStyle" type="string" value="hintslight"/>
    <property name="RGBA" type="string" value="rgb"/>
  </property>
</channel>

<?xml version="1.0" encoding="UTF-8"?>

<channel name="xfce4-desktop" version="1.0">
  <property name="desktop-icons" type="empty">
    <property name="style" type="int" value="2"/>
    <property name="icon-size" type="uint" value="48"/>
    <property name="file-icons" type="empty">
      <property name="show-home" type="bool" value="true"/>
      <property name="show-filesystem" type="bool" value="true"/>
      <property name="show-trash" type="bool" value="true"/>
      <property name="show-removable" type="bool" value="true"/>
    </property>
  </property>
</channel>

favorites=colina-install.desktop,firefox-esr.desktop,thunar.desktop,org.xfce.thunar.desktop,xfce4-terminal.desktop,org.xfce.terminal.desktop,mousepad.desktop,org.xfce.mousepad.desktop,colina-wine-setup.desktop
button-title=Inicio
button-icon=start-here
show-button-title=true
show-button-icon=true
position-search-alternate=true
position-categories-alternate=true
category-icon-size=3
item-icon-size=3
menu-width=470
menu-height=520
launcher-show-description=true
profile-shape=0
confirm-session-command=true

/* Colina OS - estilo retro: barra de tareas azul brillante, botón Inicio verde,
   ventanas y botones con relieve beige. Colores y formas originales. */

/* ============================== Barra de tareas ============================== */
.xfce4-panel.background {
  background-image: linear-gradient(to bottom,
    #5a9bf5 0%, #3c84ee 6%, #2766dc 18%, #1f5bd2 60%, #1a50c4 92%, #123c9c 100%);
  border-top: 1px solid #8dbbfa;
  color: #ffffff;
}

.xfce4-panel label,
.xfce4-panel image {
  color: #ffffff;
  text-shadow: 1px 1px 0 rgba(0, 0, 0, 0.4);
}

/* Botones de ventana en la barra */
.xfce4-panel button {
  background-image: linear-gradient(to bottom, #5d9bf3 0%, #3b7ce6 45%, #2a66d6 100%);
  border: 1px solid #1a3f9a;
  border-radius: 3px;
  color: #ffffff;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.35);
  text-shadow: 1px 1px 0 rgba(0, 0, 0, 0.35);
  padding: 1px 8px;
  margin: 3px 2px;
  min-height: 0;
}

.xfce4-panel button:hover {
  background-image: linear-gradient(to bottom, #7db0f8 0%, #5290ee 45%, #3b78e0 100%);
}

.xfce4-panel button:checked,
.xfce4-panel button:active {
  background-image: linear-gradient(to bottom, #1a46a8 0%, #2352bc 100%);
  box-shadow: inset 1px 1px 3px rgba(0, 0, 0, 0.5);
}

/* Botón Inicio */
#whiskermenu-button {
  background-image: linear-gradient(to bottom, #6fd06a 0%, #3fae3a 40%, #2f9a2c 70%, #26851f 100%);
  border: 1px solid #1c6b17;
  border-radius: 3px 16px 16px 3px;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.45), 2px 0 3px rgba(0, 0, 0, 0.35);
  color: #ffffff;
  font-style: italic;
  font-weight: bold;
  font-size: 12pt;
  text-shadow: 1px 1px 2px rgba(0, 40, 0, 0.8);
  padding: 0 22px 0 8px;
  margin: 0 10px 0 0;
}

#whiskermenu-button:hover {
  background-image: linear-gradient(to bottom, #86e080 0%, #55c250 40%, #3fae38 70%, #309a28 100%);
}

#whiskermenu-button:active,
#whiskermenu-button:checked {
  background-image: linear-gradient(to bottom, #26851f 0%, #2f9a2c 100%);
}

/* Reloj y bandeja del sistema: zona más clara, como en las barras clásicas */
#clock-button,
.xfce4-panel #clock-button {
  background-image: linear-gradient(to bottom, #1aa0f0 0%, #0f8be0 50%, #0b78cc 100%);
  border: none;
  border-left: 1px solid #0a3f98;
  border-radius: 0;
  box-shadow: inset 1px 0 0 rgba(255, 255, 255, 0.25);
  margin: 0;
  padding: 0 12px;
}

/* ============================ Menú Inicio (Whisker) ============================ */
#whiskermenu-window {
  border: 2px solid #1a4fc0;
  border-radius: 8px 8px 0 0;
}

/* ============================== Aplicaciones GTK =============================== */
.background {
  background-color: #ece9d8;
}

button {
  background-image: linear-gradient(to bottom, #ffffff 0%, #f3f1e6 55%, #dedac8 100%);
  border: 1px solid #1c4d8f;
  border-radius: 3px;
  color: #000000;
  box-shadow: none;
  text-shadow: none;
  padding: 3px 10px;
}

button:hover {
  background-image: linear-gradient(to bottom, #fffdf3 0%, #fff4d2 55%, #ffe39a 100%);
  border-color: #e0922a;
}

button:active,
button:checked {
  background-image: linear-gradient(to bottom, #d2cfbd 0%, #e6e3d3 100%);
  box-shadow: inset 1px 1px 2px rgba(0, 0, 0, 0.25);
}

button:disabled {
  background-image: none;
  background-color: #f4f2e8;
  border-color: #c4c0b0;
  color: #9a9788;
}

menubar,
.menubar {
  background-image: linear-gradient(to bottom, #fbfaf4, #ece9d8);
  border-bottom: 1px solid #c4c0b0;
}

menubar > menuitem:hover,
.menubar > .menuitem:hover {
  background-color: #316ac5;
  color: #ffffff;
}

menu,
.menu,
.popup {
  background-color: #ffffff;
  border: 1px solid #8c8975;
  box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

menuitem:hover,
.menuitem:hover {
  background-color: #316ac5;
  color: #ffffff;
}

toolbar,
.toolbar {
  background-image: linear-gradient(to bottom, #fbfaf4, #ece9d8);
  border-bottom: 1px solid #c4c0b0;
}

entry,
spinbutton {
  background-color: #ffffff;
  border: 1px solid #7f9db9;
  border-radius: 2px;
  box-shadow: none;
}

entry:focus,
spinbutton:focus {
  border-color: #316ac5;
}

selection,
.view:selected,
row:selected,
iconview:selected {
  background-color: #316ac5;
  color: #ffffff;
}

scrollbar slider {
  background-image: linear-gradient(to right, #d6e4fb, #b0cbf6);
  border: 1px solid #7ea3e0;
  border-radius: 3px;
  min-width: 14px;
  min-height: 24px;
}

notebook > header > tabs > tab:checked {
  background-color: #fffffe;
  border-top: 2px solid #f2a63b;
}

tooltip,
.tooltip {
  background-color: #ffffe1;
  color: #000000;
  border: 1px solid #000000;
  border-radius: 0;
}

[Desktop Entry]
Type=Application
Name=Instalar Colina OS
Comment=Instala el sistema en el disco duro
Exec=sudo -E calamares
Icon=system-software-install
Terminal=false
Categories=System;
Keywords=instalar;install;

[Desktop Entry]
Type=Application
Name=Compatibilidad con Windows
Comment=Prepara Wine y las fuentes para programas de Windows
Exec=/usr/local/bin/colina-wine-setup
Icon=wine
Terminal=false
Categories=System;Settings;
Keywords=wine;windows;exe;

#!/bin/sh
# Aplica el fondo predeterminado de Colina OS la primera vez que se inicia sesión
# y activa el cambio de fondo en cada arranque (entre las imágenes de la misma carpeta).
DIR=/usr/share/backgrounds/colina
IMG="$DIR/colina-manana.jpg"
MARK="$HOME/.config/colina/wallpaper-applied"

[ -f "$MARK" ] && exit 0
[ -f "$IMG" ] || exit 0

# Deja que xfdesktop termine de arrancar
sleep 3

# Un valor por cada monitor conectado
for mon in $(xrandr --query 2>/dev/null | awk '/ connected/ {print $1}'); do
  base="/backdrop/screen0/monitor${mon}/workspace0"
  xfconf-query -c xfce4-desktop -p "$base/last-image" -n -t string -s "$IMG"
  xfconf-query -c xfce4-desktop -p "$base/image-style" -n -t int -s 5
  xfconf-query -c xfce4-desktop -p "$base/backdrop-cycle-enable" -n -t bool -s true
  xfconf-query -c xfce4-desktop -p "$base/backdrop-cycle-period" -n -t int -s 3
  xfconf-query -c xfce4-desktop -p "$base/backdrop-cycle-random-order" -n -t bool -s true
done

# Propiedades que ya existieran con otros nombres de monitor
xfconf-query -c xfce4-desktop -l 2>/dev/null | grep '/last-image$' | while read -r p; do
  xfconf-query -c xfce4-desktop -p "$p" -s "$IMG"
done

mkdir -p "$(dirname "$MARK")" && : > "$MARK"

#!/bin/sh
# Prepara el entorno de Windows (Wine) del usuario y agrega fuentes comunes.
export WINEPREFIX="${WINEPREFIX:-$HOME/.wine}"
# Evita los avisos de instalación de Mono/Gecko durante la inicialización
export WINEDLLOVERRIDES="mscoree,mshtml="

(
  echo "# Creando el entorno de Windows..."
  wineboot --init
  echo "# Instalando fuentes básicas (requiere Internet)..."
  winetricks -q corefonts || true
  echo "100"
) | zenity --progress --pulsate --auto-close --no-cancel \
    --title="Compatibilidad con Windows" --text="Preparando..."

zenity --info --title="Compatibilidad con Windows" \
  --text="Listo. Ya puedes abrir archivos .exe y .msi con doble clic." 2>/dev/null

#!/bin/sh
# Crea la caché de iconos del tema ColinaRetro (acelera el arranque del escritorio).
set -e
if command -v gtk-update-icon-cache >/dev/null 2>&1; then
	gtk-update-icon-cache -f -t /usr/share/icons/ColinaRetro || true
fi

#!/bin/sh
# Identidad del sistema: nombre, versión y mensajes de consola.
set -e

cat > /usr/lib/os-release <<'EOF'
PRETTY_NAME="Colina OS 0.1"
NAME="Colina OS"
VERSION_ID="0.1"
VERSION="0.1 (base Debian 13 trixie)"
VERSION_CODENAME=trixie
ID=colina
ID_LIKE=debian
HOME_URL="https://example.org/colina-os"
SUPPORT_URL="https://example.org/colina-os/soporte"
BUG_REPORT_URL="https://example.org/colina-os/errores"
EOF

printf 'Colina OS 0.1 \\n \\l\n\n' > /etc/issue
printf 'Colina OS 0.1\n' > /etc/issue.net

#!/bin/sh
# Habilita la arquitectura i386 e instala Wine de 32 bits,
# necesario para la mayoría de programas antiguos de Windows.
set -e

dpkg --add-architecture i386
apt-get update
apt-get install -y wine32:i386 libwine:i386
apt-get clean

# Compatibilidad con programas de Windows (Wine)
# El soporte de 32 bits (wine32:i386) se instala en config/hooks/live/0100-wine32.hook.chroot
wine
wine64
libwine
fonts-wine
winetricks
cabextract
p7zip-full
zenity

# Gráficos para juegos y aplicaciones 3D bajo Wine
libgl1-mesa-dri
mesa-vulkan-drivers
libvulkan1

# Ofimática (borra este archivo si quieres una ISO más liviana)
libreoffice-writer
libreoffice-calc
libreoffice-impress
libreoffice-gtk3
libreoffice-l10n-es

# Instalador gráfico
calamares
calamares-settings-debian
gparted

# Escritorio XFCE con aspecto clásico
xfce4
xfce4-whiskermenu-plugin
xfce4-pulseaudio-plugin
xfce4-power-manager
xfce4-power-manager-plugins
xfce4-notifyd
xfce4-screenshooter
xfce4-taskmanager
xfce4-terminal
thunar-archive-plugin
thunar-volman
mousepad
ristretto
file-roller
gvfs-backends
gvfs-fuse
udisks2

# Pantalla de inicio de sesión
lightdm
lightdm-gtk-greeter

# Red y sonido
network-manager-gnome
pipewire-audio
pavucontrol

# Apariencia
greybird-gtk-theme
tango-icon-theme
adwaita-icon-theme
fonts-dejavu
fonts-liberation2

# Navegador (en español)
firefox-esr
firefox-esr-l10n-es-es

# Base del sistema de escritorio
x11-xserver-utils
dbus-x11
xdg-user-dirs-gtk
sudo
locales

# Firmware y controladores (requiere el área non-free-firmware)
firmware-linux
firmware-misc-nonfree
firmware-iwlwifi
firmware-realtek
firmware-atheros
firmware-amd-graphics
amd64-microcode

# Herramientas básicas
curl
wget
htop
bash-completion
man-db

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

chroot/
binary/
cache/
.build/
*.iso
*.img
*.log
*.contents
*.files
*.packages
live-image-*
config/binary
config/bootstrap
config/chroot
config/common
config/source

#!/usr/bin/env bash
# Construye la ISO de Colina OS (Debian 13 + XFCE + Wine).
# Uso: sudo ./build.sh
set -euo pipefail
cd "$(dirname "$0")"

if [ "$(id -u)" -ne 0 ]; then
  echo "Este script necesita permisos de root: sudo ./build.sh" >&2
  exit 1
fi

faltan=()
for cmd in lb debootstrap mksquashfs xorriso; do
  command -v "$cmd" >/dev/null 2>&1 || faltan+=("$cmd")
done
if [ "${#faltan[@]}" -gt 0 ]; then
  echo "Faltan herramientas: ${faltan[*]}" >&2
  echo "Instálalas con:" >&2
  echo "  sudo apt install live-build debootstrap squashfs-tools xorriso mtools dosfstools grub-pc-bin grub-efi-amd64-bin syslinux syslinux-utils isolinux" >&2
  exit 1
fi

# Genera el tema de ventanas y los iconos (solo biblioteca estándar de Python).
# Los fondos de escritorio ya vienen hechos en config/includes.chroot/usr/share/backgrounds/colina.
python3 tools/generate_assets.py
python3 tools/generate_icons.py

lb clean
lb config
lb build

echo
echo "Listo. ISO generada:"
ls -lh ./*.iso

# Colina OS

Distribución Linux basada en **Debian 13 (trixie)** con un escritorio **XFCE de aspecto clásico**
(barra de tareas azul, botón Inicio verde, ventanas con barra de título azul) y **compatibilidad
con programas de Windows** mediante Wine.

> "Colina OS" es un nombre provisional. Para cambiarlo: `grep -ril colina .` y reemplaza.

## Qué incluye

- Base Debian estable, construida con `live-build` (ISO híbrida BIOS/UEFI).
- Escritorio XFCE + LightDM de estilo retro, todo **original**: tema de ventanas (azul brillante),
  barra de tareas con botón Inicio verde, tema de iconos propio (`ColinaRetro`) y cinco fondos de
  colinas (mañana, primavera, atardecer, niebla y otoño) que cambian en cada arranque.
- Wine (64 y 32 bits), winetricks, Vulkan y Mesa. Doble clic en `.exe` / `.msi` los abre con Wine.
- Instalador gráfico Calamares, LibreOffice, Firefox ESR y firmware de hardware común.
- Idioma por defecto: español. Usuario en modo live: `user` / contraseña `live`.

## Requisitos para construir

- Debian 12/13 o Ubuntu reciente (en máquina real o VM), ~20 GB libres y acceso a Internet.
- Paquetes: `sudo apt install live-build debootstrap squashfs-tools xorriso mtools dosfstools grub-pc-bin grub-efi-amd64-bin syslinux syslinux-utils isolinux`

## Construir y probar

### Opción A: en GitHub (sin instalar nada)

1. Sube el proyecto a un repositorio **público** de GitHub. En uno privado el almacenamiento
   gratuito de artefactos (500 MB) no alcanza para la ISO.
2. En la pestaña **Actions** elige **Construir ISO** y pulsa **Run workflow**
   (puedes desmarcar LibreOffice para una ISO más liviana).
3. Al terminar (30-60 min) descarga el artefacto **colina-os-iso**: un .zip que contiene la ISO.
   Si falla, descarga **build-log** para ver el error.

Cada cambio que subas a `main` dentro de `auto/`, `config/` o `tools/` vuelve a construir la ISO.
Subir archivos desde Windows pierde los permisos de ejecución; el workflow los restablece solo.

### Opción B: en tu máquina Debian/Ubuntu

```bash
sudo ./build.sh        # genera colina-os-amd64.hybrid.iso (tarda 20-60 min)
./run-vm.sh            # la prueba en QEMU
```

`build.sh` genera antes el tema y el fondo con `tools/generate_assets.py` si no existen.

### Probar en VirtualBox (Windows)

1. **Nueva** → Tipo: Linux, Versión: Debian (64-bit). Elige la ISO descargada.
2. Memoria: 4096 MB, procesadores: 2, disco: 30 GB.
3. Antes de iniciar: **Configuración → Pantalla** → memoria de vídeo 128 MB y controlador gráfico VMSVGA.
4. Inicia la máquina. Para instalar, abre **Inicio → Instalar Colina OS**.

## Estructura

```
auto/                       Configuración de live-build (distribución, idioma, ISO)
config/package-lists/       Paquetes por categoría (*.list.chroot)
config/hooks/live/          Scripts que corren dentro del sistema al construirlo
config/includes.chroot/     Archivos que se copian tal cual al sistema final
  etc/skel/.config/         Configuración por defecto del usuario (panel, tema, iconos)
  usr/share/themes/         Tema de ventanas ColinaClassic (generado)
  usr/share/backgrounds/    Fondo de escritorio (generado)
  usr/local/bin/            Utilidades propias (colina-wine-setup, colina-set-wallpaper)
tools/generate_assets.py    Tema de ventanas xfwm4 (se ejecuta en cada build)
tools/generate_icons.py     Tema de iconos ColinaRetro en SVG (se ejecuta en cada build)
tools/generate_wallpapers.py  Fondos de colinas con render 3D procedural (ya incluidos como .jpg;
                            solo hace falta ejecutarlo para crear fondos nuevos: numpy, scipy, pillow)
```

## Personalizar

- **Paquetes:** edita los `.list.chroot` (borra `office.list.chroot` para una ISO más liviana).
- **Colores y formas:** `tools/generate_assets.py` (ventanas), `tools/generate_icons.py` (iconos) y `gtk.css` (barra de tareas y aplicaciones).
- **Fondos nuevos:** `python3 tools/generate_wallpapers.py <escena> --seed N` (escenas en `SCENES`); copia los .jpg a `config/includes.chroot/usr/share/backgrounds/colina/`.
- **Idioma y teclado:** `--bootappend-live` en `auto/config` (`locales=`, `keyboard-layouts=`, `timezone=`).
- **Nombre y versión:** `config/hooks/live/0200-branding.hook.chroot`.

## Compatibilidad con Windows: qué esperar

Wine ejecuta muchos programas y juegos de Windows, pero no todos. Revisa
[appdb.winehq.org](https://appdb.winehq.org) antes de prometer compatibilidad con algo concreto.
Al primer uso, el usuario puede abrir **Compatibilidad con Windows** en el menú Inicio para
preparar el entorno y las fuentes básicas.

## Marca y licencias

- Todo el arte (tema, iconos, fondos, colores) es original: no se usan logos, fondos, iconos ni nombres de Microsoft.
- Los paquetes de Debian conservan sus licencias; si distribuyes la ISO, debes ofrecer el código fuente
  correspondiente (`lb config --source true` lo genera).

## Próximos pasos sugeridos

1. Construir la primera ISO y probarla en una VM.
2. Personalizar el instalador Calamares (marca propia, ocultar el acceso directo al instalar).
3. Logo y pantalla de arranque propios (`config/bootloaders/`, Plymouth).
4. Repositorio APT propio para tus paquetes.

#!/usr/bin/env bash
# Prueba la ISO en QEMU. Uso: ./run-vm.sh [archivo.iso]
set -euo pipefail
cd "$(dirname "$0")"

ISO="${1:-$(ls -t ./*.iso 2>/dev/null | head -n1 || true)}"
if [ -z "${ISO:-}" ] || [ ! -f "$ISO" ]; then
  echo "No encuentro ninguna ISO. Ejecuta primero: sudo ./build.sh" >&2
  exit 1
fi

KVM=""
[ -w /dev/kvm ] && KVM="-enable-kvm -cpu host"

# shellcheck disable=SC2086
exec qemu-system-x86_64 $KVM -m 4096 -smp 2 -vga virtio -display gtk -cdrom "$ISO" -boot d

#!/bin/sh
# Configuración de live-build para Colina OS (base Debian 13 "trixie").
# Se ejecuta automáticamente con `lb config`.

set -e

lb config noauto \
	--mode debian \
	--distribution trixie \
	--architectures amd64 \
	--linux-flavours amd64 \
	--archive-areas "main contrib non-free-firmware" \
	--binary-images iso-hybrid \
	--bootloaders "grub-efi,syslinux" \
	--debian-installer none \
	--memtest none \
	--iso-application "Colina OS" \
	--iso-publisher "Colina OS Project" \
	--iso-volume "COLINA_OS" \
	--image-name "colina-os" \
	--bootappend-live "boot=live components quiet splash locales=es_ES.UTF-8 keyboard-layouts=es timezone=America/New_York" \
	"${@}"

#!/bin/sh
set -e

lb clean noauto "${@}"

rm -f config/binary config/bootstrap config/chroot config/common config/source
rm -f build.log

#!/bin/sh
set -e

lb build noauto "${@}" 2>&1 | tee build.log
diante Wine.

> "Colina OS" es un nombre provisional. Para cambiarlo: `grep -ril colina .` y reemplaza.

## Qué incluye

- Base Debian estable, construida con `live-build` (ISO híbrida BIOS/UEFI).
- Escritorio XFCE + LightDM, con tema de ventanas, fondo y barra de tareas **originales**.
- Wine (64 y 32 bits), winetricks, Vulkan y Mesa. Doble clic en `.exe` / `.msi` los abre con Wine.
- Instalador gráfico Calamares, LibreOffice, Firefox ESR y firmware de hardware común.
- Idioma por defecto: español. Usuario en modo live: `user` / contraseña `live`.

## Requisitos para construir

- Debian 12/13 o Ubuntu reciente (en máquina real o VM), ~20 GB libres y acceso a Internet.
- Paquetes: `sudo apt install live-build debootstrap squashfs-tools xorriso mtools dosfstools grub-pc-bin grub-efi-amd64-bin syslinux syslinux-utils isolinux python3-pil`

## Construir y probar

### Opción A: en GitHub (sin instalar nada)

1. Sube el proyecto a un repositorio **público** de GitHub. En uno privado el almacenamiento
   gratuito de artefactos (500 MB) no alcanza para la ISO.
2. En la pestaña **Actions** elige **Construir ISO** y pulsa **Run workflow**
   (puedes desmarcar LibreOffice para una ISO más liviana).
3. Al terminar (30-60 min) descarga el artefacto **colina-os-iso**: un .zip que contiene la ISO.
   Si falla, descarga **build-log** para ver el error.

Cada cambio que subas a `main` dentro de `auto/`, `config/` o `tools/` vuelve a construir la ISO.
Subir archivos desde Windows pierde los permisos de ejecución; el workflow los restablece solo.

### Opción B: en tu máquina Debian/Ubuntu

```bash
sudo ./build.sh        # genera colina-os-amd64.hybrid.iso (tarda 20-60 min)
./run-vm.sh            # la prueba en QEMU
```

`build.sh` genera antes el tema y el fondo con `tools/generate_assets.py` si no existen.

### Probar en VirtualBox (Windows)

1. **Nueva** → Tipo: Linux, Versión: Debian (64-bit). Elige la ISO descargada.
2. Memoria: 4096 MB, procesadores: 2, disco: 30 GB.
3. Antes de iniciar: **Configuración → Pantalla** → memoria de vídeo 128 MB y controlador gráfico VMSVGA.
4. Inicia la máquina. Para instalar, abre **Inicio → Instalar Colina OS**.

## Estructura

```
auto/                       Configuración de live-build (distribución, idioma, ISO)
config/package-lists/       Paquetes por categoría (*.list.chroot)
config/hooks/live/          Scripts que corren dentro del sistema al construirlo
config/includes.chroot/     Archivos que se copian tal cual al sistema final
  etc/skel/.config/         Configuración por defecto del usuario (panel, tema, iconos)
  usr/share/themes/         Tema de ventanas ColinaClassic (generado)
  usr/share/backgrounds/    Fondo de escritorio (generado)
  usr/local/bin/            Utilidades propias (colina-wine-setup, colina-set-wallpaper)
tools/generate_assets.py    Genera el arte original por código
```

## Personalizar

- **Paquetes:** edita los `.list.chroot` (borra `office.list.chroot` para una ISO más liviana).
- **Colores y formas:** `tools/generate_assets.py` (ventanas, fondo) y `gtk.css` (barra de tareas).
- **Idioma y teclado:** `--bootappend-live` en `auto/config` (`locales=`, `keyboard-layouts=`, `timezone=`).
- **Nombre y versión:** `config/hooks/live/0200-branding.hook.chroot`.

## Compatibilidad con Windows: qué esperar

Wine ejecuta muchos programas y juegos de Windows, pero no todos. Revisa
[appdb.winehq.org](https://appdb.winehq.org) antes de prometer compatibilidad con algo concreto.
Al primer uso, el usuario puede abrir **Compatibilidad con Windows** en el menú Inicio para
preparar el entorno y las fuentes básicas.

## Marca y licencias

- Todo el arte (tema, fondo, colores) es original: no se usan logos, fondos, iconos ni nombres de Microsoft.
- Los paquetes de Debian conservan sus licencias; si distribuyes la ISO, debes ofrecer el código fuente
  correspondiente (`lb config --source true` lo genera).

## Próximos pasos sugeridos

1. Construir la primera ISO y probarla en una VM.
2. Personalizar el instalador Calamares (marca propia, ocultar el acceso directo al instalar).
3. Logo y pantalla de arranque propios (`config/bootloaders/`, Plymouth).
4. Repositorio APT propio para tus paquetes.
