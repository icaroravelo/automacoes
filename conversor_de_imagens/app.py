from PIL import Image
import os

# Folder containing images
image_folder = './raw_images'

# Folder to save converted images
converted_images_folder = './converted_images'

# List of image formats to convert
images = [f for f in os.listdir(image_folder) if f.endswith('png')]

# Guarantee that the converted images folder exists, if not, create one
if not os.path.exists(converted_images_folder):
    os.makedirs(converted_images_folder)

# Loop through each image in the folder
for image_name in images:
    # Complete file path for image
    image_path = os.path.join(image_folder, image_name)

    # File name without extension
    name_without_extensions = os.path.splitext(image_name)[0]

    # Complete file path for converted image
    converted_image_path = os.path.join(converted_images_folder, name_without_extensions + '.pdf')

    # Open image using Pillow 
    image = Image.open(image_path)

    # Redimension image to 900x800 pixels
    new_dimension = (900, 800)
    dimension_image = image.resize(new_dimension)

    # Save image as PDF
    dimension_image.save(converted_image_path, "PDF", resolution=100.0)

print('Conversão com redimensionamento concluída!')