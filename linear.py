# Processing images by Doing The Simplest Thing
from pathlib import Path
from PIL import Image
import sys

in_path = Path.cwd() / "images"
out_path = Path.cwd() / "processed"

if not in_path.exists():
    print(f"Cannot find {in_path.name} directory")
    sys.exit(1)

if not out_path.exists():
    out_path.mkdir()

for image_file in in_path.glob("*"):
    outfile = out_path / image_file.stem + "-thumb.jpg"
    try:
        image = Image.open(image_file)
        im.thumbnail((128, 128))
        im.save(outfile, "JPEG")
    except IOError:
        print(f"Cannot create thumbnail for {infile}")

