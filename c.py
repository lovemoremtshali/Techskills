from PIL import Image

# Open the image
img = Image.open('img2.jpg')

# Save as JPEG
img.save('img2_fixed.jpeg', 'JPEG')