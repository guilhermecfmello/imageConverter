from imageConverter import ImageConverter
import basicFunctions as bf
import sys


imgName = bf.getArgs(sys.argv, "-i")
imgFormat = bf.getArgs(sys.argv, "-f")

converter = ImageConverter(imgName)

if(imgFormat == "cmyk"):
    converter.rgbToCmyk()
elif(imgFormat == "hsi"):
    converter.rgbToHsi()
exit()




