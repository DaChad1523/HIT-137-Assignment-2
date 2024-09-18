import tkinter as tk
from PIL import Image, ImageTk
import time

current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0:
    generated_number += 10
    


root = tk.Tk()

image = Image.open("chapter1.jpg")
width, height = image.size

rsum = 0
for x in range(width):
    for y in range(height):
        rgb = image.getpixel((x, y))
        rsum += rgb[0]
        image.putpixel((x, y), (rgb[0] + generated_number, rgb[1] + generated_number, rgb[2] +generated_number))

print(f"Generated Number:{generated_number}")
print(rsum)


photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.pack()

image.save("chapter1out.png")

root.mainloop()
