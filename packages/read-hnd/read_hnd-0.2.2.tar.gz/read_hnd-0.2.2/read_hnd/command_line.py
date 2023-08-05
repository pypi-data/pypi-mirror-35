from read_hnd import *
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import filedialog

def main():
	read_hnd.main()

#def main():
#	'''
#	Entry point from the command line
#	'''
#	def __select_file():
#		root = tk.Tk()
#		root.withdraw()
#		inputfile = filedialog.askopenfilename()
#		outputimagefile = filedialog.asksaveasfilename()
#		outputheaderfile = filedialog.asksaveasfilename()
#		root.update()
#		return (inputfile, outputimagefile, outputheaderfile)
#	
#	#inputfile = 'test_data/Proj_00000.hnd'
#	inputfile, outputimagefile, outputheaderfile = __select_file()
#	
#	fp = HndReader(inputfile)
#	fp.saveImage(outputheaderfile, outputimagefile)
#	
#	# Read the header
#	fp.headerData()
#	# ... and pixel data
#	fp.pixelData()
#		
#	# Show the image
#	plt.imshow(fp.uncompressedImage)
#	plt.show()