from webptools import cwebp

# pass input_image(.jpeg,.pnp .....) path ,
# output_image(give path where to save and image file name with .webp file tyC:\Hackathons,Workshops_and_Courses\Hackathons\Hallothon 3.0\Info_Safari\Sample Tests\Image Conversion to WebP Formats\job.jpegpe extension)
print(cwebp(input_image="job.jpeg", output_image="python_logo.webp",
            option="-q 80", logging="-v"))