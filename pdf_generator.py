# pdf_generator.py
from PIL import Image
import os

def create_pdf_from_screenshots(folder="screenshots", output="Session_Screenshots.pdf"):
    images = []
    for file in sorted(os.listdir(folder)):
        if file.endswith(".png"):
            path = os.path.join(folder, file)
            img = Image.open(path).convert("RGB")
            images.append(img)

    if images:
        images[0].save(output, save_all=True, append_images=images[1:])
        print(f"[✓] PDF created: {output}")
    else:
        print("[!] No screenshots found.")
