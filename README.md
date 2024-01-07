# Joyous Wilds Color Palette

Simple color palette for creating complementary green and pink themes with dark backgrounds.

![palette](/img/palette.png)

**Aseprite extension** and **GIMP palette file** (GPL) can be downloaded from the [Releases](https://github.com/serweryn617/joyous-wilds-palette/releases) page.

GIMP palette files can be used by most image editing software (GIMP, Aseprite, Inkscape, etc.).

# Colors

### Primary

| Color | Hex Value |
| :--- | :--- |
| ![green1](/img/green1.png) | `#00cc52` |
| ![green2](/img/green2.png) | `#00b348` |
| ![green3](/img/green3.png) | `#009a3e` |
| ![green4](/img/green4.png) | `#008134` |
| ![green5](/img/green5.png) | `#00682a` |
| ![green6](/img/green6.png) | `#004f20` |

### Accent

| Color | Hex Value |
| :--- | :--- |
| ![pink1](/img/pink1.png) | `#d849ff` |
| ![pink2](/img/pink2.png) | `#c23ee6` |
| ![pink3](/img/pink3.png) | `#ac33cd` |
| ![pink4](/img/pink4.png) | `#9628b4` |
| ![pink5](/img/pink5.png) | `#801d9b` |
| ![pink6](/img/pink6.png) | `#6a1282` |

### General

| Color | Hex Value | Usage guideline |
| :--- | :--- | :--- |
| ![white](/img/white.png)           | `#ffffff` | Active text               |
| ![text](/img/text.png)             | `#cccccc` | Text                      |
| ![light_gray](/img/light_gray.png) | `#8c8c8c` | General purpose           |
| ![dark_gray](/img/dark_gray.png)   | `#646464` | General purpose           |
| ![bg_light](/img/bg_light.png)     | `#1f1f1f` | Main area background      |
| ![bg_dark](/img/bg_dark.png)       | `#181818` | Secondary area background |

# Generating GIMP Palette File

GIMP palette file can be generated with:

```sh
python3 joyous_wilds.py > joyous_wilds.gpl
```

# Generating Aseprite Extension

Aseprite extension can be created by compressing `joyous_wilds.gpl` and `package.json` in a zip file.
