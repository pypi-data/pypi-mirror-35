import numpy as np
import math
import scipy.misc
import os
from tqdm import tqdm
import struct
import pprint
from collections import OrderedDict

class HndFile(object):
	'''
	HndFile is a class to store the HND header and image data in a new format.
	It saves each separtely.
		- header data is written as text to the specified filename
		- image data is saved using the scipy.misc.imsave function
				NB: the image format will be taken from the filename used
	'''
	def __init__(self, **kwargs):
		self.hndHeader = kwargs.get('hndHeader', None)
		self.uncompressedImage = kwargs.get('uncompressedImage', None)
		self.HEADER_FILENAME = kwargs.get('HEADER_FILENAME', None)
		self.IMAGE_FILENAME = kwargs.get('IMAGE_FILENAME', None)
		self.LINE_SPACE = 80
	
	def _saveHeaderInfo(self):
		title = "Header Data".center(self.LINE_SPACE)
		
		self.hndHeaderFile.writelines("="*self.LINE_SPACE + "\n" + title + "\n" + "="*self.LINE_SPACE + "\n")
		
		[self.hndHeaderFile.writelines('{0} = {1}\n'.format(k, self._format_property(self.hndHeader.get(k)))) for k in self.hndHeader.keys() if not(k.startswith('proj'))]
	
	def _format_property(self, val):
		return val
		#return val if type(val) is str else val.tolist()
	
	def _saveUncompressedImage(self):
		scipy.misc.imsave(self.IMAGE_FILENAME, self.uncompressedImage)
		
	def _closeHeaderFile(self):
		self.hndHeaderFile.close()
	
	def saveHeader(self, HEADER_FILENAME=None):
		if (self.hndHeader is None):
			print('header data not provided - set value of fp.hndHeader')
			return
		if (self.HEADER_FILENAME is None):
			print('header filename not provided - set value of fp.HEADER_FILENAME')
			return
		
		# Open file to write
		self.hndHeaderFile = open(self.HEADER_FILENAME, 'w')
		self.hndHeaderFile.seek(0)
		self.hndHeaderFile.truncate()
		
		self._saveHeaderInfo()
		self._closeHeaderFile()
	
	def saveImage(self, IMAGE_FILENAME=None):
		if (self.uncompressedImage is None):
			print('pixel data not provided - set value of fp.uncompressedImage')
			return
		if (self.IMAGE_FILENAME is None):
			print('image filename not provided - set value of fp.IMAGE_FILENAME')
			return
		self._saveUncompressedImage()




