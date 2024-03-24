# The code creates certificates with names written on them.

First, it imports libraries for working with images and fonts. Then it sets up the font and image size.

The Image_creator function takes a name and an index as input. It opens a certificate image, creates a drawing object, and sets the text to be drawn on the certificate. The function then calculates the width of the text to center align it on the certificate and draws the text. Finally, it saves the image with the name replacing special characters with hyphens.

The code creates a list of names and then iterates over the list, calling the Image_creator function for each name to generate a certificate with the corresponding name.
