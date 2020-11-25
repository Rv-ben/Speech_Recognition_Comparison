import speech_recognition as sr
import distance
import os
import logging

class Speech:
	def __init__(self):
		self.original = []
		self.recognized = []
		self.distances = []

	def read_original(self, inFile):

		file =  open(inFile,'r')
		for line in file:
			self.original.append(line)

	def conv_audio(self, inDir):
		r = sr.Recognizer()

		dirct = os.listdir(inDir)
		for fName in dirct:
			logging.info(" %s \\ %s ",inDir,fName)         
			audioFile = sr.AudioFile(inDir+'\\'+fName)
			with audioFile as source:
				audio = r.record(source)
				self.recognized.append(r.recognize_google(audio))
                
                
	def NLD(self,ori,rec):
		return distance.levenshtein(ori,rec) / max(len(ori),len(rec))
    
	def comp_string(self):
        
		for i in range(len(self.original)):
			splitOri = self.original[i].split(' ')
			splitRec = self.recognized[i].split(' ')
			self.distances.append(self.NLD(splitOri,splitRec))

if __name__ == '__main__':
    pass