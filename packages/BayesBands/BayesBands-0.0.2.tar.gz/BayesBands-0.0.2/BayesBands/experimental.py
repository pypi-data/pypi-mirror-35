import numpy as np

class Data:

	def __init__ (self,filename,errorType):
		self.filename = filename
		self.error = errorType
		
		f = open(filename)

		angle = []
		xs = []
		err = []
		if (self.error=="percent"):
			for line in f:
				line = line.strip().split()
				angle.append(float(line[0]))
				xs.append(float(line[1]))
				err.append(float(line[2])*float(line[1]))
		elif (self.error=="value"):
			for line in f:
				line = line.strip().split()
				angle.append(float(line[0]))
				xs.append(float(line[1]))
				err.append(float(line[2]))
		else:
			print ("Assuming 1% errors on the data")
			print ("There are either no errors or error type is unknown")
			for line in f:
				line = line.strip().split()
				angle.append(float(line[0]))
				xs.append(float(line[1]))
				err.append(0.01*float(line[2]))

		self.angles = angle
		self.xs = xs
		self.error = err

	def getAngles(self):
		return(self.angles)

	def getCrossSection(self):
		return(self.xs)
	
	def getError(self):
		return(self.error)
		