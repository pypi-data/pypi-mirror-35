import numpy as np

class Bands:

	def __init__ (self,filename):
		self.filename = filename
		self.xscalc = np.zeros((1601,181))
		self.nRuns = 1600
		self.nAngles = 181
		f = open(filename)
		tcount = 0 # angle counter
		rcount = 0 # counter for run number
		for line in f:
			if (tcount==181):
				tcount = 0
				rcount = rcount+1
			if ("END" not in line) and ("#" not in line) and ("@" not in line) and ("&" not in line) and (line.strip() != ""):
				line = line.strip().split()
				self.xscalc[0][tcount] = float(line[0])
				self.xscalc[rcount+1][tcount] = float(line[1])
				tcount = tcount + 1


	def getAngles (self):
		return (self.xscalc[0])

	def meanCrossSection (self, percent):
		meanXS = []
		allRuns = self.xscalc
		nCalc = self.nRuns
		if (percent > 1.0):
			percent = percent/100.0

		nPercentRuns = percent*nCalc
		for i in range(0,181):
			temp = []
			for j in range(nCalc):
				temp.append(allRuns[j+1][i])
			temp.sort()
			tmin = temp[0]
			tmax = temp[int(nPercentRuns)-1]
			diff = tmax - tmin
			for m in range(1,1600-int(nPercentRuns)):
				ind = 1
				if (temp[int(percent)-1+m] - temp[m])<diff:
					tmin = temp[m]
					tmax = temp[int(nPercentRuns)-1+m]
					diff = tmax - tmin
					ind = m
			meanXS.append(np.mean(temp[ind:int(nPercentRuns)-1+ind]))

		return (meanXS)

	def confidenceBands (self,percent):
		uBand = []
		lBand = []
		allRuns = self.xscalc
		nCalc = self.nRuns
		if (percent > 1.0):
			percent = percent/100.0

		nPercentRuns = percent*nCalc
		for i in range(0,181):
			temp = []
			for j in range(nCalc):
				temp.append(allRuns[j+1][i])
			temp.sort()
			tmin = temp[0]
			tmax = temp[int(nPercentRuns)-1]
			diff = tmax - tmin
			for m in range(1,1600-int(nPercentRuns)):
				ind = 1
				if (temp[int(nPercentRuns)-1+m] - temp[m])<diff:
					tmin = temp[m]
					tmax = temp[int(nPercentRuns)-1+m]
					diff = tmax - tmin
					ind = m
			uBand.append(tmax)
			lBand.append(tmin)

		return (uBand,lBand)
			
		
		
