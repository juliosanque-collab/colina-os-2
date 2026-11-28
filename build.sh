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
