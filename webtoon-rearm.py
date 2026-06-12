#!/usr/bin/env python3

import sys
from pathlib import Path
from PIL import Image

# Accepted extensions
EXTENSIONS = {".webp", ".jpg", ".jpeg", ".png"}

def main():

    if len(sys.argv) < 2 or len(sys.argv) > 5:
        print(f"Usage: {sys.argv[0]} <images_input_path> [output_path] [output.png] [width]")
        sys.exit(1)

    input_dir = Path(sys.argv[1])
    output_dir = Path(sys.argv[2]) if len(sys.argv) >= 3 else input_dir
    output_filename = sys.argv[3] if len(sys.argv) >= 4 else "output.png"
    custom_width = int(sys.argv[4]) if len(sys.argv) == 5 else None

    if not input_dir.exists():
        raise RuntimeError(f"Error: Directory does not exist '{input_dir}'")

    if not input_dir.is_dir():
        raise RuntimeError(f"Error: '{input_dir}' is not a directory")

    # Sort by name: 001.webp, 002.webp, 003.webp...
    image_paths = sorted(
        p for p in input_dir.iterdir()
        if p.suffix.lower() in EXTENSIONS
    )

    if not image_paths:
        raise RuntimeError("No images found.")

    print(f"Found {len(image_paths)} images.")

    images = []

    for path in image_paths:
        img = Image.open(path).convert("RGB")
        print(f"Loading: {path.name} - Size: {img.width}x{img.height}")
        images.append(img)

    # Use custom width if provided, otherwise use the maximum width found
    target_width = custom_width if custom_width else max(img.width for img in images)

    resized_images = []

    for img in images:

        if img.width != target_width:
            ratio = target_width / img.width
            new_height = int(img.height * ratio)

            img = img.resize((target_width, new_height), Image.LANCZOS)

        resized_images.append(img)

    total_height = sum(img.height for img in resized_images)

    print(f"Final size: {target_width}x{total_height}")
    print("Processing and saving...")

    final_image = Image.new("RGB", (target_width, total_height), "white")

    y_offset = 0

    for img in resized_images:
        final_image.paste(img, (0, y_offset))
        y_offset += img.height

    output_file = output_dir / output_filename

    final_image.save(
        output_file,
        "PNG"
    )

    print(f"Image created: {output_file}")

if __name__ == "__main__":
    main()
