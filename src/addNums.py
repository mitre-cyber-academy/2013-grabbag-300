from PIL import Image
import numpy as np
import argparse

def main():
	parser = argparse.ArgumentParser(
		description='Add the RGB bytes in an image')
	parser.add_argument('inFile', help='Input image file for addition')
	args = parser.parse_args()

	img = Image.open(args.inFile)
	imgArr = np.array(img)
	ax1, ax2, ax3 = imgArr.shape
	currSum = 0
	for i in range(ax1):
		for j in range(ax2):
			for k in range(ax3):
				currSum += imgArr[i,j,k]
	print currSum

if __name__ == '__main__':
	main()
