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
