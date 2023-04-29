# JPEGtoPNGpython
A .jpeg, .jpg, and .jfif to .png converter made by ChatGPT


# Instructions

run
pip install pillow

to install the required libraries

edit gptconverter.py and change
'YOUR OUTPUT FOLDER FILE PATH GOES HERE'
in
output_image = os.path.join(r'YOUR OUTPUT FOLDER FILE PATH GOES HERE', os.path.basename(os.path.splitext(input_image)[0])) + '.png'

to the output directory file path of your choosing

simply drag a .jpeg .jpg or a .jfif onto it and it will output the converted .png into the folder you chose!
