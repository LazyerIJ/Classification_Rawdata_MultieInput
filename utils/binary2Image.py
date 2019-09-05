import os, sys, glob
from PIL import Image

def getBinaryData(filename):
	binaryValues = []
	file = open(filename, "rb")
	data = file.read(1)
	while data != b"":
		try:
			binaryValues.append(ord(data))

		except TypeError:
			pass

		data = file.read(1)

	return binaryValues


def createGreyScaleImageSpecificWith(dataSet, outputfilename, resultDir, width=0):
	if (width == 0):
		size = len(dataSet)

		if (size < 10240):
			width = 32

		elif (10240 <= size <= 10240*3):
			width = 64

		elif (10240*3 <= size <= 10240*6):
			width = 128

		elif (10240*6 <= size <= 10240*10):
			width = 256

		elif (10240*10 <= size <= 10240*20):
			width = 384

		elif (10240*20 <= size <= 10240*50):
			width = 512

		elif (10240*50 <= size <= 10240*100):
			width = 768

		else:
			width = 1024


	height = int(size/width)+1
	image = Image.new('L', (width, height))
	image.putdata(dataSet)

	imagename = outputfilename+".png"
	image.save(os.path.join(resultDir, imagename))
	#image.show()
	print (imagename+" Created")


if __name__=="__main__":
	file_full_path = sys.argv[1]
	resultDir = sys.argv[2]
	#path = os.path.dirname(file_full_path)
	#base_name = os.path.splitext(os.path.basename(file_full_path))[0]
	#outputfilename = os.path.join(path, base_name)

	for i in glob.glob(file_full_path+"/*"):

		binaryData = getBinaryData(i)
		outputfilename = i.split('/')[-1]
		createGreyScaleImageSpecificWith(binaryData, outputfilename, resultDir)
