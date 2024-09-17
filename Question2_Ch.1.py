import time

# To import PIL module, you got to intall "py -m pip install pillow" in the TERMINAL.
from PIL import Image

# Generate the number
current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0:
    generated_number += 10

print(f"Generated number: {generated_number}")

# Open and process the image
img = Image.open("HIT-137-Assignment-2/chapter1.jpg")
pixels = img.load()
width, height = img.size

# Modify pixel values
for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        new_r = (r + generated_number) % 256
        new_g = (g + generated_number) % 256
        new_b = (b + generated_number) % 256
        pixels[x, y] = (new_r, new_g, new_b)

# Save the new image
img.save("HIT-137-Assignment-2/chapter1out.jpg")

# Calculate sum of red pixel values
red_sum = sum(pixels[x, y][0] for x in range(width) for y in range(height))

print(f"Sum of red pixel values: {red_sum}")