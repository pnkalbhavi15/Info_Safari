import re
import fitz
import PIL.Image 
import io
from pdfminer.high_level import extract_pages,extract_text

#for page_layout in extract_pages("Anime2.pdf"):
 # for element in page_layout:
  #  print(element)
text =   extract_text("anime.pdf")
print(text)
'''
pattern= re.compile(r"[a-zA-Z]+,{1}\s{1}")
matches=pattern.findall(text)
print(matches)
  
pdf =fitz.open("the_pdfile.pdf")
counter=2
for i in range (len(pdf)):
  page=pdf[i]
  image = page.get_image()
  for image in image :
    base_img=pdf.extract_image(image[0])
    image_data=base_img["image"]
    '''
