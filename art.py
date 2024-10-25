#TODO : to create a class to take the pic and turn into ascii art

import PIL.Image

# Open the uploaded image
img = PIL.Image.open("/mnt/data/image.png")

# Resize the image
width, height = img.size
aspect_ratio = height / width
new_width = 120
new_height = aspect_ratio * new_width * 0.55
img = img.resize((new_width, int(new_height)))

# Convert image to grayscale
img = img.convert('L')

# ASCII characters list
chars = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", "."]

# Map pixels to characters
pixels = img.getdata()
new_pixels = [chars[pixel // 25] for pixel in pixels]
new_pixels = ''.join(new_pixels)

# Create ASCII image string
new_pixels_count = len(new_pixels)
ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
ascii_image = "\n".join(ascii_image)

# Save ASCII art to text file
ascii_file_path = "/mnt/data/ascii_image.txt"
with open(ascii_file_path, "w") as f:
    f.write(ascii_image)

ascii_file_path
