# A simple Augmented Reality setup for mouse embryo models
#### **By Stefano and Francesca Vianello**

This GitHub repository provides a simple setup with the mininal elements to be able to trigger the appearance of an embryo model when a QR code is scanned through a phone. Such QR codes could be incorporated in a figure for publication, in a poster at a scientific conference, in slides of a presentation, or in any format one might wat to augment.

![Illustration of ARjs setup](README_image1.jpg)

* The folder "assets" contains the embryo model(s) one wants to make appear. After having created the corresponding scene in Blender, export the objects as a ".obj" file (File>Export>Wavefront (.obj)). This will also create a materials file (.mtl). Copy both files in this folder.

* The folder "barcodes" contains a library of black and white motifs that can be used as triggers of your embryonic model. When a phone camera will detect one of such motifs, the corresponding object from your asset folder will appear.

