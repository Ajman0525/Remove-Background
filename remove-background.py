from rembg import remove
from rembg.session_factory import new_session
from PIL import Image

model_name = "u2net_human_seg"
session = new_session(model_name) 

input_image_path = 'your_input_image.png' 
output_image_path = 'your_output_image.png' 

input_image = Image.open(input_image_path)
output_image = remove(input_image, session=session)

output_image.save(output_image_path)
print(f"Background removed using {model_name}. Saved to: {output_image_path}")