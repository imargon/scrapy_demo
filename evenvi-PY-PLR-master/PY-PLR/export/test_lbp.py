#!/usr/bin/python
from GrayscaleImage import GrayscaleImage
from LocalBinaryPatternizer import LocalBinaryPatternizer

image = GrayscaleImage("../images/original.jpg")

lbp = LocalBinaryPatternizer(image)
histograms = lbp.create_features_vector()

print histograms
