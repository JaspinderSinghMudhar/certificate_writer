# Certificate Name Generator
This Python script generates personalized certificates with names written on them.

 ### Features:
Creates individual certificates for each name in a list.
Centers the name on the certificate.
Replaces special characters in the name with hyphens for safe file naming.

### Requirements:
Python 3
Pillow library (pip install Pillow)

### Instructions:
Download or clone this repository.
Make sure you have Pillow installed (pip install Pillow).
Place your certificate image named CERTIFICATE.png in the same directory as the script.
Update the abc list in the script with the names of the certificate recipients.
Run the script (python script_name.py).

### Output:
The script will generate individual PNG image certificates named after each recipient in the abc list with hyphens replacing special characters, located in the output folder.

Font:

The script uses the Poppins-Medium.ttf font file. You can replace this with your desired font by updating the path in the font = ImageFont.truetype line.

Note:

This script is a basic example and can be further customized for different formatting needs.
