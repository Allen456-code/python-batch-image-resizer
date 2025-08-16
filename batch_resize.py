import os
from PIL import Image

input_folder = r"C:\Users\Helen\Desktop\python\input_image"
output_folder = r"C:\Users\Helen\Desktop\python\output_images"
new_width = 400
new_height = 400
output_format = "JPEG"

os.makedirs(output_folder, exist_ok=True)

for file_name in os.listdir(input_folder):
    input_path = os.path.join(input_folder, file_name)
    if not os.path.isfile(input_path):
        continue
    try:
        with Image.open(input_path) as img:
            resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            base_name = os.path.splitext(file_name)[0]
            output_path = os.path.join(output_folder, base_name + "." + output_format.lower())
            resized.save(output_path, output_format)
            print(f"Saved {output_path}")
    except Exception as e:
        print(f"Skipping {file_name}: {e}")
