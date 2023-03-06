from PIL import Image, ImageFilter

# Open image 
img = Image.open("example.jpg")

# Apply blur filter
blurred_img = img.filter(ImageFilter.BLUR)

# Save blurred image
blurred_img.save("example_blurred.jpg")

# Display blurred image
blurred_img.show()
