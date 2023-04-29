import os
import sys
from PIL import Image

if len(sys.argv) < 2:
    print('Usage: python convert_image.py <input_image>')
    sys.exit(1)

input_image = sys.argv[1]
output_image = os.path.join(r'C:\Users\Gaming Pc\Desktop\converter\output', os.path.basename(os.path.splitext(input_image)[0])) + '.png'

if os.path.exists(input_image):
    try:
        with Image.open(input_image) as img:
            img.save(output_image, 'PNG')
            print(f'{input_image} converted to {output_image}')
    except Exception as e:
        print(f'Error converting {input_image}: {e}')
else:
    print(f'{input_image} does not exist')