class HndReader():
	'''
	HndReader is a class to open and read a HND file. It stores the header information and the 
	pixel data
	Methods are provided for saving as a new file
	'''
	def __init__(self, filename=None):
		self.filename = filename
		self.openFile()
		self.hndFileObj = None
	
	def openFile(self):
		try:
			self.f = open(self.filename, 'rb')
		except IOError:
			# No xim file by the given name exists
			print ("xim file doesn't exist")
			exit()
	
	def headerData(self):
		self.hndHeader = OrderedDict()
		self.hndHeader['FileType'] = self.__fread('s', 32)
		self.hndHeader['FileLength'] = self.__fread('i')
		self.hndHeader['CheckSumSpec'] = self.__fread('s', 4)
		self.hndHeader['CheckSum'] = self.__fread('i')
		self.hndHeader['CreationDate'] = self.__fread('s', 8)
		self.hndHeader['CreationTime'] = self.__fread('s', 8)
		self.hndHeader['PatientID'] = self.__fread('s', 16)
		self.hndHeader['PatientSer'] = self.__fread('i')
		self.hndHeader['SeriesID'] = self.__fread('s', 16)
		self.hndHeader['SeriesSer'] = self.__fread('i')
		self.hndHeader['SliceID'] = self.__fread('s', 16)
		self.hndHeader['SliceSer'] = self.__fread('i')
		self.hndHeader['SizeX'] = self.__fread('i')
		self.hndHeader['SizeY'] = self.__fread('i')
		self.hndHeader['SliceZPos'] = self.__fread('d')
		self.hndHeader['Modality'] = self.__fread('s', 16)
		self.hndHeader['Window'] = self.__fread('i')
		self.hndHeader['Level'] = self.__fread('i')
		self.hndHeader['PixelOffset'] = self.__fread('i')
		self.hndHeader['ImageType'] = self.__fread('s', 4)
		self.hndHeader['GantryRtn'] = self.__fread('d')
		self.hndHeader['SAD'] = self.__fread('d')
		self.hndHeader['SFD'] = self.__fread('d')
		self.hndHeader['CollX1'] = self.__fread('d')
		self.hndHeader['CollX2'] = self.__fread('d')
		self.hndHeader['CollY1'] = self.__fread('d')
		self.hndHeader['CollY2'] = self.__fread('d')
		self.hndHeader['CollRtn'] = self.__fread('d')
		self.hndHeader['FieldX'] = self.__fread('d')
		self.hndHeader['FieldY'] = self.__fread('d')
		self.hndHeader['BladeX1'] = self.__fread('d')
		self.hndHeader['BladeX2'] = self.__fread('d')
		self.hndHeader['BladeY1'] = self.__fread('d')
		self.hndHeader['BladeY2'] = self.__fread('d')
		self.hndHeader['IDUPosLng'] = self.__fread('d')
		self.hndHeader['IDUPosLat'] = self.__fread('d')
		self.hndHeader['IDUPosVrt'] = self.__fread('d')
		self.hndHeader['IDUPosRtn'] = self.__fread('d')
		self.hndHeader['PatientSupportAngle'] = self.__fread('d')
		self.hndHeader['TableTopEccentricAngle'] = self.__fread('d')
		self.hndHeader['CouchVrt'] = self.__fread('d')
		self.hndHeader['CouchLng'] = self.__fread('d')
		self.hndHeader['CouchLat'] = self.__fread('d')
		self.hndHeader['IDUResolutionX'] = self.__fread('d')
		self.hndHeader['IDUResolutionY'] = self.__fread('d')
		self.hndHeader['ImageResolutionX'] = self.__fread('d')
		self.hndHeader['ImageResolutionY'] = self.__fread('d')
		self.hndHeader['Energy'] = self.__fread('d')
		self.hndHeader['DoseRate'] = self.__fread('d')
		self.hndHeader['XRayKV'] = self.__fread('d')
		self.hndHeader['XRayMA'] = self.__fread('d')
		self.hndHeader['MetersetExposure'] = self.__fread('d')
		self.hndHeader['AcqAdjustment'] = self.__fread('d')
		self.hndHeader['CTProjectionAngle'] = self.__fread('d')
		self.hndHeader['CTNormChamber'] = self.__fread('d')
		self.hndHeader['GatingTimeTag'] = self.__fread('d')
		self.hndHeader['Gating4DInfoX'] = self.__fread('d')
		self.hndHeader['Gating4DInfoY'] = self.__fread('d')
		self.hndHeader['Gating4DInfoZ'] = self.__fread('d')
		self.hndHeader['Gating4DInfoTime'] = self.__fread('d')
	
	def pixelData(self):			
		w = int(self.hndHeader['SizeX'])
		h = int(self.hndHeader['SizeY'])
		
		# Read the LUT from this location in the file with this size
		self.f.seek(1024,0)
		self.LUTsize = int(((h-1)*w)/4)
		
		# Look up table
		self.f.seek(1024,0)
		LUT = np.asarray(struct.unpack('<%iB' % self.LUTsize, self.f.read(self.LUTsize)))
		
		uncompressedPixelBuffer = self.uncompressHnd(w, h, LUT)
		
		self.uncompressedImage = np.reshape(uncompressedPixelBuffer, (h,w))
	
	def saveImage(self, IMAGE_FILENAME):
		if self.hndFileObj is None:
			kwargs = {"hndHeader" : self.hndHeader,
						"uncompressedImage" : self.uncompressedImage,
						"IMAGE_FILENAME" : IMAGE_FILENAME} #,
						#"histogramDataDict" : self.histogram,
						#"propertyDataList" : self.propertyDataList
						#}
			self.hndFileObj = HndFile(**kwargs)
		else:
			self.hndFileObj.IMAGE_FILENAME = IMAGE_FILENAME
		
		#pprint('Saving header')
		self.hndFileObj.saveImage()
		#pprint('Saving header: done')
		
	def saveHeader(self, HEADER_FILENAME):
		if self.hndFileObj is None:
			kwargs = {"hndHeader" : self.hndHeader,
						"HEADER_FILENAME" : HEADER_FILENAME,} #,
						#"histogramDataDict" : self.histogram,
						#"propertyDataList" : self.propertyDataList
						#}
			self.hndFileObj = HndFile(**kwargs)
		else:
			self.hndFileObj.HEADER_FILENAME = HEADER_FILENAME
		self.hndFileObj.saveHeader()
	
	def uncompressHnd(self, w, h, LUT):
		# Crete a buffer the size of the image
		imagePix = np.empty([w*h, 1])
		
		# Read the first row
		for i in range(0,w):
			a = self.__fread('i')
			imagePix[i] = a
		
		# Read first pixel of the second row
		a = self.__fread('i')
		i = i + 1;
		imagePix[i] = a
		
		# Decompress the rest
		lut_idx = 0
		lut_off = 0
		i = i + 1
		bytes_lookup = {0:'b', 1:'h', 2:'i'}
		for i in tqdm(range(i, w*h)):
			v = LUT[lut_idx]
			
			if lut_off == 0:
				v = v & 3
				lut_off = lut_off + 1
			elif lut_off == 1:
				v = (v & 12) >> 2
				lut_off = lut_off + 1
			elif lut_off == 2:
				v = (v & 48) >> 4
				lut_off = lut_off + 1
			elif lut_off == 3:
				v = (v & 192) >> 6
				lut_off =  0
				lut_idx = lut_idx + 1;
			
			diff = self.__fread(bytes_lookup[v])
			
			imagePix[i] = imagePix[i-1] + imagePix[i-w] + diff - imagePix[i-w-1]
			
			i = i + 1
		return self.__hnd_adjust_intensity(imagePix)
	
	def __adjust(self, b):
		HND_INTENSITY_MAX = 139000
		return b if b is 0 else math.exp(1 - (b / HND_INTENSITY_MAX)) - 1
	
	def __hnd_adjust_intensity(self, buf):
		return [self.__adjust(b) for b in buf]
	
	def __fread(self, type, nelements=1):
		d = {'b':1, 'h':2, 'i':4, 'd':8, 's':1}
		ss = self.f.read(d[type]*nelements)
		try:
			return ss.decode() if type is 's' else struct.unpack('<{}'.format(type), ss)[0]
		except:
			return ss


