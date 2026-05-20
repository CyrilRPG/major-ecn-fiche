#!/usr/bin/env python3
"""Génère un logo placeholder `assets/logo_major_ecn.png`.

À remplacer par le logo Major ECN définitif. Exécuté automatiquement par
`install.sh` si aucun logo n'est présent.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

RED = (225, 29, 72, 255)
GOLD = (201, 169, 97, 255)
ANTHRACITE = (31, 41, 55, 255)

OUTPUT = Path(__file__).resolve().parent.parent / "assets" / "logo_major_ecn.png"


def _load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    """Charge une police pour le rendu du texte, avec repli sur la police par défaut."""
    for candidate in (
        "/System/Library/Fonts/Supplemental/Georgia.ttf",
        "/Library/Fonts/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
    ):
        if Path(candidate).exists():
            try:
                return ImageFont.truetype(candidate, size)
            except OSError:
                continue
    try:
        return ImageFont.load_default(size=size)
    except TypeError:  # Pillow < 10.1
        return ImageFont.load_default()


def generate() -> None:
    """Dessine et enregistre le logo placeholder."""
    width, height = 760, 380
    image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # Croix médicale stylisée.
    cx, cy, arm, thick = 150, 168, 86, 36
    draw.rounded_rectangle(
        [cx - thick, cy - arm, cx + thick, cy + arm], radius=10, fill=RED
    )
    draw.rounded_rectangle(
        [cx - arm, cy - thick, cx + arm, cy + thick], radius=10, fill=RED
    )

    # Texte « MAJOR ECN ».
    title_font = _load_font(94)
    sub_font = _load_font(27)
    draw.text((292, 92), "MAJOR", font=title_font, fill=ANTHRACITE)
    draw.text((294, 192), "ECN", font=title_font, fill=RED)

    # Filet décoratif or.
    draw.line([(294, 300), (610, 300)], fill=GOLD, width=4)
    draw.text((294, 314), "FICHES DE RÉVISION", font=sub_font, fill=GOLD)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    image.save(OUTPUT, "PNG")
    print(f"Logo placeholder généré : {OUTPUT}")


if __name__ == "__main__":
    generate()
