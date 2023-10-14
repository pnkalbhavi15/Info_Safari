from bs4 import BeautifulSoup
import subprocess
import re

# Function to convert PNG images to WebP and update the HTML
def convert_images_to_webp(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Find all image tags in the HTML
    img_tags = soup.find_all('img')

    for img_tag in img_tags:
        src = img_tag['src']
        
        # Check if the image is in PNG format
        if src.lower().endswith('.png'):
            # Convert the PNG image to WebP using cwebp
            subprocess.run(['cwebp', src, '-o', f'{src[:-4]}.webp'])
            
            # Update the image source in the HTML
            img_tag['src'] = f'{src[:-4]}.webp'

    # Save the modified HTML to a new file
    with open('output.html', 'w', encoding='utf-8') as output_file:
        output_file.write(str(soup))

# Run the conversion function
convert_images_to_webp('C:\Hackathons,Workshops_and_Courses\Hackathons\Hallothon 3.0\trial1.html')
