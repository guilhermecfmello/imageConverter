from matplotlib.image import imread
import matplotlib.pyplot as plt
# from PIL import Image, ImageDraw
import numpy as np
import scipy.misc as smp
import math as m


RGB_MAX = 255



class ImageConverter:
	def __init__(self, imgName):
		self.imgName = imgName

	def rgbToHsi(self):
		print("Starting convertion of image: " + self.imgName + " to format HSI...")
		print("At the end, you'll be able to see the normalized image.")

		img = imread(self.imgName)

		x = len(img)
		y = len(img[0])
		data = np.zeros((x,y,3))
		for i in range(len(img)):
			for j in range(len(img[i])):
				pixel = self.__rgbToHsiPix(img[i][j][0], img[i][j][1], img[i][j][2])
				newPixel = self.__hsiRgbNormalizer(pixel)
				data[i][j] = newPixel
		imgPlot = plt.imshow(data)
		plt.show()

	def rgbToCmyk(self):
		print("Starting convertion of image: " + self.imgName + " to format CMYK...")
		print("At the end, you'll be able to see the normalized image.")
		
		img = imread(self.imgName)

		x = len(img)
		y = len(img[0])
		data = np.zeros((x,y,3), dtype=np.uint8 )
		for i in range(len(img)):
			for j in range(len(img[i])):
				pixel = self.__rgbToCmykPix(img[i][j][0], img[i][j][1], img[i][j][2])
				newPixel = self.__cmykRgbNormalizer(pixel)
				data[i][j] = newPixel
		imgPlot = plt.imshow(data)
		plt.show()

	def __rgbToCmykPix(self, r, g, b):
		if(r,g,b) == (0,0,0):
			return 0,0,0,1
		
		# Getting cmy
		c = 1 - r / RGB_MAX
		m = 1 - g / RGB_MAX
		y = 1 - b / RGB_MAX
		
		# Getting k
		k = min(c,m,y)
		c = (c - k) / (1 - k)
		m = (m - k) / (1 - k)
		y = (y - k) / (1 - k)
		return c, m, y, k
	
	def __rgbToHsiPix(self, r, g, b):
		R,G,B = self.__rgbNormalizer(r,g,b)

		dividend = ((R-G)+(R-B))/2
		divisor = np.sqrt(((R-G)**2)+((R-B)*(G-B)))
		try:
			theta = m.acos(dividend/divisor)
		except:
			print("Error calculation theta on HSI convertion")
		if B <= G:
			h = theta
		else:
			h = (2 * np.pi) - theta
		dividend = 3*(min(R,G,B))
		divisor = R+G+B
		try:
			s = 1 - (dividend / divisor)
		except e:
			print(e)
		i = (R+G+B)/3
		return h,s,i

	def __rgbNormalizer(self, r,g,b):
		r = r / RGB_MAX
		g = g / RGB_MAX
		b = b / RGB_MAX
		return r,g,b

	def __hsiRgbNormalizer(self, hsi):
		h,s,i = hsi[0],hsi[1],hsi[2]
		r,g,b = 0,0,0
		if h >= 0 and h < 120:
			b = i*(1-s)
			r = i*(1 + (s*m.cos(h)/m.cos(60-h)))
			g = 3*i-(r+b)
		elif h >= 120 and h < 240:
			h -= 120
			r = i*(1-s)
			g = i*(1+(s*m.cos(h)/m.cos(60-h)))
			b = 3*i-(r+g)
		elif h >= 240 and h < 360:
			h -= 240
			g = i*(1-s)
			b = i*(1+(s*m.cos(h)/m.cos(60-h)))
			r = 3*i-(g+b)
		else:
			r,g,b = 255,255,255

		return [r,g,b]



	def __cmykRgbNormalizer(self, cmyk):
		k = cmyk[3]
		r = (cmyk[0]) * 255
		g = (cmyk[1]) * 255
		b = (cmyk[2]) * 255
		
		tupla = [r,g,b]
		return tupla