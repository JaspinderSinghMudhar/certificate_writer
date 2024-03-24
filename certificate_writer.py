
# Use pip install Pillow 
from PIL import Image, ImageDraw, ImageFont


# Setup Font Settings and file
font = ImageFont.truetype('Poppins-Medium.ttf', 34)

# Setup Image width and height
W = 841.89

def Image_creator(x,i):
    # Set Certificate image
    i = Image.open("CERTIFICATE.png")
    # Start Drawing
    draw = ImageDraw.Draw(i)
    # Set Text
    txt = x
    # Set Width of text to make it center aligned
    w = draw.textlength(txt, font)
    # Draw Text over image
    draw.text(((W-w)/2, 250), txt, font=font, fill='#1e2433')
    # Save output Image
    i.save('output/'+ txt.replace("!@#$%^&*()[]{};:,./<>?\|`~-=_+", "-")+".png")

# Set the list of the candidates Names
abc= ["Jaspinder Singh","Deepa Kumari", "Ankita", "Sandeep"]

# Run code in loop to get all the images with the candidates name on it.
for index, x in enumerate(abc):
  Image_creator(x,index)








