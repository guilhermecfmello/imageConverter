from imageConverter import ImageConverter
import basicFunctions as bf
import sys

imgName = "images/" + bf.getArgs(sys.argv, "-i")
imgFormat = bf.getArgs(sys.argv, "-f")

converter = ImageConverter(imgName)


print("The images converted are normalized and turned to RGB again, to be possible to see the results.")
print("RGB => CMY respectively")
print("HSI is computed and cant be described\n")
if(imgFormat == "cmyk"):
    converter.rgbToCmyk()
elif(imgFormat == "hsi"):
    converter.rgbToHsi()
exit()