def __help_string():
	return 'read_hnd.py -i <inputfile> -o <outputfile> -m <metadatafile> or -f <inputfolder> or -t'

def __convert_folder(inputfolder=None):
	print('Converting contents of folder: {0!s}'.format(inputfolder))
	#print(os.getcwd())
	
	full_folder = os.path.join(inputfolder)
	files = os.listdir(inputfolder)
	if not os.path.isdir(os.path.join(inputfolder,'Processed')):	
		os.makedirs(os.path.join(inputfolder,'Processed'))
	for i in tqdm(range(len(files))):
		f = files[i]
		#outputfile = f.split('.')
		#print(outputfile[-1])
		if f.split('.')[-1] == 'hnd':
			outputfile = f.split('.')[0]
			tqdm.write("Processing file %s" % f)
			#print('-----')
			inputfile = os.path.join(inputfolder, f)
			outputheaderfile = os.path.join(inputfolder, 'Processed', outputfile) + '.txt'
			outputimagefile = os.path.join(inputfolder, 'Processed', outputfile) + '.tiff'
			
			fp = HndReader(inputfile)
			fp.headerData()
			fp.pixelData()
			fp.saveImage(outputimagefile)
			fp.saveHeader(outputheaderfile)

def __main__():
	import sys
	import getopt
	#import time
	
	inputfile = None
	outputheaderfile = None
	outputimagefile = None
	showImage = False
	convertFolder = None
	
	try:
		opts, args = getopt.getopt(sys.argv[1:],"hi:o:m:f:tp:",["ifile=","ofile=","mfile=","folder=","test","plot="])
	except getopt.GetoptError:
		print(__help_string())
		sys.exit(2)
	
	if len(opts) == 0:
		print(__help_string())
		return
	else:
		for opt, arg in opts:
			if opt == '-h':
				print(__help_string())
				sys.exit()
			elif opt in ("-i", "--ifile"):
				inputfile = arg
			elif opt in ("-o", "--ofile"):
				outputimagefile = arg
			elif opt in ("-m", "--mfile"):
				outputheaderfile = arg
			elif opt in ("-f", "--folder"):
				convertFolder = arg
			elif opt in ("-t", "--test"):
				inputfile = 'test_data/Proj_00000.hnd'
				outputheaderfile = 'test_data/Proj_00000.txt'
				outputimagefile = 'test_data/Proj_00000.tif'
			elif opt in ("-p", "--plot"):
				showImage = arg
	if convertFolder is not None:
		# Implement this
		__convert_folder(convertFolder)
	else:
		# Create a file object
		fp = HndReader(inputfile)
		
		# Read the header
		#pprint('Reading header')
		fp.headerData()
		#pprint('Reading header: Done')
		# ... and pixel data
		#pprint('pixeldata')
		if (showImage is not False) or (outputimagefile is not None):
			fp.pixelData()
		#pprint('pixeldata: Done')
		
		# Save headerData
		#pprint('Saving')
		if outputheaderfile is not None:
			fp.saveHeader(outputheaderfile)
		if outputimagefile is not None:
			fp.saveImage(outputimagefile)
		#pprint('Saving: done')
		
		# Maybe show the image
		if showImage:
			from matplotlib import pyplot as plt
			plt.imshow(fp.uncompressedImage)
			plt.show()

if __name__ == "__main__":
	__main__()
