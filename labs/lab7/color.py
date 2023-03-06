from PIL import Image

# Open image
img = Image.open("example.jpg")

# Convert image to black and white
bw_img = img.convert('L')

# Save the black and white image to a file
bw_img.save("example_bw.jpg")

# Display new image
bw_img.show()
