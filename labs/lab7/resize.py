from PIL import Image

# Open image
img = Image.open("example.jpg")

# Resize image
new_size = (img.size[0] // 2, img.size[1] // 2)
resized_img = img.resize(new_size)

# Save resized image
resized_img.save("example_resized.jpg")

# Display resized image
resized_img.show()
