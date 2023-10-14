import os
import subprocess
from bs4 import BeautifulSoup

# HTML file (make sure it's in the same directory as your script and images)
html_file = "trial1_conv.html"

# Function to convert PNG images to WebP
def convert_images_to_webp(html_dir):
    for root, dirs, files in os.walk(html_dir):
        for file in files:
            if file.lower().endswith(".png"):
                png_path = os.path.join(root, file)
                webp_path = os.path.splitext(png_path)[0] + ".webp"
                subprocess.run(["cwebp", png_path, "-o", webp_path])
                os.remove(png_path)

# Function to update HTML image tags
def update_html_image_tags(html_file):
    with open(html_file, "r") as html:
        soup = BeautifulSoup(html, "html.parser")
        for img_tag in soup.find_all("img"):
            src = img_tag.get("src")
            if src.lower().endswith(".png"):
                webp_src = os.path.splitext(src)[0] + ".webp"
                img_tag["src"] = webp_src
    with open(html_file, "w") as updated_html:
        updated_html.write(str(soup))

if __name__ == "__main__":
    html_dir = os.path.dirname(html_file)
    convert_images_to_webp(html_dir)
    update_html_image_tags(html_file)
