Python 3.3.2 (v3.3.2:d047928ae3f6, May 16 2013, 00:06:53) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Piston(object):
	def Piston_pressure(self, atmosphericPressure, mass, crossSectionalArea):
		self.mass= mass
		self.atmP= atmosphericPressure
		self.csa= crossSectionalArea
	def totalPressure(self):
		return self.atmP + (self.mass * 9.8)/self.csa
	def pistonSpringSyatem(self, mass, springLength, springFinalLength, crossSectionalArea, springConstant, atmosphericPressure):
		self.mass= mass
		self.K= springConstant
		self.finalLength= springFinalLength
		self.naturalLength= springLength
		self.csa= crossSectionalArea
		self.atmP= atmosphericPressure
	def totalPressureInSpringSystem(self):
		return (self.mass * 9.8)/self.csa + self.atmP + (self.finalLength-self.naturalLength)/self.csa
	def Piston_workIsobaric(self, pressure, initialVolume, finalVolume):
		self.initialVolume= initialVolume
		self.finalVolume= finalVolume
		self.pressure= pressure
	def totalWorkIsobaric(self):
		return self.pressure * (self.finalVolume - self.initialVolume)
	def piston_workIsothermalPressureForm(self, initialPressure, finalPressure, gasConstant, moles, temprature):
		self.initialPressure= initialPressure
		self.finalPressure= finalPressure
		self.R= gasConstant
		self.moles= moles
		self.temp= temprature
	def totalWorkIsothermalPressureForm(self):
		import math
		return self.moles * self.R * self.temp * log((self.initialPressure/self.finalPressure), 2.718281)
	def piston_workIsothermalVolumeForm(self, initialVolume, finalVolume, gasConstant, moles, temprature):
		self.initialVolume= initialVolume
		self.finalVolume= finalVolume
		self.R= gasConstant
		self.moles= moles
		self.temp= temprature
	def totalWorkdoneIsothermalVolumeForm(self):
		import math
		return self.moles * self.R * self.temp * log((self.finalVolume/self.initialVolume), 2.718281)
	def piston_workAdiabatic(self, moles, gasConstant, initialTemprature, finalTemprature):
		self.moles= moles
		self.R= gasConstant
		self.initialTemprature= initialTemprature
		self.finalTemprature= finalTemprature
	def totalWorkAdiabatic(self):
		return (-3/2)*self.moles*self.R*(self.finalTemprature - self.initialTemprature
