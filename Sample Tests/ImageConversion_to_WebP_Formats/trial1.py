from bs4 import BeautifulSoup
import subprocess
import re
import os

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
            # Generate a unique WebP filename
            webp_filename = f'{os.path.splitext(src)[0]}.webp'
            
            # Convert the PNG image to WebP using cwebp
            try:
                subprocess.run(['"C:\Hackathons,Workshops_and_Courses\Hackathons\Hallothon 3.0\Info_Safari\Sample Tests\ImageConversion_to_WebP_Formats\Path_Programs\cwebp.exe"', src, '-o', webp_filename], check=True)
                
                # Update the image source in the HTML
                img_tag['src'] = webp_filename
            except subprocess.CalledProcessError as e:
                print(f"Error converting {src} to WebP: {e}")

    # Save the modified HTML to a new file
    output_filename = os.path.join(os.path.dirname(html_file), 'output.html')
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        output_file.write(str(soup))

# Run the conversion function with a raw string for the file path
convert_images_to_webp(r'trial1.html')
