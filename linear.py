# Processing images by Doing The Simplest Thing
from pathlib import Path
from PIL import Image
from PIL import ImageFilter
import sys

in_path = Path.cwd() / "images"
out_path = Path.cwd() / "processed"

if not in_path.exists():
    print(f"Cannot find {in_path.name} directory")
    sys.exit(1)

if not out_path.exists():
    out_path.mkdir()

import time
start = time.time()
names = list(in_path.glob("*"))
for image_file in names:
    outfile = out_path / image_file.name
    try:
        image = Image.open(image_file)
        # image.thumbnail((128, 128))
        image.filter(ImageFilter.DETAIL)
        #image.save(outfile, "JPEG")
    except IOError:
        print(f"Cannot create thumbnail for {infile}")

print(time.time() - start)

