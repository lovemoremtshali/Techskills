from fpdf import FPDF

from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
from PIL import Image

image_url='https://free-braindumps.com/images/exam-dumps/DP-100/a7a1360c-d120-45af-8ecb-a45e567565f2.jpg'

driver.get(image_url)
new_img="img2.jpg"
# Wait for the page to load (adjust the wait time as needed)
time.sleep(5)

# Capture the full page as screenshot (modify as needed to capture specific area)
driver.save_screenshot(new_img)

# Close the browser
driver.quit()
# # Open the image
time.sleep(2)
img = Image.open(new_img)
f_image ="img2_fixed.jpg"
# # Save as JPEG
img.save(f_image, 'JPEG')

# Create a new PDF document
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font and size
pdf.set_font("Arial", size=12)

# Write text at a specific position (x, y)
pdf.cell(200, 10, txt="This is some simple text", ln=2, align="C")  # Adjust as needed
pdf.cell(200, 10,txt="lorem", ln=2, align="L")
pdf.line(10, 30, 200, 30)
# Save the PDF with a filename
pdf.image(f_image, x = None, y = None, w = 150, h = 100, type = '')

pdf.output("my_text_pdf3.pdf")

print("PDF created successfully!")



