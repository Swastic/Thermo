 import math
	class Piston(object):
    def __init__(self, atmosphericPressure, mass, crossSectionalArea, initialPressure, initialVolume, initialtemprature, gasConstant, moles):
        self.atmP= atmosphericPressure
        self.m= mass
        self.csa= crossSectionalArea
        self.initP= initialPressure
        self.initV= initialVolume
        self.initTemp= initialTemprature
        self.R= gasConstant
		self.moles= moles
	def pressure(self):
	""" This function calculates the total pressure in a piston cylinder system when a mass is kept on the piston"""
		return self.atmP + (self.m * 9.8)/self.csa
	def spring(self, springConstant, finalLength, length):
	"""This function calculates the total pressure in a piston cylinder system attached with a spring and a mass kept on it"""
	    self.K= springConstant
		self.final= finalLength
		self.length= length
		return (self.m * 9.8)/self.csa + self.atmP + self.K*((self.final-self.length)/self.csa)
	def WorkIsobaric(self, finalVolume):
	"""This function calculates total workdone in a piston cylinder system when the process is isobaric"""
	    self.finVol= finalVolume
		return self.initP* (self.finVol - self.initVol)
	def WorkIsothermalP(self, finalPressure):
	"""This function calculates total workdone in a piston cylinder system when the process is isothermal and initial and final presure is given"""
		self.finP= finalPressure
		return self.moles * self.R * self.initTemp * log((self.initP/self.finP), 2.718281)
	def WorkdoneIsothermalV(self, finalVolume):
	"""This function calculates total workdone in a piston cylinder system when the process is isothermal and initial and final volume is given"""
		self.finV= finalVolume
		return self.moles * self.R * self.initTemp * log((self.finV/self.initV), 2.718281)
	def WorkAdiabatic(self, finalTemprature):
	"""This function calculates total workdone in a piston cylinder system when the process is adiabatic"""
		self.finTemp= finalTemprature
		return (-3/2)*self.moles*self.R*(self.finTemp - self.initTemp)
