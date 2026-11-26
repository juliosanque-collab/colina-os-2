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
