from PIL import Image

def pixel_art(input_path, output_path, pixel_size):

    # Ouvrir l'image
    image = Image.open(input_path)

    # Redimensionner l'image en utilisant la méthode NEAREST (interpolation de pixel le plus proche)
    width, height = image.size
    new_width = width // pixel_size
    new_height = height // pixel_size
    resized_image = image.resize((new_width, new_height), resample=Image.NEAREST)

    # Redimensionner l'image à sa taille d'origine
    final_image = resized_image.resize((width, height), resample=Image.NEAREST)

    # Enregistrer l'image résultante
    final_image.save(output_path, format='PNG')

# Exemple d'utilisation
input_image_path = r'D:\Pers\git\img2pixelArt\image\bananier.webp'
output_image_path = r'D:\Pers\git\img2pixelArt\out'
pixel_size = 10  # La taille des pixels dans l'image de sortie

pixel_art(input_image_path, output_image_path, pixel_size)
